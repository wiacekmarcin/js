import json
import os
from collections import deque
from unittest import mock

import time
import board
from adafruit_ina219 import ADCResolution, BusVoltageRange, INA219

import paho.mqtt.client as mqtt
import logging

i2c_bus = board.I2C()  # uses board.SCL and board.SDA
# i2c_bus = board.STEMMA_I2C()  # For using the built-in STEMMA QT connector on a microcontroller

ina219_list = [INA219(i2c_bus, 0x40), INA219(i2c_bus, 0x41), INA219(i2c_bus, 0x42), INA219(i2c_bus, 0x43)]
ina219_list[0].set_calibration_32V_2A()
ina219_list[1].set_calibration_32V_2A()
ina219_list[2].set_calibration_32V_2A()
ina219_list[3].set_calibration_32V_2A()


ina219_list[2].bus_voltage_range = BusVoltageRange.RANGE_16V
ina219_list[3].bus_voltage_range = BusVoltageRange.RANGE_16V

for ina219 in ina219_list:
        # display some of the advanced field (just to test)
        #print("Config register:")
        #print("  bus_voltage_range:    0x%1X" % ina219.bus_voltage_range)
        #print("  gain:                 0x%1X" % ina219.gain)
        #print("  bus_adc_resolution:   0x%1X" % ina219.bus_adc_resolution)
        #print("  shunt_adc_resolution: 0x%1X" % ina219.shunt_adc_resolution)
        #print("  mode:                 0x%1X" % ina219.mode)
        #print("")

        # optional : change configuration to use 32 samples averaging for both bus voltage and shunt voltage
        ina219.bus_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        ina219.shunt_adc_resolution = ADCResolution.ADCRES_12BIT_32S
        # optional : change voltage range to 16V
        # ina219.bus_voltage_range = BusVoltageRange.RANGE_16V





infoMap = ["24V", "24V ON/OFF", "Router TPLink", "Brama Vectra"]
configMap = {}


clientmqtt = mqtt.Client(client_id="ina219CID")
clientmqtt.connect("192.168.10.254", 1883, 60)
idx = 1
for kanal in infoMap:
    voltageRasCPUConfig = \
"""{
   "device_class":"voltage",
   "state_topic":"ina219/sensor/data/ina219_%d/state",
   "unit_of_measurement":"V",
   "value_template":"{{ value_json.voltage }}",
   "unique_id":"domoticz_voltage(%s)",
   "device":{
      "identifiers":[
          "domoticz_ina219.voltage.%d"
      ],
      "name":"Napiecie %s",
   }
}""" % (idx, kanal.replace(" ",""), idx, kanal)

    currentRasCPUConfig = \
"""{
   "device_class":"current",
   "state_topic":"ina219/sensor/data/ina219_%d/state",
   "unit_of_measurement":"A",
   "value_template":"{{ value_json.current }}",
   "unique_id":"domoticz_current(%s)",
   "device":{
      "identifiers":[
          "domoticz_ina219.current.%d"
      ],
     "name":"Prad %s",
   }
}""" % (idx, kanal.replace(" ",""), idx, kanal)


    powerRasCPUConfig = \
"""{
   "device_class":"power",
   "state_topic":"ina219/sensor/data/ina219_%d/state",
   "unit_of_measurement":"W",
   "value_template":"{{ value_json.power }}",
   "unique_id":"domoticz_power(%s)",
   "device":{
      "identifiers":[
          "domoticz_ina219.power.%d"
      ],
     "name":"Moc %s",
   }
}"""  % (idx, kanal.replace(" ",""), idx, kanal)

    energyRasCPUConfig = \
"""{
   "device_class":"energy",
   "state_topic":"ina219/sensor/data/ina219_%d/state",
   "unit_of_measurement":"kWh",
   "value_template":"{{ value_json.energy }}",
   "unique_id":"domoticz_energy(%s)",
   "device":{
      "identifiers":[
          "domoticz_ina219.energy.%d"
      ],
     "name":"Energia %s",
   }
}"""  % (idx, kanal.replace(" ",""), idx, kanal)

    clientmqtt.publish("ina219/sensor/SensorConfig/Voltage%dConfig/config" % idx, voltageRasCPUConfig)
    clientmqtt.publish("ina219/sensor/SensorConfig/Current%dConfig/config" % idx, currentRasCPUConfig)
    clientmqtt.publish("ina219/sensor/SensorConfig/Power%dConfig/config" % idx, powerRasCPUConfig)
    clientmqtt.publish("ina219/sensor/SensorConfig/Energy%dConfig/config" % idx, energyRasCPUConfig)
    idx += 1
    
energyAll = [0, 0, 0, 0]
while True:
	sensor_id = 1
	for ina219 in ina219_list:
		bus_voltage = ina219.bus_voltage  # voltage on V- (load side)
		shunt_voltage = ina219.shunt_voltage  # voltage between V+ and V- across the shunt
		current = ina219.current  # current in mA
		power = ina219.power  # power in watts

		# INA219 measure bus voltage on the load side. So PSU voltage = bus_voltage + shunt_voltage
		#print("Voltage (VIN+) : {:6.3f}   V".format(bus_voltage + shunt_voltage))
		#print("Voltage (VIN-) : {:6.3f}   V".format(bus_voltage))
		#print("Shunt Voltage  : {:8.5f} V".format(shunt_voltage))
		#print("Shunt Current  : {:7.4f}  A".format(current / 1000))
		#print("Power Calc.    : {:8.5f} W".format(bus_voltage * (current / 1000)))
		#print("Power Register : {:6.3f}   W".format(power))
		#print("---------------------------")


		dictValue = {}
		dictValue["voltage"] = "{:6.3f}".format(bus_voltage + shunt_voltage)
		dictValue["current"] = "{:7.4f}".format(current / 1000)
		dictValue["power"] = "{:6.3f}".format(power)
		energyAll[sensor_id-1] += power / 3600000
		dictValue["energy"] = "{:3.6f}".format(energyAll[sensor_id-1])
		payload = '{ "power":%(power)s, "voltage":%(voltage)s, "current" : %(current)s, "energy" : %(energy)s }' % (dictValue)
		clientmqtt.publish("ina219/sensor/data/ina219_%d/state" % sensor_id, payload)
		sensor_id += 1


		# Check internal calculations haven't overflowed (doesn't detect ADC overflows)
		if ina219.overflow:
			print("Internal Math Overflow Detected!")
			print("")

	time.sleep(1)



