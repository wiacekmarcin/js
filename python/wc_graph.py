
from PySide6.QtWidgets import QGraphicsScene, QMainWindow, QFrame, QApplication, QPushButton, QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PySide6.QtWidgets import QVBoxLayout, QGraphicsRectItem, QGraphicsPathItem, QGridLayout, QToolButton, QLabel
from PySide6.QtCore import Qt, Slot, QPoint, QRect, QIODevice, QTimer, QObject, QSize, Signal, Slot
from PySide6 import QtSerialPort
from ui_wc_simulator import Ui_WC_Simulator
import threading



class InputCl:
    def __init__(self):
        self.inputs = [ False, False, False, False, False, False, False, False ]

    def setNoc(self, val):
        self.inputs[7] = not val

    def setWieczor(self, val):
        self.inputs[6] = not val

    def setZasAwar(self, val):
        self.inputs[4] = not val

    def setTaryfa2(self, val):
        self.inputs[5] = not val

    def setCzujka(self, val):
        self.inputs[0] = val 

    def setDrzwi(self, val):
        self.inputs[2] = val
    
    def setCzujnikZblizeniowy(self, val):
        self.inputs[1] = val

    def setKlawisz(self, val):
        self.inputs[3] = not val
    
    def getInput(self):
        ret = ''
        for i in range(8):
            ret += '1' if self.inputs[8-i-1] else '0'
        ret = 'D;W;I;' + ret
        return ret

class WCMainWindow(QMainWindow, Ui_WC_Simulator):
    def __init__(self, *args, obj=None, **kwargs):
        super(WCMainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.inp = InputCl()
        #self.setGeometry(0, 0, 1920, 1020)
        self.bopendrzwi = False
        self.bnoc = False
        self.bwieczor = False
        self.btaryfa2 = False
        self.bzasAwar = False

        self.pb_drzwi.clicked.connect(self.on_clicked_drzwi)
        self.pb_czujnik_ruchu.pressed.connect(self.on_clicked_czujka_ruchu)
        self.pb_czujnik_zblizeniowy.pressed.connect(self.on_clicked_czujnik_zblizeniowy)
        self.pb_klawisz.pressed.connect(self.on_clicked_klawisz)

        self.pb_czujnik_ruchu.released.connect(self.on_released_czujka_ruchu)
        self.pb_czujnik_zblizeniowy.released.connect(self.on_released_czujnik_zblizeniowy)
        self.pb_klawisz.released.connect(self.on_released_klawisz)
        
        self.pb_wieczor.clicked.connect(self.on_clicked_wieczor)
        self.pb_noc.clicked.connect(self.on_clicked_noc)
        self.pb_taryfa2.clicked.connect(self.on_clicked_taryfa2)
        self.pb_zasilanie_awaryjne.clicked.connect(self.on_clicked_zasawar)

        self.actionRS485.triggered.connect(self.on_rs485_clicked)
        self.actionRS485.setCheckable(True)

        self.actionDebug.triggered.connect(self.on_usb0_clicked)
        self.actionDebug.setCheckable(True)


        self.inp.setWieczor(False)
        self.wieczor_on.setChecked(False)
        self.wieczor_off.setChecked(True)

        self.inp.setCzujka(False)
        self.inp.setCzujnikZblizeniowy(False)
        self.inp.setKlawisz(False)
        
        self.inp.setNoc(False)
        self.noc_on.setChecked(False)
        self.noc_off.setChecked(True)
        
        self.inp.setTaryfa2(False)
        self.taryfa2_on.setChecked(False)
        self.taryfa2_off.setChecked(True)

        self.inp.setZasAwar(False)
        self.zasilanie_awaryjne_on.setChecked(False)
        self.zasilanie_awaryjne_off.setChecked(True)
        
        self.inp.setDrzwi(True)
        self.drzwi_otwarte.setChecked(False)
        self.drzwi_zamkniete.setChecked(True)

    
    def connectUsb(self, arduinoSer, rs485):
        self.ardTty = arduinoSer
        self.rs485 = rs485

        self.serial_arduino = QtSerialPort.QSerialPort(
            self.ardTty,
            baudRate = QtSerialPort.QSerialPort.Baud115200,
            readyRead = self.receive_acm0
        )

        self.serial_rs485 = QtSerialPort.QSerialPort(
            self.rs485,
            baudRate = QtSerialPort.QSerialPort.Baud115200,
            readyRead = self.receive_usb0
        )
        self.statusbar.showMessage("Arduino:%s [not open]    RS485:%s [not open]" % (arduinoSer.replace("/dev/serial/by-id/", ""), rs485.replace("/dev/serial/by-id/", "")))

    @Slot()
    def receive_usb0(self):
        while self.serial_rs485.canReadLine():
            print("..")
            text = self.serial_rs485.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_rs485.append(text)
            if text[:4] == 'S;W;V;':
                _, _, _, spos, sval, _ = text.split(";")

                pos = int(spos)
                val = sval == '1'

                #8 - oswietlenie ?
                #0 - zawor
                #1 - lustro
                #2 - swiatlo sufit
                #3 - regal  
                #4 - noc
                #5 - czujnik ruchu
                #6 - opto czujnik ruchu
                #7 - opto kontaktron

                if pos == 8:
                    self.wy_zapalone_swiatlo.setText("on" if val else "off")
                elif pos == 7:
                    self.wy_kontaktron.setText("on" if val else "off")
                elif pos == 6:
                    self.wy_czujnik_ruchu.setText("on" if val else "off")
                elif pos == 3:
                    self.regal.setText("on" if val else "off")
                elif pos == 2:
                    self.lustro.setText("on" if val else "off")
                elif pos == 1:
                    self.light.setText("on" if val else "off")
                elif pos == 0:
                    self.zawor.setText("on" if val else "off")

    def receive_acm0(self):
        while self.serial_arduino.canReadLine():
            print("++")
            text = self.serial_arduino.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_arduino.append(text)
            
    def on_clicked_drzwi(self):
        self.bopendrzwi = not self.bopendrzwi
        self.inp.setDrzwi(self.bopendrzwi)
        self.sendInput(self.inp.getInput())

        self.drzwi_otwarte.setChecked(self.bopendrzwi)
        self.drzwi_zamkniete.setChecked(not self.bopendrzwi)

    def on_clicked_noc(self):
        self.bnoc = not self.bnoc
        self.inp.setNoc(self.bnoc)
        self.sendInput(self.inp.getInput())

        self.noc_on.setChecked(self.bnoc)
        self.noc_off.setChecked(not self.bnoc)


    def on_clicked_wieczor(self):
        self.bwieczor = not self.bwieczor
        self.inp.setWieczor(self.bwieczor)
        self.sendInput(self.inp.getInput())

        self.wieczor_on.setChecked(self.bwieczor)
        self.wieczor_off.setChecked(not self.bwieczor)

    def on_clicked_zasawar(self):
        self.bzasAwar = not self.bzasAwar
        self.inp.setZasAwar(self.bzasAwar)
        self.sendInput(self.inp.getInput())

        self.zasilanie_awaryjne_on.setChecked(self.bzasAwar)
        self.zasilanie_awaryjne_off.setChecked(not self.bzasAwar)

    def on_clicked_taryfa2(self):
        self.btaryfa2 = not self.btaryfa2
        self.inp.setTaryfa2(self.btaryfa2)
        self.sendInput(self.inp.getInput())

        self.taryfa2_on.setChecked(self.btaryfa2)
        self.taryfa2_off.setChecked(not self.btaryfa2)

    def on_clicked_czujka_ruchu(self):
        self.inp.setCzujka(True)
        self.sendInput(self.inp.getInput())

    def on_released_czujka_ruchu(self):
        self.inp.setCzujka(False)
        self.sendInput(self.inp.getInput())
    
    def on_clicked_czujnik_zblizeniowy(self):
        self.inp.setCzujnikZblizeniowy(True)
        self.sendInput(self.inp.getInput())

    def on_released_czujnik_zblizeniowy(self):
        self.inp.setCzujnikZblizeniowy(False)
        self.sendInput(self.inp.getInput())

    def on_clicked_klawisz(self):
        self.inp.setKlawisz(True)
        self.sendInput(self.inp.getInput())

    def on_released_klawisz(self):
        self.inp.setKlawisz(False)
        self.sendInput(self.inp.getInput())

    def sendInput(self, msg):
        self.te_arduino.append("Send:"+msg)
        self.serial_arduino.write(msg.encode())

    def on_usb0_clicked(self):

        if not self.actionDebug.isChecked():
            if self.serial_arduino.isOpen():
                self.serial_arduino.close()

        else:
            if not self.serial_arduino.isOpen():
                r = self.serial_arduino.open(QIODevice.ReadWrite)
                self.actionDebug.setChecked(r)

        self.statusbar.showMessage("Arduino:%s [%sopen]    RS485:%s [%sopen]" % (self.serial_arduino.portName().replace("/dev/serial/by-id/", ""), ("" if self.serial_arduino.isOpen() else "not "),
                                                                                   self.serial_rs485.portName().replace("/dev/serial/by-id/", ""), ("" if self.serial_rs485.isOpen() else "not ")))
        
    def on_rs485_clicked(self):

        if not self.actionRS485.isChecked():
            if self.serial_rs485.isOpen():
                self.serial_rs485.close()

        else:
            if not self.serial_rs485.isOpen():
                r = self.serial_rs485.open(QIODevice.ReadWrite)
                self.actionRS485.setChecked(r)
        
        self.statusbar.showMessage("Arduino:%s [%sopen]    RS485:%s [%sopen]" % (self.serial_arduino.portName().replace("/dev/serial/by-id/", ""), ("" if self.serial_arduino.isOpen() else "not "),
                                                                                   self.serial_rs485.portName().replace("/dev/serial/by-id/", ""), ("" if self.serial_rs485.isOpen() else "not ")))

        


    def closeEvent(self, event):
        self.serial_arduino.close()
        self.serial_rs485.close()
        #pg.exit()

if __name__ == '__main__':
    import sys
    #if len(sys.argv) == 3:
    #    usb485 = sys.argv[1]
    #    usbusb = sys.argv[2]
    #print(usb485, usbusb)


    app = QApplication(sys.argv)
    w = WCMainWindow()
    w.show()
    w.connectUsb("/dev/serial/by-id/usb-SparkFun_SparkFun_Pro_Micro-if00", "/dev/serial/by-id/usb-Prolific_Technology_Inc._USB-Serial_Controller-if00-port0")
    sys.exit(app.exec())


