from PySide6 import QtCore, QtWidgets, QtSerialPort

from salon_sypialnia_hol import Ui_Form

class InputCl:
    def __init__(self):
        self.noc = False
        self.wieczor = False
        self.zas_awar = False
        self.taryfa2 = False

        self.czujka1 = False
        self.czujka2 = False

        self.v24_off = False

        self.z216_1 = False
        self.z214_1 = False
        self.z216_2 = False
        self.z214_2 = False
        self.z216_3 = False
        self.z214_3 = False
        self.z216_4 = False
        self.z214_4 = False
        self.z216_5 = False
        self.z214_5 = False
        self.z216_6 = False
        self.z214_6 = False
        self.z216_7 = False
        self.z214_7 = False
        self.z216_8 = False
        self.z214_8 = False
        self.z214_9 = False
        self.z214_10 = False

        self.z58_1 = False
        self.z58_2 = False
        self.z58_3 = False
        self.z58_4 = False
        self.z58_5 = False
        self.z58_6 = False
        self.z58_7 = False
        self.z58_8 = False

        self.z217_2 = False
        self.z217_3 = False

    def setNoc(self, val):
        self.noc = val

    def setWieczor(self, val):
        self.wieczor = val

    def setZasAwar(self, val):
        self.zas_awar = val

    def setTaryfa2(self, val):
        self.taryfa2 = val

    def setCzujka1(self, val):
        self.czujka1 = val 

    def setCzujka2(self, val):
        self.czujka2 = val
    
    def setV24_off(self, val):
        self.v24_off = val

    def setZ216_1(self, val):
        self.z216_1 = val
    
    def setZ214_1(self, val):
        self.z214_1 = val

    def setZ216_2(self, val):
        self.z216_2 = val
    
    def setZ214_2(self, val):
        self.z214_2 = val

    def setZ216_3(self, val):
        self.z216_3 = val
    
    def setZ214_3(self, val):
        self.z214_3 = val

    def setZ216_4(self, val):
        self.z216_4 = val
    
    def setZ214_4(self, val):
        self.z214_4 = val
    
    def setZ216_5(self, val):
        self.z216_5 = val
    
    def setZ214_5(self, val):
        self.z214_5 = val

    def setZ216_6(self, val):
        self.z216_6 = val
    
    def setZ214_6(self, val):
        self.z214_6 = val

    def setZ216_7(self, val):
        self.z216_7 = val
    
    def setZ214_7(self, val):
        self.z214_7 = val

    def setZ216_8(self, val):
        self.z216_8 = val
    
    def setZ214_8(self, val):
        self.z214_8 = val

    def setZ214_9(self, val):
        self.z214_9 = val
    
    def setZ214_10(self, val):
        self.z214_10 = val

    def setZ58_1(self, val):
        self.z58_1 = val
    
    def setZ58_2(self, val):
        self.z58_2 = val

    def setZ58_3(self, val):
        self.z58_3 = val

    def setZ58_4(self, val):
        self.z58_4 = val

    def setZ58_5(self, val):
        self.z58_5 = val

    def setZ58_6(self, val):
        self.z58_6 = val

    def setZ58_7(self, val):
        self.z58_7 = val

    def setZ58_8(self, val):
        self.z58_8 = val

    def setZ217_2(self, val):
        self.z217_2 = val
    
    def setZ217_3(self, val):
        self.z217_3 = val

    def getInput(self):
        buf = "I=["
        b_0A = 0
        b_0B = 0
        b_1A = 0
        b_1B = 0
        b_2A = 0
        b_2B = 0
        b_3A = 0
        b_3B = 0

        if not self.noc:
            b_0A += 0x1 << 2
        
        if not self.wieczor:
            b_0A += 0x1 << 3

        if not self.zas_awar:
            b_0A += 0x1

        if not self.taryfa2:
            b_0A += 0x1 << 1
        
        if self.czujka1:
            b_1A += 0x1

        if self.czujka2:
            b_1A += 0x1 << 1

        if self.v24_off:
            b_1A += 0x1 << 2

        if not self.z214_1:
            b_2B += 0x1 << 2
        
        if not self.z216_1:
            b_3A += 0x1 << 6

        if not self.z214_2:
            b_2B += 0x1 << 1  

        if not self.z216_2:
            b_3A += 0x1 << 5
        
        if not self.z214_3:
            b_2B += 0x1 
        
        if not self.z216_3:
            b_3A += 0x1 << 4

        if not self.z214_4:
            b_2A += 0x1 << 6
        
        if not self.z216_4:
            b_3A += 0x1 << 3

        if not self.z214_5:
            b_2A += 0x1 << 5
        
        if not self.z216_5:
            b_3A += 0x1 << 2

        if not self.z214_6:
            b_2A += 0x1 << 4
        
        if not self.z216_6:
            b_3A += 0x1 << 1

        if not self.z214_7:
            b_2A += 0x1 << 3
        
        if not self.z216_7:
            b_3A += 0x1 

        if not self.z214_8:
            b_2A += 0x1 << 2
        
        if not self.z216_8:
            b_2B += 0x1 << 3
        
        if not self.z214_9:
            b_2A += 0x1 << 1
        
        if not self.z214_10:
            b_2A += 0x1 

        if not self.z58_1:
            b_2B += 0x1 << 4

        if not self.z58_2:
            b_2B += 0x1 << 5

        if not self.z58_3:
            b_2B += 0x1 << 6

        if not self.z58_4:
            b_3B += 0x1 
        
        if not self.z58_5:
            b_3B += 0x1 << 1

        if not self.z58_6:
            b_3B += 0x1 << 2

        if not self.z58_7:
            b_3B += 0x1 << 3

        if not self.z58_8:
            b_3B += 0x1 << 4

        if not self.z217_2:
            b_3B += 0x1 << 6

        if not self.z217_3:
            b_3B += 0x1 << 5


        buf += "%03d %03d %03d %03d %03d %03d %03d %03d ]\n\r" % (b_3B, b_3A,b_2B, b_2A,b_1B, b_1A, b_0B, b_0A)
        print("%02x %02x %02x %02x %02x %02x %02x %02x" % (b_3B, b_3A,b_2B, b_2A,b_1B, b_1A, b_0B, b_0A))
        return buf

    
class Widget2(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.inReg = InputCl()

        self.pbusb0.toggled.connect(self.on_toggled_usb0)
        self.pbusb0.setCheckable(True)
        self.pbacm0.toggled.connect(self.on_toggled_acm0)
        self.pbacm0.setCheckable(True)

        self.val_24V.toggled.connect(self.on_toggled_24V)
        self.val_24V.setCheckable(True)
        self.val_noc.toggled.connect(self.on_toggled_noc)
        self.val_noc.setCheckable(True)
        self.val_wieczor.toggled.connect(self.on_toggled_wieczor)
        self.val_wieczor.setCheckable(True)
        self.val_zasilanieAwar.toggled.connect(self.on_toggled_zasawar)
        self.val_zasilanieAwar.setCheckable(True)
        self.val_czujka1.toggled.connect(self.on_toggled_czujka1)
        self.val_czujka1.setCheckable(True)
        self.val_czujka2.toggled.connect(self.on_toggled_czujka2)
        self.val_czujka2.setCheckable(True)

        self.pb_216_1.clicked.connect(self.clicked_pb_216_1)
        self.pb_214_1.clicked.connect(self.clicked_pb_214_1)
        self.pb_21x_1.clicked.connect(self.clicked_pb_21x_1)
        self.pb_216_2.clicked.connect(self.clicked_pb_216_2)
        self.pb_214_2.clicked.connect(self.clicked_pb_214_2)
        self.pb_21x_2.clicked.connect(self.clicked_pb_21x_2)
        self.pb_216_3.clicked.connect(self.clicked_pb_216_3)
        self.pb_214_3.clicked.connect(self.clicked_pb_214_3)
        self.pb_21x_3.clicked.connect(self.clicked_pb_21x_3)
        self.pb_216_4.clicked.connect(self.clicked_pb_216_4)
        self.pb_214_4.clicked.connect(self.clicked_pb_214_4)
        self.pb_21x_4.clicked.connect(self.clicked_pb_21x_4)
        self.pb_216_5.clicked.connect(self.clicked_pb_216_5)
        self.pb_214_5.clicked.connect(self.clicked_pb_214_5)
        self.pb_21x_5.clicked.connect(self.clicked_pb_21x_5)
        self.pb_216_6.clicked.connect(self.clicked_pb_216_6)
        self.pb_214_6.clicked.connect(self.clicked_pb_214_6)
        self.pb_21x_6.clicked.connect(self.clicked_pb_21x_6)
        self.pb_216_7.clicked.connect(self.clicked_pb_216_7)
        self.pb_214_7.clicked.connect(self.clicked_pb_214_7)
        self.pb_21x_7.clicked.connect(self.clicked_pb_21x_7)
        self.pb_216_8.clicked.connect(self.clicked_pb_216_8)
        self.pb_214_8.clicked.connect(self.clicked_pb_214_8)
        self.pb_21x_8.clicked.connect(self.clicked_pb_21x_8)
        self.pb_214_9.clicked.connect(self.clicked_pb_214_9)
        self.pb_214_10.clicked.connect(self.clicked_pb_214_10)
        self.pb_217_2.clicked.connect(self.clicked_pb_217_2)
        self.pb_217_3.clicked.connect(self.clicked_pb_217_3)
        self.pb_217_x.clicked.connect(self.clicked_pb_217_x)
        self.pb_58_1.clicked.connect(self.clicked_pb_58_1)
        self.pb_58_2.clicked.connect(self.clicked_pb_58_2)
        self.pb_58_1x2.clicked.connect(self.clicked_pb_58_1x2)
        self.pb_58_3.clicked.connect(self.clicked_pb_58_3)
        self.pb_58_4.clicked.connect(self.clicked_pb_58_4)
        self.pb_58_3x4.clicked.connect(self.clicked_pb_58_3x4)
        self.pb_58_5.clicked.connect(self.clicked_pb_58_5)
        self.pb_58_6.clicked.connect(self.clicked_pb_58_6)
        self.pb_58_5x6.clicked.connect(self.clicked_pb_58_5x6)
        self.pb_58_7.clicked.connect(self.clicked_pb_58_7)
        self.pb_58_8.clicked.connect(self.clicked_pb_58_8)
        self.pb_58_7x8.clicked.connect(self.clicked_pb_58_7x8)


    def connectUsb(self, arduinoSer, rs485):
        self.ardTty = arduinoSer
        self.rs485 = rs485
        self.ltty_ard.setText(self.ardTty)
        self.serial_arduino = QtSerialPort.QSerialPort(
            self.ardTty,
            baudRate=QtSerialPort.QSerialPort.Baud115200,
            readyRead=self.receive_acm0
        )
        self.lttyRs485.setText(self.rs485)
        self.serial_rs485 = QtSerialPort.QSerialPort(
            self.rs485,
            baudRate=QtSerialPort.QSerialPort.Baud115200,
            readyRead=self.receive_usb0
        )

    @QtCore.Slot()
    def receive_usb0(self):
        while self.serial_rs485.canReadLine():
            text = self.serial_rs485.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_usb0.append(text)
            if text[:4] == 'S;V;':
                _, _, spos, sval, _ = text.split(";")

                pos = int(spos)
                val = sval == '1'

                if pos == 4:
                    self.led4.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 5:
                    self.led3.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 14:
                    self.led1.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 15:
                    self.led2.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))

                elif pos == 6:
                    self.led3_2.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 7:
                    self.led4_4.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 8:
                    self.led4_3.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 9:
                    self.led4_2.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 10:
                    self.led4_1.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 11:
                    self.led3_1.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 12:
                    self.led3_3.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 13:
                    self.zasilacz12v.setStyleSheet("background: \"%s\"" % ("green" if val else "white"))
                
                elif pos == 24:
                    self.sypialnia2.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 25:
                    self.kinkiety.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))

                elif pos == 26:
                    self.led4_0.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 27:
                    self.sypialnia1.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 28:
                    self.salon2.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                elif pos == 31:
                    self.salon1.setStyleSheet("background: \"%s\"" % ("yellow" if val else "white"))
                
                elif pos == 21:
                    self.mix_podswielenie_1.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                    self.mix_podswietlenie_2.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                
                elif pos == 22:
                    self.podswietlenie_hol_1.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                    self.hol_podswietlenie_2.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                    self.hol_podswietlenie_3.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                
                elif pos == 23:
                    self.salon_podswietlenie_1.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                    self.salon_podswietlenie_2.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))
                    self.salon_podswietlenie_3.setStyleSheet("background: \"%s\"" % ("blue" if val else "white"))

                elif pos == 29:
                    self.gwarantowane_n.setStyleSheet("background: \"%s\"" % ("red" if val else "white"))
                elif pos == 30:
                    self.gwarantowane_l.setStyleSheet("background: \"%s\"" % ("red" if val else "white"))
                
                elif pos == 19:
                    self.swiatlo_sypialnia.setStyleSheet("background: \"%s\"" % ("green" if val else "white"))
                elif pos == 20:
                    self.czujka_ruchu.setStyleSheet("background: \"%s\"" % ("green" if val else "white"))
                elif pos == 39:
                    self.swiatlo_hol.setStyleSheet("background: \"%s\"" % ("green" if val else "white"))
                elif pos == 47:
                    self.swiatlo_salon.setStyleSheet("background: \"%s\"" % ("green" if val else "white"))



    @QtCore.Slot()
    def receive_acm0(self):
        while self.serial_arduino.canReadLine():
            text = self.serial_arduino.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_acm0.append(text)
            

    @QtCore.Slot(bool)
    def on_toggled_24V(self, val):
        self.inReg.setV24_off(val)
        self.sendInput()

    @QtCore.Slot(bool)
    def on_toggled_noc(self, val):
        self.inReg.setNoc(val)
        self.sendInput()

    @QtCore.Slot(bool)
    def on_toggled_wieczor(self, val):
        self.inReg.setWieczor(val)
        self.sendInput()

    @QtCore.Slot(bool)
    def on_toggled_zasawar(self, val):
        self.inReg.setZasAwar(val)
        self.sendInput()

    @QtCore.Slot(bool)
    def on_toggled_czujka1(self, val):
        self.inReg.setCzujka1(val)
        self.sendInput()
    
    @QtCore.Slot(bool)
    def on_toggled_czujka2(self, val):
        self.inReg.setCzujka2(val)
        self.sendInput()
    
    @QtCore.Slot()
    def clicked_pb_216_1(self):
        self.inReg.setZ216_1(True)
        self.sendInput()
        self.inReg.setZ216_1(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_1(self):
        self.inReg.setZ214_1(True)
        self.sendInput()
        self.inReg.setZ214_1(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_1(self):
        self.inReg.setZ216_1(True)
        self.inReg.setZ214_1(True)
        self.sendInput()
        self.inReg.setZ216_1(False)
        self.inReg.setZ214_1(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_2(self):
        self.inReg.setZ216_2(True)
        self.sendInput()
        self.inReg.setZ216_2(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_2(self):
        self.inReg.setZ214_2(True)
        self.sendInput()
        self.inReg.setZ214_2(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_2(self):
        self.inReg.setZ216_2(True)
        self.inReg.setZ214_2(True)
        self.sendInput()
        self.inReg.setZ216_2(False)
        self.inReg.setZ214_2(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_3(self):
        self.inReg.setZ216_3(True)
        self.sendInput()
        self.inReg.setZ216_3(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_3(self):
        self.inReg.setZ214_3(True)
        self.sendInput()
        self.inReg.setZ214_3(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_3(self):
        self.inReg.setZ216_3(True)
        self.inReg.setZ214_3(True)
        self.sendInput()
        self.inReg.setZ216_3(False)
        self.inReg.setZ214_3(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_4(self):
        self.inReg.setZ216_4(True)
        self.sendInput()
        self.inReg.setZ216_4(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_4(self):
        self.inReg.setZ214_4(True)
        self.sendInput()
        self.inReg.setZ214_4(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_4(self):
        self.inReg.setZ216_4(True)
        self.inReg.setZ214_4(True)
        self.sendInput()
        self.inReg.setZ216_4(False)
        self.inReg.setZ214_4(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_5(self):
        self.inReg.setZ216_5(True)
        self.sendInput()
        self.inReg.setZ216_5(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_5(self):
        self.inReg.setZ214_5(True)
        self.sendInput()
        self.inReg.setZ214_5(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_5(self):
        self.inReg.setZ216_5(True)
        self.inReg.setZ214_5(True)
        self.sendInput()
        self.inReg.setZ216_5(False)
        self.inReg.setZ214_5(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_6(self):
        self.inReg.setZ216_6(True)
        self.sendInput()
        self.inReg.setZ216_6(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_6(self):
        self.inReg.setZ214_6(True)
        self.sendInput()
        self.inReg.setZ214_6(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_6(self):
        self.inReg.setZ216_6(True)
        self.inReg.setZ214_6(True)
        self.sendInput()
        self.inReg.setZ216_6(False)
        self.inReg.setZ214_6(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_7(self):
        self.inReg.setZ216_7(True)
        self.sendInput()
        self.inReg.setZ216_7(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_7(self):
        self.inReg.setZ214_7(True)
        self.sendInput()
        self.inReg.setZ214_7(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_7(self):
        self.inReg.setZ216_7(True)
        self.inReg.setZ214_7(True)
        self.sendInput()
        self.inReg.setZ216_7(False)
        self.inReg.setZ214_7(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_216_8(self):
        self.inReg.setZ216_8(True)
        self.sendInput()
        self.inReg.setZ216_8(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_214_8(self):
        self.inReg.setZ214_8(True)
        self.sendInput()
        self.inReg.setZ214_8(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_21x_8(self):
        self.inReg.setZ216_8(True)
        self.inReg.setZ214_8(True)
        self.sendInput()
        self.inReg.setZ216_8(False)
        self.inReg.setZ214_8(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_214_9(self):
        self.inReg.setZ214_9(True)
        self.sendInput()
        self.inReg.setZ214_9(False)
        self.sendInput()
    
    @QtCore.Slot()
    def clicked_pb_214_10(self):
        self.inReg.setZ214_10(True)
        self.sendInput()
        self.inReg.setZ214_10(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_58_1(self):
        self.inReg.setZ58_1(True)
        self.sendInput()
        self.inReg.setZ58_1(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_2(self):
        self.inReg.setZ58_2(True)
        self.sendInput()
        self.inReg.setZ58_2(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_58_1x2(self):
        self.inReg.setZ58_1(True)
        self.inReg.setZ58_2(True)
        self.sendInput()
        self.inReg.setZ58_1(False)
        self.inReg.setZ58_2(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_3(self):
        self.inReg.setZ58_3(True)
        self.sendInput()
        self.inReg.setZ58_3(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_4(self):
        self.inReg.setZ58_4(True)
        self.sendInput()
        self.inReg.setZ58_4(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_58_3x4(self):
        self.inReg.setZ58_3(True)
        self.inReg.setZ58_4(True)
        self.sendInput()
        self.inReg.setZ58_3(False)
        self.inReg.setZ58_4(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_5(self):
        self.inReg.setZ58_5(True)
        self.sendInput()
        self.inReg.setZ58_5(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_6(self):
        self.inReg.setZ58_6(True)
        self.sendInput()
        self.inReg.setZ58_6(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_58_5x6(self):
        self.inReg.setZ58_5(True)
        self.inReg.setZ58_6(True)
        self.sendInput()
        self.inReg.setZ58_5(False)
        self.inReg.setZ58_6(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_7(self):
        self.inReg.setZ58_7(True)
        self.sendInput()
        self.inReg.setZ58_7(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_58_8(self):
        self.inReg.setZ58_8(True)
        self.sendInput()
        self.inReg.setZ58_8(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_58_7x8(self):
        self.inReg.setZ58_7(True)
        self.inReg.setZ58_8(True)
        self.sendInput()
        self.inReg.setZ58_7(False)
        self.inReg.setZ58_8(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_217_2(self):
        self.inReg.setZ217_2(True)
        self.sendInput()
        self.inReg.setZ217_2(False)
        self.sendInput()


    @QtCore.Slot()
    def clicked_pb_217_3(self):
        self.inReg.setZ217_3(True)
        self.sendInput()
        self.inReg.setZ217_3(False)
        self.sendInput()

    @QtCore.Slot()
    def clicked_pb_217_x(self):
        self.inReg.setZ217_2(True)
        self.inReg.setZ217_3(True)
        self.sendInput()
        self.inReg.setZ217_2(False)
        self.inReg.setZ217_3(False)
        self.sendInput()

    def sendMsg(self):
        self.serial_rs485.write(self.message_le.text().encode())

    def sendInput(self):
        msg = self.inReg.getInput()
        self.te_acm0.append("Send:"+msg)
        self.serial_arduino.write(msg.encode())

    @QtCore.Slot(bool)
    def on_toggled_usb0(self, checked):
        self.pbusb0.setText(u"Rozlacz" if checked else u"Połącz")
        if checked:
            if not self.serial_rs485.isOpen():
                if not self.serial_rs485.open(QtCore.QIODevice.ReadWrite):
                    self.pbusb0.setChecked(False)
            else:
                self.serial_rs485.close()

    @QtCore.Slot(bool)
    def on_toggled_acm0(self, checked):
        self.pbacm0.setText(u"Rozlacz" if checked else u"Połącz")
        if checked:
            if not self.serial_arduino.isOpen():
                if not self.serial_arduino.open(QtCore.QIODevice.ReadWrite):
                    self.pbacm0.setChecked(False)
            else:
                self.serial_arduino.close()
    
    def closeEvent(self, event):
        self.serial_arduino.close()
        self.serial_rs485.close()

""""
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.message_le = QtWidgets.QLineEdit()
        self.send_btn = QtWidgets.QPushButton(
            text="Send",
            clicked=self.send
        )
        self.output_te = QtWidgets.QTextEdit(readOnly=True)
        self.button = QtWidgets.QPushButton(
            text="Connect",
            checkable=True,
            toggled=self.on_toggled
        )
        lay = QtWidgets.QVBoxLayout(self)
        hlay = QtWidgets.QHBoxLayout()
        hlay.addWidget(self.message_le)
        hlay.addWidget(self.send_btn)
        lay.addLayout(hlay)
        lay.addWidget(self.output_te)
        lay.addWidget(self.button)

        self.serial = QtSerialPort.QSerialPort(
            '/dev/ttyUSB0',
            baudRate=115200,
            readyRead=self.receive
        )

    @QtCore.Slot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.output_te.append(text)

    @QtCore.Slot()
    def send(self):
        self.serial.write(self.message_le.text().encode())

    @QtCore.Slot(bool)
    def on_toggled(self, checked):
        self.button.setText("Disconnect" if checked else "Connect")
        if checked:
            if not self.serial.isOpen():
                if not self.serial.open(QtCore.QIODevice.ReadWrite):
                    self.button.setChecked(False)
        else:
            self.serial.close()
"""

if __name__ == '__main__':
    import sys
    #if len(sys.argv) == 3:
    #    usb485 = sys.argv[1]
    #    usbusb = sys.argv[2]
    #print(usb485, usbusb)
    app = QtWidgets.QApplication(sys.argv)
    w = Widget2()
    w.show()
    w.connectUsb("/dev/serial/by-id/usb-SparkFun_SparkFun_Pro_Micro-if00", "/dev/serial/by-id/usb-WCH.CN_USB_Quad_Serial_BC5644ABCD-if00")
    sys.exit(app.exec())
