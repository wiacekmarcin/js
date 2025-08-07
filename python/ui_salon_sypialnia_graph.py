# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salon_sypialnia_graph.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QGraphicsView, QGridLayout,
    QHBoxLayout, QLabel, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTabWidget, QTextEdit, QVBoxLayout, QWidget)

class Ui_SalonSypialniaHol(object):
    def setupUi(self, SalonSypialniaHol):
        if not SalonSypialniaHol.objectName():
            SalonSypialniaHol.setObjectName(u"SalonSypialniaHol")
        SalonSypialniaHol.resize(1742, 946)
        self.centralwidget = QWidget(SalonSypialniaHol)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(2, 2, 2, 2)
        self.frame_5 = QFrame(self.frame)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(1150, 16777215))
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_5)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.ltty_ard = QLabel(self.frame_5)
        self.ltty_ard.setObjectName(u"ltty_ard")

        self.horizontalLayout.addWidget(self.ltty_ard)

        self.horizontalSpacer_2 = QSpacerItem(650, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.lttyRs485 = QLabel(self.frame_5)
        self.lttyRs485.setObjectName(u"lttyRs485")

        self.horizontalLayout.addWidget(self.lttyRs485)


        self.verticalLayout.addWidget(self.frame_5)

        self.plan = QGraphicsView(self.frame)
        self.plan.setObjectName(u"plan")

        self.verticalLayout.addWidget(self.plan)


        self.gridLayout_2.addWidget(self.frame, 0, 1, 2, 1)

        self.tabWidget_output = QTabWidget(self.centralwidget)
        self.tabWidget_output.setObjectName(u"tabWidget_output")
        self.tabWidget_output.setMinimumSize(QSize(400, 0))
        self.tabWidget_output.setMaximumSize(QSize(400, 16777215))
        self.tabWidget_outputPage1 = QWidget()
        self.tabWidget_outputPage1.setObjectName(u"tabWidget_outputPage1")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidget_outputPage1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lo_04 = QLabel(self.tabWidget_outputPage1)
        self.lo_04.setObjectName(u"lo_04")

        self.verticalLayout_4.addWidget(self.lo_04)

        self.lo_05 = QLabel(self.tabWidget_outputPage1)
        self.lo_05.setObjectName(u"lo_05")

        self.verticalLayout_4.addWidget(self.lo_05)

        self.lo_06 = QLabel(self.tabWidget_outputPage1)
        self.lo_06.setObjectName(u"lo_06")

        self.verticalLayout_4.addWidget(self.lo_06)

        self.lo_07 = QLabel(self.tabWidget_outputPage1)
        self.lo_07.setObjectName(u"lo_07")

        self.verticalLayout_4.addWidget(self.lo_07)

        self.lo_08 = QLabel(self.tabWidget_outputPage1)
        self.lo_08.setObjectName(u"lo_08")

        self.verticalLayout_4.addWidget(self.lo_08)

        self.lo_09 = QLabel(self.tabWidget_outputPage1)
        self.lo_09.setObjectName(u"lo_09")

        self.verticalLayout_4.addWidget(self.lo_09)

        self.lo_10 = QLabel(self.tabWidget_outputPage1)
        self.lo_10.setObjectName(u"lo_10")

        self.verticalLayout_4.addWidget(self.lo_10)

        self.lo_11 = QLabel(self.tabWidget_outputPage1)
        self.lo_11.setObjectName(u"lo_11")

        self.verticalLayout_4.addWidget(self.lo_11)

        self.lo_12 = QLabel(self.tabWidget_outputPage1)
        self.lo_12.setObjectName(u"lo_12")

        self.verticalLayout_4.addWidget(self.lo_12)

        self.lo_13 = QLabel(self.tabWidget_outputPage1)
        self.lo_13.setObjectName(u"lo_13")

        self.verticalLayout_4.addWidget(self.lo_13)

        self.lo_14 = QLabel(self.tabWidget_outputPage1)
        self.lo_14.setObjectName(u"lo_14")

        self.verticalLayout_4.addWidget(self.lo_14)

        self.lo_15 = QLabel(self.tabWidget_outputPage1)
        self.lo_15.setObjectName(u"lo_15")

        self.verticalLayout_4.addWidget(self.lo_15)

        self.lo_19 = QLabel(self.tabWidget_outputPage1)
        self.lo_19.setObjectName(u"lo_19")

        self.verticalLayout_4.addWidget(self.lo_19)

        self.lo_20 = QLabel(self.tabWidget_outputPage1)
        self.lo_20.setObjectName(u"lo_20")

        self.verticalLayout_4.addWidget(self.lo_20)

        self.lo_21 = QLabel(self.tabWidget_outputPage1)
        self.lo_21.setObjectName(u"lo_21")

        self.verticalLayout_4.addWidget(self.lo_21)

        self.lo_22 = QLabel(self.tabWidget_outputPage1)
        self.lo_22.setObjectName(u"lo_22")

        self.verticalLayout_4.addWidget(self.lo_22)

        self.lo_23 = QLabel(self.tabWidget_outputPage1)
        self.lo_23.setObjectName(u"lo_23")

        self.verticalLayout_4.addWidget(self.lo_23)

        self.lo_24 = QLabel(self.tabWidget_outputPage1)
        self.lo_24.setObjectName(u"lo_24")

        self.verticalLayout_4.addWidget(self.lo_24)

        self.lo_25 = QLabel(self.tabWidget_outputPage1)
        self.lo_25.setObjectName(u"lo_25")

        self.verticalLayout_4.addWidget(self.lo_25)

        self.lo_26 = QLabel(self.tabWidget_outputPage1)
        self.lo_26.setObjectName(u"lo_26")

        self.verticalLayout_4.addWidget(self.lo_26)

        self.lo_27 = QLabel(self.tabWidget_outputPage1)
        self.lo_27.setObjectName(u"lo_27")

        self.verticalLayout_4.addWidget(self.lo_27)

        self.lo_28 = QLabel(self.tabWidget_outputPage1)
        self.lo_28.setObjectName(u"lo_28")

        self.verticalLayout_4.addWidget(self.lo_28)

        self.lo_29 = QLabel(self.tabWidget_outputPage1)
        self.lo_29.setObjectName(u"lo_29")

        self.verticalLayout_4.addWidget(self.lo_29)

        self.lo_30 = QLabel(self.tabWidget_outputPage1)
        self.lo_30.setObjectName(u"lo_30")

        self.verticalLayout_4.addWidget(self.lo_30)

        self.lo_31 = QLabel(self.tabWidget_outputPage1)
        self.lo_31.setObjectName(u"lo_31")

        self.verticalLayout_4.addWidget(self.lo_31)

        self.lo_39 = QLabel(self.tabWidget_outputPage1)
        self.lo_39.setObjectName(u"lo_39")

        self.verticalLayout_4.addWidget(self.lo_39)

        self.lo_47 = QLabel(self.tabWidget_outputPage1)
        self.lo_47.setObjectName(u"lo_47")

        self.verticalLayout_4.addWidget(self.lo_47)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget_output.addTab(self.tabWidget_outputPage1, "")
        self.tabWidget_outputPage2 = QWidget()
        self.tabWidget_outputPage2.setObjectName(u"tabWidget_outputPage2")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidget_outputPage2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.li_00 = QLabel(self.tabWidget_outputPage2)
        self.li_00.setObjectName(u"li_00")

        self.verticalLayout_3.addWidget(self.li_00)

        self.li_01 = QLabel(self.tabWidget_outputPage2)
        self.li_01.setObjectName(u"li_01")

        self.verticalLayout_3.addWidget(self.li_01)

        self.li_02 = QLabel(self.tabWidget_outputPage2)
        self.li_02.setObjectName(u"li_02")

        self.verticalLayout_3.addWidget(self.li_02)

        self.li_03 = QLabel(self.tabWidget_outputPage2)
        self.li_03.setObjectName(u"li_03")

        self.verticalLayout_3.addWidget(self.li_03)

        self.li_16 = QLabel(self.tabWidget_outputPage2)
        self.li_16.setObjectName(u"li_16")

        self.verticalLayout_3.addWidget(self.li_16)

        self.li_17 = QLabel(self.tabWidget_outputPage2)
        self.li_17.setObjectName(u"li_17")

        self.verticalLayout_3.addWidget(self.li_17)

        self.li_18 = QLabel(self.tabWidget_outputPage2)
        self.li_18.setObjectName(u"li_18")

        self.verticalLayout_3.addWidget(self.li_18)

        self.li_32 = QLabel(self.tabWidget_outputPage2)
        self.li_32.setObjectName(u"li_32")

        self.verticalLayout_3.addWidget(self.li_32)

        self.li_33 = QLabel(self.tabWidget_outputPage2)
        self.li_33.setObjectName(u"li_33")

        self.verticalLayout_3.addWidget(self.li_33)

        self.li_34 = QLabel(self.tabWidget_outputPage2)
        self.li_34.setObjectName(u"li_34")

        self.verticalLayout_3.addWidget(self.li_34)

        self.li_35 = QLabel(self.tabWidget_outputPage2)
        self.li_35.setObjectName(u"li_35")

        self.verticalLayout_3.addWidget(self.li_35)

        self.li_36 = QLabel(self.tabWidget_outputPage2)
        self.li_36.setObjectName(u"li_36")

        self.verticalLayout_3.addWidget(self.li_36)

        self.li_37 = QLabel(self.tabWidget_outputPage2)
        self.li_37.setObjectName(u"li_37")

        self.verticalLayout_3.addWidget(self.li_37)

        self.li_38 = QLabel(self.tabWidget_outputPage2)
        self.li_38.setObjectName(u"li_38")

        self.verticalLayout_3.addWidget(self.li_38)

        self.li_40 = QLabel(self.tabWidget_outputPage2)
        self.li_40.setObjectName(u"li_40")

        self.verticalLayout_3.addWidget(self.li_40)

        self.li_41 = QLabel(self.tabWidget_outputPage2)
        self.li_41.setObjectName(u"li_41")

        self.verticalLayout_3.addWidget(self.li_41)

        self.li_42 = QLabel(self.tabWidget_outputPage2)
        self.li_42.setObjectName(u"li_42")

        self.verticalLayout_3.addWidget(self.li_42)

        self.li_43 = QLabel(self.tabWidget_outputPage2)
        self.li_43.setObjectName(u"li_43")

        self.verticalLayout_3.addWidget(self.li_43)

        self.li_44 = QLabel(self.tabWidget_outputPage2)
        self.li_44.setObjectName(u"li_44")

        self.verticalLayout_3.addWidget(self.li_44)

        self.li_45 = QLabel(self.tabWidget_outputPage2)
        self.li_45.setObjectName(u"li_45")

        self.verticalLayout_3.addWidget(self.li_45)

        self.li_46 = QLabel(self.tabWidget_outputPage2)
        self.li_46.setObjectName(u"li_46")

        self.verticalLayout_3.addWidget(self.li_46)

        self.li_48 = QLabel(self.tabWidget_outputPage2)
        self.li_48.setObjectName(u"li_48")

        self.verticalLayout_3.addWidget(self.li_48)

        self.li_49 = QLabel(self.tabWidget_outputPage2)
        self.li_49.setObjectName(u"li_49")

        self.verticalLayout_3.addWidget(self.li_49)

        self.li_50 = QLabel(self.tabWidget_outputPage2)
        self.li_50.setObjectName(u"li_50")

        self.verticalLayout_3.addWidget(self.li_50)

        self.li_51 = QLabel(self.tabWidget_outputPage2)
        self.li_51.setObjectName(u"li_51")

        self.verticalLayout_3.addWidget(self.li_51)

        self.li_52 = QLabel(self.tabWidget_outputPage2)
        self.li_52.setObjectName(u"li_52")

        self.verticalLayout_3.addWidget(self.li_52)

        self.li_53 = QLabel(self.tabWidget_outputPage2)
        self.li_53.setObjectName(u"li_53")

        self.verticalLayout_3.addWidget(self.li_53)

        self.li_54 = QLabel(self.tabWidget_outputPage2)
        self.li_54.setObjectName(u"li_54")

        self.verticalLayout_3.addWidget(self.li_54)

        self.li_56 = QLabel(self.tabWidget_outputPage2)
        self.li_56.setObjectName(u"li_56")

        self.verticalLayout_3.addWidget(self.li_56)

        self.li_57 = QLabel(self.tabWidget_outputPage2)
        self.li_57.setObjectName(u"li_57")

        self.verticalLayout_3.addWidget(self.li_57)

        self.li_58 = QLabel(self.tabWidget_outputPage2)
        self.li_58.setObjectName(u"li_58")

        self.verticalLayout_3.addWidget(self.li_58)

        self.li_59 = QLabel(self.tabWidget_outputPage2)
        self.li_59.setObjectName(u"li_59")

        self.verticalLayout_3.addWidget(self.li_59)

        self.li_60 = QLabel(self.tabWidget_outputPage2)
        self.li_60.setObjectName(u"li_60")

        self.verticalLayout_3.addWidget(self.li_60)

        self.li_61 = QLabel(self.tabWidget_outputPage2)
        self.li_61.setObjectName(u"li_61")

        self.verticalLayout_3.addWidget(self.li_61)

        self.li_62 = QLabel(self.tabWidget_outputPage2)
        self.li_62.setObjectName(u"li_62")

        self.verticalLayout_3.addWidget(self.li_62)

        self.tabWidget_output.addTab(self.tabWidget_outputPage2, "")

        self.gridLayout_2.addWidget(self.tabWidget_output, 0, 0, 1, 1)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.pb_2taryfa = QPushButton(self.frame_2)
        self.pb_2taryfa.setObjectName(u"pb_2taryfa")

        self.gridLayout_3.addWidget(self.pb_2taryfa, 0, 4, 1, 1)

        self.pb_zasawar = QPushButton(self.frame_2)
        self.pb_zasawar.setObjectName(u"pb_zasawar")

        self.gridLayout_3.addWidget(self.pb_zasawar, 0, 0, 1, 1)

        self.pb_czujka2 = QPushButton(self.frame_2)
        self.pb_czujka2.setObjectName(u"pb_czujka2")

        self.gridLayout_3.addWidget(self.pb_czujka2, 0, 6, 1, 1)

        self.pb_noc = QPushButton(self.frame_2)
        self.pb_noc.setObjectName(u"pb_noc")

        self.gridLayout_3.addWidget(self.pb_noc, 0, 2, 1, 1)

        self.pb_wieczor = QPushButton(self.frame_2)
        self.pb_wieczor.setObjectName(u"pb_wieczor")

        self.gridLayout_3.addWidget(self.pb_wieczor, 0, 3, 1, 1)

        self.pb_czujka1 = QPushButton(self.frame_2)
        self.pb_czujka1.setObjectName(u"pb_czujka1")

        self.gridLayout_3.addWidget(self.pb_czujka1, 0, 5, 1, 1)

        self.pb_24V = QPushButton(self.frame_2)
        self.pb_24V.setObjectName(u"pb_24V")

        self.gridLayout_3.addWidget(self.pb_24V, 0, 7, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 1, 1, 1)

        self.frame_4 = QFrame(self.centralwidget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMaximumSize(QSize(400, 16777215))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.pbacm0 = QPushButton(self.frame_4)
        self.pbacm0.setObjectName(u"pbacm0")

        self.gridLayout.addWidget(self.pbacm0, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(369, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 2, 1, 1)

        self.pbusb0 = QPushButton(self.frame_4)
        self.pbusb0.setObjectName(u"pbusb0")

        self.gridLayout.addWidget(self.pbusb0, 2, 3, 1, 1)


        self.gridLayout_2.addWidget(self.frame_4, 2, 0, 1, 1)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.te_acm0 = QTextEdit(self.frame_3)
        self.te_acm0.setObjectName(u"te_acm0")

        self.verticalLayout_2.addWidget(self.te_acm0)

        self.te_usb0 = QTextEdit(self.frame_3)
        self.te_usb0.setObjectName(u"te_usb0")

        self.verticalLayout_2.addWidget(self.te_usb0)


        self.gridLayout_2.addWidget(self.frame_3, 0, 2, 3, 1)

        SalonSypialniaHol.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(SalonSypialniaHol)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1742, 23))
        SalonSypialniaHol.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(SalonSypialniaHol)
        self.statusbar.setObjectName(u"statusbar")
        SalonSypialniaHol.setStatusBar(self.statusbar)

        self.retranslateUi(SalonSypialniaHol)

        self.tabWidget_output.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(SalonSypialniaHol)
    # setupUi

    def retranslateUi(self, SalonSypialniaHol):
        SalonSypialniaHol.setWindowTitle(QCoreApplication.translate("SalonSypialniaHol", u"MainWindow", None))
        self.ltty_ard.setText(QCoreApplication.translate("SalonSypialniaHol", u"?", None))
        self.lttyRs485.setText(QCoreApplication.translate("SalonSypialniaHol", u"?", None))
        self.lo_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 1 salon/\u0142azienka", None))
        self.lo_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 2 salon/\u0142azienka", None))
        self.lo_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 3.2 hol", None))
        self.lo_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 4.4 hol", None))
        self.lo_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 4.3 hol", None))
        self.lo_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 4.2 hol", None))
        self.lo_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 4.1 hol", None))
        self.lo_11.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 3.1 hol", None))
        self.lo_12.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 3.3 hol", None))
        self.lo_13.setText(QCoreApplication.translate("SalonSypialniaHol", u"Zasilacz 12V", None))
        self.lo_14.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 1 salon/jadalnia", None))
        self.lo_15.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 2 salon/jadalnia", None))
        self.lo_19.setText(QCoreApplication.translate("SalonSypialniaHol", u"\u015awiat\u0142o sypialnia", None))
        self.lo_20.setText(QCoreApplication.translate("SalonSypialniaHol", u"Czujka ruchu", None))
        self.lo_21.setText(QCoreApplication.translate("SalonSypialniaHol", u"Pod\u015b. w\u0142.  mix", None))
        self.lo_22.setText(QCoreApplication.translate("SalonSypialniaHol", u"Pod\u015b w\u0142. hol", None))
        self.lo_23.setText(QCoreApplication.translate("SalonSypialniaHol", u"Pod\u015b. w\u0142. salon", None))
        self.lo_24.setText(QCoreApplication.translate("SalonSypialniaHol", u"Sypialnia 1", None))
        self.lo_25.setText(QCoreApplication.translate("SalonSypialniaHol", u"Sypialnia kinkiety", None))
        self.lo_26.setText(QCoreApplication.translate("SalonSypialniaHol", u"Led 4.0 hol", None))
        self.lo_27.setText(QCoreApplication.translate("SalonSypialniaHol", u"Sypialnia 2", None))
        self.lo_28.setText(QCoreApplication.translate("SalonSypialniaHol", u"Salon 2", None))
        self.lo_29.setText(QCoreApplication.translate("SalonSypialniaHol", u"Gwarantowane N", None))
        self.lo_30.setText(QCoreApplication.translate("SalonSypialniaHol", u"Gwarantowane L", None))
        self.lo_31.setText(QCoreApplication.translate("SalonSypialniaHol", u"Salon 1", None))
        self.lo_39.setText(QCoreApplication.translate("SalonSypialniaHol", u"\u015awiat\u0142o hol", None))
        self.lo_47.setText(QCoreApplication.translate("SalonSypialniaHol", u" \u015awiat\u0142o syp.", None))
        self.tabWidget_output.setTabText(self.tabWidget_output.indexOf(self.tabWidget_outputPage1), QCoreApplication.translate("SalonSypialniaHol", u"OUTPUT", None))
        self.li_00.setText(QCoreApplication.translate("SalonSypialniaHol", u"0", None))
        self.li_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1", None))
        self.li_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2", None))
        self.li_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3", None))
        self.li_16.setText(QCoreApplication.translate("SalonSypialniaHol", u"16", None))
        self.li_17.setText(QCoreApplication.translate("SalonSypialniaHol", u"17", None))
        self.li_18.setText(QCoreApplication.translate("SalonSypialniaHol", u"18", None))
        self.li_32.setText(QCoreApplication.translate("SalonSypialniaHol", u"32", None))
        self.li_33.setText(QCoreApplication.translate("SalonSypialniaHol", u"33", None))
        self.li_34.setText(QCoreApplication.translate("SalonSypialniaHol", u"34", None))
        self.li_35.setText(QCoreApplication.translate("SalonSypialniaHol", u"35", None))
        self.li_36.setText(QCoreApplication.translate("SalonSypialniaHol", u"36", None))
        self.li_37.setText(QCoreApplication.translate("SalonSypialniaHol", u"37", None))
        self.li_38.setText(QCoreApplication.translate("SalonSypialniaHol", u"38", None))
        self.li_40.setText(QCoreApplication.translate("SalonSypialniaHol", u"40", None))
        self.li_41.setText(QCoreApplication.translate("SalonSypialniaHol", u"41", None))
        self.li_42.setText(QCoreApplication.translate("SalonSypialniaHol", u"42", None))
        self.li_43.setText(QCoreApplication.translate("SalonSypialniaHol", u"43", None))
        self.li_44.setText(QCoreApplication.translate("SalonSypialniaHol", u"44", None))
        self.li_45.setText(QCoreApplication.translate("SalonSypialniaHol", u"45", None))
        self.li_46.setText(QCoreApplication.translate("SalonSypialniaHol", u"46", None))
        self.li_48.setText(QCoreApplication.translate("SalonSypialniaHol", u"48", None))
        self.li_49.setText(QCoreApplication.translate("SalonSypialniaHol", u"49", None))
        self.li_50.setText(QCoreApplication.translate("SalonSypialniaHol", u"50", None))
        self.li_51.setText(QCoreApplication.translate("SalonSypialniaHol", u"51", None))
        self.li_52.setText(QCoreApplication.translate("SalonSypialniaHol", u"52", None))
        self.li_53.setText(QCoreApplication.translate("SalonSypialniaHol", u"53", None))
        self.li_54.setText(QCoreApplication.translate("SalonSypialniaHol", u"54", None))
        self.li_56.setText(QCoreApplication.translate("SalonSypialniaHol", u"56", None))
        self.li_57.setText(QCoreApplication.translate("SalonSypialniaHol", u"57", None))
        self.li_58.setText(QCoreApplication.translate("SalonSypialniaHol", u"58", None))
        self.li_59.setText(QCoreApplication.translate("SalonSypialniaHol", u"59", None))
        self.li_60.setText(QCoreApplication.translate("SalonSypialniaHol", u"60", None))
        self.li_61.setText(QCoreApplication.translate("SalonSypialniaHol", u"61", None))
        self.li_62.setText(QCoreApplication.translate("SalonSypialniaHol", u"62", None))
        self.tabWidget_output.setTabText(self.tabWidget_output.indexOf(self.tabWidget_outputPage2), QCoreApplication.translate("SalonSypialniaHol", u"INPUT", None))
        self.pb_2taryfa.setText(QCoreApplication.translate("SalonSypialniaHol", u"2 taryfa", None))
        self.pb_zasawar.setText(QCoreApplication.translate("SalonSypialniaHol", u"Zas. awar.", None))
        self.pb_czujka2.setText(QCoreApplication.translate("SalonSypialniaHol", u"Czujka 2", None))
        self.pb_noc.setText(QCoreApplication.translate("SalonSypialniaHol", u"Noc", None))
        self.pb_wieczor.setText(QCoreApplication.translate("SalonSypialniaHol", u"Wiecz\u00f3r", None))
        self.pb_czujka1.setText(QCoreApplication.translate("SalonSypialniaHol", u"Czujka 1", None))
        self.pb_24V.setText(QCoreApplication.translate("SalonSypialniaHol", u"24V_ON", None))
        self.pbacm0.setText(QCoreApplication.translate("SalonSypialniaHol", u"Po\u0142\u0105cz z ACM", None))
        self.pbusb0.setText(QCoreApplication.translate("SalonSypialniaHol", u"Po\u0142\u0105cz z USB", None))
    # retranslateUi

