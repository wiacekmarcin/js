from base_plugin import LPlugin
from base_app import TimeoutClass 
import serial
import re
import time

class SerialReader(LPlugin):
    def __init__(self, master, app, *args, **kwargs):
        super().__init__(app)

        self.regexp = re.compile(r'^DHT=(?P<lhum>\d+\.{0,1}\d*);(?P<ltemp>\d+\.{0,1}\d*):(?P<key1>[0-9a-fA-F]{16})=(?P<value1>\d+\.{0,1}\d*):(?P<key2>[0-9a-fA-F]{16})=(?P<value2>\d+\.{0,1}\d*)$')
        try:
            self.ser = serial.Serial(
            #port='/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00',\
            port='/dev/serial/by-id/usb-Silicon_Labs_CP2102_USB_to_UART_Bridge_Controller_0001-if00-port0',\
            baudrate=115200,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
        except:
            return
        
        app.after(5000, self.delay_start)

    def timeout(self, dt):
        pass

    def delay_start(self):
        print("Delay function")
        time.sleep(30)
        self.thread = TimeoutClass(self.readValues)

    def __delete__(self, instance):
        self.ser.close()

    def readValues(self):
        bline = self.ser.readline()
        if len(bline) == 0:
            #sleep()
            return
        try:

            line = bline.decode('ascii').strip()
        except:
            return
        #print(line)
        obj = self.regexp.match(line)
        if obj is not None:

            valg = obj.groupdict()
            vals = {}
            vals['lazienka_temp'] = valg['ltemp']
            vals['lazienka_humi'] = valg['lhum']
            vals[valg['key1']] = valg['value1']
            vals[valg['key2']] = valg['value2']
            self.sendNotification(vals)
