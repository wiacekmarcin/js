import sys
from PySide6.QtWidgets import QDialog, QApplication, QLabel

from ui_kalkulator_wejsc_salon import Ui_Dialog

pins = [
    [0,  4,  'OUTPUT', "213.06",  "Salon ledy k. łaz. 1"],
    [0,  5,  'OUTPUT', "213.05",  "Salon ledy k. łaz. 2"],
    [0,  6,  'OUTPUT', "209.08",  "Hol 3.1"],
    [0,  7,  'OUTPUT', "209.07",  "Hol 3.2"],
    [0,  8,  'OUTPUT', "209.06",  "Hol 3.3"],
    [0,  9,  'OUTPUT', "209.05",  "Hol 4.4"],
    [0, 10,  'OUTPUT', "209.04",  "Hol 4.3"],
    [0, 11,  'OUTPUT', "209.03",  "Hol 4.2"],
    [0, 12,  'OUTPUT', "209.02",  "Hol 4.1"],
    [0, 13,  'OUTPUT', "209.01",  "Zasilacz 12V"],
    [0, 14,  'OUTPUT', "213.04",  "Salon ledy k. jad. 2"],
    [0, 15,  'OUTPUT', "213.03",  "Salon ledy k. jad. 1"],

    [1,  3,  'OUTPUT', " 59.05",  "Włączone światlo sypialnia"],
    [1,  4,  'OUTPUT', " 59.06",  "Czujka ruchu OUT"],
    [1,  5,  'OUTPUT', "Pods_C",  "Podswietelenie mix"],
    [1,  6,  'OUTPUT', "Pods_B",  "Podswietlenie holu"],
    [1,  7,  'OUTPUT', "Pods_A",  "Podswietlenie salonu"],
    [1,  8,  'OUTPUT', "211.01",  "Sypialnia 1"],
    [1,  9,  'OUTPUT', "211.02",  "Sypialnia kinkiety"],
    [1, 10,  'OUTPUT', "210.04",  "Hol 4.00"],
    [1, 11,  'OUTPUT', "210.03",  "Sypialnia 2"],
    [1, 12,  'OUTPUT', "210.02",  "Salon 2"],
    [1, 13,  'OUTPUT', "212.02",  "Gwarantowane L"],
    [1, 14,  'OUTPUT', "212.01",  "Gwarantowane N"],
    [1, 15,  'OUTPUT', "210.01",  "Salon 1"],

    [2,  7,  'OUTPUT', " 59.03",  "Włączone światło w holu"],
    [2, 15,  'OUTPUT', " 59.04",  "Włączone światło w salonie"],

]

class WidgetCalc(QDialog, Ui_Dialog):
    def __init__(self, *args, obj=None, **kwargs):
        super(WidgetCalc, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.labels = {}
        for p in pins:
            idx = 16*p[0]+p[1]
            self.labels[idx] = QLabel(self.frame)
            self.labels[idx].setObjectName(u"i_%d" % idx)
            self.labels[idx].setText(p[4])
            self.labels[idx].setDisabled(True)
            self.labelsgrid.addWidget(self.labels[idx], p[1], p[0], 1, 1)

        self.b00_15.textChanged.connect(self.b00_15_change)
        self.b16_31.textChanged.connect(self.b16_31_change)
        self.b32_47.textChanged.connect(self.b32_47_change)
        self.b48_63.textChanged.connect(self.b48_63_change)

        self.lineEdit.textChanged.connect(self.lineChanged)
        self.setWindowTitle("Kalkulator wyjść")

    #@Slot(str)
    def b00_15_change(self, text:str):
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i in self.labels:
                self.labels[i].setDisabled(not bval)
            
    def b16_31_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i+16 in self.labels:
                self.labels[i+16].setDisabled(not bval)

    def b32_47_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i+32 in self.labels:
                self.labels[i+32].setDisabled(not bval)

    def b48_63_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i+48 in self.labels:
                self.labels[i+48].setDisabled(not bval)


    def lineChanged(self, txt:str):
        bytes = txt.replace(' ', '')
        #self.b48_63_change(bytes[0:4])
        self.b48_63.setText(bytes[0:4])
        #self.b32_47_change(bytes[4:8])
        self.b32_47.setText(bytes[4:8])
        #self.b16_31_change(bytes[8:12])
        self.b16_31.setText(bytes[8:12])
        #self.b00_15_change(bytes[12:16])
        self.b00_15.setText(bytes[12:16])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = WidgetCalc()
    w.show()
    app.exec()        