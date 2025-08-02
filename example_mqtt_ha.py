import json
import os, time

import paho.mqtt.client as mqtt
import logging

clientmqtt = mqtt.Client(client_id="mydevice")
clientmqtt.username_pw_set("mqtt", "mqtt")

clientmqtt.connect("192.168.10.250", 1883, 60)
idx = 1

deviceDiscoveryConfig = \
"""{
  "dev": {
    "ids": "ea334450945afc",
    "name": "Główna Centrala 2",
    "mf": "Marcin Wiącek",
    "mdl": "python",
    "sw": "1.2",
    "sn": "ea334450945afc",
    "hw": "1.0rev3"
  },
  "o": {
    "name":"uart2mqtt",
    "sw": "2.1",
  },
  "cmps": {
    "some_unique_component_id1": {
      "p": "sensor",
      "device_class":"temperature",
      "unit_of_measurement":"°C",
      "value_template":"{{ value_json.temperature}}",
      "unique_id":"temp01ae_t"
    },
    "some_unique_id2": {
      "p": "sensor",
      "device_class":"humidity",
      "unit_of_measurement":"%",
      "value_template":"{{ value_json.humidity}}",
      "unique_id":"temp01ae_h"
    }
  },
  "state_topic":"testPyDevice/out/test_device/state",
}"""


clientmqtt.publish("homeassistant/device/test_device/config", deviceDiscoveryConfig, retain=True)
    

while True:
    payload = '{ "temperature":0.01, "humidity":22.01 }'
    clientmqtt.publish("testPyDevice/out/test_device/state", payload, retain=False)


    time.sleep(3)


