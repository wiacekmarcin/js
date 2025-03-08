#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import urllib3
from bs4  import BeautifulSoup

import blackwidget
import stats_ui
import os
import socket
from urllib.request import urlopen
import json

options = {
    "measure_temp": ["temp", "'C"],
    "get_mem gpu": ["gpu", "M"],
    "get_mem arm": ["arm", "M"],
    "measure_clock core": ["frequency(1)", ""],
    "measure_clock arm": ["frequency(48)", ""],
    "measure_clock v3d": ["frequency(46)", ""],
    "measure_volts core": ["volt", "V"],
    "measure_volts sdram_c": ["volt", "V"],
    "measure_volts sdram_i": ["volt", "V"],
    "measure_volts sdram_p": ["volt", "V"],
    "get_throttled": ["throttled", "x0"],
}


def vcgencmd(option):
    """
        https://elinux.org/RPI_vcgencmd_usage
        https://github.com/nezticle/RaspberryPi-BuildRoot/wiki/VideoCore-Tools
    """
    if option in options:
        cmd = "/opt/vc/bin/vcgencmd {}".format(option)
        try:
            res = os.popen(cmd).readline()
            res = res.replace("{}=".format(options[option][0]), "")
            res = res.replace("{}\n".format(options[option][1]), "")
        except:
            res = "0"
    else:
        res = "0"
    return res


# --------------------------------------------------------------------------------

global _last_idle, _last_total
_last_idle = _last_total = 0


def getBits(value, start, length):
    return (value >> start) & 2 ** length - 1


def getClock(p):
    if p in [
        "arm",
        "core",
        "dpi",
        "emmc",
        "h264",
        "hdmi",
        "isp",
        "pixel",
        "pwm",
        "uart",
        "v3d",
        "vec",
    ]:
        res = vcgencmd("measure_clock {}".format(p))
    else:
        res = "0"
    return res


def getCPUcount():
    return os.cpu_count()


def getCPUcurrentSpeed():
    # Return CPU speed in Mhz
    try:
        res = os.popen(
            "cat /sys/devices/system/cpu/cpu0/cpufreq/scaling_cur_freq"
        ).readline()
    except:
        res = "0"
    return round(int(res) / 1000)


def getCPUtemperature():
    # Return CPU temperature
    try:
        res = os.popen("cat /sys/class/thermal/thermal_zone0/temp").readline()
    except:
        res = "0"
    return round(float(res) / 1000, 1)


def getCPUuptime():
    try:
        with open("/proc/uptime") as f:
            fields = [float(column) for column in f.readline().strip().split()]
        res = round(fields[0])
    except:
        res = 0.0
    return res


def getCPUuse():
    """
        Return % of CPU used by user
        Based on: https://rosettacode.org/wiki/Linux_CPU_utilization#Python
    """
    global _last_idle, _last_total
    try:
        with open("/proc/stat") as f:
            fields = [float(column) for column in f.readline().strip().split()[1:]]
        idle, total = fields[3], sum(fields)
        idle_delta, total_delta = idle - _last_idle, total - _last_total
        _last_idle, _last_total = idle, total
        res = round(100.0 * (1.0 - idle_delta / total_delta), 2)
    except:
        res = 0.0
    return res


def getAppMemory():
    # ps aux | grep domoticz | awk '{sum=sum+$6}; END {print sum}'
    try:
        res = (
            os.popen("ps aux | grep pyqt5app.py | awk '{sum=sum+$6}; END {print sum}'")
            .readline()
            .replace("\n", "")
        )
    except:
        res = "0"
    return float(res)


def getGatewayLatency():
    try:
        gateway = (
            os.popen("route -n | awk '$1 == \"0.0.0.0\" { print $2 }'")
            .readline()
            .strip()
        )
        rtt = (
            os.popen("ping -c1 {} | grep rtt".format(gateway))
            .readline()
            .split()[3]
            .split("/")[0]
        )
    except:
        rtt = "0"
    return float(rtt)


def getGPUtemperature():
    # Return GPU temperature
    return float(vcgencmd("measure_temp"))


def getHostname():
    return socket.gethostname()


def getIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("8.8.8.8", 1))
    except socket.error:
        return None
    return s.getsockname()[0]

def getIPOut():
    response = urlopen("http://httpbin.org/ip")
    data_json = json.loads(response.read().decode('utf-8'))
    return data_json["origin"]
    

def getIP6():
    s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
    try:
        s.connect(("2001:4860:4860::8888", 1))
    except socket.error:
        return None
    return s.getsockname()[0]


def getMemory(p):
    if p in ["arm", "gpu"]:
        res = vcgencmd("get_mem {}".format(p))
    else:
        res = "0"
    return float(res)


def getNetworkConnections(state):
    # Return number of network connections
    res = 0
    try:
        for line in os.popen("netstat -tun").readlines():
            if line.find(state) >= 0:
                res += 1
    except:
        res = 0
    return res


def getPiRevision():
    try:
        res = (
            os.popen("cat /proc/cpuinfo | grep Revision\t")
            .readline()
            .replace("\n", "")
            .split(":")[1]
            .strip()
        )
        # Convert hex to int
        res = int(res, 16)
    except:
        res = None
    return res


def getRAMinfo():
    # Return RAM information in a list
    # Based on: https://gist.github.com/funvill/5252169
    p = os.popen("free -b")
    i = 0
    while 1:
        i = i + 1
        line = p.readline()
        if i == 2:
            res = line.split()[1:4]
            # Index 0: total RAM
            # Index 1: used RAM
            # Index 2: free RAM
            return round(100 * int(res[1]) / int(res[0]), 2)


# http://www.microcasts.tv/episodes/2014/03/15/memory-usage-on-the-raspberry-pi/
# https://www.raspberrypi.org/forums/viewtopic.php?f=63&t=164787
# https://stackoverflow.com/questions/22102999/get-total-physical-memory-in-python/28161352
# https://stackoverflow.com/questions/17718449/determine-free-ram-in-python
# https://www.reddit.com/r/raspberry_pi/comments/60h5qv/trying_to_make_a_system_info_monitor_with_an_lcd/


def getThrottled():
    return int(vcgencmd("throttled"))


def getUpStats():
    # Get uptime of RPi
    # Based on: http://cagewebdev.com/raspberry-pi-showing-some-system-info-with-a-python-script/
    # Returns a tuple (uptime, 5 min load average)
    try:
        s = os.popen("uptime").readline()
        load_split = s.split("load average: ")
        up = load_split[0]
        up_pos = up.rfind(",", 0, len(up) - 4)
        up = up[:up_pos].split("up ")[1]
        return up
    except:
        return ""


def getVoltage(p):
    # Get voltage
    # Based on: https://www.raspberrypi.org/forums/viewtopic.php?t=30697
    if p in ["core", "sdram_c", "sdram_i", "sdram_p"]:
        res = vcgencmd("measure_volts {}".format(p))
    else:
        res = "0"
    return float(res)


import smbus
import time

# Config Register (R/W)
_REG_CONFIG                 = 0x00
# SHUNT VOLTAGE REGISTER (R)
_REG_SHUNTVOLTAGE           = 0x01

# BUS VOLTAGE REGISTER (R)
_REG_BUSVOLTAGE             = 0x02

# POWER REGISTER (R)
_REG_POWER                  = 0x03

# CURRENT REGISTER (R)
_REG_CURRENT                = 0x04

# CALIBRATION REGISTER (R/W)
_REG_CALIBRATION            = 0x05

class BusVoltageRange:
    """Constants for ``bus_voltage_range``"""
    RANGE_16V               = 0x00      # set bus voltage range to 16V
    RANGE_32V               = 0x01      # set bus voltage range to 32V (default)

class Gain:
    """Constants for ``gain``"""
    DIV_1_40MV              = 0x00      # shunt prog. gain set to  1, 40 mV range
    DIV_2_80MV              = 0x01      # shunt prog. gain set to /2, 80 mV range
    DIV_4_160MV             = 0x02      # shunt prog. gain set to /4, 160 mV range
    DIV_8_320MV             = 0x03      # shunt prog. gain set to /8, 320 mV range

class ADCResolution:
    """Constants for ``bus_adc_resolution`` or ``shunt_adc_resolution``"""
    ADCRES_9BIT_1S          = 0x00      #  9bit,   1 sample,     84us
    ADCRES_10BIT_1S         = 0x01      # 10bit,   1 sample,    148us
    ADCRES_11BIT_1S         = 0x02      # 11 bit,  1 sample,    276us
    ADCRES_12BIT_1S         = 0x03      # 12 bit,  1 sample,    532us
    ADCRES_12BIT_2S         = 0x09      # 12 bit,  2 samples,  1.06ms
    ADCRES_12BIT_4S         = 0x0A      # 12 bit,  4 samples,  2.13ms
    ADCRES_12BIT_8S         = 0x0B      # 12bit,   8 samples,  4.26ms
    ADCRES_12BIT_16S        = 0x0C      # 12bit,  16 samples,  8.51ms
    ADCRES_12BIT_32S        = 0x0D      # 12bit,  32 samples, 17.02ms
    ADCRES_12BIT_64S        = 0x0E      # 12bit,  64 samples, 34.05ms
    ADCRES_12BIT_128S       = 0x0F      # 12bit, 128 samples, 68.10ms

class Mode:
    """Constants for ``mode``"""
    POWERDOW                = 0x00      # power down
    SVOLT_TRIGGERED         = 0x01      # shunt voltage triggered
    BVOLT_TRIGGERED         = 0x02      # bus voltage triggered
    SANDBVOLT_TRIGGERED     = 0x03      # shunt and bus voltage triggered
    ADCOFF                  = 0x04      # ADC off
    SVOLT_CONTINUOUS        = 0x05      # shunt voltage continuous
    BVOLT_CONTINUOUS        = 0x06      # bus voltage continuous
    SANDBVOLT_CONTINUOUS    = 0x07      # shunt and bus voltage continuous


class INA219:
    def __init__(self, i2c_bus=1, addr=0x40):
        self.bus = smbus.SMBus(i2c_bus);
        self.addr = addr

        # Set chip to known config values to start
        self._cal_value = 0
        self._current_lsb = 0
        self._power_lsb = 0
        self.set_calibration_32V_2A()

    def read(self,address):
        data = self.bus.read_i2c_block_data(self.addr, address, 2)
        return ((data[0] * 256 ) + data[1])

    def write(self,address,data):
        temp = [0,0]
        temp[1] = data & 0xFF
        temp[0] =(data & 0xFF00) >> 8
        self.bus.write_i2c_block_data(self.addr,address,temp)

    def set_calibration_32V_2A(self):
        """Configures to INA219 to be able to measure up to 32V and 2A of current. Counter
           overflow occurs at 3.2A.
           ..note :: These calculations assume a 0.1 shunt ohm resistor is present
        """
        # By default we use a pretty huge range for the input voltage,
        # which probably isn't the most appropriate choice for system
        # that don't use a lot of power.  But all of the calculations
        # are shown below if you want to change the settings.  You will
        # also need to change any relevant register settings, such as
        # setting the VBUS_MAX to 16V instead of 32V, etc.

        # VBUS_MAX = 16V             (Assumes 32V, can also be set to 16V)
        # VSHUNT_MAX = 0.32          (Assumes Gain 8, 320mV, can also be 0.16, 0.08, 0.04)
        # RSHUNT = 4.7               (Resistor value in ohms)

        # 1. Determine max possible current
        # MaxPossible_I = VSHUNT_MAX / RSHUNT
        # MaxPossible_I = 3.2A

        # 2. Determine max expected current
        # MaxExpected_I = 2.0A

        # 3. Calculate possible range of LSBs (Min = 15-bit, Max = 12-bit)
        # MinimumLSB = MaxExpected_I/32767
        # MinimumLSB = 0.000061              (61uA per bit)
        # MaximumLSB = MaxExpected_I/4096
        # MaximumLSB = 0,000488              (488uA per bit)

        # 4. Choose an LSB between the min and max values
        #    (Preferrably a roundish number close to MinLSB)
        # CurrentLSB = 0.0001 (100uA per bit)
        self._current_lsb = .1  # Current LSB = 100uA per bit

        # 5. Compute the calibration register
        # Cal = trunc (0.04096 / (Current_LSB * RSHUNT))
        # Cal = 4096 (0x1000)

        self._cal_value = 4096

        # 6. Calculate the power LSB
        # PowerLSB = 20 * CurrentLSB
        # PowerLSB = 0.002 (2mW per bit)
        self._power_lsb = .002  # Power LSB = 2mW per bit

        # 7. Compute the maximum current and shunt voltage values before overflow
        #
        # Max_Current = Current_LSB * 32767
        # Max_Current = 3.2767A before overflow
        #
        # If Max_Current > Max_Possible_I then
        #    Max_Current_Before_Overflow = MaxPossible_I
        # Else
        #    Max_Current_Before_Overflow = Max_Current
        # End If
        #
        # Max_ShuntVoltage = Max_Current_Before_Overflow * RSHUNT
        # Max_ShuntVoltage = 0.32V
        #
        # If Max_ShuntVoltage >= VSHUNT_MAX
        #    Max_ShuntVoltage_Before_Overflow = VSHUNT_MAX
        # Else
        #    Max_ShuntVoltage_Before_Overflow = Max_ShuntVoltage
        # End If

        # 8. Compute the Maximum Power
        # MaximumPower = Max_Current_Before_Overflow * VBUS_MAX
        # MaximumPower = 3.2 * 32V
        # MaximumPower = 102.4W

        # Set Calibration register to 'Cal' calculated above
        self.write(_REG_CALIBRATION,self._cal_value)

        # Set Config register to take into account the settings above
        self.bus_voltage_range = BusVoltageRange.RANGE_32V
        self.gain = Gain.DIV_8_320MV
        self.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        self.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        self.mode = Mode.SANDBVOLT_CONTINUOUS
        self.config = self.bus_voltage_range << 13 | \
                      self.gain << 11 | \
                      self.bus_adc_resolution << 7 | \
                      self.shunt_adc_resolution << 3 | \
                      self.mode
        self.write(_REG_CONFIG,self.config)

        """Configures to INA219 to be able to measure up to 32V and 2A of current. Counter
           overflow occurs at 3.2A.
           ..note :: These calculations assume a 0.1 shunt ohm resistor is present
        """
        # By default we use a pretty huge range for the input voltage,
        # which probably isn't the most appropriate choice for system
        # that don't use a lot of power.  But all of the calculations
        # are shown below if you want to change the settings.  You will
        # also need to change any relevant register settings, such as
        # setting the VBUS_MAX to 16V instead of 32V, etc.

        # VBUS_MAX = 32V             (Assumes 32V, can also be set to 16V)
        # VSHUNT_MAX = 0.32          (Assumes Gain 8, 320mV, can also be 0.16, 0.08, 0.04)
        # RSHUNT = 0.1               (Resistor value in ohms)

        # 1. Determine max possible current
        # MaxPossible_I = VSHUNT_MAX / RSHUNT
        # MaxPossible_I = 3.2A

        # 2. Determine max expected current
        # MaxExpected_I = 2.0A

        # 3. Calculate possible range of LSBs (Min = 15-bit, Max = 12-bit)
        # MinimumLSB = MaxExpected_I/32767
        # MinimumLSB = 0.000061              (61uA per bit)
        # MaximumLSB = MaxExpected_I/4096
        # MaximumLSB = 0,000488              (488uA per bit)

        # 4. Choose an LSB between the min and max values
        #    (Preferrably a roundish number close to MinLSB)
        # CurrentLSB = 0.0001 (100uA per bit)
        self._current_lsb = .1  # Current LSB = 100uA per bit

        # 5. Compute the calibration register
        # Cal = trunc (0.04096 / (Current_LSB * RSHUNT))
        # Cal = 4096 (0x1000)

        self._cal_value = 4096

        # 6. Calculate the power LSB
        # PowerLSB = 20 * CurrentLSB
        # PowerLSB = 0.002 (2mW per bit)
        self._power_lsb = .002  # Power LSB = 2mW per bit

        # 7. Compute the maximum current and shunt voltage values before overflow
        #
        # Max_Current = Current_LSB * 32767
        # Max_Current = 3.2767A before overflow
        #
        # If Max_Current > Max_Possible_I then
        #    Max_Current_Before_Overflow = MaxPossible_I
        # Else
        #    Max_Current_Before_Overflow = Max_Current
        # End If
        #
        # Max_ShuntVoltage = Max_Current_Before_Overflow * RSHUNT
        # Max_ShuntVoltage = 0.32V
        #
        # If Max_ShuntVoltage >= VSHUNT_MAX
        #    Max_ShuntVoltage_Before_Overflow = VSHUNT_MAX
        # Else
        #    Max_ShuntVoltage_Before_Overflow = Max_ShuntVoltage
        # End If

        # 8. Compute the Maximum Power
        # MaximumPower = Max_Current_Before_Overflow * VBUS_MAX
        # MaximumPower = 3.2 * 32V
        # MaximumPower = 102.4W

        # Set Calibration register to 'Cal' calculated above
        self.write(_REG_CALIBRATION,self._cal_value)

        # Set Config register to take into account the settings above
        self.bus_voltage_range = BusVoltageRange.RANGE_32V
        self.gain = Gain.DIV_8_320MV
        self.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        self.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        self.mode = Mode.SANDBVOLT_CONTINUOUS
        self.config = self.bus_voltage_range << 13 | \
                      self.gain << 11 | \
                      self.bus_adc_resolution << 7 | \
                      self.shunt_adc_resolution << 3 | \
                      self.mode
        self.write(_REG_CONFIG,self.config)

    
    def getShuntVoltage_mV(self):
        self.write(_REG_CALIBRATION,self._cal_value)
        value = self.read(_REG_SHUNTVOLTAGE)
        if value > 32767:
            value -= 65535
        return value * 0.01

    def getBusVoltage_V(self):
        self.write(_REG_CALIBRATION,self._cal_value)
        self.read(_REG_BUSVOLTAGE)
        return (self.read(_REG_BUSVOLTAGE) >> 3) * 0.004

    def getCurrent_mA(self):
        value = self.read(_REG_CURRENT)
        if value > 32767:
            value -= 65535
        return value * self._current_lsb

    def getPower_W(self):
        self.write(_REG_CALIBRATION,self._cal_value)
        value = self.read(_REG_POWER)
        if value > 32767:
            value -= 65535
        return value * self._power_lsb
        
class StatsWidget(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(StatsWidget, self).__init__(parent)
        self.statsUi = stats_ui.Ui_Stats()
        self.setupUi(self)
        self.firstTime = True
        self.raspTemp = "--"
        self.monitorTemp = "--"
        self.ina219 = INA219(addr=0x42)
        self.allEnergy = 0.0

    def getRect(self):
        return QRect(0, 1920-400, 250, 400)
    
    def setupUi(self, StatsWidget):
        self.statsUi.setupUi(StatsWidget)

    def receiveNotfication(self, dictValue):
        if "28fff708640400a3" in dictValue:
            self.monitorTemp = dictValue["28fff708640400a3"]
        if "286cf90f0b0000ae" in dictValue:
            self.raspTemp = dictValue["286cf90f0b0000ae"]

    def timeout(self, dt):
        hour = dt.time().hour()
        min = dt.time().minute()
        sec = dt.time().second()
        vals = {}

        vals['cpuFreq'] = getCPUcurrentSpeed()
        self.statsUi.cpuSpeed.setText("%d MHz" % vals['cpuFreq'])

        vals['cpuUse'] = getCPUuse()
        self.statsUi.cpuUsage.setText("%d %%" % vals['cpuUse'])

        vals['current'] = "%3.3f" % (self.ina219.getCurrent_mA() / 1000)
        self.statsUi.current.setText("%0.3f mA" % self.ina219.getCurrent_mA())

        vals['voltage'] = "%2.2f" % self.ina219.getBusVoltage_V()
        self.statsUi.voltage.setText("%0.1f V" % self.ina219.getBusVoltage_V())
        power = self.ina219.getPower_W()
        vals['power'] = "%0.3f" % power
        self.allEnergy += power/3600000
        self.statsUi.power.setText("%0.3f W" % power)
        self.statsUi.energia.setText("%0.3f kWh (%s)" % (self.allEnergy, getUpStats()))
        vals['energy'] = self.allEnergy

        bus_voltage = self.ina219.getBusVoltage_V()
        p = (bus_voltage - 6)/2.4*100
        if(p > 100):p = 100
        if(p < 0):p = 0
        if p < 20:
            os.system("sudo sudo argonone-cli --manual --fan 100")
            os.system("sudo shutdown -h now")

        self.statsUi.tempGPU.setText("%2.1f\u00B0C" % getCPUtemperature())
        vals['tempGPU'] = "%2.1f" % getCPUtemperature()
        self.statsUi.tempMonitor.setText("%s\u00B0C" % self.monitorTemp)
        self.statsUi.tempRasp.setText("%s\u00B0C" % self.raspTemp)
        self.sendNotification(vals)

        if not self.firstTime and min % 5 != 0 or sec != 0:
            return
        vals = {}
        if self.firstTime or (min == 0 and sec == 0):
            self.statsUi.localIp.setText("%s" % getIP())
            vals['lustro-ip'] = "%s" % getIP()
            self.statsUi.zewnetrzneIp.setText("%s" % getIPOut())
            vals['lustro-ip-out'] = "%s" % getIPOut()

        self.firstTime = False

        self.sendNotification(vals)



#for p in [
#    "arm",
#    "core",
#    "dpi",
#    "emmc",
#    "h264",
#    "hdmi",
#    "isp",
#    "pixel",
#    "pwm",
#    "uart",
#    "v3d",
#    "vec",
#    ]:
#    print(p, getClock(p))
#print("cpucount", getCPUcount())
#print("current speed", getCPUcurrentSpeed())
#print("cpuTemp",getCPUtemperature())
#print("cpuTime", getCPUuptime())

#print("cpuUse", getCPUuse())
#print("appMem", getAppMemory())
#print("gateway", getGatewayLatency())
#print("gpuTemp", getGPUtemperature())
#print("hostname", getHostname())
#print("ip",getIP())
#print("ip6",getIP6())    
#print("memory arm",getMemory("arm"))
#print("memory gpu",getMemory("gpu"))
#print("piRev", getPiRevision())
#print("RamInfo",getRAMinfo())
#print("throttled",getThrottled())
#print("stats",getUpStats())

#for p in ["core", "sdram_c", "sdram_i", "sdram_p"]:
#    print(p, getVoltage(p))