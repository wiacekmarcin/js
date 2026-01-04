#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import os
import datetime
import time

import blackwidget
import kredyty_ui



class Kredyty(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Kredyty, self).__init__(parent)
        self.kred = kredyty_ui.Ui_Kredyty()
        self.setupUi(self)
        self.isImage = False
        self.maxCnt = 0
        self.cntSec = self.maxCnt
        self.showKredyty = True
        self.str_pic = ""

    def getRect(self):
        return QRect(1020-700, 1920-150, 700, 150)
    
    def setupUi(self, Kredyty):
        self.kred.setupUi(Kredyty)
    
    def receiveNotfication(self, dictValue):
        if "feature.kredyty" in dictValue:
            self.showKredyty = dictValue["feature.kredyty"]
            if not self.showKredyty:
                self.kred.label.setPixmap(QPixmap());
                #self.kred.label.setMask(pixmap.mask());
    def timeout(self, dt):
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()

        fstr = 'kredyty_%d_' % y
        if mm < 10: fstr += '0'
        fstr += '%d' % mm

        
        if not self.showKredyty and self.str_pic == fstr and self.isImage:
            return
        self.str_pic = fstr
        self.isImage = False

        fpath = os.path.join("/home/pi/tmp", fstr) + ".png"
        if os.path.exists(fpath):
            if not self.isImage:
                self.isImage = True
                pixmap = QPixmap (fpath)
                self.kred.label.setPixmap(pixmap);
                self.kred.label.setMask(pixmap.mask());
        else:
            self.isImage = False


        


    
    
