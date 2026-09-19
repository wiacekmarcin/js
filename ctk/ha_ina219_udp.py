#import logging
import time
import socket
import json
import os
import shutil
#logger = logging.getLogger(__name__)
#FORMAT = '%(asctime)s %(message)s'

#logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=FORMAT)

from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1

UDP_PORT = 9003
UDP_IP = "192.168.10.250"
UDP_PORT2 = 9004

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



class MyIna219:
	dzielnik = 1000*3600
	def __init__(self, ID, address):
		self.ina_r = INA219(SHUNT_OHMS, busnum=1, address=address)
		self.ina_r.configure()
		self.Wh = 0.0
		self.ID = ID
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
		self.secs = 0

	def timeout(self):
		voltage_V = float(self.ina_r.voltage())
		current_mA = float(self.ina_r.current())
		power_mW = float(self.ina_r.power())
		self.Wh += (voltage_V*current_mA/1000.0)/3600
		data = {
			"voltage_%s" %self.ID : "%.3f" % voltage_V,
			"current_%s" %self.ID : "%.6f" % (current_mA/1000),
			"power_%s"   %self.ID : "%.6f" % (power_mW/1000),
			"energy_%s"  %self.ID : "%.3f" % self.Wh
		}
		self.sock.sendto(json.dumps(data).encode('utf-8'), (UDP_IP, UDP_PORT))

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) 
idx = 0
def timeout(sock, idx):

    vals = {}		
    vals['domoticz_uptime'] = "%3.2f" % get_uptime()
    
    idx = ( idx + 1 ) % 60

    if idx in [0, 15, 30, 45]:
        vals['domoticz_cpu_temp'] = '%2.1f' % getCPUtemperature()
        vals['domoticz_ram'] = '%2.2f' % getRAMinfo()
        vals['domoticz_cpu'] = '%2.2f' % getCPUuse()

    if idx == 0:
        total, used, free = getDiskUsage()
        vals['domoticz_disk_total'] =  total
        vals['domoticz_disk_used'] = used
        vals['domoticz_disk_free'] = free	

    sock.sendto(json.dumps(vals).encode('utf-8'), (UDP_IP, UDP_PORT2))
    return idx
     

inas = [ MyIna219("1", 0x40),
	MyIna219("2", 0x41),
	MyIna219("3", 0x42),
	MyIna219("4", 0x43) ]

while True:
	start = time.time()
	for ina in inas:
		ina.timeout()
	idx = timeout(sock, idx)
	duration = time.time() - start
	
        
	time.sleep(min(1, 1-duration))
