
from PySide6.QtWidgets import QGraphicsScene, QDialog, QFrame, QGraphicsLineItem, QApplication, QPushButton, QGraphicsEllipseItem, QGraphicsSimpleTextItem
from PySide6.QtWidgets import QVBoxLayout, QGraphicsRectItem, QGraphicsPathItem, QGridLayout, QToolButton, QLabel
from PySide6.QtGui import QBrush, QPen, QPolygonF, QPainterPath
from PySide6.QtCore import Qt, Slot, QPoint, QRect, QIODevice, QTimer, QObject, QSize, Signal, Slot
from PySide6 import QtSerialPort
from random import randint
import pyqtgraph as pg
import numpy as np
from ui_salon_sypialnia_graph import Ui_SalonSypialniaHol
import threading

pins = [
    [0,  0,  'INPUT',  " 57.08",  "Zasilanie awaryjne"],
    [0,  1,  'INPUT',  " 57.06",  "Druga taryfa"],
    [0,  2,  'INPUT',  " 57.04",  "Noc"],
    [0,  3,  'INPUT',  " 57.02",  "Wieczor"],
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

    [1,  0,  'INPUT',  " 55.02",  "Czujka ruchu 1 IN"],
    [1,  1,  'INPUT',  " 55.03",  "Czujka ruchu 2 IN"],
    [1,  2,  'INPUT',  "24_OFF",  "Zasilanie 24_OFF"],
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

    [2,  0,  'INPUT',  "214.10",  "29/15 Klawisz przy drzwiach wejsciowych"],
    [2,  1,  'INPUT',  "214.09",  "28/13 Hol na scianie pokoi"],
    [2,  2,  'INPUT',  "214.08",  "27/12 Hol na ścianie łazienki klawisz prawy"],
    [2,  3,  'INPUT',  "214.07",  "26/10 Hol na ścianie sypialnie lewy klawisz prawy"],
    [2,  4,  'INPUT',  "214.06",  "25/9 Hol na ścianie sypialnie prawy klawisz prawy"],
    [2,  5,  'INPUT',  "214.05",  "24/11 Salon na ścianie łazienki klawisz prawy"],
    [2,  6,  'INPUT',  "214.04",  "23/7 Salon na ścianie sypialni lewy klawisz prawy"],
    [2,  7,  'OUTPUT', " 59.03",  "Włączone światło w holu"],
    [2,  8,  'INPUT',  "214.03",  "22/6 Salon na ścianie sypialni prawy klawisz prawy"],
    [2,  9,  'INPUT',  "214.02",  "21/8 Salon klawisz prawy"],
    [2, 10,  'INPUT',  "214.01",  "20/5 Sypialnia klawisz prawy"],
    [2, 11,  'INPUT',  "216.08",  "7/12 Hol na ścianie łazienki klawisz lewy"],
    [2, 12,  'INPUT',  " 58.01",  "-/4 Salon obok jadalni lewy klawisz lewy"],
    [2, 13,  'INPUT',  " 58.02",  "-/4 Salon obok jadalni lewy klawisz prawy"],
    [2, 14,  'INPUT',  " 58.03",  "-/3 Salon obok jadalni prawy klawisz lewy"],
    [2, 15,  'OUTPUT', " 59.04",  "Włączone światło w salonie"],

    [3,  0,  'INPUT',  "216.07",  "6/10 Hol na ścianie sypialnie lewy klawisz lewy"],
    [3,  1,  'INPUT',  "216.06",  "5/9 Hol na ścianie sypialnie prawy klawisz lewy"],
    [3,  2,  'INPUT',  "216.05",  "4/11 Salon na ścianie łazienki klawisz lewy"],
    [3,  3,  'INPUT',  "216.04",  "3/7 Salon na ścianie sypialni lewy klawisz lewy"],
    [3,  4,  'INPUT',  "216.03",  "2/6 Salon na ścianie sypialni prawy klawisz lewy"],
    [3,  5,  'INPUT',  "216.02",  "1/8 Salon klawisz lewy"],
    [3,  6,  'INPUT',  "216.01",  "0/5 Sypialnia klawisz lewy"],
    [3,  7,  'OUTPUT', "------",  "x"],
    [3,  8,  'INPUT',  " 58.04",  "-/3 Salon obok jadalni prawy klawisz prawy"],
    [3,  9,  'INPUT',  " 58.05",  "-/2 kuchnia prawy klawisz lewy"],
    [3, 10,  'INPUT',  " 58.06",  "-/2 kuchnia prawy klawisz prawy"],
    [3, 11,  'INPUT',  " 58.07",  "-/14 Hol na scianie WC klawisz lewy"],
    [3, 12,  'INPUT',  " 58.08",  "-/14 Hol na scianie WC klawisz prawy"],
    [3, 13,  'INPUT',  "217.03",  "105/1 kuchnia lewy klawisz lewy"],
    [3, 14,  'INPUT',  "217.02",  "107/1 kuchnia lewy klawisz prawy"],
    [3, 15,  'OUTPUT', "------",  "x"],
]

others_pins = [
    ["217.02",  "107/1 kuchnia lewy klawisz prawy"],
]

class FrameButton(QFrame):
    def __init__(self, pionowo:bool, lefttxt:str, rigthtxt:str, clicked, parent=None):
        super(FrameButton, self).__init__(parent)

        if not self.objectName():
            self.setObjectName(u"FrameButton")
        if not pionowo:
            self.resize(75, 25)
        else:
            self.resize(25, 75)
        
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_both = QToolButton(self)
        self.pb_both.setObjectName(u"pb_both")
        self.pb_both.setMinimumSize(QSize(10, 15))
        self.pb_both.setMaximumSize(QSize(20, 20))
        font = self.font()
        font.setPointSize(6)
        self.pb_both.setFont(font)

        if not pionowo:
            self.gridLayout.addWidget(self.pb_both, 0, 1, 1, 1)
        else:
            self.gridLayout.addWidget(self.pb_both, 1, 0, 1, 1)

        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(10, 10))
        self.label.setMaximumSize(QSize(20, 10))
        self.label.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        self.label.setFont(font)

        if not pionowo:
            self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
        else:
            self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.pb_left = QToolButton(self)
        self.pb_left.setObjectName(u"pb_left")
        self.pb_left.setText(lefttxt)
        self.pb_left.setFont(font)

        if not pionowo:
            self.gridLayout.addWidget(self.pb_left, 0, 0, 2, 1)
        else:
            self.gridLayout.addWidget(self.pb_left, 0, 0, 1, 2)

        self.pb_rigth = QToolButton(self)
        self.pb_rigth.setObjectName(u"pb_rigth")
        self.pb_rigth.setText(rigthtxt)
        self.pb_rigth.setFont(font)

        if not pionowo:
            self.gridLayout.addWidget(self.pb_rigth, 0, 2, 2, 1)
        else:
            self.gridLayout.addWidget(self.pb_rigth, 2, 0, 1, 2)
        self.label.setText("")
        self.pb_both.setText("x")
        self.pb_both.setFont(font)

        _, pblid = lefttxt.split("\n")
        _, pbrid = rigthtxt.split("\n")

        self.pb_rigth.clicked.connect(lambda : clicked('', pbrid))
        self.pb_both.clicked.connect(lambda : clicked(pblid, pbrid))
        self.pb_left.clicked.connect(lambda : clicked(pblid, ''))

        self.ligth = False
        self.setValue(False)

    def setValue(self, val:bool):
        self.ligth = val
        if val:
            self.label.setStyleSheet(u"background-color: rgb(26, 95, 180);")
        else:
            self.label.setStyleSheet(u"background-color: rgb(255, 255, 255);")



class Wykres:
    def __init__(self, wykres):
        self.scene = QGraphicsScene(0, 0, 1090, 64*20+100)
        self.wykres = wykres
        self.wykres.setScene(self.scene)
        self.wykres.setMinimumHeight(970)
        self.wykres.setMinimumWidth(400)
        self.wykres.setMaximumHeight(970)
        self.wykres.setMaximumWidth(400)
        self.values = {}
        self.posMap = {}
        self.input = '0000000000000000'
        self.output = '0000000000000000'
                
        inr = 0
        marginx = 0
        self.ypin = []
        for p in pins:
            self.values[p[0]*16+p[1]] = []
            
        self.pinsMap = {}
        self.setInput(self.input)
        self.setOutput(self.output)
    
    def txt(self):
        marginx = 0
        txt1 = self.scene.addSimpleText('INPUT:%s' % (self.input))
        txt1.setPos(0, 0)
        txt2 = self.scene.addSimpleText('OUTPUT:%s' % (self.output))
        txt2.setPos(0, txt1.sceneBoundingRect().bottom()+5)
        y = txt2.sceneBoundingRect().bottom()+5

        xp = 0
        yp = y
        for p in pins:
            p1 = self.scene.addRect(xp, yp+5, 5, 5, brush=Qt.GlobalColor.red)
            p2 = self.scene.addRect(xp, yp+5, 5, 5, brush=Qt.GlobalColor.green)
            p3 = self.scene.addRect(xp, yp+12, 5, 5, brush=Qt.GlobalColor.red)
            p4 = self.scene.addRect(xp, yp+12, 5, 5, brush=Qt.GlobalColor.green)
            self.pinsMap[p[0]*16+p[1]] = (p1, p2, p3, p4)
            xp += 7
        y += 30
        
        for p in pins:
            txt = self.scene.addSimpleText('%d' % (p[0]*16+p[1]))
            self.posMap[p[0]*16+p[1]] = y

            txt.setPos(0, y)
            rect = txt.sceneBoundingRect()
            marginx = max(marginx, rect.right())
            y += 20
        self.marginx = marginx


    
    def setInput(self, input):
        self.input = input
        self.setValPos(0, self.input[15], self.output[15])
        self.setValPos(4, self.input[14], self.output[14])
        self.setValPos(8, self.input[13], self.output[13])
        self.setValPos(12, self.input[12], self.output[12])
        self.setValPos(16, self.input[11], self.output[11])
        self.setValPos(20, self.input[10], self.output[10])
        self.setValPos(24, self.input[9], self.output[9])
        self.setValPos(28, self.input[8], self.output[8])
        self.setValPos(32, self.input[7], self.output[7])
        self.setValPos(36, self.input[6], self.output[6])
        self.setValPos(40, self.input[5], self.output[5])
        self.setValPos(44, self.input[4], self.output[4])
        self.setValPos(48, self.input[3], self.output[3])
        self.setValPos(52, self.input[2], self.output[2])
        self.setValPos(56, self.input[1], self.output[1])
        self.setValPos(60, self.input[0], self.output[0])
        self.updateValues()

    def setOutput(self, output):
        self.output = output 
        self.setValPos(0, self.input[15], self.output[15])
        self.setValPos(4, self.input[14], self.output[14])
        self.setValPos(8, self.input[13], self.output[13])
        self.setValPos(12, self.input[12], self.output[12])
        self.setValPos(16, self.input[11], self.output[11])
        self.setValPos(20, self.input[10], self.output[10])
        self.setValPos(24, self.input[9], self.output[9])
        self.setValPos(28, self.input[8], self.output[8])
        self.setValPos(32, self.input[7], self.output[7])
        self.setValPos(36, self.input[6], self.output[6])
        self.setValPos(40, self.input[5], self.output[5])
        self.setValPos(44, self.input[4], self.output[4])
        self.setValPos(48, self.input[3], self.output[3])
        self.setValPos(52, self.input[2], self.output[2])
        self.setValPos(56, self.input[1], self.output[1])
        self.setValPos(60, self.input[0], self.output[0])
        self.updateValues()

    def setValPos(self, id, input, output):
        hex = '%x' % (int(input, 16) | int(output, 16))

        if hex == '0':
            self.values[id+3].append(0)
            self.values[id+2].append(0)
            self.values[id+1].append(0)
            self.values[id+0].append(0)
        elif hex == '1':
            self.values[id+3].append(0)
            self.values[id+2].append(0)
            self.values[id+1].append(0)
            self.values[id+0].append(1)
        elif hex == '2':
            self.values[id+3].append(0)
            self.values[id+2].append(0)
            self.values[id+1].append(1)
            self.values[id+0].append(0)
        elif hex == '3':
            self.values[id+3].append(0)
            self.values[id+2].append(0)
            self.values[id+1].append(1)
            self.values[id+0].append(1)
        elif hex == '4':
            self.values[id+3].append(0)
            self.values[id+2].append(1)
            self.values[id+1].append(0)
            self.values[id+0].append(0)
        elif hex == '5':
            self.values[id+3].append(0)
            self.values[id+2].append(1)
            self.values[id+1].append(0)
            self.values[id+0].append(1)
        elif hex == '6':
            self.values[id+3].append(0)
            self.values[id+2].append(1)
            self.values[id+1].append(1)
            self.values[id+0].append(0)
        elif hex == '7':
            self.values[id+3].append(0)
            self.values[id+2].append(1)
            self.values[id+1].append(1)
            self.values[id+0].append(1)
        elif hex == '8':
            self.values[id+3].append(1)
            self.values[id+2].append(0)
            self.values[id+1].append(0)
            self.values[id+0].append(0)
        elif hex == '9':
            self.values[id+3].append(1)
            self.values[id+2].append(0)
            self.values[id+1].append(0)
            self.values[id+0].append(1)
        elif hex == 'a' or hex == 'A':
            self.values[id+3].append(1)
            self.values[id+2].append(0)
            self.values[id+1].append(1)
            self.values[id+0].append(0)
        elif hex == 'b' or hex == 'B':
            self.values[id+3].append(1)
            self.values[id+2].append(0)
            self.values[id+1].append(1)
            self.values[id+0].append(1)
        elif hex == 'c' or hex == 'C':
            self.values[id+3].append(1)
            self.values[id+2].append(1)
            self.values[id+1].append(0)
            self.values[id+0].append(0)
        elif hex == 'd' or hex == 'D':
            self.values[id+3].append(1)
            self.values[id+2].append(1)
            self.values[id+1].append(0)
            self.values[id+0].append(1)
        elif hex == 'e' or hex == 'E':
            self.values[id+3].append(1)
            self.values[id+2].append(1)
            self.values[id+1].append(1)
            self.values[id+0].append(0)
        elif hex == 'f' or hex == 'F':
            self.values[id+3].append(1)
            self.values[id+2].append(1)
            self.values[id+1].append(1)
            self.values[id+0].append(1)

    def setIORejestr(self, id, pref, val1, val2, val3, val4):
        if val1:
            self.pinsMap[id-3][pref+0].hide()
            self.pinsMap[id-3][pref+1].show()
        else:
            self.pinsMap[id-3][pref+1].hide()
            self.pinsMap[id-3][pref+0].show()

        if val2:
            self.pinsMap[id-2][pref+0].hide()
            self.pinsMap[id-2][pref+1].show()
        else:
            self.pinsMap[id-2][pref+1].hide()
            self.pinsMap[id-2][pref+0].show()

        if val3:
            self.pinsMap[id-1][pref+0].hide()
            self.pinsMap[id-1][pref+1].show()
        else:
            self.pinsMap[id-1][pref+1].hide()
            self.pinsMap[id-1][pref+0].show()

        if val4:
            self.pinsMap[id-0][pref+0].hide()
            self.pinsMap[id-0][pref+1].show()
        else:
            self.pinsMap[id-0][pref+1].hide()
            self.pinsMap[id-0][pref+0].show()

    def setRejestr(self, id, input, output):
        hex = int(input, 16)
        self.setIORejestr(63-id, 0, (hex>>3)&0x1, (hex>>2)&0x1, (hex>>1)&0x1, hex&0x1)
        hex = int(output, 16)
        self.setIORejestr(63-id, 2, (hex>>3)&0x1, (hex>>2)&0x1, (hex>>1)&0x1, hex&0x1)
        
    def updateValues(self):
        self.scene.clear()
        self.txt()

        self.setRejestr(0, self.input[15], self.output[15])
        self.setRejestr(4, self.input[14], self.output[14])
        self.setRejestr(8, self.input[13], self.output[13])
        self.setRejestr(12, self.input[12], self.output[12])
        self.setRejestr(16, self.input[11], self.output[11])
        self.setRejestr(20, self.input[10], self.output[10])
        self.setRejestr(24, self.input[9], self.output[9])
        self.setRejestr(28, self.input[8], self.output[8])
        self.setRejestr(32, self.input[7], self.output[7])
        self.setRejestr(36, self.input[6], self.output[6])
        self.setRejestr(40, self.input[5], self.output[5])
        self.setRejestr(44, self.input[4], self.output[4])
        self.setRejestr(48, self.input[3], self.output[3])
        self.setRejestr(52, self.input[2], self.output[2])
        self.setRejestr(56, self.input[1], self.output[1])
        self.setRejestr(60, self.input[0], self.output[0])

        for k in self.posMap.keys():
            prev = 0
            path = QPainterPath()
            polyline = QPolygonF()
            y = self.posMap[k]
            y0 = y + 13
            y1 = y + 2
            x = int(self.marginx)
            polyline.append(QPoint(x, y0))
            
            for iv in range(len(self.values[k])-1):
                val = self.values[k][iv]
                x += 5
                if val == prev:
                    prev = val
                    continue        
                prev = val
                if val == 0:
                    polyline.append(QPoint(x,  y1))
                    polyline.append(QPoint(x,  y0))
                else:
                    polyline.append(QPoint(x,  y0))
                    polyline.append(QPoint(x,  y1))
            val = self.values[k][-1]
            x+=5
            if val == 0:
                polyline.append(QPoint(x,  y0))
                polyline.append(QPoint(x,  y1))
            else:
                polyline.append(QPoint(x,  y1))
                polyline.append(QPoint(x,  y0))
            path.addPolygon(polyline)
            new_item = QGraphicsPathItem(path, None)
            new_item.setPath(path)
            self.scene.addItem(new_item)

class Swiatlo:
    def __init__(self, scene, x:int, y:int, txt:str):
        pen2 = QPen(Qt.GlobalColor.black)
        pen2.setWidth(2)
        self.widgets = { True : QGraphicsEllipseItem(QRect(0, 0, 35, 35)), False : QGraphicsEllipseItem(QRect(0, 0, 35, 35))}
        for s in [True, False]:
            self.widgets[s].setPos(x, y)
            self.widgets[s].setPen(pen2)
            scene.addItem(self.widgets[s])

        self.widgets[True].setBrush(Qt.GlobalColor.yellow)
        self.widgets[True].hide()
        self.widgets[False].setBrush(Qt.GlobalColor.gray)
        txtI = QGraphicsSimpleTextItem(txt)
        txtI.setPos(x+4, y+8)        
        scene.addItem(txtI)

    def setVal(self, val:bool):
        self.widgets[val].show()
        self.widgets[not val].hide()

class KontrolkaBox(object):
    def __init__(self, scene, x:int, y:int, txt:str, color = Qt.GlobalColor.red):
        super(KontrolkaBox, self).__init__()
        pen2 = QPen(Qt.GlobalColor.black)
        f = scene.font()
        f.setPointSize(8)
        txtI = QGraphicsSimpleTextItem(txt)
        txtI.setFont(f)
        txtI.setPos(x+12, y-3)        
        scene.addItem(txtI)
        self.widgets = { True : QGraphicsEllipseItem(QRect(0, 0, 10, 10)), False : QGraphicsEllipseItem(QRect(0, 0, 10, 10))}
        for s in [True, False]:
            self.widgets[s].setPos(x, y)
            self.widgets[s].setPen(pen2)
            scene.addItem(self.widgets[s])

        self.widgets[True].setBrush(Qt.GlobalColor.red)
        self.widgets[True].hide()
        self.widgets[False].setBrush(Qt.GlobalColor.gray)
    
    def setVal(self, val:bool):
        self.widgets[val].show()
        self.widgets[not val].hide()

class Wlacznik(object):
    def __init__(self, scene:QGraphicsScene, x:int, y:int, txtL:str, txtR:str, clicked):
        super(Wlacznik, self).__init__()
        #font = scene.font()
        #font.setPointSize(6)
        #self.items = []
        
        #self.left = QPushButton(txtL)
        #self.left.setGeometry(x, y, 30, 30)
        #self.left.clicked.connect(clickedL)
        #self.left.setFont(font)
        #self.items.append(scene.addWidget(self.left))

        #self.both = QPushButton("x")
        #self.both.setGeometry(x+26, y, 15, 30)
        #self.both.clicked.connect(clickedX) 
        #self.both.setFont(font)
        #self.items.append(scene.addWidget(self.both))

        #self.right = QPushButton(txtR)
        #self.right.setGeometry(x+37, y, 30, 30)
        #self.right.clicked.connect(clickedR)
        #self.right.setFont(font)
        #self.items.append(scene.addWidget(self.right))
        self.btns = FrameButton(False, txtL, txtR, clicked)
        item = scene.addWidget(self.btns)
        item.setPos(x, y)

class WlacznikPods(Wlacznik):
    def __init__(self, scene, x:int, y:int, txtL:str, txtR:str, clicked, top:bool = True):
        super(WlacznikPods, self).__init__(scene, x, y, txtL, txtR, clicked)
        #self.widgets = { True : QGraphicsEllipseItem(QRect(0, 0, 10, 10)), False : QGraphicsEllipseItem(QRect(0, 0, 10, 10))}        
        #pen2 = QPen(Qt.GlobalColor.black)
        #pen2.setWidth(1)
        #for s in [True, False]:
        #    self.widgets[s].setPos(x+31, y+35 if top else y-15)
        #    self.widgets[s].setPen(pen2)
        #    scene.addItem(self.widgets[s])

        #self.widgets[True].setBrush(Qt.GlobalColor.blue)
        #self.widgets[True].hide()
        #self.widgets[False].setBrush(Qt.GlobalColor.gray)

    #def setVal(self, val:bool):
    #    self.widgets[val].show()
    #    self.widgets[not val].hide()

class WlacznikR:
    def __init__(self, scene:QGraphicsScene, x:int, y:int, txtL:str, txtR:str, clicked):
        #font = scene.font()
        #font.setPointSize(6)
        #self.items = []
        
        #self.left = QPushButton(txtL)
        #self.left.setGeometry(x, y, 30, 30)
        #self.left.clicked.connect(clickedL)
        #self.left.setFont(font)
        #self.items.append(scene.addWidget(self.left))

        #self.both = QPushButton("x")
        #self.both.setGeometry(x, y+31, 30, 15)
        #self.both.clicked.connect(clickedX) 
        #self.both.setFont(font)
        #self.items.append(scene.addWidget(self.both))

        #self.right = QPushButton(txtR)
        #self.right.setGeometry(x, y+46, 30, 30)
        #self.right.clicked.connect(clickedR)
        #self.right.setFont(font)
        #self.items.append(scene.addWidget(self.right))
        self.btns = FrameButton(True, txtL, txtR, clicked)
        self.btns.resize(25, 75)
        item = scene.addWidget(self.btns)
        item.setPos(x, y)

class WlacznikPodsR(WlacznikR):
    def __init__(self, scene, x:int, y:int, txtL:str, txtR:str, clicked, right:bool = True):
        super(WlacznikPodsR, self).__init__(scene, x, y, txtL, txtR, clicked)
        #self.widgets = { True : QGraphicsEllipseItem(QRect(0, 0, 10, 10)), False : QGraphicsEllipseItem(QRect(0, 0, 10, 10))}        
        #pen2 = QPen(Qt.GlobalColor.black)
        #pen2.setWidth(1)
        #for s in [True, False]:
        #    self.widgets[s].setPos(x+35 if right else x-15, y+34)
        #    self.widgets[s].setPen(pen2)
        #    scene.addItem(self.widgets[s])

        #self.widgets[True].setBrush(Qt.GlobalColor.blue)
        #self.widgets[True].hide()
        #self.widgets[False].setBrush(Qt.GlobalColor.gray)
        self.btns = FrameButton(True, txtL, txtR, clicked)
        self.btns.resize(25, 75)
        item = scene.addWidget(self.btns)
        item.setPos(x, y)

    #def setVal(self, val:bool):
    #    self.widgets[val].show()
    #    self.widgets[not val].hide()

class Wlacznik1:
    def __init__(self, scene:QGraphicsScene, x:int, y:int, txt:str, clicked):
        font = scene.font()
        font.setPointSize(6)
        self.items = []
        
        self.pb = QPushButton(txt)
        self.pb.setGeometry(x, y, 30, 30)

        _, pbid = txt.split("\n")
        self.pb.clicked.connect(lambda : clicked(pbid.strip(), ''))
        self.pb.setFont(font)
        self.items.append(scene.addWidget(self.pb))

class InputCl:
    def __init__(self):
        self.inputs = {}
        self.mapP = {}
        for p in pins:
            idx = p[0]*16+p[1]
            if p[2] == 'INPUT':
                self.inputs[idx] = False if idx in [16,17,18] else True
                try :
                    d1, d2 = p[3].split('.')
                    self.mapP['%d.%d' % (int(d1), int(d2))] = idx
                except:
                    pass

    def setNoc(self, val):
        self.inputs[2] = not val

    def setWieczor(self, val):
        self.inputs[3] = not val

    def setZasAwar(self, val):
        self.inputs[0] = not val

    def setTaryfa2(self, val):
        self.inputs[1] = not val

    def setCzujka1(self, val):
        self.inputs[16] = val 

    def setCzujka2(self, val):
        self.inputs[17] = val
    
    def setV24_off(self, val):
        self.inputs[18] = val
    
    def set(self, pos:str, val:bool):
        print(pos, val)
        if pos in self.mapP:
            idx = self.mapP[pos]
            print(idx)
            self.inputs[idx] = not val
        else:
            print(self.mapP.keys())
    
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

        for i in range(8):
            idx = 56+i
            if idx in self.inputs and self.inputs[idx]:
                b_3B += 0x1 << i

        for i in range(8):
            idx = 48+i
            if idx in self.inputs and self.inputs[idx]:
                b_3A += 0x1 << i

        for i in range(8):
            idx = 40+i
            if idx in self.inputs and self.inputs[idx]:
                b_2B += 0x1 << i

        for i in range(8):
            idx = 32+i
            if idx in self.inputs and self.inputs[idx]:
                b_2A += 0x1 << i

        for i in range(8):
            idx = 24+i
            if idx in self.inputs and self.inputs[idx]:
                b_1B += 0x1 << i

        for i in range(8):
            idx = 16+i
            if idx in self.inputs and self.inputs[idx]:
                b_1A += 0x1 << i

        for i in range(8):
            idx = 8+i
            if idx in self.inputs and self.inputs[idx]:
                b_0B += 0x1 << i

        for i in range(8):
            idx = i
            if idx in self.inputs and self.inputs[idx]:
                b_0A += 0x1 << i

        buf += "%03d %03d %03d %03d %03d %03d %03d %03d ]\n\r" % (b_3B, b_3A, b_2B, b_2A,b_1B, b_1A, b_0B, b_0A)
        buf2 = "%02x%02x %02x%02x %02x%02x %02x%02x" % (b_3B, b_3A,b_2B, b_2A,b_1B, b_1A, b_0B, b_0A)
        return buf, buf2

class Widget2(QDialog, Ui_SalonSypialniaHol):
    def __init__(self, *args, obj=None, **kwargs):
        super(Widget2, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.setGeometry(0, 0, 1920, 1020)
        self.inReg = InputCl()

        self.opisKlawiszy = {
            "sypialnia" : ("5P42\n214.1", "5L54\n216.1"),
            "salon_sypialnia_lewy": ("7L38\n216.4", "7P51\n214.4"),
            "salon_sypialnia_prawy": ("6L40\n216.3", "6P52\n214.3"),
            "salon_jadalnia_lewy": ("4L4\n58.1", "4P45\n58.2"),
            "salon_jadalnia_prawy": ("3L46\n58.3", "3P56\n58.4"),
            "salon_kuchnia_lewy": ("1L61\n217.2", "1P62\n217.3"),
            "salon_kuchnia_prawy": ("2L57\n58.5", "2P58\n58.6"),
            "salon": ("8L53\n216.2", "8P41\n214.2"),
            "salon_lazienka": ("11L51\n216.5", "11P37\n214.5"),
            "hol_lazienka": ("12L43\n216.8", "12P34\n214.8"),
            "hol_salon_lewy": ("10L48\n216.7", "10P35\n214.7"),
            "hol_salon_prawy": ("9L49\n216.6", "9P36\n214.6"),
            "hol_wc": ("14L59\n58.7", "14P60\n58.8"),
            "hol_pokoje": ("13K33\n214.9",),
            "hol_drzwi": ("15K32\n214.10",)
        }

        self.scene = QGraphicsScene(0, 0, 1160, 920)
        self.plan.setScene(self.scene)
        self.plan.setMinimumHeight(930)
        self.plan.setMinimumWidth(1170)
        self.plan.setMaximumHeight(930)
        self.plan.setMaximumWidth(1170)

        self.mix_podswielenie = [KontrolkaBox(self.scene, 5, 560, "Podśw. włączników mix (21)")]
        self.hol_podswielenie = [KontrolkaBox(self.scene, 5, 585, "Podśw. włączników hol (22)")]
        self.salon_podswielenie = [KontrolkaBox(self.scene, 5, 610, "Podśw. włączników salon (23)")]

        self.sypialnia()
        self.salon()
        self.hol()
        self.zarys()
        for p in pins:
            lp = "%02d" % (p[0]*16+p[1])
            if p[2] == 'OUTPUT':
                txt = getattr(self, 'lo_'+lp, None)
                if txt is not None:
                    txt.setText("%d, %s" % (p[0]*16+p[1], p[4]))
            if p[2] == 'INPUT':
                txt = getattr(self, 'li_'+lp, None)
                if txt is not None:
                    txt.setText("%d, %s" % (p[0]*16+p[1], p[4]))

            zlacze = 'z{}'.format(p[3].strip().replace('.','_'))
            l = getattr(self, zlacze, None)
            if l is not None:
                l.setText(p[4])                      

        self.zasilacz12v = KontrolkaBox(self.scene, 413, 210, "Zasilacz 12V (13)")
        self.gwarantowane_n = KontrolkaBox(self.scene, 413, 240, "Gwarantowane N (29)")
        self.gwarantowane_l = KontrolkaBox(self.scene, 413, 270, "Gwarantowane L (30)")

        

        self.swiatlo_sypialnia = KontrolkaBox(self.scene, 5, 660, "Światło sypialnia (19)", Qt.GlobalColor.green)
        self.swiatlo_hol = KontrolkaBox(self.scene, 5, 685, "Światło hol (39)", Qt.GlobalColor.green)
        self.swiatlo_salon = KontrolkaBox(self.scene, 5, 710, "Światło salon (47)", Qt.GlobalColor.green)
        self.czujka_ruchu = KontrolkaBox(self.scene, 5, 735, "Czujka ruchu (20)", Qt.GlobalColor.green)


        self.zasawaryjne = KontrolkaBox(self.scene, 8, 10, "Zasilanie awaryjne (0)", Qt.GlobalColor.blue)
        self.taryfa2 = KontrolkaBox(self.scene, 8, 35, "Druga taryfa (1)", Qt.GlobalColor.blue)
        self.noc = KontrolkaBox(self.scene, 8, 60, "Noc (2)", Qt.GlobalColor.blue)
        self.wieczor = KontrolkaBox(self.scene, 8, 85, "Wieczor (3)", Qt.GlobalColor.blue)
        self.zasilanie24V = KontrolkaBox(self.scene, 8, 110, "Zasilanie 24V (18)", Qt.GlobalColor.blue)

        self.czujka1 = KontrolkaBox(self.scene, 8, 135, "Czujka A (16)", Qt.GlobalColor.blue)
        self.czujka2 = KontrolkaBox(self.scene, 8, 160, "Czujka B (17)", Qt.GlobalColor.blue)

        self.inputs = {
            "24V" : False,
            "2taryfa" : False,
            "noc" : False,
            "wieczor" : False,
            "zasawar" : False,
            "czujka1" : False,
            "czujka2" : False,
            "usb0" : False,
            "acm0" : False,
        }

        self.pb_24V.clicked.connect(self.on_clicked_24V)
        self.pb_2taryfa.clicked.connect(self.on_clicked_2taryfa)
        self.pb_noc.clicked.connect(self.on_clicked_noc)
        self.pb_wieczor.clicked.connect(self.on_clicked_wieczor)
        self.pb_zasawar.clicked.connect(self.on_clicked_zasawar)
        self.pb_czujka1.clicked.connect(self.on_clicked_czujka1)
        self.pb_czujka2.clicked.connect(self.on_clicked_czujka2)
                
        self.pbusb0.clicked.connect(self.on_usb0_clicked)
        self.pbacm0.clicked.connect(self.on_acm0_clicked)
        
        self.wykresClass = Wykres(self.wykres)


    def zarys(self):
            rects = []        
            lines1 = []
            lines2 = []
            lines3 = []
            lines4 = []
            lines5 = []
            lines6 = []
            lines7 = []
            lines8 = []
            lines9 = []
            lines = []

            lines1.append(QPoint(360,0))
            lines1.append(QPoint(390,0))
            lines1.append(QPoint(390,300))
            lines1.append(QPoint(990,300))
            lines.append(lines1)

            lines2.append(QPoint(1110,300))
            lines2.append(QPoint(1140,300))
            lines.append(lines2)

            lines3.append(QPoint(210,0))
            lines3.append(QPoint(180,0))
            lines3.append(QPoint(180,225))
            lines3.append(QPoint(150,225))
            lines.append(lines3)

            lines4.append(QPoint(30,225))
            lines4.append(QPoint(0,225))
            lines4.append(QPoint(0,255))
            lines.append(lines4)

            lines5.append(QPoint(0,355))
            lines5.append(QPoint(0,395))
            lines.append(lines5)
        
            lines6.append(QPoint(0,495))
            lines6.append(QPoint(0,525))
            lines6.append(QPoint(30,525))
            lines.append(lines6)
        
            lines7.append(QPoint(150,525))
            lines7.append(QPoint(300,525))
            lines7.append(QPoint(300,825))
            lines.append(lines7)

            lines8.append(QPoint(420,750))
            lines8.append(QPoint(420,825))
            lines8.append(QPoint(900,825))
            lines.append(lines8)

            lines9.append(QPoint(405,0))
            lines9.append(QPoint(1140,0))
            lines9.append(QPoint(1140,900))
            lines.append(lines9)
            
            brush = QBrush(Qt.GlobalColor.black)
            pen = QPen(Qt.GlobalColor.black)
            pen.setWidth(10)
            for lines in lines:
                prev = None
                for p in lines:
                    if prev is None:
                        prev = p
                        continue
                    line = QGraphicsLineItem(prev.x(), prev.y(), p.x(), p.y())
                    line.setPen(pen)
                    self.scene.addItem(line)
                    prev = p

    def sypialnia(self):
        self.sypialniaSw = Wlacznik(self.scene, 920, 260, *self.opisKlawiszy["sypialnia"], self.clicked_pb)
        
        self.sypialnia1 = Swiatlo(self.scene, 675, 113, "1.27")
        self.sypialnia2 = Swiatlo(self.scene, 715, 113, "2.24")
        self.kinkiety = Swiatlo(self.scene, 720, 15, "k.25")
        
    def salon(self):
        pen2 = QPen(Qt.GlobalColor.black)
        pen2.setWidth(2)

        self.salon1 = Swiatlo(self.scene, 705, 553, "1.31")
        self.salon2 = Swiatlo(self.scene, 745, 553, "2.28")

        self.led_salsyp1 = Swiatlo(self.scene, 1020, 490, "1.14")
        self.led_salsyp2 = Swiatlo(self.scene, 1020, 530, "2.15")
        
        self.salonsw2 = WlacznikPods(self.scene, 840, 308, *self.opisKlawiszy["salon_sypialnia_lewy"], self.clicked_pb)
        self.salonsw1 = WlacznikPods(self.scene, 920, 308, *self.opisKlawiszy["salon_sypialnia_prawy"], self.clicked_pb)
        self.salon_podswielenie.append(self.salonsw1)
        self.salon_podswielenie.append(self.salonsw2)

        self.salonsw3 = WlacznikPods(self.scene, 387, 308, *self.opisKlawiszy["salon"], self.clicked_pb)
        self.mix_podswielenie.append(self.salonsw3)

        self.salonsw5 = WlacznikPods(self.scene, 750, 780, *self.opisKlawiszy["salon_jadalnia_prawy"], self.clicked_pb, False)
        self.salonsw4 = WlacznikPods(self.scene, 830, 780, *self.opisKlawiszy["salon_jadalnia_lewy"], self.clicked_pb, False)
        self.salon_podswielenie.append(self.salonsw5)
        self.salon_podswielenie.append(self.salonsw4)

        self.salonsw7 = WlacznikR(self.scene, 375, 780, *self.opisKlawiszy["salon_kuchnia_prawy"], self.clicked_pb)
        self.salonsw6 = WlacznikR(self.scene, 375, 690, *self.opisKlawiszy["salon_kuchnia_lewy"], self.clicked_pb)

        self.salonsw8 = WlacznikPodsR(self.scene, 308, 525, *self.opisKlawiszy["salon_lazienka"], self.clicked_pb)
        self.mix_podswielenie.append(self.salonsw8)
        
        self.led_sallaz1 = Swiatlo(self.scene, 375, 490, "1.04")
        self.led_sallaz2 = Swiatlo(self.scene, 375, 530, "2.05")
        
    def hol(self):
        
        self.salonsw11 = WlacznikPodsR(self.scene, 345, 220, *self.opisKlawiszy["hol_salon_prawy"], self.clicked_pb, False)
        self.salonsw10 = WlacznikPodsR(self.scene, 345, 140, *self.opisKlawiszy["hol_salon_lewy"], self.clicked_pb, False)
        self.hol_podswielenie.append(self.salonsw11)
        self.hol_podswielenie.append(self.salonsw10)

        self.salonsw12 = WlacznikPodsR(self.scene, 188, 156, *self.opisKlawiszy["hol_wc"], self.clicked_pb)
        self.hol_podswielenie.append(self.salonsw12)

        self.salonsw13 = WlacznikPods(self.scene, 230, 490, *self.opisKlawiszy["hol_lazienka"], self.clicked_pb, False)
        self.hol_podswielenie.append(self.salonsw13)
        self.salonsw14 = Wlacznik1(self.scene, 190, 40, *self.opisKlawiszy["hol_drzwi"], self.clicked_pb)
        self.salonsw15 = Wlacznik1(self.scene, 10, 360, *self.opisKlawiszy["hol_pokoje"], self.clicked_pb)

        self.led_3_1 = Swiatlo(self.scene, 255, 40, "1.11")
        self.led_3_2 = Swiatlo(self.scene, 255, 80, "2.06")
        self.led_3_3 = Swiatlo(self.scene, 255, 120, "3.12")

        self.led_4_0 = Swiatlo(self.scene, 90, 355, "0.26")
        self.led_4_1 = Swiatlo(self.scene, 150, 375, "1.10")
        self.led_4_2 = Swiatlo(self.scene, 150, 335, "2.09")
        self.led_4_3 = Swiatlo(self.scene, 190, 335, "3.08")
        self.led_4_4 = Swiatlo(self.scene, 190, 375, "4.07")

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

    @Slot()
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
                    self.led_sallaz1.setVal(val)
                elif pos == 5:
                    self.led_sallaz2.setVal(val)
                elif pos == 14:
                    self.led_salsyp1.setVal(val)
                elif pos == 15:
                    self.led_salsyp2.setVal(val)

                elif pos == 6:
                    self.led_3_1.setVal(val)
                elif pos == 7:
                    self.led_3_2.setVal(val)
                elif pos == 8:
                    self.led_3_3.setVal(val)
                elif pos == 9:
                    self.led_4_4.setVal(val)
                elif pos == 10:
                    self.led_4_3.setVal(val)
                elif pos == 11:
                    self.led_4_2.setVal(val)
                elif pos == 12:
                    self.led_4_1.setVal(val)
                elif pos == 13:
                    self.zasilacz12v.setVal(val)
                
                elif pos == 24:
                    self.sypialnia1.setVal(val)
                elif pos == 25:
                    self.kinkiety.setVal(val)

                elif pos == 26:
                    self.led_4_0.setVal(val)
                elif pos == 27:
                    self.sypialnia2.setVal(val)
                elif pos == 28:
                    self.salon2.setVal(val)
                elif pos == 31:
                    self.salon1.setVal(val)
                
                elif pos == 21:
                    for p in self.mix_podswielenie:
                        p.setVal(val)
                    
                
                elif pos == 22:
                    for p in self.hol_podswielenie:
                        p.setVal(val)
                
                elif pos == 23:
                    for p in self.salon_podswielenie:
                        p.setVal(val)

                elif pos == 29:
                    self.gwarantowane_n.setVal(val)
                elif pos == 30:
                    self.gwarantowane_l.setVal(val)
                
                elif pos == 19:
                    self.swiatlo_sypialnia.setVal(val)
                elif pos == 20:
                    self.czujka_ruchu.setVal(val)
                elif pos == 39:
                    self.swiatlo_hol.setVal(val)
                elif pos == 47:
                    self.swiatlo_salon.setVal(val)
            elif text[:4] == 'S;H;':
                chks = text.split(";")
                
                if chks[2] == 'Chg in':
                    self.wykresClass.setInput(chks[3])
                elif chks[2] == 'Chg out':
                    self.wykresClass.setOutput(chks[3])
            elif text[:4] == 'S;I;':
                _, _, txt, hexI, hexO = text.split(";")
                self.wykresClass.setInput(hexI)
                self.wykresClass.setOutput(hexO)

    @Slot()
    def receive_acm0(self):
        while self.serial_arduino.canReadLine():
            text = self.serial_arduino.readLine().data().decode()
            text = text.rstrip('\r\n')
            self.te_acm0.append(text)
            
    @Slot()
    def on_clicked_24V(self):
        k = "24V"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setV24_off(val)
        self.sendInput()
        self.zasilanie24V.setVal(val)

    @Slot()
    def on_clicked_noc(self):
        k = "noc"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setNoc(val)
        self.sendInput()
        self.noc.setVal(val)

    @Slot()
    def on_clicked_wieczor(self):
        k = "wieczor"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setWieczor(val)
        self.sendInput()
        self.wieczor.setVal(val)

    @Slot()
    def on_clicked_zasawar(self):
        print("on_clicked_zasawar")
        k = "zasawar"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setZasAwar(val)
        self.sendInput()
        self.zasawaryjne.setVal(val)

    @Slot()
    def on_clicked_czujka1(self):
        k = "czujka1"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setCzujka1(val)
        self.sendInput()
        self.czujka1.setVal(val)
    
    @Slot()
    def on_clicked_czujka2(self):
        k = "czujka2"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setCzujka2(val)
        self.sendInput()
        self.czujka2.setVal(val)
    
    @Slot()
    def on_clicked_2taryfa(self):
        k = "2taryfa"
        val = not self.inputs[k]
        self.inputs[k] = val
        self.inReg.setTaryfa2(val)
        self.sendInput()
        self.taryfa2.setVal(val)

    def clicked_pb(self, left:str, right:str):
        if len(left) > 0 and len(right) > 0:
            self.inReg.set(left, True)
            self.inReg.set(right, True)
            self.sendInput()    
            self.inReg.set(left, False)
            self.inReg.set(right, False)
            self.sendInput()
        elif len(left) > 0:
            self.inReg.set(left, True)
            self.sendInput()    
            self.inReg.set(left, False)
            self.sendInput()
        elif len(right) > 0:
            self.inReg.set(right, True)
            self.sendInput()    
            self.inReg.set(right, False)
            self.sendInput()
    


    def sendMsg(self):
        self.serial_rs485.write(self.message_le.text().encode())

    def sendInput(self):
        msg, dgb = self.inReg.getInput()
        self.te_acm0.append("Send:"+msg)
        self.te_acm0.append("INPUT:"+dgb)
        self.serial_arduino.write(msg.encode())

    @Slot()
    def on_usb0_clicked(self):
        k = "usb0"
        val = not self.inputs[k]
        
        self.inputs[k] = val
        if val:
            if not self.serial_rs485.isOpen():
                if not self.serial_rs485.open(QIODevice.ReadWrite):
                    self.inputs[k] = False
                else:
                    self.serial_rs485.write("I;".encode('ascii'))
                    self.serial_rs485.write("S;I;".encode('ascii'))
        else:
            self.serial_rs485.close()
        self.pbusb0.setText(u"Rozlacz z USB" if self.inputs[k] else u"Połącz z USB")

    @Slot()
    def on_acm0_clicked(self):
        k = "acm0"
        val = not self.inputs[k]
        
        if val:
            if not self.serial_arduino.isOpen():
                if not self.serial_arduino.open(QIODevice.ReadWrite):
                    self.inputs[k] = False

        else:
            self.serial_arduino.close()
        self.pbacm0.setText(u"Rozlacz z ACM0" if self.inputs[k] else u"Połącz z ACMO")

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
    w = Widget2()
    w.show()
    w.connectUsb("/dev/serial/by-id/usb-SparkFun_SparkFun_Pro_Micro-if00", "/dev/serial/by-id/usb-WCH.CN_USB_Quad_Serial_BC5644ABCD-if04")
    sys.exit(app.exec())


