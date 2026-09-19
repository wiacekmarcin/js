#*-* coding:utf-8 *-*
import os
from base_plugin import LPlugin
from ina219 import INA219
from math import floor
import shutil

global _last_idle, _last_total
_last_idle = _last_total = 0

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


def getCPUtemperature():
    # Return CPU temperature
    try:
        with open("/sys/class/thermal/thermal_zone0/temp") as f:
            res = f.readline().strip()
    except:
        res = "0"
    return round(float(res) / 1000, 1)

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

def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptime_seconds = float(f.readline().split()[0])

    #days = floor(uptime_seconds / 24*3600)
    #sec2 = uptime_seconds - days*24*3600
    #hour = floor( sec2 / 3600)
    #sec3 = sec2 - 3600*hour
    #minute = floor( sec3 / 60)
    #second = sec3 - 60*minute
    
    return uptime_seconds / 3600.0
    #return "d dni, %h:%02d%02d" % (days, hour, minute, second)


def getDiskUsage():
    total, used, free = shutil.disk_usage("/")
    return total, used, free


class EnergyRaspberry(LPlugin):
    SHUNT_OHMS = 0.1
    MAX_EXPECTED_AMPS = 1.5
    ADDR = 0x42
    I2C_BUS=1
    def __init__(self, app):
        super().__init__(app)
        self.ina = INA219(self.SHUNT_OHMS, self.MAX_EXPECTED_AMPS, self.I2C_BUS, self.ADDR)
        self.ina.configure(INA219.RANGE_16V)

   
    def getShuntVoltage_mV(self):
        return self.ina.shunt_voltage()

    def getBusVoltage_V(self):
        return self.ina.supply_voltage()

    def getCurrent_mA(self):
        return self.ina.current()

    def getPower_W(self):
        return self.ina.power() / 1000.0
        
    def timeout(self, dt):

        secs = dt.second
        vals = {}
        #vals['cpuUse'] = getCPUuse()
        #self.statsUi.cpuUsage.setText("%d %%" % vals['cpuUse'])

        vals['current'] = "%3.3f" % (self.ina.current())
        #self.statsUi.current.setText("%0.3f mA" % self.ina219.getCurrent_mA())

        vals['voltage'] = "%2.2f" % self.ina.voltage()
        #self.statsUi.voltage.setText("%0.1f V" % self.ina219.getBusVoltage_V())
        power = self.ina.power()
        vals['power'] = "%0.3f" % power
        #self.allEnergy += power/3600000
        #self.statsUi.power.setText("%0.3f W" % power)
        #self.statsUi.energia.setText("%0.3f kWh (%s)" % (self.allEnergy, getUpStats()))
        #vals['energy'] = self.allEnergy

        #bus_voltage = self.ina219.getBusVoltage_V()
        #p = (bus_voltage - 6)/2.4*100
        #if(p > 100):p = 100
        #if(p < 0):p = 0
        #if p < 20 and float(vals['voltage']) > 5.0:
        #    os.system("sudo argonone-cli --manual --fan 100")
        #    os.system("sudo shutdown -h now")

        #self.statsUi.tempGPU.setText("%2.1f\u00B0C" % getCPUtemperature())
        #vals['tempGPU'] = "%2.1f" % getCPUtemperature()
        #self.statsUi.tempMonitor.setText("%s\u00B0C" % self.monitorTemp)
        #self.statsUi.tempRasp.setText("%s\u00B0C" % self.raspTemp)
        #self.sendNotification(vals)

        #if not self.firstTime and min % 5 != 0 or sec != 0:
        #    return
        #vals = {}
        #if self.firstTime or (min == 0 and sec == 0):
        #    self.statsUi.localIp.setText("%s" % getIP())
        #    vals['lustro-ip'] = "%s" % getIP()
        #    self.statsUi.zewnetrzneIp.setText("%s" % getIPOut())
        #    vals['lustro-ip-out'] = "%s" % getIPOut()

        #self.firstTime = False
        vals['uptime'] = "%3.2f" % get_uptime()
        d = {'energy_1s' : vals}
        
        self.sendNotification(d)

        if secs in [0, 15, 30, 45]:
            vals_15 = {}
            vals_15['raspberry_ram'] = '%2.2f' % getRAMinfo()
            vals_15['raspberry_cpu'] = '%2.2f' % getCPUuse()
            vals_15['raspberry_cpu_temp'] = '%2.1f' % getCPUtemperature()
            self.sendNotification({'energy_15s' : vals_15})

        if secs == 0:
            total, used, free = getDiskUsage()
            vals_60 = {'raspberry_disk_total' : total,
                       'raspberry_disk_used' : used,
                       'raspberry_disk_free' : free}
            self.sendNotification({'energy_60s' : vals_60})


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
