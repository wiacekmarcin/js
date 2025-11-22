#!/usr/bin/python
# -*- coding: utf-8 -*-
from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Sensor, SensorInfo

import paho.mqtt.client as mqtt
import time
import json

import os
# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, reason_code, properties):
    print(f"Connected with result code {reason_code}")
    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("hmd/sensor/energy/#")

mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
mqttc.on_connect = on_connect


mqttc.username_pw_set("mqtt", "mqtt")
mqttc.connect("192.168.10.250", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.

mqtt_settings = Settings.MQTT(client=mqttc)


class MqttConn:
    def __init__(self):
        # Configure the required parameters for the MQTT broker
        self.mqtt_settings = mqtt_settings

        # Define the device. At least one of `identifiers` or `connections` must be supplied
        self.device_info = DeviceInfo(name="EnergyCalculator", identifiers="energy_calculator_bodycha_120")


class Tariff(MqttConn):
    def __init__(self, tariff:str, short_tariff:str, who:str, who_id:str):
        super(Tariff, self).__init__()
        self.sum_energy = 0.0
        self.sum_cost = 0.0
        self.fname_e = '.%s_%s_energy.txt' % (who_id, short_tariff)
        self.fname_c = '.%s_%s_cost.txt' % (who_id, short_tariff)
        
        f_bck_e = os.path.join("../backup", self.fname_e)
        if os.path.exists(f_bck_e):
            with open(f_bck_e, 'r') as feb:
                start_energy = float(feb.readline())
        else:
            start_energy = 0
        
        f_bck_c = os.path.join("../backup", self.fname_c)
        if os.path.exists(f_bck_c):
            with open(f_bck_c, 'r') as fcb:
                start_cost = float(fcb.readline())
        else:
            start_cost = 0
        
        
        if os.path.exists(self.fname_e):
            with open(self.fname_e, 'r') as fe:
                self.sum_energy = float(fe.readline())
            self.sum_energy -= start_energy
            with open(self.fname_e, 'w+') as fe:
                fe.write('%f\n' % self.sum_energy)
        else:
            with open(self.fname_e, 'w+') as fe:
                fe.write('0\n')
        
        if os.path.exists(self.fname_c):                
            with open(self.fname_c, 'r') as fc:
                self.sum_cost = float(fc.readline())
            self.sum_cost -= start_cost
            with open(self.fname_c, 'w+') as fc:
                fc.write('%f\n' % self.sum_cost)
        else:
            with open(self.fname_c, 'w+') as fc:
                fc.write('0\n')


        energy_info = SensorInfo(name="%s energia %s taryfa" % (who, tariff),
                                 device_class="energy",
                                 state_class= "total",
                                 unit_of_measurement="kWh",
                                 device=self.device_info,
                                 unique_id="%s_energia_%s" % (who_id, short_tariff)
                                 )

        energy_settings = Settings(mqtt=mqtt_settings, entity=energy_info)
        self.energy_sensor = Sensor(energy_settings)
        
        cost_info = SensorInfo(name="%s koszt %s taryfa" % (who, tariff),
                               device_class="monetary",
                               state_class= "total",
                               unit_of_measurement="PLN",
                               device=self.device_info,
                               unique_id="%s_koszt_%s" % (who_id, short_tariff)
                               )

        cost_settings = Settings(mqtt=mqtt_settings, entity=cost_info)
        self.cost_sensor = Sensor(cost_settings)

        self.energy_sensor.set_state(self.sum_energy)
        self.cost_sensor.set_state(self.sum_cost)
        

    def calculate(self, price: float, energy: float):
        self.sum_energy += energy
        self.sum_cost += price*energy

        self.energy_sensor.set_state(self.sum_energy)
        self.cost_sensor.set_state(self.sum_cost)

        with open(self.fname_e, 'w') as fe:
            fe.write("%f\n" % self.sum_energy)
        with open(self.fname_c, 'w') as fc:
            fc.write("%f\n" % self.sum_cost)


class BothTariff(MqttConn):
    def __init__(self, who:str):
        super(BothTariff, self).__init__()
        wid = who.lower().replace(' ', '_').replace('ą','a').replace('ć','c').replace('ę','e').replace('ó','o').replace('ś','s').replace('ł','l').replace('ż','z').replace('ź','z').replace('ń','ń')
        self.day = Tariff("dzienna", "day", who, wid)
        self.night = Tariff("nocna", "night", who, wid)
        self.sum_energy = 0
        self.prev_energy = None
        self.sum_cost = 0
        self.sum_cost_g11 = 0
        self.price_g11 = 1.15
        #1.21
        #0.75

        self.fname_e = '.%s_all_energy.txt' % wid
        self.fname_c = '.%s_all_cost.txt' % wid
        self.fname_c11 = '.%s_all_cost_g11.txt' % wid
        self.fname_prev_energy = '.%s_prev_energy.txt' % wid
        


        if os.path.exists(self.fname_e):
            with open(self.fname_e, 'r') as fe:
                self.sum_energy = float(fe.readline())
        else:
            with open(self.fname_e, 'w+') as fe:
                fe.write('0\n')

        if os.path.exists(self.fname_c):                
            with open(self.fname_c, 'r') as fc:
                self.sum_cost = float(fc.readline())
        else:
            with open(self.fname_c, 'w+') as fc:
                fc.write('0\n')

        if os.path.exists(self.fname_c11):                
            with open(self.fname_c11, 'r') as fc11:
                self.sum_cost_g11 = float(fc11.readline())
        else:
            with open(self.fname_c11, 'w+') as fc11:
                fc11.write('0\n')

        if os.path.exists(self.fname_prev_energy):                 
            with open(self.fname_prev_energy, 'r') as fpe:
                self.prev_energy = float(fpe.readline())

        sensor_info = SensorInfo(name="%s suma energi" % who,
                                 device_class="energy",
                                 state_class= "total",
                                 unit_of_measurement="kWh",
                                 device=self.device_info,
                                 unique_id="%s_energy_all" % wid
                                 )

        energy_settings = Settings(mqtt=mqtt_settings, entity=sensor_info)
        self.energy_sensor = Sensor(energy_settings)

        cost_info = SensorInfo(name="%s całkowity koszt" % who,
                               device_class="monetary",
                               state_class= "total",
                               unit_of_measurement="PLN",
                               device=self.device_info,
                               unique_id="%s_cost_all" % wid
                               )

        cost_settings = Settings(mqtt=mqtt_settings, entity=cost_info)
        self.cost_sensor = Sensor(cost_settings)

        cost_info11 = SensorInfo(name="%s koszt g11" % who,
                               device_class="monetary",
                               state_class= "total",
                               unit_of_measurement="PLN",
                               device=self.device_info,
                               unique_id="%s_cost_g11" % wid
                               )

        cost_settings11 = Settings(mqtt=mqtt_settings, entity=cost_info11)
        self.cost_sensor11 = Sensor(cost_settings11)

        self.energy_sensor.set_state(self.sum_energy)
        self.cost_sensor.set_state(self.sum_cost)
        self.cost_sensor11.set_state(self.sum_cost_g11)

    def calculate(self, day: bool, price: float, energy: float):
        if self.prev_energy is None:
            self.prev_energy = float(energy)
            return

        delta = float(energy) - float(self.prev_energy)
        self.prev_energy = float(energy)
        if delta <= 0:
            return

        self.sum_energy += delta
        self.sum_cost += float(price)*delta
        self.sum_cost_g11 += float(self.price_g11)*delta

        self.energy_sensor.set_state(self.sum_energy)
        self.cost_sensor.set_state(self.sum_cost)
        self.cost_sensor11.set_state(self.sum_cost_g11)

        with open(self.fname_e, 'w') as fe:
            fe.write("%f\n" % self.sum_energy)
        with open(self.fname_c, 'w') as fc:
            fc.write("%f\n" % self.sum_cost)
        with open(self.fname_c11, 'w') as fc11:
            fc11.write("%f\n" % self.sum_cost_g11)
        with open(self.fname_prev_energy, 'w') as fprev:
            fprev.write("%f\n" % self.prev_energy)

        if day:
            self.day.calculate(float(price), delta)
        else:
            self.night.calculate(float(price), delta)

class EnergyCost(BothTariff):
    def __init__(self, who:str):
        super(EnergyCost, self).__init__(who)
        self.tariff_1 = True
        self.price = 0.0

    def setParams(self, day: bool, price: float, energy: float):
        self.tariff_1 = day
        self.price = float(price)
        self.calculate(day, float(price), float(energy))



allE = EnergyCost("Wszystko")
bramka_wifi = BothTariff("Bramka Wifi")
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
    print(message.topic, msgrec)

    if message.topic == "hmd/sensor/energy/all":
        payload = json.loads(msgrec)
        energy = payload.get('energy', 0)
        cost = payload.get('cost', 0)
        dzien = payload.get('taryfa_dzien', "on")
        allE.setParams(dzien == "on", float(cost), float(energy))
        return

    if message.topic == "hmd/sensor/energy/bramkawifi":
        bramka_wifi.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/tv":
        tv.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/centrala_sieciowa":
        centsieciowa.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/decoder_vectra":
        decoder_vectra.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/charger2":
        charger2.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/microwave":
        microwave.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/lights":
        lights.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/roaster":
        roaster.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/kettle":
        kettle.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/computer":
        computer.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/fridge":
        fridge.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/charger1":
        charger1.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/dvd":
        dvd.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/heat":
        heat.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/washing_machine":
        washing_machine.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/electric_dryer":
        electric_dryer.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/bathroom_el_socket":
        bathroom_el_socket.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/kitchen_hood":
        kitchen_hood.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/power_supply_24V_OFF":
        power_supply_24V_OFF.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/power_supply_24V_ON":
        power_supply_24V_ON.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/dishwasher":
        dishwasher.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/power_supply_guaranteed":
        power_supply_guaranteed.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/main_switch":
        main_switch.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/iron":
        iron.calculate(allE.tariff_1, allE.price, float(msgrec))
        return

    if message.topic == "hmd/sensor/energy/vacuum_cleaner":
        vacuum_cleaner.calculate(allE.tariff_1, allE.price, float(msgrec))
        return




mqttc.on_message = on_message
#mqttc.loop()
#while True:
#    time.sleep(1)

#mqttc.loop_stop() #stop loop
#mqttc.disconnect() #disconnect

mqttc.loop_forever()

