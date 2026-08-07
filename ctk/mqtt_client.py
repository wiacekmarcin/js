import paho.mqtt.client as mqtt
import json
from typing import Callable
tempConfig = \
"""{
   "device_class":"temperature",
   "state_topic":"lustro_new/sensor/data/TiHLazienka1/state",
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
   "state_topic":"lustro_new/sensor/data/TiHLazienka1/state",
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
   "state_topic":"lustro_new/sensor/data/TLustroMon/state",
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
   "state_topic":"lustro_new/sensor/data/TLustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/TLustroRasCPU/state",
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
   "state_topic":"lustro_new/sensor/data/CPULustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/CPULustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/Ina219LustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/Ina219LustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/Ina219LustroRas/state",
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
   "state_topic":"lustro_new/sensor/data/Ina219LustroRas/state",
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

class SensorBase:

    def __init__(self, topic:str, prefix:str):
        self.topic = topic
        self.prefix = prefix

    def subscribe(self, client):
        client.subscribe(self.topic)

    def test(self, topic):
        return self.topic == topic

    def parse(self, data):
        pass

class TempHumi(SensorBase):
    def __init__(self, topic:str, prefix:str):
        super().__init__(topic, prefix)

    def parse(self, data):
        #val = data.decode('utf-8')
        sdict = json.loads(data)
        ret = {}
        try:
            humi = sdict["humidity"]
            temp = sdict["temperature"]
            ret = {
                '%s_humi' % self.prefix : humi,
                '%s_temp' % self.prefix : temp,
            }
        except:
            pass
        return ret

class Temp(SensorBase):
    def __init__(self, topic:str, prefix:str):
        super().__init__(topic, prefix)

    def parse(self, data):
        #val = data.decode('utf-8')
        sdict = json.loads(data)
        ret = {}
        try:
            temp = sdict["temperature"]
            ret = {
                '%s_temp' % self.prefix : temp,
            }
        except:
            pass
        return ret

class TempAll:
    def __init__(self):
    
        self.lst = []
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_children/*", 'dzieci'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_salon/*",'salon_1'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_kitchen/*", 'kuchnia'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_sypialnia/*", 'sypialnia'))

        self.lst.append(TempHumi("zigbee2mqtt/tih_z_hol_wc/*", 'hol'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_salon_hol/*", 'salon_2'))
        
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_wc/*", 'wc'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_outside/*", 'outside_2'))
        self.lst.append(TempHumi("zigbee2mqtt/tih_z_pracownia/*", 'pracownia'))
        self.lst.append(Temp("zigbee2mqtt/outside_temperature/*", 'outside_1'))

    def parse(self, topic, data):
        for t in self.lst:
            if t.test(topic):
                return t.parse(data)
        return {}

    def subscribe(self, client):
        for t in self.lst:
            t.subscribe(client)
    
class PahoMqttWriter:

    def __init__(self, handler:callable):
        self._function = handler
        self.clientmqtt = mqtt.Client(client_id="lustroCID", protocol=mqtt.MQTTv5,
                                       callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        self.clientmqtt.username_pw_set("mqtt", "mqtt")
        self.clientmqtt.on_connect = self.msg_on_connect
        self.clientmqtt.on_message = self.msg_on_message
  
        self.clientmqtt.user_data_set([])
        #self.clientmqtt.connect("192.168.10.250", 1883, 60)

        self.temps = TempAll()
        self.isconnect = False
        self.try_connect()

    def msg_on_connect(self, client, userdata, flags, rc, properties):

        if rc.is_failure:
            print(f"Failed to connect: {rc}. loop_forever() will retry connection")
        else:
            self.isconnect = True
            #print("Connected")

            # Subscribing in on_connect() means that if we lose the connection and
            # reconnect then subscriptions will be renewed.
            self.temps.subscribe(client)
            
            

    def msg_on_message(self, client, userdata, msg):
        print("receive")
        print(msg.topic+" "+str(msg.payload))
        #print(client)
        #print(userdata)
        topic = msg.topic
        #data = 
        if msg.topic == "lustro/features/show_kredyty":
            pass
        d = self.temps.parse(msg.topic, msg.payload)
        if len(d) > 0:
            self._function(d)

    def try_connect(self):
        if self.isconnect:
            return

        print("mqtt connect")
        try:
            self.clientmqtt.connect("192.168.10.250", 1883, 600)
            self.isconnect = True
            self.clientmqtt.loop_start()
            print("ok")
        except:
            print("error")
            self.isconnect = False
            return
        try :
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/TiHLazienkaT/config", tempConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/TiHLazienkaH/config", humiConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/TLazienkaMon/config", tempMonConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/TLazienkaRas/config", tempRasConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/TLustroRasCPU/config", tempRasCPUConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/CPULustroRasUsage/config", usageRasCPUConfig)
            #self.clientmqtt.publish("lustro_new/sensor/sensorConfig/sensorCPULustroRasFreq/config", freqRasCPUConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/VoltRasCPUConfig/config",voltageRasCPUConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/CurrRasCPUConfig/config",currentRasCPUConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/PowerRasCPUConfig/config",powerRasCPUConfig)
            self.clientmqtt.publish("lustro_new/sensor/sensorConfig/EnergyRasCPUConfig/config", energyRasCPUConfig)
            print("ok2")
        except:
            print("Err")
            self.isconect = False

    def receiveNotfication(self, dictValue):

        if not self.isconnect:
            self.try_connect()
            return
        try:
            if "lazienka_temp" in dictValue.keys() and "lazienka_humi" in dictValue.keys():
                payload = '{ "temperature":%s, "humidity":%s }' % (dictValue["lazienka_temp"], dictValue["lazienka_humi"])
                self.clientmqtt.publish("lustro_new/sensor/data/TiHLazienka1/state", payload)
            if "286cf90f0b0000ae" in dictValue.keys():
                payload = '{ "temperature":%s}' % (dictValue["286cf90f0b0000ae"])
                self.clientmqtt.publish("lustro_new/sensor/data/TLustroRas/state", payload)
            if "28fff708640400a3" in dictValue.keys():
                payload = '{ "temperature":%s}' % (dictValue["28fff708640400a3"])
                self.clientmqtt.publish("lustro_new/sensor/data/TLustroMon/state", payload)

            if "tempGPU" in dictValue.keys():
                payload = '{ "temperature":%s}' % (dictValue["tempGPU"])
                self.clientmqtt.publish("lustro_new/sensor/data/TLustroRasCPU/state", payload)

            if "cpuFreq" in dictValue.keys() and "cpuUse" in dictValue.keys():
                payload = '{ "usage":%s, "freq":%s }' % (dictValue["cpuUse"], dictValue["cpuFreq"])
                self.clientmqtt.publish("lustro_new/sensor/data/CPULustroRas/state", payload)
            if "current" in dictValue.keys() and "voltage" in dictValue.keys() and "power" in dictValue.keys() and "energy" in dictValue.keys():
                payload = '{ "power":%(power)s, "voltage":%(voltage)s, "current" : %(current)s , "energy" : %(energy)s }' % (dictValue)
                self.clientmqtt.publish("lustro_new/sensor/data/Ina219LustroRas/state", payload)
        except:
            print("Err publishing")
            self.isconnect = False
            pass

    def sendMqtt(self, topic, dictValue):
        if not self.isconnect:
            self.try_connect()
            return
        try:
            payload = json.dumps(dictValue)
            self.clientmqtt.publish(topic, payload)
        except:
            print("Err publishing")
            self.isconnect = False

