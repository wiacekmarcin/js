import sys
from PySide6.QtWidgets import QDialog, QApplication, QLabel

from ui_kalkulator_wejsc_salon import Ui_Dialog

pins = [
    [0,  0,  'INPUT',  " 57.08",  "Zasilanie awaryjne"],
    [0,  1,  'INPUT',  " 57.06",  "Druga taryfa"],
    [0,  2,  'INPUT',  " 57.04",  "Noc"],
    [0,  3,  'INPUT',  " 57.02",  "Wieczor"],

    [1,  0,  'INPUT',  " 55.02",  "Czujka ruchu 1 IN"],
    [1,  1,  'INPUT',  " 55.03",  "Czujka ruchu 2 IN"],
    [1,  2,  'INPUT',  "24_OFF",  "Zasilanie 24_OFF"],

    [2,  0,  'INPUT',  "214.10",  "29/15 Klawisz przy drzwiach wejsciowych"],
    [2,  1,  'INPUT',  "214.09",  "28/13 Hol na scianie pokoi"],
    [2,  2,  'INPUT',  "214.08",  "27/12 Hol na ścianie łazienki klawisz prawy"],
    [2,  3,  'INPUT',  "214.07",  "26/10 Hol na ścianie sypialnie lewy klawisz prawy"],
    [2,  4,  'INPUT',  "214.06",  "25/9 Hol na ścianie sypialnie prawy klawisz prawy"],
    [2,  5,  'INPUT',  "214.05",  "24/11 Salon na ścianie łazienki klawisz prawy"],
    [2,  6,  'INPUT',  "214.04",  "23/7 Salon na ścianie sypialni lewy klawisz prawy"],

    [2,  8,  'INPUT',  "214.03",  "22/6 Salon na ścianie sypialni prawy klawisz prawy"],
    [2,  9,  'INPUT',  "214.02",  "21/8 Salon klawisz prawy"],
    [2, 10,  'INPUT',  "214.01",  "20/5 Sypialnia klawisz prawy"],
    [2, 11,  'INPUT',  "216.08",  "7/12 Hol na ścianie łazienki klawisz lewy"],
    [2, 12,  'INPUT',  " 58.01",  "-/4 Salon obok jadalni lewy klawisz lewy"],
    [2, 13,  'INPUT',  " 58.02",  "-/4 Salon obok jadalni lewy klawisz prawy"],
    [2, 14,  'INPUT',  " 58.03",  "-/3 Salon obok jadalni prawy klawisz lewy"],


    [3,  0,  'INPUT',  "216.07",  "6/10 Hol na ścianie sypialnie lewy klawisz lewy"],
    [3,  1,  'INPUT',  "216.06",  "5/9 Hol na ścianie sypialnie prawy klawisz lewy"],
    [3,  2,  'INPUT',  "216.05",  "4/11 Salon na ścianie łazienki klawisz lewy"],
    [3,  3,  'INPUT',  "216.04",  "3/7 Salon na ścianie sypialni lewy klawisz lewy"],
    [3,  4,  'INPUT',  "216.03",  "2/6 Salon na ścianie sypialni prawy klawisz lewy"],
    [3,  5,  'INPUT',  "216.02",  "1/8 Salon klawisz lewy"],
    [3,  6,  'INPUT',  "216.01",  "0/5 Sypialnia klawisz lewy"],

    [3,  8,  'INPUT',  " 58.04",  "-/3 Salon obok jadalni prawy klawisz prawy"],
    [3,  9,  'INPUT',  " 58.05",  "-/2 kuchnia prawy klawisz lewy"],
    [3, 10,  'INPUT',  " 58.06",  "-/2 kuchnia prawy klawisz prawy"],
    [3, 11,  'INPUT',  " 58.07",  "-/14 Hol na scianie WC klawisz lewy"],
    [3, 12,  'INPUT',  " 58.08",  "-/14 Hol na scianie WC klawisz prawy"],
    [3, 13,  'INPUT',  "217.03",  "105/1 kuchnia lewy klawisz lewy"],
    [3, 14,  'INPUT',  "217.02",  "107/1 kuchnia lewy klawisz prawy"],
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
        self.setWindowTitle("Kalkulator wejść")

    #@Slot(str)
    def b00_15_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i in self.labels:
                self.labels[i].setDisabled(bval)
            
    def b16_31_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            print(i, bval) 
            if i+16 in self.labels:
                self.labels[i+16].setDisabled(not bval)

    def b32_47_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i+32 in self.labels:
                self.labels[i+32].setDisabled(bval)

    def b48_63_change(self, text:str):
        val = int(text, 16)
        for i in range(16):
            bval = ((val >> i) & 0x1) == 1
            if i+48 in self.labels:
                self.labels[i+48].setDisabled(bval)


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