from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Switch, SwitchInfo, Light, LightInfo
from paho.mqtt.client import Client, MQTTMessage
import logging
import json
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s %(message)s'

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=FORMAT)

class MqttConn:
    def __init__(self):
        # Configure the required parameters for the MQTT broker        
        self.mqtt_settings = Settings.MQTT(host="192.168.10.250", username='mqtt', password='mqtt')

        # Define the device. At least one of `identifiers` or `connections` must be supplied
        self.device_info = DeviceInfo(name="ArduinoMega", identifiers="arduino_mega_bodycha_120")

class Ogrzewanie(MqttConn):
    def __init__(self):
        super(Ogrzewanie, self).__init__()

        # Information about the switch
        ogrz_pompa_switch_info = SwitchInfo(name="Pompa", unique_id="arduino_mega_ogrz_pompa_switch", device=self.device_info)
        ogrz_pompa_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_pompa_switch_info)
        self.ogrz_pompa_switch = Switch(ogrz_pompa_settings, self.ogrz_pompa_switch_callback)

        ogrz_salon_switch_info = SwitchInfo(name="Ogrzewanie podłogowe salon", unique_id="arduino_mega_ogrz_salon_switch", device=self.device_info)
        ogrz_salon_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_salon_switch_info)
        self.ogrz_salon_switch = Switch(ogrz_salon_settings, self.ogrz_salon_switch_callback)

        ogrz_kuchnia_switch_info = SwitchInfo(name="Ogrzewanie podłogowe kuchnia", unique_id="arduino_mega_ogrz_kuchnia_switch", device=self.device_info)
        ogrz_kuchnia_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_kuchnia_switch_info)
        self.ogrz_kuchnia_switch = Switch(ogrz_kuchnia_settings, self.ogrz_kuchnia_switch_callback)

        ogrz_lazienka_switch_info = SwitchInfo(name="Ogrzewanie podłogowe łazienka", unique_id="arduino_mega_ogrz_lazienka_switch", device=self.device_info)
        ogrz_lazienka_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_lazienka_switch_info)
        self.ogrz_lazienka_switch = Switch(ogrz_lazienka_settings, self.ogrz_lazienka_switch_callback)

        self.ligth_info = LightInfo(name="Oświetlenie pod wanną", unique_id="arduino_mega_ogrz_oswietlenie_light", device=self.device_info)
        ogrz_oswietlenie_settings = Settings(mqtt=self.mqtt_settings, entity=self.ligth_info)
        self.ogrz_oswietlenie_ligth = Light(ogrz_oswietlenie_settings, self.ogrz_oswietlenie_ligth_callback)

        ogrz_wc_switch_info = SwitchInfo(name="Ogrzewanie podłogowe wc", unique_id="arduino_mega_ogrz_wc_switch", device=self.device_info)
        ogrz_wc_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_wc_switch_info)
        self.ogrz_wc_switch = Switch(ogrz_wc_settings, self.ogrz_wc_switch_callback)

        ogrz_hol1_switch_info = SwitchInfo(name="Ogrzewanie podłogowe hol 1", unique_id="arduino_mega_ogrz_hol_1_switch", device=self.device_info)
        ogrz_hol1_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_hol1_switch_info)
        self.ogrz_hol1_switch = Switch(ogrz_hol1_settings, self.ogrz_hol1_switch_callback)

        ogrz_hol2_switch_info = SwitchInfo(name="Ogrzewanie podłogowe hol 2", unique_id="arduino_mega_ogrz_hol_2_switch", device=self.device_info)
        ogrz_hol2_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_hol2_switch_info)
        self.ogrz_hol2_switch = Switch(ogrz_hol2_settings, self.ogrz_hol2_switch_callback)

        ogrz_hol3_switch_info = SwitchInfo(name="Ogrzewanie podłogowe hol 3", unique_id="arduino_mega_ogrz_hol_3_switch", device=self.device_info)
        ogrz_hol3_settings = Settings(mqtt=self.mqtt_settings, entity=ogrz_hol3_switch_info)
        self.ogrz_hol3_switch = Switch(ogrz_hol3_settings, self.ogrz_hol3_switch_callback)


    # To receive state commands from HA, define a callback function:
    def ogrz_pompa_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("pompa_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_pompa_switch.on()
        elif payload == "OFF":
            print("pompa_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_pompa_switch.off()

    def ogrz_salon_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_salon_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_salon_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_salon_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_salon_switch.off()

    def ogrz_kuchnia_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_kuchnia_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_kuchnia_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_kuchnia_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_kuchnia_switch.off()
    
    def ogrz_lazienka_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_lazienka_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_lazienka_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_lazienka_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_lazienka_switch.off()

    def ogrz_oswietlenie_ligth_callback(self, client: Client, user_data, message: MQTTMessage):
        # Make sure received payload is JSON
        try:
            payload = json.loads(message.payload.decode())
        except ValueError:
            print("Ony JSON schema is supported for light entities!")
            return
        if "state" in payload:
            if payload["state"] == self.ligth_info.payload_on:
                ##//turn_on_my_light()
                self.ogrz_oswietlenie_ligth.on()
            else:
                ##//turn_off_my_light()
                self.ogrz_oswietlenie_ligth.off()
        else:
            print("Unknown payload")

    def ogrz_wc_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_wc_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_wc_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_wc_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_wc_switch.off()

    def ogrz_hol1_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_hol1_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_hol1_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_hol1_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_hol1_switch.off()

    def ogrz_hol2_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_hol2_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_hol2_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_hol2_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_hol2_switch.off()

    def ogrz_hol3_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            print("ogrzewanie_hol3_on")
            # Let HA know that the switch was successfully activated
            self.ogrz_hol3_switch.on()
        elif payload == "OFF":
            print("ogrzewanie_hol3_off")
            # Let HA know that the switch was successfully deactivated
            self.ogrz_hol3_switch.off()



# Instantiate the switch

o = Ogrzewanie()

# Set the initial state of the switch, which also makes it discoverable
o.ogrz_pompa_switch.off()
o.ogrz_salon_switch.off()
o.ogrz_kuchnia_switch.off()
o.ogrz_lazienka_switch.off()
o.ogrz_oswietlenie_ligth.off()
o.ogrz_hol1_switch.off()
o.ogrz_hol2_switch.off()
o.ogrz_hol3_switch.off()
while True:
    pass