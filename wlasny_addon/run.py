#!/usr/bin/python3
# -*- coding: utf-8 -*-
print("Running python")
from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo

from paho.mqtt.enums import CallbackAPIVersion
import paho.mqtt.client as mqtt
from datetime import datetime
import json

#DEBUG=True
DEBUG=False

if not DEBUG:
    dir_data = '/root/data/'
else:
    dir_data = './data'
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
        if not DEBUG:
            self.device_info = DeviceInfo(name="EnergyCalc2", identifiers="energy_calculator_bodycha_120")
        else:
            self.device_info = DeviceInfo(name="EnergyCalc2Test", identifiers="energy_calculator_bodycha_120")
        

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
                name="%s_energy_%s_month" % (who_id, tariff),
                #object_id="%s_energy_%s_m" % (who_id, tariff),
                unique_id="%s_energy_%s_m" % (who_id, short_tariff),
                device_class="energy",
                state_class= "total",
                unit_of_measurement="kWh",
                device=self.device_info,
        )

        energy_settings_m = Settings(mqtt=mqtt_settings, entity=energy_info_m)
        self.energy_sensor_m = Sensor(energy_settings_m)

        cost_info_m = SensorInfo(
                #name="%s koszt %s taryfa (m)" % (who, tariff),
                name="%s_cost_%s_month" % (who_id, tariff),
                #object_id="%s_cost_%s_m" % (who_id, tariff),
                device_class="monetary",
                state_class= "total",
                unit_of_measurement="PLN",
                device=self.device_info,
                unique_id="%s_cost_%s_m" % (who_id, short_tariff)
        )

        cost_settings_m = Settings(mqtt=mqtt_settings, entity=cost_info_m)
        self.cost_sensor_m = Sensor(cost_settings_m)

        energy_info_y = SensorInfo(
                #name="%s energy %s taryfa (y)" % (who, tariff),
                name="%s_energy_%s_year" % (who_id, tariff),
                unique_id="%s_energy_%s_y" % (who_id, short_tariff),
                #object_id="%s_energy_%s_y" % (who_id, tariff),
                device_class="energy",
                state_class= "total",
                unit_of_measurement="kWh",
                device=self.device_info,
        )

        energy_settings_y = Settings(mqtt=mqtt_settings, entity=energy_info_y)
        self.energy_sensor_y = Sensor(energy_settings_y)

        cost_info_y = SensorInfo(
                #name="%s koszt %s taryfa (y)" % (who, tariff),
                name="%s_cost_%s_year" % (who_id, tariff),
                #object_id="%s_cost_%s_y" % (who_id, tariff),
                device_class="monetary",
                state_class= "total",
                unit_of_measurement="PLN",
                device=self.device_info,
                unique_id="%s_cost_%s_y" % (who_id, short_tariff)
        )

        cost_settings_y = Settings(mqtt=mqtt_settings, entity=cost_info_y)
        self.cost_sensor_y = Sensor(cost_settings_y)

        self.initialize(m, y)

    def initialize(self, m, y):

        self.prev_m = m
        self.fname_e_y = dir_data + '%s_%s_energy_%d.txt' % (self.who_id, self.short_tariff, y)
        self.fname_c_y = dir_data + '%s_%s_cost_%d.txt' % (self.who_id, self.short_tariff, y)

        self.fname_e_m = dir_data + '%s_%s_energy_%02d_%d.txt' % (self.who_id, self.short_tariff, m, y)
        self.fname_c_m = dir_data + '%s_%s_cost_%02d_%d.txt' % (self.who_id, self.short_tariff, m, m)


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
            name="%s_energy_all_month" % wid,
            #object_id="%s_energy_all_m" % wid,
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
            name="%s_energy_all_year" % wid,
            #object_id="%s_energy_all_y" % wid,
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
            name="%s_cost_all_month" % wid,
            #object_id="%s_cost_all_m" % wid,
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
            name="%s_cost_all_year" % wid,
            #object_id="%s_cost_all_y" % wid,
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
            name="%s_cost_g11_month" % wid,
            #object_id="%s_cost_g11_m" % wid,
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
            name="%s_cost_g11_year" % wid,
            #object_id="%s_cost_g11_y" % wid,
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
        self.fname_e_y = dir_data + '%s_all_energy_%d.txt' % (self.wid, y)
        self.fname_e_m = dir_data + '%s_all_energy_%02d_%d.txt' % (self.wid, m, y)
        self.fname_c_y = dir_data + '%s_all_cost_%d.txt' % (self.wid, y)
        self.fname_c_m = dir_data + '%s_all_cost_%02d_%d.txt' % (self.wid, m, y)
        self.fname_c11_y = dir_data + '%s_all_cost_g11_%d.txt' % (self.wid, y)
        self.fname_c11_m = dir_data + '%s_all_cost_g11_%02d_%d.txt' % (self.wid, m, y)
        self.fname_prev_energy = dir_data + '%s_prev_energy.txt' % self.wid

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

    def parseMsg(self, topic:str, param : EnergyCost, payload: dict):
        try:
            energy = payload.get('energy', None)
            if energy is not None:
                self.calculate(param, energy)
        except:
            pass

class VirtualDevice(BothTariff):
    def __init__(self, who_s:str, wid_s=None):
        super(VirtualDevice, self).__init__(who_s, wid_s)

        self.current = {}
        self.voltage = {}
        self.power = {}
        self.all_energy = 0.0
        self.energy = {}

        entity_current = SensorInfo(
            #name="%s suma energi (m)" % who,
            name="%s_current" % self.wid,
            #object_id="%s_energy_all_m" % wid,
            device_class="current",
            state_class= "measurent",
            unit_of_measurement="A",
            device=self.device_info,
            unique_id="%s_current" % self.wid
        )

        settings_current = Settings(mqtt=mqtt_settings, entity=entity_current)
        self.sensor_current = Sensor(settings_current)
        self.sensor_current.set_state(0)

        entity_voltage = SensorInfo(
            #name="%s suma energi (m)" % who,
            name="%s_voltage" % self.wid,
            #object_id="%s_energy_all_m" % wid,
            device_class="voltage",
            state_class= "measurent",
            unit_of_measurement="V",
            device=self.device_info,
            unique_id="%s_voltage" % self.wid
        )

        settings_voltage = Settings(mqtt=mqtt_settings, entity=entity_voltage)
        self.sensor_voltage = Sensor(settings_voltage)
        self.sensor_voltage.set_state(0)

        entity_power = SensorInfo(
            #name="%s suma energi (m)" % who,
            name="%s_power" % self.wid,
            #object_id="%s_energy_all_m" % wid,
            device_class="power",
            state_class= "measurent",
            unit_of_measurement="W",
            device=self.device_info,
            unique_id="%s_power" % self.wid
        )

        settings_power = Settings(mqtt=mqtt_settings, entity=entity_power)
        self.sensor_power = Sensor(settings_power)
        self.sensor_power.set_state(0)

        entity_energy = SensorInfo(
            #name="%s suma energi (m)" % who,
            name="%s_energy" % self.wid,
            #object_id="%s_energy_all_m" % wid,
            device_class="energy",
            state_class= "Total",
            unit_of_measurement="kWh",
            device=self.device_info,
            unique_id="%s_energy" % self.wid
        )

        settings_energy = Settings(mqtt=mqtt_settings, entity=entity_energy)
        self.sensor_energy = Sensor(settings_energy)
        self.sensor_energy.set_state(0)

    def parseMsg(self, topic:str, param : EnergyCost, payload: dict):
        self.parseCurrent(topic, param, payload)
        self.parsePower(topic, param, payload)
        self.parseVoltage(topic, param, payload)
        self.parseEnergy(topic, param, payload)
        
    def parseCurrent(self, topic:str, param : EnergyCost, payload: dict):
        try:
            current = payload.get('current', 0)
            self.current[topic] = float(current)
            sumcurrent = 0           
            for curr in self.current:
                sumcurrent += self.current[curr]
            self.sensor_current.set_state(sumcurrent)
        except:
            pass

    def parsePower(self, topic:str, param : EnergyCost, payload: dict):
        try:
            power = payload.get('power', 0)
            self.power[topic] = float(power)
            sumpower = 0           
            for pow in self.power:
                sumpower += self.power[pow]
            self.sensor_power.set_state(sumpower)
        except:
            pass

    def parseVoltage(self, topic:str, param : EnergyCost, payload: dict):
        try:
            self.voltage[topic] = float(payload.get('voltage', 0))
            maxvoltage = 0           
            for voltage in self.voltage:
                if self.voltage[voltage] > maxvoltage:
                    maxvoltage = self.voltage[voltage]
            self.sensor_voltage.set_state(maxvoltage)
        except:
            pass

    def parseEnergy(self, topic:str, params: EnergyCost, payload: dict):
        try:
            energy = float(payload.get('energy', 0))
            if energy == 0:
                return
            
            if topic not in self.energy.keys():
                self.energy[topic] = energy
                return
            
            if self.energy[topic] == energy:
                return
            
            delta = energy - self.energy[topic]
            self.energy[topic] = energy
            if delta <= 0:
                return
            
            self.all_energy += delta 
            print(f"{topic} ({self.energy[topic]}) all={self.all_energy}")

            
            self.sensor_energy.set_state(self.all_energy)
            self.calculate(params, self.all_energy)
        except:
            pass


param = EnergyCost()
centrala_sieciowa = VirtualDevice("centrala_sieciowa", "Centrala sieciowa")
tv_rozrywka = VirtualDevice("rozrywka", "TV Rozrywka")
inne_gniazda = VirtualDevice("inne_gniazda", "Pozostały sprzęt agd")
kuchnia_gniazda = VirtualDevice("kuchnia_gniazda", "Sprzęt AGD kuchnia")
objects = [
    ('zigbee2mqtt/energy',              [BothTariff("energy_all", "Całe zużycie")]),
    ('zigbee2mqtt/bathroom_el_socket',  [BothTariff("bathroom_el_socket", "Gniazda łazienka")]),
    ('zigbee2mqtt/brama_vectra',        [BothTariff("brama_vectra", "Router Vectry"), centrala_sieciowa]),
    ('zigbee2mqtt/charger_1',           [BothTariff("charger_1", "Ładowarka tel. 1"), inne_gniazda]),
    ('zigbee2mqtt/charger_2',           [BothTariff("charger_2", "Ładowarka tel. 2"), inne_gniazda]),
    ('zigbee2mqtt/computer',            [BothTariff("computer", "Komputer"), inne_gniazda]),
    ('zigbee2mqtt/dishwasher',          [BothTariff("dishwasher", "Zmywarka"), kuchnia_gniazda]),
    ('zigbee2mqtt/dvd_player',          [BothTariff("dvd_player", "Odtwarzacz DVD"), tv_rozrywka]),
    ('zigbee2mqtt/electric_dryer',      [BothTariff("electric_dryer", "Szuszarka elektryczna")]),
    ('zigbee2mqtt/fridge',              [BothTariff("fridge", "Lodówka")]),
    ('zigbee2mqtt/heating',             [BothTariff("heating", "Ogrzewanie")]),
    ('zigbee2mqtt/choinka',             [BothTariff("choinka", "Choinka"), inne_gniazda]),
    ('zigbee2mqtt/iron',                [BothTariff("iron", "Żelazko"),inne_gniazda]),
    ('zigbee2mqtt/kitchen_hood',        [BothTariff("kitchen_hood", "Okap w kuchni"), kuchnia_gniazda]),
    ('zigbee2mqtt/light',               [BothTariff("light", "Oświetlenie")]),
    ('zigbee2mqtt/main_power_switch',   [BothTariff("main_power_switch", "Wyłącznik główny"), centrala_sieciowa]),
    ('zigbee2mqtt/microwave',           [BothTariff("microwave", "Mikrofala"), kuchnia_gniazda]),
    ('zigbee2mqtt/power_24v_on',        [BothTariff("power_24v_on", "Zasilacz 24V on"), centrala_sieciowa]),
    ('zigbee2mqtt/power_24v_off',       [BothTariff("power_24v_off", "Zasilacz 24V off"), centrala_sieciowa]),
    ('zigbee2mqtt/power_guaranted',     [BothTariff("power_guaranted", "Zasilanie gwarantowane"), centrala_sieciowa]),
    ('zigbee2mqtt/reserved_lte',        [BothTariff("reserved_lte", "Zapasowy router LTE"), centrala_sieciowa]),
    ('zigbee2mqtt/roaster',             [BothTariff("roaster", "Piekarnik"), kuchnia_gniazda]),
    ('zigbee2mqtt/server_ha',           [BothTariff("server_ha", "Server HA"), centrala_sieciowa]),
    ('zigbee2mqtt/server_nas',          [BothTariff("server_nas", "Server Synology"), centrala_sieciowa]),
    ('zigbee2mqtt/teapot_electric',     [BothTariff("teapot_electric", "Czajnik elektryczny"), kuchnia_gniazda]),
    ('zigbee2mqtt/tv_samsung',          [BothTariff("tv_samsung", "Telewizor Samsung"), tv_rozrywka]),
    ('zigbee2mqtt/vacuum_cleaner',      [BothTariff("vacuum_cleaner", "Odkurzacz"), inne_gniazda]),
    ('zigbee2mqtt/vectra_decoder',      [BothTariff("vectra_decoder", "Dekoder Vectry"), tv_rozrywka]),
    ('zigbee2mqtt/washing_machine',     [BothTariff("washing_machine", "Pralka")]),
    ('zigbee2mqtt/wifi_access_point_1', [BothTariff("wifi_access_point_1", "Bramka WiFi 1"), centrala_sieciowa]),
    
]


# sensor.power_tauron_g12w_current_price
# sensor.moc_pobrana
decoder = json.JSONDecoder()


def on_message(client, userdata, message):

    msgrec = message.payload.decode("utf-8")
    #print(message.topic, msgrec)

    if message.topic == "hmd/sensor/tauron_taryfa":
        payload = json.loads(msgrec)
        try:
            param.setParams(payload['taryfa'] == 'dzienna', float(payload['price']), float(payload['g11']))
            print(payload)
        except:
            return
        #day: bool, price: float, price_g11:float

    for topic, objs in objects:
        if message.topic == topic:
            payload = json.loads(msgrec)
            for object in objs:
                object.parseMsg(topic, param, payload)
            break





mqttc.on_message = on_message
#mqttc.loop()
#while True:
#    time.sleep(1)

#mqttc.loop_stop() #stop loop
#mqttc.disconnect() #disconnect
print("running")
mqttc.loop_forever()

