from base_plugin import LPlugin
from base_app import TimeoutClass 
import serial
import re



# Step 1: Create a worker class
class Worker(QObject):
    #finished = pyqtSignal()
    #progress = pyqtSignal(int)

    def __init__(self, parent = None):
        super().__init__(parent)
        self.regexp = re.compile(r'^DHT=(?P<lhum>\d+\.{0,1}\d*);(?P<ltemp>\d+\.{0,1}\d*):(?P<key1>[0-9a-f]{16})=(?P<value1>\d+\.{0,1}\d*):(?P<key2>[0-9a-f]{16})=(?P<value2>\d+\.{0,1}\d*)$')
        #DHT=62.5;24.3:286cf90f0b0000ae=34.9:28fff708640400a3=30.7
    



    def run(self):
        """Long-running task."""
        self.isRun = True
        self.ser = serial.Serial(
            port='/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
        while self.isRun:
            bline = self.ser.readline()
            if len(bline) == 0:
                #sleep()
                continue
            line = bline.decode('ascii').strip()
            #print(line)
            obj = self.regexp.match(line)
            if obj is not None:
                valg = obj.groupdict()
                vals = {}
                vals['lazienka_temp'] = valg['ltemp']
                vals['lazienka_humi'] = valg['lhum']
                vals[valg['key1']] = valg['value1']
                vals[valg['key2']] = valg['value2']
                self.blackwidget.sendNotification(vals)
        self.ser.close()


class SerialReader(LPlugin):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.thread = TimeoutClass(self.readValues)
        self.regexp = re.compile(r'^DHT=(?P<lhum>\d+\.{0,1}\d*);(?P<ltemp>\d+\.{0,1}\d*):(?P<key1>[0-9a-f]{16})=(?P<value1>\d+\.{0,1}\d*):(?P<key2>[0-9a-f]{16})=(?P<value2>\d+\.{0,1}\d*)$')
        self.ser = serial.Serial(
            port='/dev/serial/by-id/usb-Arduino_LLC_Arduino_Micro-if00',\
            baudrate=9600,\
            parity=serial.PARITY_NONE,\
            stopbits=serial.STOPBITS_ONE,\
            bytesize=serial.EIGHTBITS,\
            timeout=0)
        self.thread.start()

    def timeout(self, dt):
        pass

    def __delete__(self, instance):
        self.ser.close()

    def readValues(self):
        bline = self.ser.readline()
        if len(bline) == 0:
            #sleep()
            return
        line = bline.decode('ascii').strip()
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
