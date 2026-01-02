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

        web = QWebEngineView()
        web.load(QUrl("http://192.168.10.250:8123/dashboard-moc/zuzycie-energii?kiosk"))
        web.show()

    def getRect(self):
        return QRect(1080-800, 1920-150, 800, 150)
    
    def setupUi(self, HA_WWW):
        pass
    
    def timeout(self, dt):
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()

        


        


    
    