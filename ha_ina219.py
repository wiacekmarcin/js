from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo
from paho.mqtt.client import Client, MQTTMessage
import logging
import time
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=FORMAT)

from ina219 import INA219
from ina219 import DeviceRangeError

SHUNT_OHMS = 0.1



class MqttConn:
    def __init__(self, number:str):
        # Configure the required parameters for the MQTT broker        
        self.mqtt_settings = Settings.MQTT(host="192.168.10.250", username='mqtt', password='mqtt')

        # Define the device. At least one of `identifiers` or `connections` must be supplied
        self.device_info = DeviceInfo(name="Ina219" % number, identifiers="raspberry_ina219" % number)

class MyIna219(MqttConn):
    def __init__(self, number:str):
        super(MyIna219, self).__init__(number)
        self.kWh = 0

        # Information about the switch
        currentinfo = SensorInfo(name="Prąd %s" % number, 
                            unique_id="ina219_%s_current" % number, 
                            device=self.device_info,
                            device_class="current",
                            unit_of_measurement="mA")
        current_settings = Settings(mqtt=self.mqtt_settings, entity=currentinfo)
        self.current = Sensor(current_settings)

        voltageinfo = SensorInfo(name="Napięcie %s" % number, 
                            unique_id="ina219_%s_voltage" % number, 
                            device=self.device_info,
                            device_class="voltage",
                            unit_of_measurement="V")
        voltage_settings = Settings(mqtt=self.mqtt_settings, entity=voltageinfo)
        self.voltage = Sensor(voltage_settings)

        powerinfo = SensorInfo(name="Moc %s" % number, 
                            unique_id="ina219_%s_power" % number, 
                            device=self.device_info,
                            device_class="power",
                            unit_of_measurement="mW")
        power_settings = Settings(mqtt=self.mqtt_settings, entity=powerinfo)
        self.power = Sensor(power_settings)

        energyinfo = SensorInfo(name="Energia %s" % number, 
                            unique_id="ina219_%s_energy" % number, 
                            device=self.device_info,
                            device_class="energy",
                            unit_of_measurement="kWh")
        energy_settings = Settings(mqtt=self.mqtt_settings, entity=energyinfo)
        self.energy = Sensor(energy_settings)


    def setPower(self, power):
        ina_m.power.set_state(ina_r.power())
        self.kWh += power / (1000 * 3600)
        self.energy.set_state(self.kWh)


# Instantiate the switch

ina_m1 = MyIna219("1")
ina_m2 = MyIna219("2")
ina_m3 = MyIna219("3")
ina_m4 = MyIna219("4")


ina_r1 = INA219(SHUNT_OHMS, busnum=1, address=0x40)
ina_r2 = INA219(SHUNT_OHMS, busnum=1, address=0x41)
ina_r3 = INA219(SHUNT_OHMS, busnum=1, address=0x42)
ina_r4 = INA219(SHUNT_OHMS, busnum=1, address=0x43)

inas = [(ina_r1, ina_m1), (ina_r2, ina_m2), (ina_r3, ina_m3), (ina_r4, ina_m4)]

ina_r1.configure()
ina_r2.configure()
ina_r3.configure()
ina_r4.configure()
while True:
    for ina in inas:
        ina_r, ina_m = ina
        ina_m.voltage.set_state(ina_r.voltage())
        ina_m.current.set_state(ina_r.current())
        ina_m.setPower(ina_r.power())
        
    time.sleep(1)
