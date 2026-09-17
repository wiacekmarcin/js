from PySide6 import QtCore, QtWidgets, QtSerialPort

from salon_sypialnia_hol import Ui_Form


class Widget2(QtWidgets.QWidget, Ui_Form):
    def __init__(self, *args, obj=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        self.pbusb0.toggled.connect(self.on_toggled_usb0)
        self.pbusb0.setCheckable(True)
        self.pbacm0.toggled.connect(self.on_toggled_acm0)
        self.pbacm0.setCheckable(True)

        self.pb_216_1.clicked.connect(self.clicked_pb_216_1)
        self.pb_214_1.clicked.connect(self.clicked_pb_214_1)

        self.serial1 = QtSerialPort.QSerialPort(
            '/dev/ttyACM0',
            baudRate=115200,
            readyRead=self.receive_acm0
        )
        
        self.serial2 = QtSerialPort.QSerialPort(
            '/dev/ttyUSB0',
            baudRate=115200,
            readyRead=self.receive_usb0
        )

    @QtCore.Slot()
    def receive_usb0(self):
        while self.serial2.canReadLine():
            text = self.serial2.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_usb0.append(text)

    @QtCore.Slot()
    def receive_acm0(self):
        while self.serial2.canReadLine():
            text = self.serial2.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_acm0.append(text)

    @QtCore.Slot()
    def clicked_pb_216_1(self):
        print("Sypialnia 1")

    @QtCore.Slot()
    def clicked_pb_214_1(self):
        print("Sypialnia 2")

    @QtCore.Slot()
    def send(self):
        #self.serial.write(self.message_le.text().encode())
        pass

    @QtCore.Slot(bool)
    def on_toggled_usb0(self, checked):
        print("on_toggled_usb0")
        self.pbusb0.setText(u"Rozlacz" if checked else u"Połącz")
        if checked:
            if not self.serial2.isOpen():
                if not self.serial2.open(QtCore.QIODevice.ReadWrite):
                    self.pbusb0.setChecked(False)
        else:
            self.serial2.close()

    @QtCore.Slot(bool)
    def on_toggled_acm0(self, checked):
        print("on_toggled_acm0")
        self.pbacm0.setText(u"Rozlacz" if checked else u"Połącz")
        if checked:
            if not self.serial1.isOpen():
                if not self.serial1.open(QtCore.QIODevice.ReadWrite):
                    self.pbacm0.setChecked(False)
        else:
            self.serial1.close()

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

    @QtCore.pyqtSlot()
    def receive(self):
        while self.serial.canReadLine():
            text = self.serial.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.output_te.append(text)

    @QtCore.pyqtSlot()
    def send(self):
        self.serial.write(self.message_le.text().encode())

    @QtCore.pyqtSlot(bool)
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
    app = QtWidgets.QApplication(sys.argv)
    w = Widget2()
    w.show()
    sys.exit(app.exec())
