from ha_mqtt_discoverable import Settings, DeviceInfo
from ha_mqtt_discoverable.sensors import Switch, SwitchInfo, Light, LightInfo
from paho.mqtt.client import Client, MQTTMessage
import logging
import json
logger = logging.getLogger(__name__)
FORMAT = '%(asctime)s %(message)s'
from threading import Lock
import serial

logging.basicConfig(filename='debug.log', level=logging.DEBUG, format=FORMAT)
#fpath = '/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0'
fpath='/dev/serial/by-id/usb-1a86_USB_Serial-if00-port0'
ser = serial.Serial(fpath, 115200, 8, "N", 1,  1.0)

P_SALON_TV=26
P_SW_KW_PRYSZNIC=27
P_SW_KW_WANNA=28
P_T_KALORYFER=29
P_T_SALON=30
P_OSW_WANNA=31
P_T_KUCHNIA=32
P_T_LAZIENKA=33
P_POMPA=34

P_HOL_C=35
P_WC=36
P_HOL_A=37
P_HOL_B=38

P_WIATRAK_1=39
P_WIATRAK_2=40

serlock = Lock()
def setDigital(dig:int, val:int) -> bool:
    with serlock:
        cmd_on = ("S%d=%d;\r\n" % (dig, val)).encode('ascii')
        print(cmd_on)
        ser.write(cmd_on)
        
        line = ser.readline()
        line = line.decode('ascii')
        line = line.split(';')
        print(line)
        return line[0] == "OK"



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

        wiatrak_lazienka_switch_info = SwitchInfo(name="Wiatrak łazienka", unique_id="arduino_mega_wiatrak_lazienka_switch", device=self.device_info)
        wiatrak_lazienka_settings = Settings(mqtt=self.mqtt_settings, entity=wiatrak_lazienka_switch_info)
        self.wiatrak_lazienka_switch = Switch(wiatrak_lazienka_settings, self.wiatrak_lazienka_switch_callback)

        wiatrak_kuchnia_switch_info = SwitchInfo(name="Wiatrak kuchnia", unique_id="arduino_mega_wiatrak_kuchnia_switch", device=self.device_info)
        wiatrak_kuchnia_settings = Settings(mqtt=self.mqtt_settings, entity=wiatrak_kuchnia_switch_info)
        self.wiatrak_kuchnia_switch = Switch(wiatrak_kuchnia_settings, self.wiatrak_kuchnia_switch_callback)


    # To receive state commands from HA, define a callback function:
    def ogrz_pompa_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_POMPA, 1):
                self.ogrz_pompa_switch.on()
        elif payload == "OFF":
            if setDigital(P_POMPA, 0):
                self.ogrz_pompa_switch.off()

    def ogrz_salon_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_T_SALON, 1):
                self.ogrz_salon_switch.on()
        elif payload == "OFF":
            if setDigital(P_T_SALON, 0):
                self.ogrz_salon_switch.off()

    def ogrz_kuchnia_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_T_KUCHNIA, 1):
                self.ogrz_kuchnia_switch.on()
        elif payload == "OFF":
            if setDigital(P_T_KUCHNIA, 0):
                self.ogrz_kuchnia_switch.off()
    
    def ogrz_lazienka_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
             if setDigital(P_T_LAZIENKA, 1):
                 self.ogrz_lazienka_switch.on()
        elif payload == "OFF":
            if setDigital(P_T_LAZIENKA, 0):
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
                if setDigital(P_OSW_WANNA, 1):
                    self.ogrz_oswietlenie_ligth.on()
            else:
                if setDigital(P_OSW_WANNA, 0):
                    self.ogrz_oswietlenie_ligth.off()
        else:
            print("Unknown payload")

    def ogrz_wc_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_WC, 1):
                self.ogrz_wc_switch.on()
        elif payload == "OFF":
            if setDigital(P_WC, 0):
                self.ogrz_wc_switch.off()

    def ogrz_hol1_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_HOL_A, 1):
                self.ogrz_hol1_switch.on()
        elif payload == "OFF":
            if setDigital(P_HOL_A, 0):
                self.ogrz_hol1_switch.off()

    def ogrz_hol2_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_HOL_B, 1):
                self.ogrz_hol2_switch.on()
        elif payload == "OFF":
            if setDigital(P_HOL_B, 0):
                self.ogrz_hol2_switch.off()

    def ogrz_hol3_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_HOL_C, 1):
                self.ogrz_hol3_switch.on()
        elif payload == "OFF":
            if setDigital(P_HOL_C, 0):
                self.ogrz_hol3_switch.off()

    def wiatrak_lazienka_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        print("wiatrak_switch")
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_WIATRAK_1, 1):
                self.wiatrak_lazienka_switch.on()
        elif payload == "OFF":
            if setDigital(P_WIATRAK_1, 0):
                self.wiatrak_lazienka_switch.off()

    def wiatrak_kuchnia_switch_callback(self, client: Client, user_data, message: MQTTMessage):
        payload = message.payload.decode()
        if payload == "ON":
            if setDigital(P_WIATRAK_2, 1):
                self.wiatrak_kuchnia_switch.on()
        elif payload == "OFF":
            if setDigital(P_WIATRAK_2, 0):
                self.wiatrak_kuchnia_switch.off()



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

o.wiatrak_lazienka_switch.off()
o.wiatrak_kuchnia_switch.off()
while True:
    #line = ser.readline()   # read a '\n' terminated line
    #line = line.decode('ascii')
    #chunks = line.split(';')
    #print(chunks)
    #if chunks[0] == 'F':
    #    num = int(chunks[1])
    #    val1 = int(chunks[2])
    #    val2 = int(chunks[3])
    #    flows[num-1].setflow(val1)
    #elif chunks[0] == 'W':
    #    num = int(chunks[1])
    #    val = False if int(chunks[2]) == 0 else True
    #    fans[num-1].set(val)
    pass
