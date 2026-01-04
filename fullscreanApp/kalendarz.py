#*-* coding:utf-8 *-*
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


import os
import datetime
import time

import kalendarz_ui
import blackwidget

class Kalendarz(blackwidget.BlackWidget):
    def __init__(self, parent=None):
        super(Kalendarz, self).__init__(parent)
        self.kalendarz_ui = kalendarz_ui.Ui_Kalendarz()
        self.setupUi(self)


    def setupUi(self, kalendarz):
        self.kalendarz_ui.setupUi(kalendarz)

    def getRect(self):
       h = 400 
       return QRect(0, 1920-h-600, 1020, h)
    
    def timeout(self, dt):
        ddate = dt.date()

        y = ddate.year()
        mm = ddate.month()
