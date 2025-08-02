# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salon_sypialnia_hol.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QSpacerItem, QTextEdit, QToolButton,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1569, 899)
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout = QVBoxLayout(self.groupBox_2)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.frame_2 = QFrame(self.groupBox_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setSpacing(5)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(5, 5, 5, 5)
        self.led4 = QFrame(self.frame_2)
        self.led4.setObjectName(u"led4")
        self.led4.setMinimumSize(QSize(25, 25))
        self.led4.setMaximumSize(QSize(25, 25))
        self.led4.setAutoFillBackground(False)
        self.led4.setStyleSheet(u"background: \"white\"")
        self.led4.setFrameShape(QFrame.StyledPanel)
        self.led4.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.led4, 5, 2, 1, 1)

        self.led2 = QFrame(self.frame_2)
        self.led2.setObjectName(u"led2")
        self.led2.setMinimumSize(QSize(25, 25))
        self.led2.setMaximumSize(QSize(25, 25))
        self.led2.setAutoFillBackground(False)
        self.led2.setStyleSheet(u"background: \"white\"")
        self.led2.setFrameShape(QFrame.StyledPanel)
        self.led2.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.led2, 0, 2, 1, 1)

        self.line = QFrame(self.frame_2)
        self.line.setObjectName(u"line")
        self.line.setMinimumSize(QSize(150, 2))
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line, 1, 0, 1, 3)

        self.salon1 = QFrame(self.frame_2)
        self.salon1.setObjectName(u"salon1")
        self.salon1.setMinimumSize(QSize(25, 25))
        self.salon1.setMaximumSize(QSize(25, 25))
        self.salon1.setAutoFillBackground(False)
        self.salon1.setStyleSheet(u"background: \"white\"")
        self.salon1.setFrameShape(QFrame.StyledPanel)
        self.salon1.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.salon1, 2, 1, 1, 1)

        self.line_2 = QFrame(self.frame_2)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setMinimumSize(QSize(150, 2))
        self.line_2.setSizeIncrement(QSize(1024, 0))
        self.line_2.setBaseSize(QSize(150, 2))
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout_7.addWidget(self.line_2, 4, 0, 1, 3)

        self.lsalon1 = QLabel(self.frame_2)
        self.lsalon1.setObjectName(u"lsalon1")

        self.gridLayout_7.addWidget(self.lsalon1, 2, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_7.addItem(self.verticalSpacer_2, 6, 0, 1, 1)

        self.salon2 = QFrame(self.frame_2)
        self.salon2.setObjectName(u"salon2")
        self.salon2.setMinimumSize(QSize(25, 25))
        self.salon2.setMaximumSize(QSize(25, 25))
        self.salon2.setAutoFillBackground(False)
        self.salon2.setStyleSheet(u"background: \"white\"")
        self.salon2.setFrameShape(QFrame.StyledPanel)
        self.salon2.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.salon2, 2, 2, 1, 1)

        self.lled1 = QLabel(self.frame_2)
        self.lled1.setObjectName(u"lled1")

        self.gridLayout_7.addWidget(self.lled1, 0, 0, 1, 1)

        self.led1 = QFrame(self.frame_2)
        self.led1.setObjectName(u"led1")
        self.led1.setMinimumSize(QSize(25, 25))
        self.led1.setMaximumSize(QSize(25, 25))
        self.led1.setAutoFillBackground(False)
        self.led1.setStyleSheet(u"background: \"white\"")
        self.led1.setFrameShape(QFrame.StyledPanel)
        self.led1.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.led1, 0, 1, 1, 1)

        self.lled3 = QLabel(self.frame_2)
        self.lled3.setObjectName(u"lled3")

        self.gridLayout_7.addWidget(self.lled3, 5, 0, 1, 1)

        self.led3 = QFrame(self.frame_2)
        self.led3.setObjectName(u"led3")
        self.led3.setMinimumSize(QSize(25, 25))
        self.led3.setMaximumSize(QSize(25, 25))
        self.led3.setAutoFillBackground(False)
        self.led3.setStyleSheet(u"background: \"white\"")
        self.led3.setFrameShape(QFrame.StyledPanel)
        self.led3.setFrameShadow(QFrame.Raised)

        self.gridLayout_7.addWidget(self.led3, 5, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.groupBox_3 = QGroupBox(self.groupBox_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pb_216_4 = QPushButton(self.groupBox_3)
        self.pb_216_4.setObjectName(u"pb_216_4")

        self.horizontalLayout_2.addWidget(self.pb_216_4)

        self.pb_21x_4 = QToolButton(self.groupBox_3)
        self.pb_21x_4.setObjectName(u"pb_21x_4")

        self.horizontalLayout_2.addWidget(self.pb_21x_4)

        self.pb_214_4 = QPushButton(self.groupBox_3)
        self.pb_214_4.setObjectName(u"pb_214_4")

        self.horizontalLayout_2.addWidget(self.pb_214_4)

        self.salon_podswietlenie_1 = QFrame(self.groupBox_3)
        self.salon_podswietlenie_1.setObjectName(u"salon_podswietlenie_1")
        self.salon_podswietlenie_1.setMinimumSize(QSize(25, 25))
        self.salon_podswietlenie_1.setMaximumSize(QSize(25, 25))
        self.salon_podswietlenie_1.setAutoFillBackground(False)
        self.salon_podswietlenie_1.setStyleSheet(u"background: \"white\"")
        self.salon_podswietlenie_1.setFrameShape(QFrame.StyledPanel)
        self.salon_podswietlenie_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.salon_podswietlenie_1)

        self.pb_216_3 = QPushButton(self.groupBox_3)
        self.pb_216_3.setObjectName(u"pb_216_3")

        self.horizontalLayout_2.addWidget(self.pb_216_3)

        self.pb_21x_3 = QToolButton(self.groupBox_3)
        self.pb_21x_3.setObjectName(u"pb_21x_3")

        self.horizontalLayout_2.addWidget(self.pb_21x_3)

        self.pb_214_3 = QPushButton(self.groupBox_3)
        self.pb_214_3.setObjectName(u"pb_214_3")

        self.horizontalLayout_2.addWidget(self.pb_214_3)


        self.verticalLayout.addWidget(self.groupBox_3)

        self.groupBox_6 = QGroupBox(self.groupBox_2)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.horizontalLayout_5 = QHBoxLayout(self.groupBox_6)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.pb_58_1 = QPushButton(self.groupBox_6)
        self.pb_58_1.setObjectName(u"pb_58_1")

        self.horizontalLayout_5.addWidget(self.pb_58_1)

        self.pb_58_1x2 = QToolButton(self.groupBox_6)
        self.pb_58_1x2.setObjectName(u"pb_58_1x2")

        self.horizontalLayout_5.addWidget(self.pb_58_1x2)

        self.pb_58_2 = QPushButton(self.groupBox_6)
        self.pb_58_2.setObjectName(u"pb_58_2")

        self.horizontalLayout_5.addWidget(self.pb_58_2)

        self.salon_podswietlenie_3 = QFrame(self.groupBox_6)
        self.salon_podswietlenie_3.setObjectName(u"salon_podswietlenie_3")
        self.salon_podswietlenie_3.setMinimumSize(QSize(25, 25))
        self.salon_podswietlenie_3.setMaximumSize(QSize(25, 25))
        self.salon_podswietlenie_3.setAutoFillBackground(False)
        self.salon_podswietlenie_3.setStyleSheet(u"background: \"white\"")
        self.salon_podswietlenie_3.setFrameShape(QFrame.StyledPanel)
        self.salon_podswietlenie_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.salon_podswietlenie_3)

        self.pb_58_3 = QPushButton(self.groupBox_6)
        self.pb_58_3.setObjectName(u"pb_58_3")

        self.horizontalLayout_5.addWidget(self.pb_58_3)

        self.pb_58_3x4 = QToolButton(self.groupBox_6)
        self.pb_58_3x4.setObjectName(u"pb_58_3x4")

        self.horizontalLayout_5.addWidget(self.pb_58_3x4)

        self.pb_58_4 = QPushButton(self.groupBox_6)
        self.pb_58_4.setObjectName(u"pb_58_4")

        self.horizontalLayout_5.addWidget(self.pb_58_4)


        self.verticalLayout.addWidget(self.groupBox_6)

        self.groupBox_5 = QGroupBox(self.groupBox_2)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.horizontalLayout_4 = QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.pb_217_2 = QPushButton(self.groupBox_5)
        self.pb_217_2.setObjectName(u"pb_217_2")

        self.horizontalLayout_4.addWidget(self.pb_217_2)

        self.pb_217_x = QToolButton(self.groupBox_5)
        self.pb_217_x.setObjectName(u"pb_217_x")

        self.horizontalLayout_4.addWidget(self.pb_217_x)

        self.pb_217_3 = QPushButton(self.groupBox_5)
        self.pb_217_3.setObjectName(u"pb_217_3")

        self.horizontalLayout_4.addWidget(self.pb_217_3)

        self.kuchnia_podswietlenie = QFrame(self.groupBox_5)
        self.kuchnia_podswietlenie.setObjectName(u"kuchnia_podswietlenie")
        self.kuchnia_podswietlenie.setMinimumSize(QSize(25, 25))
        self.kuchnia_podswietlenie.setMaximumSize(QSize(25, 25))
        self.kuchnia_podswietlenie.setAutoFillBackground(False)
        self.kuchnia_podswietlenie.setStyleSheet(u"background: \"silver\"")
        self.kuchnia_podswietlenie.setFrameShape(QFrame.StyledPanel)
        self.kuchnia_podswietlenie.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.kuchnia_podswietlenie)

        self.pb_58_5 = QPushButton(self.groupBox_5)
        self.pb_58_5.setObjectName(u"pb_58_5")

        self.horizontalLayout_4.addWidget(self.pb_58_5)

        self.pb_58_5x6 = QToolButton(self.groupBox_5)
        self.pb_58_5x6.setObjectName(u"pb_58_5x6")

        self.horizontalLayout_4.addWidget(self.pb_58_5x6)

        self.pb_58_6 = QPushButton(self.groupBox_5)
        self.pb_58_6.setObjectName(u"pb_58_6")

        self.horizontalLayout_4.addWidget(self.pb_58_6)


        self.verticalLayout.addWidget(self.groupBox_5)

        self.groupBox_4 = QGroupBox(self.groupBox_2)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.pb_216_2 = QPushButton(self.groupBox_4)
        self.pb_216_2.setObjectName(u"pb_216_2")

        self.horizontalLayout_3.addWidget(self.pb_216_2)

        self.pb_21x_2 = QToolButton(self.groupBox_4)
        self.pb_21x_2.setObjectName(u"pb_21x_2")

        self.horizontalLayout_3.addWidget(self.pb_21x_2)

        self.pb_214_2 = QPushButton(self.groupBox_4)
        self.pb_214_2.setObjectName(u"pb_214_2")

        self.horizontalLayout_3.addWidget(self.pb_214_2)

        self.salon_podswietlenie_2 = QFrame(self.groupBox_4)
        self.salon_podswietlenie_2.setObjectName(u"salon_podswietlenie_2")
        self.salon_podswietlenie_2.setMinimumSize(QSize(25, 25))
        self.salon_podswietlenie_2.setMaximumSize(QSize(25, 25))
        self.salon_podswietlenie_2.setAutoFillBackground(False)
        self.salon_podswietlenie_2.setStyleSheet(u"background: \"white\"")
        self.salon_podswietlenie_2.setFrameShape(QFrame.StyledPanel)
        self.salon_podswietlenie_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_3.addWidget(self.salon_podswietlenie_2)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)


        self.verticalLayout.addWidget(self.groupBox_4)

        self.groupBox_7 = QGroupBox(self.groupBox_2)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.horizontalLayout_6 = QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_6.setSpacing(5)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(5, 5, 5, 5)
        self.pb_216_5 = QPushButton(self.groupBox_7)
        self.pb_216_5.setObjectName(u"pb_216_5")

        self.horizontalLayout_6.addWidget(self.pb_216_5)

        self.pb_21x_5 = QToolButton(self.groupBox_7)
        self.pb_21x_5.setObjectName(u"pb_21x_5")

        self.horizontalLayout_6.addWidget(self.pb_21x_5)

        self.pb_214_5 = QPushButton(self.groupBox_7)
        self.pb_214_5.setObjectName(u"pb_214_5")

        self.horizontalLayout_6.addWidget(self.pb_214_5)

        self.mix_podswielenie_1 = QFrame(self.groupBox_7)
        self.mix_podswielenie_1.setObjectName(u"mix_podswielenie_1")
        self.mix_podswielenie_1.setMinimumSize(QSize(25, 25))
        self.mix_podswielenie_1.setMaximumSize(QSize(25, 25))
        self.mix_podswielenie_1.setAutoFillBackground(False)
        self.mix_podswielenie_1.setStyleSheet(u"background: \"white\"")
        self.mix_podswielenie_1.setFrameShape(QFrame.StyledPanel)
        self.mix_podswielenie_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_6.addWidget(self.mix_podswielenie_1)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)


        self.verticalLayout.addWidget(self.groupBox_7)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.groupBox_15 = QGroupBox(self.groupBox_2)
        self.groupBox_15.setObjectName(u"groupBox_15")
        self.gridLayout_4 = QGridLayout(self.groupBox_15)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.val_zasilanieAwar = QCheckBox(self.groupBox_15)
        self.val_zasilanieAwar.setObjectName(u"val_zasilanieAwar")

        self.gridLayout_4.addWidget(self.val_zasilanieAwar, 0, 2, 1, 1)

        self.val_czujka1 = QCheckBox(self.groupBox_15)
        self.val_czujka1.setObjectName(u"val_czujka1")

        self.gridLayout_4.addWidget(self.val_czujka1, 1, 0, 1, 1)

        self.val_24V = QCheckBox(self.groupBox_15)
        self.val_24V.setObjectName(u"val_24V")

        self.gridLayout_4.addWidget(self.val_24V, 1, 2, 1, 1)

        self.val_wieczor = QCheckBox(self.groupBox_15)
        self.val_wieczor.setObjectName(u"val_wieczor")

        self.gridLayout_4.addWidget(self.val_wieczor, 0, 1, 1, 1)

        self.val_czujka2 = QCheckBox(self.groupBox_15)
        self.val_czujka2.setObjectName(u"val_czujka2")

        self.gridLayout_4.addWidget(self.val_czujka2, 1, 1, 1, 1)

        self.val_noc = QCheckBox(self.groupBox_15)
        self.val_noc.setObjectName(u"val_noc")

        self.gridLayout_4.addWidget(self.val_noc, 0, 0, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 2, 1, 1, 1)

        self.checkBox = QCheckBox(self.groupBox_15)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout_4.addWidget(self.checkBox, 2, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_15)


        self.gridLayout.addWidget(self.groupBox_2, 0, 3, 2, 1)

        self.groupBox_8 = QGroupBox(Form)
        self.groupBox_8.setObjectName(u"groupBox_8")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox_8)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.frame_3 = QFrame(self.groupBox_8)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(5)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(5, 5, 5, 5)
        self.lhol1 = QLabel(self.frame_3)
        self.lhol1.setObjectName(u"lhol1")

        self.gridLayout_2.addWidget(self.lhol1, 0, 0, 1, 1)

        self.led3_2 = QFrame(self.frame_3)
        self.led3_2.setObjectName(u"led3_2")
        self.led3_2.setMinimumSize(QSize(25, 25))
        self.led3_2.setMaximumSize(QSize(25, 25))
        self.led3_2.setAutoFillBackground(False)
        self.led3_2.setStyleSheet(u"background: \"white\"")
        self.led3_2.setFrameShape(QFrame.StyledPanel)
        self.led3_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led3_2, 4, 2, 1, 1)

        self.led4_2 = QFrame(self.frame_3)
        self.led4_2.setObjectName(u"led4_2")
        self.led4_2.setMinimumSize(QSize(25, 25))
        self.led4_2.setMaximumSize(QSize(25, 25))
        self.led4_2.setAutoFillBackground(False)
        self.led4_2.setStyleSheet(u"background: \"white\"")
        self.led4_2.setFrameShape(QFrame.StyledPanel)
        self.led4_2.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led4_2, 0, 2, 1, 1)

        self.led4_0 = QFrame(self.frame_3)
        self.led4_0.setObjectName(u"led4_0")
        self.led4_0.setMinimumSize(QSize(25, 25))
        self.led4_0.setMaximumSize(QSize(25, 25))
        self.led4_0.setAutoFillBackground(False)
        self.led4_0.setStyleSheet(u"background: \"white\"")
        self.led4_0.setFrameShape(QFrame.StyledPanel)
        self.led4_0.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led4_0, 0, 5, 1, 1)

        self.led4_3 = QFrame(self.frame_3)
        self.led4_3.setObjectName(u"led4_3")
        self.led4_3.setMinimumSize(QSize(25, 25))
        self.led4_3.setMaximumSize(QSize(25, 25))
        self.led4_3.setAutoFillBackground(False)
        self.led4_3.setStyleSheet(u"background: \"white\"")
        self.led4_3.setFrameShape(QFrame.StyledPanel)
        self.led4_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led4_3, 1, 1, 2, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 5, 0, 1, 1)

        self.led3_3 = QFrame(self.frame_3)
        self.led3_3.setObjectName(u"led3_3")
        self.led3_3.setMinimumSize(QSize(25, 25))
        self.led3_3.setMaximumSize(QSize(25, 25))
        self.led3_3.setAutoFillBackground(False)
        self.led3_3.setStyleSheet(u"background: \"white\"")
        self.led3_3.setFrameShape(QFrame.StyledPanel)
        self.led3_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led3_3, 4, 3, 1, 2)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_7, 4, 5, 1, 1)

        self.line_3 = QFrame(self.frame_3)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_3, 3, 0, 1, 1)

        self.led4_1 = QFrame(self.frame_3)
        self.led4_1.setObjectName(u"led4_1")
        self.led4_1.setMinimumSize(QSize(25, 25))
        self.led4_1.setMaximumSize(QSize(25, 25))
        self.led4_1.setAutoFillBackground(False)
        self.led4_1.setStyleSheet(u"background: \"white\"")
        self.led4_1.setFrameShape(QFrame.StyledPanel)
        self.led4_1.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led4_1, 0, 1, 1, 1)

        self.led4_4 = QFrame(self.frame_3)
        self.led4_4.setObjectName(u"led4_4")
        self.led4_4.setMinimumSize(QSize(25, 25))
        self.led4_4.setMaximumSize(QSize(25, 25))
        self.led4_4.setAutoFillBackground(False)
        self.led4_4.setStyleSheet(u"background: \"white\"")
        self.led4_4.setFrameShape(QFrame.StyledPanel)
        self.led4_4.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led4_4, 1, 2, 2, 1)

        self.lhol2 = QLabel(self.frame_3)
        self.lhol2.setObjectName(u"lhol2")

        self.gridLayout_2.addWidget(self.lhol2, 4, 0, 1, 1)

        self.led3_1 = QFrame(self.frame_3)
        self.led3_1.setObjectName(u"led3_1")
        self.led3_1.setMinimumSize(QSize(25, 25))
        self.led3_1.setMaximumSize(QSize(25, 25))
        self.led3_1.setAutoFillBackground(False)
        self.led3_1.setStyleSheet(u"background: \"white\"")
        self.led3_1.setFrameShape(QFrame.StyledPanel)
        self.led3_1.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.led3_1, 4, 1, 1, 1)

        self.line_4 = QFrame(self.frame_3)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.VLine)
        self.line_4.setFrameShadow(QFrame.Sunken)

        self.gridLayout_2.addWidget(self.line_4, 0, 3, 3, 2)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.groupBox_9 = QGroupBox(self.groupBox_8)
        self.groupBox_9.setObjectName(u"groupBox_9")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBox_9)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(5, 5, 5, 5)
        self.pb_214_7 = QPushButton(self.groupBox_9)
        self.pb_214_7.setObjectName(u"pb_214_7")

        self.horizontalLayout_7.addWidget(self.pb_214_7)

        self.pb_21x_7 = QToolButton(self.groupBox_9)
        self.pb_21x_7.setObjectName(u"pb_21x_7")

        self.horizontalLayout_7.addWidget(self.pb_21x_7)

        self.pb_216_7 = QPushButton(self.groupBox_9)
        self.pb_216_7.setObjectName(u"pb_216_7")

        self.horizontalLayout_7.addWidget(self.pb_216_7)

        self.podswietlenie_hol_1 = QFrame(self.groupBox_9)
        self.podswietlenie_hol_1.setObjectName(u"podswietlenie_hol_1")
        self.podswietlenie_hol_1.setMinimumSize(QSize(25, 25))
        self.podswietlenie_hol_1.setMaximumSize(QSize(25, 25))
        self.podswietlenie_hol_1.setAutoFillBackground(False)
        self.podswietlenie_hol_1.setStyleSheet(u"background: \"white\"")
        self.podswietlenie_hol_1.setFrameShape(QFrame.StyledPanel)
        self.podswietlenie_hol_1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_7.addWidget(self.podswietlenie_hol_1)

        self.pb_214_6 = QPushButton(self.groupBox_9)
        self.pb_214_6.setObjectName(u"pb_214_6")

        self.horizontalLayout_7.addWidget(self.pb_214_6)

        self.pb_21x_6 = QToolButton(self.groupBox_9)
        self.pb_21x_6.setObjectName(u"pb_21x_6")

        self.horizontalLayout_7.addWidget(self.pb_21x_6)

        self.pb_216_6 = QPushButton(self.groupBox_9)
        self.pb_216_6.setObjectName(u"pb_216_6")

        self.horizontalLayout_7.addWidget(self.pb_216_6)


        self.verticalLayout_2.addWidget(self.groupBox_9)

        self.groupBox_10 = QGroupBox(self.groupBox_8)
        self.groupBox_10.setObjectName(u"groupBox_10")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBox_10)
        self.horizontalLayout_8.setSpacing(5)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.pb_214_8 = QPushButton(self.groupBox_10)
        self.pb_214_8.setObjectName(u"pb_214_8")

        self.horizontalLayout_8.addWidget(self.pb_214_8)

        self.pb_21x_8 = QToolButton(self.groupBox_10)
        self.pb_21x_8.setObjectName(u"pb_21x_8")

        self.horizontalLayout_8.addWidget(self.pb_21x_8)

        self.pb_216_8 = QPushButton(self.groupBox_10)
        self.pb_216_8.setObjectName(u"pb_216_8")

        self.horizontalLayout_8.addWidget(self.pb_216_8)

        self.mix_podswietlenie_2 = QFrame(self.groupBox_10)
        self.mix_podswietlenie_2.setObjectName(u"mix_podswietlenie_2")
        self.mix_podswietlenie_2.setMinimumSize(QSize(25, 25))
        self.mix_podswietlenie_2.setMaximumSize(QSize(25, 25))
        self.mix_podswietlenie_2.setAutoFillBackground(False)
        self.mix_podswietlenie_2.setStyleSheet(u"background: \"white\"")
        self.mix_podswietlenie_2.setFrameShape(QFrame.StyledPanel)
        self.mix_podswietlenie_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_8.addWidget(self.mix_podswietlenie_2)

        self.horizontalSpacer_9 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_9)


        self.verticalLayout_2.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(self.groupBox_8)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBox_11)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(5, 5, 5, 5)
        self.pb_58_7 = QPushButton(self.groupBox_11)
        self.pb_58_7.setObjectName(u"pb_58_7")

        self.horizontalLayout_9.addWidget(self.pb_58_7)

        self.pb_58_7x8 = QToolButton(self.groupBox_11)
        self.pb_58_7x8.setObjectName(u"pb_58_7x8")

        self.horizontalLayout_9.addWidget(self.pb_58_7x8)

        self.pb_58_8 = QPushButton(self.groupBox_11)
        self.pb_58_8.setObjectName(u"pb_58_8")

        self.horizontalLayout_9.addWidget(self.pb_58_8)

        self.hol_podswietlenie_2 = QFrame(self.groupBox_11)
        self.hol_podswietlenie_2.setObjectName(u"hol_podswietlenie_2")
        self.hol_podswietlenie_2.setMinimumSize(QSize(25, 25))
        self.hol_podswietlenie_2.setMaximumSize(QSize(25, 25))
        self.hol_podswietlenie_2.setAutoFillBackground(False)
        self.hol_podswietlenie_2.setStyleSheet(u"background: \"white\"")
        self.hol_podswietlenie_2.setFrameShape(QFrame.StyledPanel)
        self.hol_podswietlenie_2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.hol_podswietlenie_2)

        self.horizontalSpacer_10 = QSpacerItem(193, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_10)


        self.verticalLayout_2.addWidget(self.groupBox_11)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.groupBox_12 = QGroupBox(self.groupBox_8)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBox_12)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.pb_214_10 = QPushButton(self.groupBox_12)
        self.pb_214_10.setObjectName(u"pb_214_10")

        self.horizontalLayout_10.addWidget(self.pb_214_10)

        self.hol_podswietlenie_3 = QFrame(self.groupBox_12)
        self.hol_podswietlenie_3.setObjectName(u"hol_podswietlenie_3")
        self.hol_podswietlenie_3.setMinimumSize(QSize(25, 25))
        self.hol_podswietlenie_3.setMaximumSize(QSize(25, 25))
        self.hol_podswietlenie_3.setAutoFillBackground(False)
        self.hol_podswietlenie_3.setStyleSheet(u"background: \"white\"")
        self.hol_podswietlenie_3.setFrameShape(QFrame.StyledPanel)
        self.hol_podswietlenie_3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.hol_podswietlenie_3)

        self.horizontalSpacer_11 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_11)


        self.horizontalLayout_12.addWidget(self.groupBox_12)

        self.groupBox_13 = QGroupBox(self.groupBox_8)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.horizontalLayout_11 = QHBoxLayout(self.groupBox_13)
        self.horizontalLayout_11.setSpacing(5)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(5, 5, 5, 5)
        self.pb_214_9 = QPushButton(self.groupBox_13)
        self.pb_214_9.setObjectName(u"pb_214_9")

        self.horizontalLayout_11.addWidget(self.pb_214_9)

        self.led4_9 = QFrame(self.groupBox_13)
        self.led4_9.setObjectName(u"led4_9")
        self.led4_9.setMinimumSize(QSize(25, 25))
        self.led4_9.setMaximumSize(QSize(25, 25))
        self.led4_9.setAutoFillBackground(False)
        self.led4_9.setStyleSheet(u"background: \"silver\"")
        self.led4_9.setFrameShape(QFrame.StyledPanel)
        self.led4_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_11.addWidget(self.led4_9)

        self.horizontalSpacer_12 = QSpacerItem(81, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_12)


        self.horizontalLayout_12.addWidget(self.groupBox_13)


        self.verticalLayout_2.addLayout(self.horizontalLayout_12)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_5)


        self.gridLayout.addWidget(self.groupBox_8, 1, 2, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_6 = QGridLayout(self.groupBox)
        self.gridLayout_6.setSpacing(5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(5, 5, 5, 5)
        self.kinkiety = QFrame(self.groupBox)
        self.kinkiety.setObjectName(u"kinkiety")
        self.kinkiety.setMinimumSize(QSize(25, 25))
        self.kinkiety.setMaximumSize(QSize(25, 25))
        self.kinkiety.setAutoFillBackground(False)
        self.kinkiety.setStyleSheet(u"background: \"white\"")
        self.kinkiety.setFrameShape(QFrame.StyledPanel)
        self.kinkiety.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.kinkiety, 1, 1, 1, 1)

        self.sypialnia2 = QFrame(self.groupBox)
        self.sypialnia2.setObjectName(u"sypialnia2")
        self.sypialnia2.setMinimumSize(QSize(25, 25))
        self.sypialnia2.setMaximumSize(QSize(25, 25))
        self.sypialnia2.setAutoFillBackground(False)
        self.sypialnia2.setStyleSheet(u"background: \"white\"")
        self.sypialnia2.setFrameShape(QFrame.StyledPanel)
        self.sypialnia2.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.sypialnia2, 0, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_6.addItem(self.verticalSpacer, 4, 0, 1, 1)

        self.lsypialnia1 = QLabel(self.groupBox)
        self.lsypialnia1.setObjectName(u"lsypialnia1")

        self.gridLayout_6.addWidget(self.lsypialnia1, 0, 0, 1, 1)

        self.lkinkiety = QLabel(self.groupBox)
        self.lkinkiety.setObjectName(u"lkinkiety")

        self.gridLayout_6.addWidget(self.lkinkiety, 1, 0, 1, 1)

        self.sypialnia1 = QFrame(self.groupBox)
        self.sypialnia1.setObjectName(u"sypialnia1")
        self.sypialnia1.setMinimumSize(QSize(25, 25))
        self.sypialnia1.setMaximumSize(QSize(25, 25))
        self.sypialnia1.setAutoFillBackground(False)
        self.sypialnia1.setStyleSheet(u"background: \"white\"")
        self.sypialnia1.setFrameShape(QFrame.StyledPanel)
        self.sypialnia1.setFrameShadow(QFrame.Raised)

        self.gridLayout_6.addWidget(self.sypialnia1, 0, 1, 1, 1)

        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_6.addItem(self.horizontalSpacer_13, 0, 3, 1, 1)

        self.frame = QFrame(self.groupBox)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_216_1 = QPushButton(self.frame)
        self.pb_216_1.setObjectName(u"pb_216_1")

        self.horizontalLayout.addWidget(self.pb_216_1)

        self.pb_21x_1 = QToolButton(self.frame)
        self.pb_21x_1.setObjectName(u"pb_21x_1")

        self.horizontalLayout.addWidget(self.pb_21x_1)

        self.pb_214_1 = QPushButton(self.frame)
        self.pb_214_1.setObjectName(u"pb_214_1")

        self.horizontalLayout.addWidget(self.pb_214_1)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.gridLayout_6.addWidget(self.frame, 3, 0, 1, 4)


        self.gridLayout.addWidget(self.groupBox, 0, 2, 1, 1)

        self.groupBox_18 = QGroupBox(Form)
        self.groupBox_18.setObjectName(u"groupBox_18")
        self.verticalLayout_5 = QVBoxLayout(self.groupBox_18)
        self.verticalLayout_5.setSpacing(5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(5, 5, 5, 5)
        self.label_6 = QLabel(self.groupBox_18)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_5.addWidget(self.label_6)

        self.label_7 = QLabel(self.groupBox_18)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_5.addWidget(self.label_7)

        self.label_9 = QLabel(self.groupBox_18)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_5.addWidget(self.label_9)

        self.label_10 = QLabel(self.groupBox_18)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_5.addWidget(self.label_10)

        self.label_11 = QLabel(self.groupBox_18)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_5.addWidget(self.label_11)

        self.label_12 = QLabel(self.groupBox_18)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_5.addWidget(self.label_12)

        self.label_13 = QLabel(self.groupBox_18)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_5.addWidget(self.label_13)

        self.label_14 = QLabel(self.groupBox_18)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_5.addWidget(self.label_14)

        self.label_15 = QLabel(self.groupBox_18)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_5.addWidget(self.label_15)

        self.label_16 = QLabel(self.groupBox_18)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_5.addWidget(self.label_16)

        self.label_17 = QLabel(self.groupBox_18)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_5.addWidget(self.label_17)

        self.label_18 = QLabel(self.groupBox_18)
        self.label_18.setObjectName(u"label_18")

        self.verticalLayout_5.addWidget(self.label_18)

        self.label_32 = QLabel(self.groupBox_18)
        self.label_32.setObjectName(u"label_32")

        self.verticalLayout_5.addWidget(self.label_32)

        self.label_33 = QLabel(self.groupBox_18)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_5.addWidget(self.label_33)

        self.label_19 = QLabel(self.groupBox_18)
        self.label_19.setObjectName(u"label_19")

        self.verticalLayout_5.addWidget(self.label_19)

        self.label_20 = QLabel(self.groupBox_18)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_5.addWidget(self.label_20)

        self.label_21 = QLabel(self.groupBox_18)
        self.label_21.setObjectName(u"label_21")

        self.verticalLayout_5.addWidget(self.label_21)

        self.label_22 = QLabel(self.groupBox_18)
        self.label_22.setObjectName(u"label_22")

        self.verticalLayout_5.addWidget(self.label_22)

        self.label_23 = QLabel(self.groupBox_18)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_5.addWidget(self.label_23)

        self.label_24 = QLabel(self.groupBox_18)
        self.label_24.setObjectName(u"label_24")

        self.verticalLayout_5.addWidget(self.label_24)

        self.label_25 = QLabel(self.groupBox_18)
        self.label_25.setObjectName(u"label_25")

        self.verticalLayout_5.addWidget(self.label_25)

        self.label_26 = QLabel(self.groupBox_18)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_5.addWidget(self.label_26)

        self.label_28 = QLabel(self.groupBox_18)
        self.label_28.setObjectName(u"label_28")

        self.verticalLayout_5.addWidget(self.label_28)

        self.label_29 = QLabel(self.groupBox_18)
        self.label_29.setObjectName(u"label_29")

        self.verticalLayout_5.addWidget(self.label_29)

        self.label_27 = QLabel(self.groupBox_18)
        self.label_27.setObjectName(u"label_27")

        self.verticalLayout_5.addWidget(self.label_27)

        self.label_30 = QLabel(self.groupBox_18)
        self.label_30.setObjectName(u"label_30")

        self.verticalLayout_5.addWidget(self.label_30)

        self.label_31 = QLabel(self.groupBox_18)
        self.label_31.setObjectName(u"label_31")

        self.verticalLayout_5.addWidget(self.label_31)

        self.line_10 = QFrame(self.groupBox_18)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShape(QFrame.HLine)
        self.line_10.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_10)


        self.gridLayout.addWidget(self.groupBox_18, 0, 0, 2, 1)

        self.groupBox_14 = QGroupBox(Form)
        self.groupBox_14.setObjectName(u"groupBox_14")
        self.gridLayout_3 = QGridLayout(self.groupBox_14)
        self.gridLayout_3.setSpacing(5)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(5, 5, 5, 5)
        self.gwarantowane_l = QFrame(self.groupBox_14)
        self.gwarantowane_l.setObjectName(u"gwarantowane_l")
        self.gwarantowane_l.setMinimumSize(QSize(25, 25))
        self.gwarantowane_l.setMaximumSize(QSize(25, 25))
        self.gwarantowane_l.setAutoFillBackground(False)
        self.gwarantowane_l.setStyleSheet(u"background: \"white\"")
        self.gwarantowane_l.setFrameShape(QFrame.StyledPanel)
        self.gwarantowane_l.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.gwarantowane_l, 7, 4, 1, 1)

        self.lgwarantowanel = QLabel(self.groupBox_14)
        self.lgwarantowanel.setObjectName(u"lgwarantowanel")

        self.gridLayout_3.addWidget(self.lgwarantowanel, 7, 3, 1, 1)

        self.gwarantowane_n = QFrame(self.groupBox_14)
        self.gwarantowane_n.setObjectName(u"gwarantowane_n")
        self.gwarantowane_n.setMinimumSize(QSize(25, 25))
        self.gwarantowane_n.setMaximumSize(QSize(25, 25))
        self.gwarantowane_n.setAutoFillBackground(False)
        self.gwarantowane_n.setStyleSheet(u"background: \"white\"")
        self.gwarantowane_n.setFrameShape(QFrame.StyledPanel)
        self.gwarantowane_n.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.gwarantowane_n, 7, 1, 1, 1)

        self.swiatlo_hol = QFrame(self.groupBox_14)
        self.swiatlo_hol.setObjectName(u"swiatlo_hol")
        self.swiatlo_hol.setMinimumSize(QSize(25, 25))
        self.swiatlo_hol.setMaximumSize(QSize(25, 25))
        self.swiatlo_hol.setAutoFillBackground(False)
        self.swiatlo_hol.setStyleSheet(u"background: \"white\"")
        self.swiatlo_hol.setFrameShape(QFrame.StyledPanel)
        self.swiatlo_hol.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.swiatlo_hol, 1, 4, 1, 1)

        self.lczujkaruchu = QLabel(self.groupBox_14)
        self.lczujkaruchu.setObjectName(u"lczujkaruchu")

        self.gridLayout_3.addWidget(self.lczujkaruchu, 0, 0, 1, 1)

        self.zasilacz12v = QFrame(self.groupBox_14)
        self.zasilacz12v.setObjectName(u"zasilacz12v")
        self.zasilacz12v.setMinimumSize(QSize(25, 25))
        self.zasilacz12v.setMaximumSize(QSize(25, 25))
        self.zasilacz12v.setAutoFillBackground(False)
        self.zasilacz12v.setStyleSheet(u"background: \"white\"")
        self.zasilacz12v.setFrameShape(QFrame.StyledPanel)
        self.zasilacz12v.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.zasilacz12v, 5, 1, 1, 1)

        self.lwiatlosypialnia = QLabel(self.groupBox_14)
        self.lwiatlosypialnia.setObjectName(u"lwiatlosypialnia")

        self.gridLayout_3.addWidget(self.lwiatlosypialnia, 0, 3, 1, 1)

        self.swiatlo_sypialnia = QFrame(self.groupBox_14)
        self.swiatlo_sypialnia.setObjectName(u"swiatlo_sypialnia")
        self.swiatlo_sypialnia.setMinimumSize(QSize(25, 25))
        self.swiatlo_sypialnia.setMaximumSize(QSize(25, 25))
        self.swiatlo_sypialnia.setAutoFillBackground(False)
        self.swiatlo_sypialnia.setStyleSheet(u"background: \"white\"")
        self.swiatlo_sypialnia.setFrameShape(QFrame.StyledPanel)
        self.swiatlo_sypialnia.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.swiatlo_sypialnia, 0, 4, 1, 1)

        self.lswiatlosalon = QLabel(self.groupBox_14)
        self.lswiatlosalon.setObjectName(u"lswiatlosalon")

        self.gridLayout_3.addWidget(self.lswiatlosalon, 1, 0, 1, 1)

        self.lswiatlohol = QLabel(self.groupBox_14)
        self.lswiatlohol.setObjectName(u"lswiatlohol")

        self.gridLayout_3.addWidget(self.lswiatlohol, 1, 3, 1, 1)

        self.line_7 = QFrame(self.groupBox_14)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.HLine)
        self.line_7.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_7, 4, 0, 1, 5)

        self.line_6 = QFrame(self.groupBox_14)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.VLine)
        self.line_6.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_6, 0, 2, 2, 1)

        self.line_5 = QFrame(self.groupBox_14)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.VLine)
        self.line_5.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_5, 7, 2, 1, 1)

        self.lzasilacz12v = QLabel(self.groupBox_14)
        self.lzasilacz12v.setObjectName(u"lzasilacz12v")

        self.gridLayout_3.addWidget(self.lzasilacz12v, 5, 0, 1, 1)

        self.lgwarantowanen = QLabel(self.groupBox_14)
        self.lgwarantowanen.setObjectName(u"lgwarantowanen")

        self.gridLayout_3.addWidget(self.lgwarantowanen, 7, 0, 1, 1)

        self.czujka_ruchu = QFrame(self.groupBox_14)
        self.czujka_ruchu.setObjectName(u"czujka_ruchu")
        self.czujka_ruchu.setMinimumSize(QSize(25, 25))
        self.czujka_ruchu.setMaximumSize(QSize(25, 25))
        self.czujka_ruchu.setAutoFillBackground(False)
        self.czujka_ruchu.setStyleSheet(u"background: \"white\"")
        self.czujka_ruchu.setFrameShape(QFrame.StyledPanel)
        self.czujka_ruchu.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.czujka_ruchu, 0, 1, 1, 1)

        self.swiatlo_salon = QFrame(self.groupBox_14)
        self.swiatlo_salon.setObjectName(u"swiatlo_salon")
        self.swiatlo_salon.setMinimumSize(QSize(25, 25))
        self.swiatlo_salon.setMaximumSize(QSize(25, 25))
        self.swiatlo_salon.setAutoFillBackground(False)
        self.swiatlo_salon.setStyleSheet(u"background: \"white\"")
        self.swiatlo_salon.setFrameShape(QFrame.StyledPanel)
        self.swiatlo_salon.setFrameShadow(QFrame.Raised)

        self.gridLayout_3.addWidget(self.swiatlo_salon, 1, 1, 1, 1)

        self.line_8 = QFrame(self.groupBox_14)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_8, 6, 0, 1, 5)

        self.line_9 = QFrame(self.groupBox_14)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShape(QFrame.VLine)
        self.line_9.setFrameShadow(QFrame.Sunken)

        self.gridLayout_3.addWidget(self.line_9, 5, 2, 1, 1)


        self.gridLayout.addWidget(self.groupBox_14, 2, 2, 1, 1)

        self.frame_4 = QFrame(Form)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.ltty_ard = QLabel(self.frame_4)
        self.ltty_ard.setObjectName(u"ltty_ard")

        self.verticalLayout_4.addWidget(self.ltty_ard)

        self.te_usb0 = QTextEdit(self.frame_4)
        self.te_usb0.setObjectName(u"te_usb0")

        self.verticalLayout_4.addWidget(self.te_usb0)

        self.lttyRs485 = QLabel(self.frame_4)
        self.lttyRs485.setObjectName(u"lttyRs485")

        self.verticalLayout_4.addWidget(self.lttyRs485)

        self.te_acm0 = QTextEdit(self.frame_4)
        self.te_acm0.setObjectName(u"te_acm0")

        self.verticalLayout_4.addWidget(self.te_acm0)


        self.gridLayout.addWidget(self.frame_4, 0, 1, 3, 1)

        self.groupBox_16 = QGroupBox(Form)
        self.groupBox_16.setObjectName(u"groupBox_16")
        self.gridLayout_5 = QGridLayout(self.groupBox_16)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label = QLabel(self.groupBox_16)
        self.label.setObjectName(u"label")

        self.gridLayout_5.addWidget(self.label, 0, 0, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_14, 0, 2, 1, 1)

        self.pbusb0 = QPushButton(self.groupBox_16)
        self.pbusb0.setObjectName(u"pbusb0")

        self.gridLayout_5.addWidget(self.pbusb0, 0, 1, 1, 1)

        self.label_2 = QLabel(self.groupBox_16)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout_5.addWidget(self.label_2, 0, 3, 1, 1)

        self.pbacm0 = QPushButton(self.groupBox_16)
        self.pbacm0.setObjectName(u"pbacm0")

        self.gridLayout_5.addWidget(self.pbacm0, 0, 4, 1, 1)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer_7, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.groupBox_16, 2, 3, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"Salon", None))
        self.lsalon1.setText(QCoreApplication.translate("Form", u"Salon", None))
        self.lled1.setText(QCoreApplication.translate("Form", u"Listwa salon/sypialnia", None))
        self.lled3.setText(QCoreApplication.translate("Form", u"Listwa salon/\u0142azienka", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"Salon/Sypialnia", None))
        self.pb_216_4.setText(QCoreApplication.translate("Form", u"L 51", None))
        self.pb_21x_4.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_214_4.setText(QCoreApplication.translate("Form", u"P 38", None))
        self.pb_216_3.setText(QCoreApplication.translate("Form", u"L 52", None))
        self.pb_21x_3.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_214_3.setText(QCoreApplication.translate("Form", u"P 40", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("Form", u"Salon/Jadalnia", None))
        self.pb_58_1.setText(QCoreApplication.translate("Form", u"L 44", None))
        self.pb_58_1x2.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_58_2.setText(QCoreApplication.translate("Form", u"P 45", None))
        self.pb_58_3.setText(QCoreApplication.translate("Form", u"L 46", None))
        self.pb_58_3x4.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_58_4.setText(QCoreApplication.translate("Form", u"P 56", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Form", u"Salon/Kuchnia", None))
        self.pb_217_2.setText(QCoreApplication.translate("Form", u"L 61", None))
        self.pb_217_x.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_217_3.setText(QCoreApplication.translate("Form", u"P 62", None))
        self.pb_58_5.setText(QCoreApplication.translate("Form", u"L 58", None))
        self.pb_58_5x6.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_58_6.setText(QCoreApplication.translate("Form", u"P 57", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("Form", u"Salon/Salon", None))
        self.pb_216_2.setText(QCoreApplication.translate("Form", u"L 53", None))
        self.pb_21x_2.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_214_2.setText(QCoreApplication.translate("Form", u"P 41", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("Form", u"Salon/\u0141azienka", None))
        self.pb_216_5.setText(QCoreApplication.translate("Form", u"L 50", None))
        self.pb_21x_5.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_214_5.setText(QCoreApplication.translate("Form", u"P 37", None))
        self.groupBox_15.setTitle(QCoreApplication.translate("Form", u"Wej\u015bcia", None))
        self.val_zasilanieAwar.setText(QCoreApplication.translate("Form", u"0. Zasilanie awaryjne", None))
        self.val_czujka1.setText(QCoreApplication.translate("Form", u"16. Czujka 1", None))
        self.val_24V.setText(QCoreApplication.translate("Form", u"18. Zasilanie 24V_OFF", None))
        self.val_wieczor.setText(QCoreApplication.translate("Form", u"3. Wiecz\u00f3r", None))
        self.val_czujka2.setText(QCoreApplication.translate("Form", u"17. Czujka 2", None))
        self.val_noc.setText(QCoreApplication.translate("Form", u"2. Noc", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"1. 2 Taryfa", None))
        self.groupBox_8.setTitle(QCoreApplication.translate("Form", u"Przedpok\u00f3j", None))
        self.lhol1.setText(QCoreApplication.translate("Form", u"Lampa A", None))
        self.lhol2.setText(QCoreApplication.translate("Form", u"Lampa B", None))
        self.groupBox_9.setTitle(QCoreApplication.translate("Form", u"Hol/Sypialnia", None))
        self.pb_214_7.setText(QCoreApplication.translate("Form", u"L 48", None))
        self.pb_21x_7.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_216_7.setText(QCoreApplication.translate("Form", u"P 35", None))
        self.pb_214_6.setText(QCoreApplication.translate("Form", u"L 49", None))
        self.pb_21x_6.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_216_6.setText(QCoreApplication.translate("Form", u"P 36", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("Form", u"Hol/\u0141azienka", None))
        self.pb_214_8.setText(QCoreApplication.translate("Form", u"L 43", None))
        self.pb_21x_8.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_216_8.setText(QCoreApplication.translate("Form", u"P 34", None))
        self.groupBox_11.setTitle(QCoreApplication.translate("Form", u"Hol/WC", None))
        self.pb_58_7.setText(QCoreApplication.translate("Form", u"L 59", None))
        self.pb_58_7x8.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_58_8.setText(QCoreApplication.translate("Form", u"P 60", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("Form", u"Hol/Pokoje", None))
        self.pb_214_10.setText(QCoreApplication.translate("Form", u"K 33", None))
        self.groupBox_13.setTitle(QCoreApplication.translate("Form", u"Hol/Wej\u015bcie", None))
        self.pb_214_9.setText(QCoreApplication.translate("Form", u"K 32", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"Sypialnia", None))
        self.lsypialnia1.setText(QCoreApplication.translate("Form", u"Sypialnia", None))
        self.lkinkiety.setText(QCoreApplication.translate("Form", u"Kinkiety", None))
        self.pb_216_1.setText(QCoreApplication.translate("Form", u"L 54", None))
        self.pb_21x_1.setText(QCoreApplication.translate("Form", u"x", None))
        self.pb_214_1.setText(QCoreApplication.translate("Form", u"P 42", None))
        self.groupBox_18.setTitle(QCoreApplication.translate("Form", u"Wyj\u015bcia", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"4. Ledy w salonie 1 k. \u0142azienki", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"5. Ledy w salonie 2 k. \u0142azienki", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"6. Lampa w holu L3.2", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"7. Lampa w holu L4.4", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"8. Lampa w holu L4.3", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"9. Lampa w holu L4.2", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"10. Lampa w holu L4.1", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"11. Lampa w holu L3.1", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"12. Lampa w holu L3.3", None))
        self.label_16.setText(QCoreApplication.translate("Form", u"13. Zasilacz 12V", None))
        self.label_17.setText(QCoreApplication.translate("Form", u"14. Ledy w salonie 1 k. sypialni", None))
        self.label_18.setText(QCoreApplication.translate("Form", u"15. Ledy w salonie 2 k. sypialni", None))
        self.label_32.setText(QCoreApplication.translate("Form", u"19. \u015awiat\u0142o w sypialni", None))
        self.label_33.setText(QCoreApplication.translate("Form", u"20. Czujka ruchu", None))
        self.label_19.setText(QCoreApplication.translate("Form", u"21. Pod\u015bwietlenie w\u0142  mix", None))
        self.label_20.setText(QCoreApplication.translate("Form", u"22. Pod\u015bwietlenie w\u0142 hol", None))
        self.label_21.setText(QCoreApplication.translate("Form", u"23. Pod\u015bwietlenie w\u0142. salon", None))
        self.label_22.setText(QCoreApplication.translate("Form", u"24. Lampa w sypialni 2", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"25. Kinkiety sypialnia", None))
        self.label_24.setText(QCoreApplication.translate("Form", u"26. Lampa w holu L4.0", None))
        self.label_25.setText(QCoreApplication.translate("Form", u"27. Lampa w sypialni 1", None))
        self.label_26.setText(QCoreApplication.translate("Form", u"28.  Lampa w salonie 2", None))
        self.label_28.setText(QCoreApplication.translate("Form", u"29. Gwarantowane N", None))
        self.label_29.setText(QCoreApplication.translate("Form", u"30. Gwarantowane L", None))
        self.label_27.setText(QCoreApplication.translate("Form", u"31. Lampa w salonie 1", None))
        self.label_30.setText(QCoreApplication.translate("Form", u"39. \u015awiat\u0142o w holu", None))
        self.label_31.setText(QCoreApplication.translate("Form", u"47. \u015awiat\u0142o w salonie", None))
        self.groupBox_14.setTitle(QCoreApplication.translate("Form", u"Dodatkowe wyj\u015bcia", None))
        self.lgwarantowanel.setText(QCoreApplication.translate("Form", u"Gwarantowe L", None))
        self.lczujkaruchu.setText(QCoreApplication.translate("Form", u"Czujka ruchu", None))
        self.lwiatlosypialnia.setText(QCoreApplication.translate("Form", u"\u015awiat\u0142o w sypialni", None))
        self.lswiatlosalon.setText(QCoreApplication.translate("Form", u"\u015awiat\u0142o w salonie", None))
        self.lswiatlohol.setText(QCoreApplication.translate("Form", u"\u015awiat\u0142o w holu", None))
        self.lzasilacz12v.setText(QCoreApplication.translate("Form", u"Zasilacz 12V", None))
        self.lgwarantowanen.setText(QCoreApplication.translate("Form", u"Gwarantowane N", None))
        self.ltty_ard.setText(QCoreApplication.translate("Form", u"Arduino", None))
        self.lttyRs485.setText(QCoreApplication.translate("Form", u"RS485", None))
        self.groupBox_16.setTitle(QCoreApplication.translate("Form", u"Po\u0142\u0105czenie", None))
        self.label.setText(QCoreApplication.translate("Form", u"RS485", None))
        self.pbusb0.setText(QCoreApplication.translate("Form", u"Po\u0142\u0105cz", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Arduino", None))
        self.pbacm0.setText(QCoreApplication.translate("Form", u"Po\u0142\u0105cz", None))
    # retranslateUi

