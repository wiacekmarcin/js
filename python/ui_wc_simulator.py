# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wc_simulator.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QLabel, QMainWindow,
    QMenu, QMenuBar, QPushButton, QRadioButton,
    QSizePolicy, QSpacerItem, QStatusBar, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_WC_Simulator(object):
    def setupUi(self, WC_Simulator):
        if not WC_Simulator.objectName():
            WC_Simulator.setObjectName(u"WC_Simulator")
        WC_Simulator.resize(873, 415)
        self.actionRS485 = QAction(WC_Simulator)
        self.actionRS485.setObjectName(u"actionRS485")
        self.actionRS485.setCheckable(True)
        self.actionDebug = QAction(WC_Simulator)
        self.actionDebug.setObjectName(u"actionDebug")
        self.actionDebug.setCheckable(True)
        self.actionZako_cz = QAction(WC_Simulator)
        self.actionZako_cz.setObjectName(u"actionZako_cz")
        self.centralwidget = QWidget(WC_Simulator)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pb_wieczor = QPushButton(self.widget)
        self.pb_wieczor.setObjectName(u"pb_wieczor")

        self.horizontalLayout.addWidget(self.pb_wieczor)

        self.wieczor_on = QRadioButton(self.widget)
        self.wieczor_on.setObjectName(u"wieczor_on")

        self.horizontalLayout.addWidget(self.wieczor_on)

        self.wieczor_off = QRadioButton(self.widget)
        self.wieczor_off.setObjectName(u"wieczor_off")

        self.horizontalLayout.addWidget(self.wieczor_off)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pb_noc = QPushButton(self.widget_2)
        self.pb_noc.setObjectName(u"pb_noc")

        self.horizontalLayout_2.addWidget(self.pb_noc)

        self.noc_on = QRadioButton(self.widget_2)
        self.noc_on.setObjectName(u"noc_on")

        self.horizontalLayout_2.addWidget(self.noc_on)

        self.noc_off = QRadioButton(self.widget_2)
        self.noc_off.setObjectName(u"noc_off")

        self.horizontalLayout_2.addWidget(self.noc_off)


        self.verticalLayout.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pb_taryfa2 = QPushButton(self.widget_3)
        self.pb_taryfa2.setObjectName(u"pb_taryfa2")

        self.horizontalLayout_3.addWidget(self.pb_taryfa2)

        self.taryfa2_on = QRadioButton(self.widget_3)
        self.taryfa2_on.setObjectName(u"taryfa2_on")

        self.horizontalLayout_3.addWidget(self.taryfa2_on)

        self.taryfa2_off = QRadioButton(self.widget_3)
        self.taryfa2_off.setObjectName(u"taryfa2_off")

        self.horizontalLayout_3.addWidget(self.taryfa2_off)


        self.verticalLayout.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pb_zasilanie_awaryjne = QPushButton(self.widget_4)
        self.pb_zasilanie_awaryjne.setObjectName(u"pb_zasilanie_awaryjne")

        self.horizontalLayout_4.addWidget(self.pb_zasilanie_awaryjne)

        self.zasilanie_awaryjne_on = QRadioButton(self.widget_4)
        self.zasilanie_awaryjne_on.setObjectName(u"zasilanie_awaryjne_on")

        self.horizontalLayout_4.addWidget(self.zasilanie_awaryjne_on)

        self.zasilanie_awaryjne_off = QRadioButton(self.widget_4)
        self.zasilanie_awaryjne_off.setObjectName(u"zasilanie_awaryjne_off")

        self.horizontalLayout_4.addWidget(self.zasilanie_awaryjne_off)


        self.verticalLayout.addWidget(self.widget_4)


        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.te_arduino = QTextEdit(self.groupBox)
        self.te_arduino.setObjectName(u"te_arduino")

        self.verticalLayout_2.addWidget(self.te_arduino)


        self.gridLayout_3.addWidget(self.groupBox, 0, 2, 2, 1)

        self.gbInput = QGroupBox(self.centralwidget)
        self.gbInput.setObjectName(u"gbInput")
        self.gridLayout_2 = QGridLayout(self.gbInput)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.pb_czujnik_ruchu = QPushButton(self.gbInput)
        self.pb_czujnik_ruchu.setObjectName(u"pb_czujnik_ruchu")

        self.gridLayout_2.addWidget(self.pb_czujnik_ruchu, 1, 0, 1, 3)

        self.drzwi_otwarte = QRadioButton(self.gbInput)
        self.drzwi_otwarte.setObjectName(u"drzwi_otwarte")

        self.gridLayout_2.addWidget(self.drzwi_otwarte, 0, 1, 1, 1)

        self.drzwi_zamkniete = QRadioButton(self.gbInput)
        self.drzwi_zamkniete.setObjectName(u"drzwi_zamkniete")

        self.gridLayout_2.addWidget(self.drzwi_zamkniete, 0, 2, 1, 1)

        self.pb_czujnik_zblizeniowy = QPushButton(self.gbInput)
        self.pb_czujnik_zblizeniowy.setObjectName(u"pb_czujnik_zblizeniowy")

        self.gridLayout_2.addWidget(self.pb_czujnik_zblizeniowy, 2, 0, 1, 3)

        self.pb_drzwi = QPushButton(self.gbInput)
        self.pb_drzwi.setObjectName(u"pb_drzwi")

        self.gridLayout_2.addWidget(self.pb_drzwi, 0, 0, 1, 1)

        self.pb_klawisz = QPushButton(self.gbInput)
        self.pb_klawisz.setObjectName(u"pb_klawisz")

        self.gridLayout_2.addWidget(self.pb_klawisz, 3, 0, 1, 1)


        self.gridLayout_3.addWidget(self.gbInput, 1, 0, 1, 1)

        self.gbOutput = QGroupBox(self.centralwidget)
        self.gbOutput.setObjectName(u"gbOutput")
        self.formLayout = QFormLayout(self.gbOutput)
        self.formLayout.setObjectName(u"formLayout")
        self.lswiatlo = QLabel(self.gbOutput)
        self.lswiatlo.setObjectName(u"lswiatlo")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.lswiatlo)

        self.light = QLabel(self.gbOutput)
        self.light.setObjectName(u"light")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.light)

        self.llustro = QLabel(self.gbOutput)
        self.llustro.setObjectName(u"llustro")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.llustro)

        self.lustro = QLabel(self.gbOutput)
        self.lustro.setObjectName(u"lustro")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lustro)

        self.lregal = QLabel(self.gbOutput)
        self.lregal.setObjectName(u"lregal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.lregal)

        self.regal = QLabel(self.gbOutput)
        self.regal.setObjectName(u"regal")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.regal)

        self.lzawor = QLabel(self.gbOutput)
        self.lzawor.setObjectName(u"lzawor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.lzawor)

        self.zawor = QLabel(self.gbOutput)
        self.zawor.setObjectName(u"zawor")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.zawor)

        self.line = QFrame(self.gbOutput)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.line)

        self.lzapalone_swiatlo = QLabel(self.gbOutput)
        self.lzapalone_swiatlo.setObjectName(u"lzapalone_swiatlo")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.lzapalone_swiatlo)

        self.wy_zapalone_swiatlo = QLabel(self.gbOutput)
        self.wy_zapalone_swiatlo.setObjectName(u"wy_zapalone_swiatlo")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.wy_zapalone_swiatlo)

        self.lczujnikruchuwy = QLabel(self.gbOutput)
        self.lczujnikruchuwy.setObjectName(u"lczujnikruchuwy")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.lczujnikruchuwy)

        self.wy_czujnik_ruchu = QLabel(self.gbOutput)
        self.wy_czujnik_ruchu.setObjectName(u"wy_czujnik_ruchu")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.wy_czujnik_ruchu)

        self.lkontaktronwy = QLabel(self.gbOutput)
        self.lkontaktronwy.setObjectName(u"lkontaktronwy")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.lkontaktronwy)

        self.wy_kontaktron = QLabel(self.gbOutput)
        self.wy_kontaktron.setObjectName(u"wy_kontaktron")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.wy_kontaktron)

        self.line_2 = QFrame(self.gbOutput)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.formLayout.setWidget(8, QFormLayout.ItemRole.SpanningRole, self.line_2)

        self.pb_clear_debug = QPushButton(self.gbOutput)
        self.pb_clear_debug.setObjectName(u"pb_clear_debug")

        self.formLayout.setWidget(9, QFormLayout.ItemRole.LabelRole, self.pb_clear_debug)

        self.pb_clear_rs485 = QPushButton(self.gbOutput)
        self.pb_clear_rs485.setObjectName(u"pb_clear_rs485")

        self.formLayout.setWidget(10, QFormLayout.ItemRole.LabelRole, self.pb_clear_rs485)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.formLayout.setItem(11, QFormLayout.ItemRole.LabelRole, self.verticalSpacer)


        self.gridLayout_3.addWidget(self.gbOutput, 0, 1, 2, 1)

        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.te_rs485 = QTextEdit(self.groupBox_2)
        self.te_rs485.setObjectName(u"te_rs485")

        self.verticalLayout_3.addWidget(self.te_rs485)


        self.gridLayout_3.addWidget(self.groupBox_2, 0, 3, 2, 1)

        WC_Simulator.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(WC_Simulator)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 873, 23))
        self.menuPo_cz = QMenu(self.menubar)
        self.menuPo_cz.setObjectName(u"menuPo_cz")
        WC_Simulator.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(WC_Simulator)
        self.statusbar.setObjectName(u"statusbar")
        WC_Simulator.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuPo_cz.menuAction())
        self.menuPo_cz.addAction(self.actionRS485)
        self.menuPo_cz.addAction(self.actionDebug)
        self.menuPo_cz.addSeparator()
        self.menuPo_cz.addAction(self.actionZako_cz)

        self.retranslateUi(WC_Simulator)

        QMetaObject.connectSlotsByName(WC_Simulator)
    # setupUi

    def retranslateUi(self, WC_Simulator):
        WC_Simulator.setWindowTitle(QCoreApplication.translate("WC_Simulator", u"MainWindow", None))
        self.actionRS485.setText(QCoreApplication.translate("WC_Simulator", u"RS485", None))
        self.actionDebug.setText(QCoreApplication.translate("WC_Simulator", u"Debug", None))
        self.actionZako_cz.setText(QCoreApplication.translate("WC_Simulator", u"Zako\u0144cz", None))
        self.pb_wieczor.setText(QCoreApplication.translate("WC_Simulator", u"Wiecz\u00f3r", None))
        self.wieczor_on.setText(QCoreApplication.translate("WC_Simulator", u"On", None))
        self.wieczor_off.setText(QCoreApplication.translate("WC_Simulator", u"Off", None))
        self.pb_noc.setText(QCoreApplication.translate("WC_Simulator", u"Noc", None))
        self.noc_on.setText(QCoreApplication.translate("WC_Simulator", u"On", None))
        self.noc_off.setText(QCoreApplication.translate("WC_Simulator", u"Off", None))
        self.pb_taryfa2.setText(QCoreApplication.translate("WC_Simulator", u"2 taryfa", None))
        self.taryfa2_on.setText(QCoreApplication.translate("WC_Simulator", u"On", None))
        self.taryfa2_off.setText(QCoreApplication.translate("WC_Simulator", u"Off", None))
        self.pb_zasilanie_awaryjne.setText(QCoreApplication.translate("WC_Simulator", u"Zasilanie awaryjne", None))
        self.zasilanie_awaryjne_on.setText(QCoreApplication.translate("WC_Simulator", u"On", None))
        self.zasilanie_awaryjne_off.setText(QCoreApplication.translate("WC_Simulator", u"Off", None))
        self.groupBox.setTitle(QCoreApplication.translate("WC_Simulator", u"Debug", None))
        self.gbInput.setTitle(QCoreApplication.translate("WC_Simulator", u"Wej\u015bcia", None))
        self.pb_czujnik_ruchu.setText(QCoreApplication.translate("WC_Simulator", u"Czujnik ruchu", None))
        self.drzwi_otwarte.setText(QCoreApplication.translate("WC_Simulator", u"Otwarte", None))
        self.drzwi_zamkniete.setText(QCoreApplication.translate("WC_Simulator", u"Zamkni\u0119te", None))
        self.pb_czujnik_zblizeniowy.setText(QCoreApplication.translate("WC_Simulator", u"Czujnik zbli\u017ceniowy", None))
        self.pb_drzwi.setText(QCoreApplication.translate("WC_Simulator", u"Drzwi", None))
        self.pb_klawisz.setText(QCoreApplication.translate("WC_Simulator", u"Klawisz", None))
        self.gbOutput.setTitle(QCoreApplication.translate("WC_Simulator", u"Wyj\u015bcia", None))
        self.lswiatlo.setText(QCoreApplication.translate("WC_Simulator", u"Swi\u0105t\u0142o g\u00f3rne", None))
        self.light.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.llustro.setText(QCoreApplication.translate("WC_Simulator", u"Lustro", None))
        self.lustro.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.lregal.setText(QCoreApplication.translate("WC_Simulator", u"Rega\u0142", None))
        self.regal.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.lzawor.setText(QCoreApplication.translate("WC_Simulator", u"Zaw\u00f3r", None))
        self.zawor.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.lzapalone_swiatlo.setText(QCoreApplication.translate("WC_Simulator", u"Zapalone \u015bwiat\u0142o", None))
        self.wy_zapalone_swiatlo.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.lczujnikruchuwy.setText(QCoreApplication.translate("WC_Simulator", u"Czujnik ruchu", None))
        self.wy_czujnik_ruchu.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.lkontaktronwy.setText(QCoreApplication.translate("WC_Simulator", u"Kontaktorn", None))
        self.wy_kontaktron.setText(QCoreApplication.translate("WC_Simulator", u"off", None))
        self.pb_clear_debug.setText(QCoreApplication.translate("WC_Simulator", u"Czy\u015b\u0107 debug", None))
        self.pb_clear_rs485.setText(QCoreApplication.translate("WC_Simulator", u"Czy\u015b\u0107 RS485", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("WC_Simulator", u"RS485", None))
        self.menuPo_cz.setTitle(QCoreApplication.translate("WC_Simulator", u"Po\u0142\u0105cz", None))
    # retranslateUi

