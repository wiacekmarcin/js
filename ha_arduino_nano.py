from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo, SwitchInfo, Switch
from paho.mqtt.client import Client, MQTTMessage
#import logging
import time
import serial


class MqttConn:
    def __init__(self):
        # Configure the required parameters for the MQTT broker        
        self.mqtt_settings = Settings.MQTT(host="192.168.10.250", username='mqtt', password='mqtt')

        # Define the device. At least one of `identifiers` or `connections` must be supplied
        self.device_info = DeviceInfo(name="ArduinoFlowMeters", identifiers="arduino_flowmeters")

class MyFlowMeter(MqttConn):
    def __init__(self, number:str):
        super(MyFlowMeter, self).__init__()
        self.allImpulse = 0
        self.actImpulse = 0

        # Information about the switch
        actFlowSI = SensorInfo(name="Przepływ %s" % number, 
                            unique_id="flow_%s_flowrate" % number, 
                            device=self.device_info,
                            device_class="volume_flow_rate",
                            unit_of_measurement="L/min")
        actFlow_settings = Settings(mqtt=self.mqtt_settings, entity=actFlowSI)
        self.actFlow = Sensor(actFlow_settings)

        allFlowSI = SensorInfo(name="Zużycie wody %s" % number, 
                            unique_id="flow_%s_water" % number, 
                            device=self.device_info,
                            device_class="water",
                            unit_of_measurement="L")
        allFlow_settings = Settings(mqtt=self.mqtt_settings, entity=allFlowSI)
        self.allFlow = Sensor(allFlow_settings)

    def setflow(self, flow):
        self.allImpulse += flow
        self.actImpuls = flow
        self.actFlow.set_state(self.actImpuls)
        self.allFlow.set_state(self.allImpulse)

class FunSwitch(MqttConn):
    def __init__(self, id:int, name:str, ser:serial.Serial):
        super(FunSwitch, self).__init__()
        self.cmd_on = ("W;%d;1;\r\n" % id).encode('ascii')
        self.cmd_off = ("W;%d;0;\r\n" % id).encode('ascii')
        self.serial = ser
        # Information about the switch
        fun_info = SwitchInfo(name="Wiatrak %s" % name, unique_id="fun_%d_switch" % id, device=self.device_info)
        fun_settings = Settings(mqtt=self.mqtt_settings, entity=fun_info)
        self.fun_switch = Switch(fun_settings, self.switch_callback)

    def switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print(self.cmd_on)
            self.serial.write(self.cmd_on)
        elif payload == "OFF":
            print(self.cmd_off)
            # Let HA know that the switch was successfully deactivated
            self.serial.write(self.cmd_off)
    
    def set(self, val:bool):
        if val:
            self.fun_switch.on()
        else:
            self.fun_switch.off()


# Instantiate the switch
mapsDevice = [
    "wc_umywalka_z","wc_umywalka_c", "wc_sedes", "wc_pralka_z", "wc_Pralka_c",
    "lazienka_prysznic_c", "lazienka_prysznic_z", "lazienka_wanna_c", "lazienka_wanna_z", 
    "lazienka_umywalka_c", "lazienka_umywalka_z", "lazienka_sedes",
    "kuchnia_umywalka_c", "kuchnia_umywalka_z", "kuchnia_zmywarka" ]

flows = []
for i in range(15):
    flows.append(MyFlowMeter(mapsDevice[i]))
    flows[i].setflow(0)
    

ser = serial.Serial('/dev/serial/by-id/usb-Arduino_LLC_Arduino_Nano_Every_1D01FEC651514C4630202020FF0E0F4C-if00',
                    115200)  # open serial port
mapsFun = ["kuchnia", "lazienka", "wc"]

fans = []
for i in range(3):
    fans.append(FunSwitch(i+1, mapsFun[i], ser))
    fans[i].set(False)

print(ser.name)         # check which port was really used

while True:
    line = ser.readline()   # read a '\n' terminated line
    line = line.decode('ascii')
    chunks = line.split(';')
    print(chunks)
    if chunks[0] == 'F':
        num = int(chunks[1])
        val1 = int(chunks[2])
        val2 = int(chunks[3])
        flows[num-1].setflow(val1)
    elif chunks[0] == 'W':
        num = int(chunks[1])
        val = False if int(chunks[2]) == 0 else True
        fans[num-1].set(val)

ser.close()    