import json
from typing import Callable
import socket

class UdpSend() :
    UDP_IP = "192.168.10.250"
    UDP_PORT_1 = 9100
    UDP_PORT_2 = 9101
    

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, # Internet
             socket.SOCK_DGRAM) # UDP
        
    def sendUdpNotfication(self, dictValue):
        if 'lazienka_temp' in dictValue:
            data = json.dumps({'temperature' : dictValue['lazienka_temp'], 
                               'humidity' :    dictValue['lazienka_humi']})
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_1)) 

        if '286CF90F0B0000AE' in dictValue and '28FFF708640400A3' in dictValue:
            data = json.dumps({'monitor_temp' : dictValue['286CF90F0B0000AE'],
                               'raspberry_temp' : dictValue['28FFF708640400A3']})
            
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_2)) 

        if 'energy_1s' in dictValue: 
            data = json.dumps({'raspberrry_current' : dictValue['energy_1s']['current'],
                               'raspberry_voltage' : dictValue['energy_1s']['voltage'],
                               'raspberry_power' : dictValue['energy_1s']['power'],
                               'raspberry_uptime' : dictValue['energy_1s']['uptime']})
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_2)) 

        if 'energy_15s' in dictValue: 
            data = json.dumps({'raspberry_ram' : dictValue['energy_15s']['raspberry_ram'],
                                'raspberry_cpu' : dictValue['energy_15s']['raspberry_cpu'],
                                'raspberry_cpu_temp' : dictValue['energy_15s']['raspberry_cpu_temp']})
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_2)) 

        if 'energy_60s' in dictValue: 
            data = json.dumps({'raspberry_disk_total' : dictValue['energy_60s']['raspberry_disk_total'],
                                'raspberry_disk_used' : dictValue['energy_60s']['raspberry_disk_used'],
                                'raspberry_disk_free' : dictValue['energy_60s']['raspberry_disk_free']})
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_2)) 

        if 'lustro_switch_screan' in dictValue:
            data = json.dumps({'lustro_switch_screan' : dictValue['lustro_switch_screan']})
            self.sock.sendto(data.encode('utf-8'), (self.UDP_IP, self.UDP_PORT_2)) 