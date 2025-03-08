import blackwidget

from PyQt5.QtCore import *

import paho.mqtt.client as mqtt

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("$SYS/#")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic+" "+str(msg.payload))

class PahoMqttWriter(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.clientmqtt = mqtt.Client(client_id="lustroCID")
        self.clientmqtt.on_connect = on_connect
        self.clientmqtt.on_message = on_message
        try:
            self.clientmqtt.connect("192.168.10.254", 1883, 60)
            self.connect = True
        except:
            self.connect = False 
            return


        
        tempConfig = \
"""{
   "device_class":"temperature",
   "state_topic":"lustro/sensor/data/TiHLazienka1/state",
   "unit_of_measurement":"°C",
   "value_template":"{{ value_json.temperature}}",
   "unique_id":"temp(Lazienka)",
   "device":{
      "identifiers":[
          "lazienkaTiH_L_temp"
      ],
      "name":"Temperatura Lazienka",
      "model": "DHT 22",
   }
}"""
        humiConfig = \
"""
{
   "device_class":"humidity",
   "state_topic":"lustro/sensor/data/TiHLazienka1/state",
   "unit_of_measurement":"%",
   "value_template":"{{ value_json.humidity}}",
   "unique_id":"humi(Lazienka)",
   "device":{
        "identifiers":[
          "lazienkaTiH_L_humi"
      ],
      "name":"Wilgotnosc Lazienka",
      "model": "DHT 22",
    }
}
"""

        tempMonConfig = \
"""{
   "device_class":"temperature",
   "state_topic":"lustro/sensor/data/TLustroMon/state",
   "unit_of_measurement":"°C",
   "value_template":"{{ value_json.temperature}}",
   "unique_id":"Temp(Monitor)",
   "device":{
      "identifiers":[
          "286cf90f0b0000ae",
          "lazienkaTMonitor"  
      ],
      "name":"Temperatura Monitora",
      "manufacturer": "Toshiba",
      "model": "DS1820",
   }
}"""

        tempRasConfig = \
"""{
   "device_class":"temperature",
   "state_topic":"lustro/sensor/data/TLustroRas/state",
   "unit_of_measurement":"°C",
   "value_template":"{{ value_json.temperature}}",
   "unique_id":"Temp(Raspberry)",
   "device":{
      "identifiers":[
          "28fff708640400a3",
          "LazienkaTRaspberry"
      ],
      "name":"Temperatura Raspberry",
      "manufacturer": "Toshiba",
      "model": "DS1820",
   }
}"""

        tempRasCPUConfig = \
"""{
   "device_class":"temperature",
   "state_topic":"lustro/sensor/data/TLustroRasCPU/state",
   "unit_of_measurement":"°C",
   "value_template":"{{ value_json.temperature}}",
   "unique_id":"Temp(RaspberryCPU)",
   "device":{
      "identifiers":[
          "temp_raspberry_lustro_cpu"
      ],
      "name":"Temperatura CPU Raspberry",
      "manufacturer": "Raspberry",
   }
}"""

        usageRasCPUConfig = \
"""{
   "device_class":"percentage",
   "state_topic":"lustro/sensor/data/CPULustroRas/state",
   "unit_of_measurement":"%",
   "value_template":"{{ value_json.usage }}",
   "unique_id":"Usage(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_cpu.usage"
      ],
      "name":"Lustro CPU",
      "manufacturer": "Raspberry",
   }
}"""

        freqRasCPUConfig = \
"""{
   "device_class":"frequency",
   "state_topic":"lustro/sensor/data/CPULustroRas/state",
   "unit_of_measurement":"MHz",
   "value_template":"{{ value_json.freq }}",
   "unique_id":"Freq(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_cpu.freq"
      ],
   }
""" 

        voltageRasCPUConfig = \
"""{
   "device_class":"voltage",
   "state_topic":"lustro/sensor/data/Ina219LustroRas/state",
   "unit_of_measurement":"V",
   "value_template":"{{ value_json.voltage }}",
   "unique_id":"Voltage(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_ina219.voltage"
      ],
      "name":"Lustro - napiecie",
      "manufacturer": "Raspberry",
   }
}"""

        currentRasCPUConfig = \
"""{
   "device_class":"current",
   "state_topic":"lustro/sensor/data/Ina219LustroRas/state",
   "unit_of_measurement":"A",
   "value_template":"{{ value_json.current }}",
   "unique_id":"Current(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_ina219.current"
      ],
      "name":"Lustro - prad",
      "manufacturer": "Raspberry",
   }
}"""


        powerRasCPUConfig = \
"""{
   "device_class":"power",
   "state_topic":"lustro/sensor/data/Ina219LustroRas/state",
   "unit_of_measurement":"W",
   "value_template":"{{ value_json.power }}",
   "unique_id":"Power(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_ina219.power"
      ],
      "name":"Lustro - moc",
      "manufacturer": "Raspberry",
   }
}""" 
        energyRasCPUConfig = \
"""{
   "device_class":"energy",
   "state_topic":"lustro/sensor/data/Ina219LustroRas/state",
   "unit_of_measurement":"kWh",
   "value_template":"{{ value_json.energy }}",
   "unique_id":"Power(RaspberryCPU)Lustro",
   "device":{
      "identifiers":[
          "raspberry_lustro_ina219.energy"
      ],
      "name":"Lustro - energia",
      "manufacturer": "Raspberry",
   }
}"""

        self.clientmqtt.publish("lustro/sensor/sensorConfig/TiHLazienkaT/config", tempConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/TiHLazienkaH/config", humiConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/TLazienkaMon/config", tempMonConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/TLazienkaRas/config", tempRasConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/TLustroRasCPU/config", tempRasCPUConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/CPULustroRasUsage/config", usageRasCPUConfig)
        #self.clientmqtt.publish("lustro/sensor/sensorConfig/sensorCPULustroRasFreq/config", freqRasCPUConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/VoltRasCPUConfig/config",voltageRasCPUConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/CurrRasCPUConfig/config",currentRasCPUConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/PowerRasCPUConfig/config",powerRasCPUConfig)
        self.clientmqtt.publish("lustro/sensor/sensorConfig/EnergyRasCPUConfig/config", energyRasCPUConfig)

    def receiveNotfication(self, dictValue):
        print(dictValue)
        if not self.connect:
            try:
                self.clientmqtt.connect("192.168.10.254", 1883, 60)
                self.connect = True
            except:
                self.connect = False 
                return
        if "lazienka_temp" in dictValue.keys() and "lazienka_humi" in dictValue.keys():
            payload = '{ "temperature":%s, "humidity":%s }' % (dictValue["lazienka_temp"], dictValue["lazienka_humi"])
            self.clientmqtt.publish("lustro/sensor/data/TiHLazienka1/state", payload)
        if "286cf90f0b0000ae" in dictValue.keys():
            payload = '{ "temperature":%s}' % (dictValue["286cf90f0b0000ae"])
            self.clientmqtt.publish("lustro/sensor/data/TLustroRas/state", payload)   
        if "28fff708640400a3" in dictValue.keys():
            payload = '{ "temperature":%s}' % (dictValue["28fff708640400a3"])
            self.clientmqtt.publish("lustro/sensor/data/TLustroMon/state", payload)   

        if "tempGPU" in dictValue.keys():
            payload = '{ "temperature":%s}' % (dictValue["tempGPU"])
            self.clientmqtt.publish("lustro/sensor/data/TLustroRasCPU/state", payload) 

        if "cpuFreq" in dictValue.keys() and "cpuUse" in dictValue.keys():
            payload = '{ "usage":%s, "freq":%s }' % (dictValue["cpuUse"], dictValue["cpuFreq"])
            self.clientmqtt.publish("lustro/sensor/data/CPULustroRas/state", payload)
        if "current" in dictValue.keys() and "voltage" in dictValue.keys() and "power" in dictValue.keys() and "energy" in dictValue.keys():
            payload = '{ "power":%(power)s, "voltage":%(voltage)s, "current" : %(current)s , "energy" : %(energy)s }' % (dictValue)
            self.clientmqtt.publish("lustro/sensor/data/Ina219LustroRas/state", payload)


    def getRect(self):
        return QRect(1080,1920,0,0)
    
    def timeout(self, dt):
        pass
