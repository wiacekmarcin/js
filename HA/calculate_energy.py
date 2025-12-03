#!/usr/bin/python
# -*- coding: utf-8 -*-
from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo

from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt
from datetime import datetime
import json

import os
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("zigbee2mqtt/#")
    client.subscribe("hmd/sensor/tauron_taryfa")

mqttc = mqtt.Client(CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect


mqttc.username_pw_set("mqtt", "mqtt")
mqttc.connect("192.168.10.250", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

mqtt_settings = Settings.MQTT(client=mqttc)

try:
    os.mkdir("data")
except:
    pass    
class MqttConn:
    def __init__(self):
        # Configure the required parameters for the MQTT broker
        self.mqtt_settings = mqtt_settings

        # Define the device. At least one of `identifiers` or `connections` must be supplied
        self.device_info = DeviceInfo(name="ECalc", identifiers="energy_calculator_bodycha_120")

class EnergyCost():
    def __init__(self):
        self.tariff_1 = False
        self.price = 0.70
        self.price_g11 = 1.15

    def setParams(self, day: bool, price: float, price_g11:float):
        self.tariff_1 = day
        self.price = float(price)
        self.price_g11 = float(price_g11)
class Tariff(MqttConn):
    def __init__(self, tariff:str, short_tariff:str, who:str, who_id:str):
        super(Tariff, self).__init__()
        self.sum_energy_y = 0.0
        self.sum_cost_y = 0.0
        self.sum_energy_m = 0.0
        self.sum_cost_m = 0.0

        dt = datetime.now()
        y = dt.year
        m = dt.month

        self.who_id = who_id
        self.short_tariff = short_tariff
        self.prev_m = m

        energy_info_m = SensorInfo(
                #name="%s energy %s taryfa (m)" % (who, tariff),
                name="%s_energy_%s_m" % (who_id, tariff),
                object_id="%s_energy_%s_m" % (who_id, tariff),
                unique_id="%s_energy_%s_m" % (who_id, tariff),
                device_class="energy",
                state_class= "total",
                unit_of_measurement="kWh",
                device=self.device_info,
        )

        energy_settings_m = Settings(mqtt=mqtt_settings, entity=energy_info_m)
        self.energy_sensor_m = Sensor(energy_settings_m)
        
        cost_info_m = SensorInfo(
                #name="%s koszt %s taryfa (m)" % (who, tariff),
                name="%s_cost_%s_m" % (who_id, tariff),
                object_id="%s_cost_%s_m" % (who_id, tariff),
                device_class="monetary",
                state_class= "total",
                unit_of_measurement="PLN",
                device=self.device_info,
                unique_id="%s_cost_%s_m" % (who_id, tariff)
        )

        cost_settings_m = Settings(mqtt=mqtt_settings, entity=cost_info_m)
        self.cost_sensor_m = Sensor(cost_settings_m)

        energy_info_y = SensorInfo(
                #name="%s energy %s taryfa (y)" % (who, tariff),
                name="%s_energy_%s_y" % (who_id, tariff),
                unique_id="%s_energy_%s_y" % (who_id, tariff),
                object_id="%s_energy_%s_y" % (who_id, tariff),
                device_class="energy",
                state_class= "total",
                unit_of_measurement="kWh",
                device=self.device_info,
        )

        energy_settings_y = Settings(mqtt=mqtt_settings, entity=energy_info_y)
        self.energy_sensor_y = Sensor(energy_settings_y)
        
        cost_info_y = SensorInfo(
                #name="%s koszt %s taryfa (y)" % (who, tariff),
                name="%s_cost_%s_y" % (who_id, tariff),
                object_id="%s_cost_%s_y" % (who_id, tariff),
                device_class="monetary",
                state_class= "total",
                unit_of_measurement="PLN",
                device=self.device_info,
                unique_id="%s_cost_%s_y" % (who_id, tariff)
        )

        cost_settings_y = Settings(mqtt=mqtt_settings, entity=cost_info_y)
        self.cost_sensor_y = Sensor(cost_settings_y)

        cost_info_g11_m = SensorInfo(
                #name="%s koszt g11 (m)" % (who),
                name="%s_koszt_g11_m" % (who_id),
                object_id="%s_koszt_g11_m" % (who_id),
                device_class="monetary",
                state_class= "total",
                unit_of_measurement="PLN",
                device=self.device_info,
                unique_id="%s_koszt_g11_m" % (who_id)
        )

        cost_settings_g11_m = Settings(mqtt=mqtt_settings, entity=cost_info_g11_m)
        self.cost_sensor_g11_m = Sensor(cost_settings_g11_m)

        self.initialize(m, y)

    def initialize(self, m, y):
        
        self.prev_m = m
        self.fname_e_y = 'data/%s_%s_energy_%d.txt' % (self.who_id, self.short_tariff, y)
        self.fname_c_y = 'data/%s_%s_cost_%d.txt' % (self.who_id, self.short_tariff, y)
        
        self.fname_e_m = 'data/%s_%s_energy_%02d_%d.txt' % (self.who_id, self.short_tariff, m, y)
        self.fname_c_m = 'data/%s_%s_cost_%02d_%d.txt' % (self.who_id, self.short_tariff, m, m)
        

        if os.path.exists(self.fname_e_y):
            with open(self.fname_e_y, 'r') as fe:
                self.sum_energy_y = float(fe.readline())
        else:
            self.sum_energy_y = 0.0
            with open(self.fname_e_y, 'w+') as fe:
                fe.write('0\n')
        
        if os.path.exists(self.fname_c_y):                
            with open(self.fname_c_y, 'r') as fc:
                self.sum_cost_y = float(fc.readline())
        else:
            self.sum_cost_y = 0.0
            with open(self.fname_c_y, 'w+') as fc:
                fc.write('0\n')
        
        if os.path.exists(self.fname_e_m):
            with open(self.fname_e_m, 'r') as fe:
                self.sum_energy_m = float(fe.readline())
        else:
            self.sum_energy_m = 0.0
            with open(self.fname_e_m, 'w+') as fe:
                fe.write('0\n')
        
        if os.path.exists(self.fname_c_m):                
            with open(self.fname_c_m, 'r') as fc:
                self.sum_cost_m = float(fc.readline())
        else:
            self.sum_cost_m = 0.0
            with open(self.fname_c_m, 'w+') as fc:
                fc.write('0\n')

        self.energy_sensor_m.set_state(self.sum_energy_m)
        self.cost_sensor_m.set_state(self.sum_cost_m)
        self.energy_sensor_y.set_state(self.sum_energy_y)
        self.cost_sensor_y.set_state(self.sum_cost_y)
        

    def calculate(self, price: float, energy: float):
        
        dt = datetime.now()
        y = dt.year
        m = dt.month

        if m != self.prev_m:
            self.initialize(m, y)

        self.sum_energy_m += energy
        self.sum_cost_m += price*energy
        self.sum_energy_y += energy
        self.sum_cost_y += price*energy

        self.energy_sensor_m.set_state(self.sum_energy_m)
        self.cost_sensor_m.set_state(self.sum_cost_m)
        self.energy_sensor_y.set_state(self.sum_energy_y)
        self.cost_sensor_y.set_state(self.sum_cost_y)

        with open(self.fname_e_y, 'w') as fey:
            fey.write("%f\n" % self.sum_energy_y)
        with open(self.fname_e_m, 'w') as fem:
            fem.write("%f\n" % self.sum_energy_m)
        with open(self.fname_c_y, 'w') as fcy:
            fcy.write("%f\n" % self.sum_cost_y)
        with open(self.fname_c_m, 'w') as fcm:
            fcm.write("%f\n" % self.sum_cost_m)


class BothTariff(MqttConn):
    def __init__(self, who_s:str, wid_s=None):
        super(BothTariff, self).__init__()
        if wid_s is None:
            wid = who_s.lower().replace(' ', '_').replace('ą','a').replace('ć','c').replace('ę','e').replace('ó','o').replace('ś','s').replace('ł','l').replace('ż','z').replace('ź','z').replace('ń','ń')
            who = who_s
        else:
            wid = who_s
            who = wid_s

        self.day = Tariff("dzienna", "day", who, wid)
        self.night = Tariff("nocna", "night", who, wid)
        self.prev_energy = None
        self.sum_energy_y = 0
        self.sum_energy_m = 0
        self.sum_cost_y = 0
        self.sum_cost_m = 0
        self.sum_cost_g11_y = 0
        self.sum_cost_g11_m = 0
        

        dt = datetime.now()
        y = dt.year
        m = dt.month

        self.wid = wid
        self.prev_m = m
        #self.price_g11 = 1.15
        #1.21
        #0.75

        sensor_info_m = SensorInfo(
            #name="%s suma energi (m)" % who,
            name="%s_energy_all_m" % wid,
            object_id="%s_energy_all_m" % wid,
            device_class="energy",
            state_class= "total",
            unit_of_measurement="kWh",
            device=self.device_info,
            unique_id="%s_energy_all_m" % wid
        )

        energy_settings_m = Settings(mqtt=mqtt_settings, entity=sensor_info_m)
        self.energy_sensor_m = Sensor(energy_settings_m)

        sensor_info_y = SensorInfo(
            #name="%s suma energi (y)" % who,
            name="%s_energy_all_y" % wid,
            object_id="%s_energy_all_y" % wid,
            device_class="energy",
            state_class= "total",
            unit_of_measurement="kWh",
            device=self.device_info,
            unique_id="%s_energy_all_y" % wid
        )

        energy_settings_y = Settings(mqtt=mqtt_settings, entity=sensor_info_y)
        self.energy_sensor_y = Sensor(energy_settings_y)

        cost_info_m = SensorInfo(
            #name="%s całkowity koszt (m)" % who,
            name="%s_cost_all_m" % wid,
            object_id="%s_cost_all_m" % wid,
            device_class="monetary",
            state_class= "total",
            unit_of_measurement="PLN",
            device=self.device_info,
            unique_id="%s_cost_all_m" % wid
        )

        cost_settings_m = Settings(mqtt=mqtt_settings, entity=cost_info_m)
        self.cost_sensor_m = Sensor(cost_settings_m)


        cost_info_y = SensorInfo(
            #name="%s całkowity koszt (y)" % who,
            name="%s_cost_all_y" % wid,
            object_id="%s_cost_all_y" % wid,
            device_class="monetary",
            state_class= "total",
            unit_of_measurement="PLN",
            device=self.device_info,
            unique_id="%s_cost_all_y" % wid
        )

        cost_settings_y = Settings(mqtt=mqtt_settings, entity=cost_info_y)
        self.cost_sensor_y = Sensor(cost_settings_y)

        cost_info11_m = SensorInfo(
            #name="%s koszt g11 (m)" % who,
            name="%s_cost_g11_m" % wid,
            object_id="%s_cost_g11_m" % wid,
            device_class="monetary",
            state_class= "total",
            unit_of_measurement="PLN",
            device=self.device_info,
            unique_id="%s_cost_g11_m" % wid
        )

        cost_settings11_m = Settings(mqtt=mqtt_settings, entity=cost_info11_m)
        self.cost_sensor11_m = Sensor(cost_settings11_m)

        cost_info11_y = SensorInfo(
            #name="%s koszt g11 (y)" % who,
            name="%s_cost_g11_y" % wid,
            object_id="%s_cost_g11_y" % wid,
            device_class="monetary",
            state_class= "total",
            unit_of_measurement="PLN",
            device=self.device_info,
            unique_id="%s_cost_g11_y" % wid
                               )

        cost_settings11_y = Settings(mqtt=mqtt_settings, entity=cost_info11_y)
        self.cost_sensor11_y = Sensor(cost_settings11_y)
        self.initialize(m, y)

    def initialize(self, m, y):
        self.prev_m = m
        self.fname_e_y = 'data/%s_all_energy_%d.txt' % (self.wid, y)
        self.fname_e_m = 'data/%s_all_energy_%02d_%d.txt' % (self.wid, m, y)
        self.fname_c_y = 'data/%s_all_cost_%d.txt' % (self.wid, y)
        self.fname_c_m = 'data/%s_all_cost_%02d_%d.txt' % (self.wid, m, y)
        self.fname_c11_y = 'data/%s_all_cost_g11_%d.txt' % (self.wid, y)
        self.fname_c11_m = 'data/%s_all_cost_g11_%02d_%d.txt' % (self.wid, m, y)
        self.fname_prev_energy = 'data/%s_prev_energy.txt' % self.wid
        
        if os.path.exists(self.fname_e_y):
            with open(self.fname_e_y, 'r') as fey:
                self.sum_energy_y = float(fey.readline())
        else:
            self.sum_energy_y = 0.0
            with open(self.fname_e_y, 'w+') as fey:
                fey.write('0\n')

        if os.path.exists(self.fname_e_m):
            with open(self.fname_e_m, 'r') as fem:
                self.sum_energy_m = float(fem.readline())
        else:
            self.sum_energy_m = 0.0
            with open(self.fname_e_m, 'w+') as fem:
                fem.write('0\n')

        if os.path.exists(self.fname_c_y):                
            with open(self.fname_c_y, 'r') as fcy:
                self.sum_cost_y = float(fcy.readline())
        else:
            self.sum_cost_y = 0
            with open(self.fname_c_y, 'w+') as fcy:
                fcy.write('0\n')

        if os.path.exists(self.fname_c_m):                
            with open(self.fname_c_m, 'r') as fcm:
                self.sum_cost_m = float(fcm.readline())
        else:
            self.sum_cost_m = 0
            with open(self.fname_c_m, 'w+') as fcm:
                fcm.write('0\n')

        if os.path.exists(self.fname_c11_y):                
            with open(self.fname_c11_y, 'r') as fc11y:
                self.sum_cost_g11_y = float(fc11y.readline())
        else:
            self.sum_cost_g11_y = 0
            with open(self.fname_c11_y, 'w+') as fc11y:
                fc11y.write('0\n')

        if os.path.exists(self.fname_c11_m):                
            with open(self.fname_c11_m, 'r') as fc11m:
                self.sum_cost_g11_m = float(fc11m.readline())
        else:
            self.sum_cost_g11_m = 0
            with open(self.fname_c11_m, 'w+') as fc11m:
                fc11m.write('0\n')

        if os.path.exists(self.fname_prev_energy):                 
            with open(self.fname_prev_energy, 'r') as fpe:
                self.prev_energy = float(fpe.readline())



        self.energy_sensor_y.set_state(self.sum_energy_y)
        self.energy_sensor_m.set_state(self.sum_energy_m)
        self.cost_sensor_y.set_state(self.sum_cost_y)
        self.cost_sensor_m.set_state(self.sum_cost_m)
        self.cost_sensor11_y.set_state(self.sum_cost_g11_y)
        self.cost_sensor11_m.set_state(self.sum_cost_g11_m)

    def calculate(self, ob : EnergyCost, energy: float):
        day = ob.tariff_1
        price = ob.price
        price_g11 = ob.price_g11
        dt = datetime.now()
        y = dt.year
        m = dt.month

        if m != self.prev_m:
            self.initialize(m, y)
        
        if energy == 0:
            return 
        
        if self.prev_energy is None:
            self.prev_energy = float(energy)
            return

        delta = float(energy) - float(self.prev_energy)
        if delta <= 0:
            return
        self.prev_energy = float(energy)

        self.sum_energy_y += delta
        self.sum_energy_m += delta
        self.sum_cost_y += float(price)*delta
        self.sum_cost_m += float(price)*delta
        self.sum_cost_g11_y += float(price_g11)*delta
        self.sum_cost_g11_m += float(price_g11)*delta

        self.energy_sensor_y.set_state(self.sum_energy_y)
        self.energy_sensor_m.set_state(self.sum_energy_m)
        self.cost_sensor_y.set_state(self.sum_cost_y)
        self.cost_sensor_m.set_state(self.sum_cost_m)
        self.cost_sensor11_y.set_state(self.sum_cost_g11_y)
        self.cost_sensor11_m.set_state(self.sum_cost_g11_m)

        with open(self.fname_e_y, 'w') as fey:
            fey.write("%f\n" % self.sum_energy_y)
        with open(self.fname_e_m, 'w') as fem:
            fem.write("%f\n" % self.sum_energy_m)
        with open(self.fname_c_y, 'w') as fcy:
            fcy.write("%f\n" % self.sum_cost_y)
        with open(self.fname_c_m, 'w') as fcm:
            fcm.write("%f\n" % self.sum_cost_m)
        with open(self.fname_c11_y, 'w') as fc11y:
            fc11y.write("%f\n" % self.sum_cost_g11_y)
        with open(self.fname_c11_m, 'w') as fc11m:
            fc11m.write("%f\n" % self.sum_cost_g11_m)
        with open(self.fname_prev_energy, 'w') as fprev:
            fprev.write("%f\n" % self.prev_energy)

        if day:
            self.day.calculate(float(price), delta)
        else:
            self.night.calculate(float(price), delta)



param = EnergyCost()
allE = BothTariff("Wszystko")
objects = [
    ('zigbee2mqtt/energy',              BothTariff("energys_all", "Całe zużycie")),
    ('zigbee2mqtt/wifi_access_point_1', BothTariff("wifi_access_point_1", "Bramka WiFi 1")),
    ('zigbee2mqtt/heating',             BothTariff("heating", "Ogrzewanie")),
    ('zigbee2mqtt/power_24v_on',        BothTariff("power_24v_on", "Zasilacz 24V on")),
    ('zigbee2mqtt/power_24v_off',       BothTariff("power_24v_off", "Zasilacz 24V off")),
    ('zigbee2mqtt/light',               BothTariff("light", "Oświetlenie")),
    ('zigbee2mqtt/power_guaranted',     BothTariff("power_guaranted", "Zasilanie gwarantowane")),
    ('zigbee2mqtt/roaster',             BothTariff("roaster", "Piekarnik")),
    ('zigbee2mqtt/main_power_switch',   BothTariff("main_power_switch", "Wyłącznik główny")),
    ('zigbee2mqtt/electric_dryer',      BothTariff("electric_dryer", "Szuszarka elektryczna")),
    ('zigbee2mqtt/teapot_electric',     BothTariff("teapot_electric", "Szuszarka elektryczna")),
    ('zigbee2mqtt/vectra_decoder',      BothTariff("vectra_decoder", "Dekoder Vectry")),
    ('zigbee2mqtt/charger_1',           BothTariff("charger_1", "Ładowarka tel. 1")),
    ('zigbee2mqtt/charger_2',           BothTariff("charger_2", "Ładowarka tel. 2")),
    ('zigbee2mqtt/microwave',           BothTariff("microwave", "Mikrofala")),
    ('zigbee2mqtt/dvd_player',          BothTariff("microwave", "Odtwarzacz DVD")),
    ('zigbee2mqtt/tv_samsung',          BothTariff("tv_samsung", "Telewizor Samsung")),
    ('zigbee2mqtt/washing_machine',     BothTariff("washing_machine", "Pralka")),
    ('zigbee2mqtt/bathroom_el_socket',  BothTariff("bathroom_el_socket", "Gniazda łazienka")),
    ('zigbee2mqtt/kitchen_hood',        BothTariff("kitchen_hood", "Okap w kuchni")),
    ('zigbee2mqtt/iron',                BothTariff("iron", "Żelazko")),
    ('zigbee2mqtt/dishwasher',          BothTariff("dishwasher", "Zmywarka")),
    ('zigbee2mqtt/brama_vectra',        BothTariff("brama_vectra", "Router Vectry")),
    ('zigbee2mqtt/Centrala sieciowa',   BothTariff("Centrala sieciowa", "Centrala sieciowa")),
    ('zigbee2mqtt/fridge',              BothTariff("fridge", "Lodówka")),
    ('zigbee2mqtt/vacuum_cleaner',      BothTariff("vacuum_cleaner", "Odkurzacz")),
    ('zigbee2mqtt/computer',            BothTariff("computer", "Komputer")),
]


tv = BothTariff("Samsung TV")
centsieciowa = BothTariff("Centrala Sieciowa")
decoder_vectra = BothTariff("Dekoder Vectry")
charger2 = BothTariff("Ładow. telef. 2")
microwave = BothTariff("Mikrofala")
lights = BothTariff("Oświetlenie")
roaster = BothTariff("Piekarnik")
kettle = BothTariff("Czajnik")
computer = BothTariff("Komputer")
fridge = BothTariff("Lodówka")
charger1 = BothTariff("Ładow. telef. 1")
dvd = BothTariff("Odtwarzacz DVD")
heat = BothTariff("Ogrzewanie")
washing_machine = BothTariff("Pralka")
electric_dryer = BothTariff("Szuszarka el.")
bathroom_el_socket = BothTariff("Gniazda łazienka")
kitchen_hood = BothTariff("Okap")
power_supply_24V_OFF = BothTariff("Zasilacz 24V off")
power_supply_24V_ON = BothTariff("Zasilacz 24V on")
dishwasher = BothTariff("Zmywarka")
power_supply_guaranteed = BothTariff("Zasilanie gwarantowane")
main_switch = BothTariff("Włącznik główny")
iron = BothTariff("Żelazko")
vacuum_cleaner = BothTariff("Odkurzacz")


# sensor.power_tauron_g12w_current_price
# sensor.moc_pobrana
decoder = json.JSONDecoder()


def on_message(client, userdata, message):

    msgrec = message.payload.decode("utf-8")
    #print(message.topic, msgrec)

    if message.topic == "hmd/sensor/tauron_taryfa":
        payload = json.loads(msgrec)
        param.setParams(payload['taryfa'] == 'dzienna', float(payload['price']), float(payload['g11']))
        print(payload)
        #day: bool, price: float, price_g11:float

    for topic, o in objects:
        if message.topic == topic:
            payload = json.loads(msgrec)
            o.calculate(param, float(payload['energy']))
            break
    




mqttc.on_message = on_message
#mqttc.loop()
#while True:
#    time.sleep(1)

#mqttc.loop_stop() #stop loop
#mqttc.disconnect() #disconnect

mqttc.loop_forever()

