#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *

import os
import datetime
import time

import blackwidget

class HA_WWW(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(HA_WWW, self).__init__(parent)
        self.initUI()


    def initUI(self):
        vbox = QVBoxLayout(self)

        self.web = QWebEngineView()
        self.loadPage()
        vbox.addWidget(self.web)
        self.setLayout(vbox)

        r = self.getRect()
        self.setGeometry(r.x(), r.y(), r.width(), r.height())
        self.web.setZoomFactor(0.75)
        self.web.setMaximumHeight(r.height())
        self.web.setMaximumWidth(r.width())
 
        #self.setWindowTitle('QWebEngineView')
        self.show()

    def loadPage(self):
        self.web.load(QUrl("http://192.168.10.250:8123/dashboard-moc/zuzycie-energii?kiosk"))
        #self.web.load(QUrl("http://192.168.10.250:8123/zuzycie-energii-lustro?kiosk"))
    
    def getRect(self):
       h = 350
       return QRect(0, 1920-h-150, 1020, h)
    
    def setupUi(self, HA_WWW):
        pass
    
    def timeout(self, dt):
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()
