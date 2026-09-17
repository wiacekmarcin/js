# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'salon_sypialnia_graph.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QFrame,
    QGraphicsView, QGridLayout, QGroupBox, QHBoxLayout,
    QLabel, QPushButton, QScrollArea, QSizePolicy,
    QSpacerItem, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_SalonSypialniaHol(object):
    def setupUi(self, SalonSypialniaHol):
        if not SalonSypialniaHol.objectName():
            SalonSypialniaHol.setObjectName(u"SalonSypialniaHol")
        SalonSypialniaHol.resize(1742, 978)
        self.gridLayout_4 = QGridLayout(SalonSypialniaHol)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(SalonSypialniaHol)
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

        self.tabWidget = QTabWidget(SalonSypialniaHol)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(400, 0))
        self.tabWidget.setMaximumSize(QSize(400, 16777215))
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.tabWidget_output = QWidget()
        self.tabWidget_output.setObjectName(u"tabWidget_output")
        self.verticalLayout_4 = QVBoxLayout(self.tabWidget_output)
        self.verticalLayout_4.setSpacing(2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 5, 5, 5)
        self.lo_04 = QLabel(self.tabWidget_output)
        self.lo_04.setObjectName(u"lo_04")

        self.verticalLayout_4.addWidget(self.lo_04)

        self.lo_05 = QLabel(self.tabWidget_output)
        self.lo_05.setObjectName(u"lo_05")

        self.verticalLayout_4.addWidget(self.lo_05)

        self.lo_06 = QLabel(self.tabWidget_output)
        self.lo_06.setObjectName(u"lo_06")

        self.verticalLayout_4.addWidget(self.lo_06)

        self.lo_07 = QLabel(self.tabWidget_output)
        self.lo_07.setObjectName(u"lo_07")

        self.verticalLayout_4.addWidget(self.lo_07)

        self.lo_08 = QLabel(self.tabWidget_output)
        self.lo_08.setObjectName(u"lo_08")

        self.verticalLayout_4.addWidget(self.lo_08)

        self.lo_09 = QLabel(self.tabWidget_output)
        self.lo_09.setObjectName(u"lo_09")

        self.verticalLayout_4.addWidget(self.lo_09)

        self.lo_10 = QLabel(self.tabWidget_output)
        self.lo_10.setObjectName(u"lo_10")

        self.verticalLayout_4.addWidget(self.lo_10)

        self.lo_11 = QLabel(self.tabWidget_output)
        self.lo_11.setObjectName(u"lo_11")

        self.verticalLayout_4.addWidget(self.lo_11)

        self.lo_12 = QLabel(self.tabWidget_output)
        self.lo_12.setObjectName(u"lo_12")

        self.verticalLayout_4.addWidget(self.lo_12)

        self.lo_13 = QLabel(self.tabWidget_output)
        self.lo_13.setObjectName(u"lo_13")

        self.verticalLayout_4.addWidget(self.lo_13)

        self.lo_14 = QLabel(self.tabWidget_output)
        self.lo_14.setObjectName(u"lo_14")

        self.verticalLayout_4.addWidget(self.lo_14)

        self.lo_15 = QLabel(self.tabWidget_output)
        self.lo_15.setObjectName(u"lo_15")

        self.verticalLayout_4.addWidget(self.lo_15)

        self.lo_19 = QLabel(self.tabWidget_output)
        self.lo_19.setObjectName(u"lo_19")

        self.verticalLayout_4.addWidget(self.lo_19)

        self.lo_20 = QLabel(self.tabWidget_output)
        self.lo_20.setObjectName(u"lo_20")

        self.verticalLayout_4.addWidget(self.lo_20)

        self.lo_21 = QLabel(self.tabWidget_output)
        self.lo_21.setObjectName(u"lo_21")

        self.verticalLayout_4.addWidget(self.lo_21)

        self.lo_22 = QLabel(self.tabWidget_output)
        self.lo_22.setObjectName(u"lo_22")

        self.verticalLayout_4.addWidget(self.lo_22)

        self.lo_23 = QLabel(self.tabWidget_output)
        self.lo_23.setObjectName(u"lo_23")

        self.verticalLayout_4.addWidget(self.lo_23)

        self.lo_24 = QLabel(self.tabWidget_output)
        self.lo_24.setObjectName(u"lo_24")

        self.verticalLayout_4.addWidget(self.lo_24)

        self.lo_25 = QLabel(self.tabWidget_output)
        self.lo_25.setObjectName(u"lo_25")

        self.verticalLayout_4.addWidget(self.lo_25)

        self.lo_26 = QLabel(self.tabWidget_output)
        self.lo_26.setObjectName(u"lo_26")

        self.verticalLayout_4.addWidget(self.lo_26)

        self.lo_27 = QLabel(self.tabWidget_output)
        self.lo_27.setObjectName(u"lo_27")

        self.verticalLayout_4.addWidget(self.lo_27)

        self.lo_28 = QLabel(self.tabWidget_output)
        self.lo_28.setObjectName(u"lo_28")

        self.verticalLayout_4.addWidget(self.lo_28)

        self.lo_29 = QLabel(self.tabWidget_output)
        self.lo_29.setObjectName(u"lo_29")

        self.verticalLayout_4.addWidget(self.lo_29)

        self.lo_30 = QLabel(self.tabWidget_output)
        self.lo_30.setObjectName(u"lo_30")

        self.verticalLayout_4.addWidget(self.lo_30)

        self.lo_31 = QLabel(self.tabWidget_output)
        self.lo_31.setObjectName(u"lo_31")

        self.verticalLayout_4.addWidget(self.lo_31)

        self.lo_39 = QLabel(self.tabWidget_output)
        self.lo_39.setObjectName(u"lo_39")

        self.verticalLayout_4.addWidget(self.lo_39)

        self.lo_47 = QLabel(self.tabWidget_output)
        self.lo_47.setObjectName(u"lo_47")

        self.verticalLayout_4.addWidget(self.lo_47)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabWidget_output, "")
        self.tabWidget_input = QWidget()
        self.tabWidget_input.setObjectName(u"tabWidget_input")
        self.verticalLayout_3 = QVBoxLayout(self.tabWidget_input)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(5, 5, 5, 5)
        self.li_00 = QLabel(self.tabWidget_input)
        self.li_00.setObjectName(u"li_00")

        self.verticalLayout_3.addWidget(self.li_00)

        self.li_01 = QLabel(self.tabWidget_input)
        self.li_01.setObjectName(u"li_01")

        self.verticalLayout_3.addWidget(self.li_01)

        self.li_02 = QLabel(self.tabWidget_input)
        self.li_02.setObjectName(u"li_02")

        self.verticalLayout_3.addWidget(self.li_02)

        self.li_03 = QLabel(self.tabWidget_input)
        self.li_03.setObjectName(u"li_03")

        self.verticalLayout_3.addWidget(self.li_03)

        self.li_16 = QLabel(self.tabWidget_input)
        self.li_16.setObjectName(u"li_16")

        self.verticalLayout_3.addWidget(self.li_16)

        self.li_17 = QLabel(self.tabWidget_input)
        self.li_17.setObjectName(u"li_17")

        self.verticalLayout_3.addWidget(self.li_17)

        self.li_18 = QLabel(self.tabWidget_input)
        self.li_18.setObjectName(u"li_18")

        self.verticalLayout_3.addWidget(self.li_18)

        self.li_32 = QLabel(self.tabWidget_input)
        self.li_32.setObjectName(u"li_32")

        self.verticalLayout_3.addWidget(self.li_32)

        self.li_33 = QLabel(self.tabWidget_input)
        self.li_33.setObjectName(u"li_33")

        self.verticalLayout_3.addWidget(self.li_33)

        self.li_34 = QLabel(self.tabWidget_input)
        self.li_34.setObjectName(u"li_34")

        self.verticalLayout_3.addWidget(self.li_34)

        self.li_35 = QLabel(self.tabWidget_input)
        self.li_35.setObjectName(u"li_35")

        self.verticalLayout_3.addWidget(self.li_35)

        self.li_36 = QLabel(self.tabWidget_input)
        self.li_36.setObjectName(u"li_36")

        self.verticalLayout_3.addWidget(self.li_36)

        self.li_37 = QLabel(self.tabWidget_input)
        self.li_37.setObjectName(u"li_37")

        self.verticalLayout_3.addWidget(self.li_37)

        self.li_38 = QLabel(self.tabWidget_input)
        self.li_38.setObjectName(u"li_38")

        self.verticalLayout_3.addWidget(self.li_38)

        self.li_40 = QLabel(self.tabWidget_input)
        self.li_40.setObjectName(u"li_40")

        self.verticalLayout_3.addWidget(self.li_40)

        self.li_41 = QLabel(self.tabWidget_input)
        self.li_41.setObjectName(u"li_41")

        self.verticalLayout_3.addWidget(self.li_41)

        self.li_42 = QLabel(self.tabWidget_input)
        self.li_42.setObjectName(u"li_42")

        self.verticalLayout_3.addWidget(self.li_42)

        self.li_43 = QLabel(self.tabWidget_input)
        self.li_43.setObjectName(u"li_43")

        self.verticalLayout_3.addWidget(self.li_43)

        self.li_44 = QLabel(self.tabWidget_input)
        self.li_44.setObjectName(u"li_44")

        self.verticalLayout_3.addWidget(self.li_44)

        self.li_45 = QLabel(self.tabWidget_input)
        self.li_45.setObjectName(u"li_45")

        self.verticalLayout_3.addWidget(self.li_45)

        self.li_46 = QLabel(self.tabWidget_input)
        self.li_46.setObjectName(u"li_46")

        self.verticalLayout_3.addWidget(self.li_46)

        self.li_48 = QLabel(self.tabWidget_input)
        self.li_48.setObjectName(u"li_48")

        self.verticalLayout_3.addWidget(self.li_48)

        self.li_49 = QLabel(self.tabWidget_input)
        self.li_49.setObjectName(u"li_49")

        self.verticalLayout_3.addWidget(self.li_49)

        self.li_50 = QLabel(self.tabWidget_input)
        self.li_50.setObjectName(u"li_50")

        self.verticalLayout_3.addWidget(self.li_50)

        self.li_51 = QLabel(self.tabWidget_input)
        self.li_51.setObjectName(u"li_51")

        self.verticalLayout_3.addWidget(self.li_51)

        self.li_52 = QLabel(self.tabWidget_input)
        self.li_52.setObjectName(u"li_52")

        self.verticalLayout_3.addWidget(self.li_52)

        self.li_53 = QLabel(self.tabWidget_input)
        self.li_53.setObjectName(u"li_53")

        self.verticalLayout_3.addWidget(self.li_53)

        self.li_54 = QLabel(self.tabWidget_input)
        self.li_54.setObjectName(u"li_54")

        self.verticalLayout_3.addWidget(self.li_54)

        self.li_56 = QLabel(self.tabWidget_input)
        self.li_56.setObjectName(u"li_56")

        self.verticalLayout_3.addWidget(self.li_56)

        self.li_57 = QLabel(self.tabWidget_input)
        self.li_57.setObjectName(u"li_57")

        self.verticalLayout_3.addWidget(self.li_57)

        self.li_58 = QLabel(self.tabWidget_input)
        self.li_58.setObjectName(u"li_58")

        self.verticalLayout_3.addWidget(self.li_58)

        self.li_59 = QLabel(self.tabWidget_input)
        self.li_59.setObjectName(u"li_59")

        self.verticalLayout_3.addWidget(self.li_59)

        self.li_60 = QLabel(self.tabWidget_input)
        self.li_60.setObjectName(u"li_60")

        self.verticalLayout_3.addWidget(self.li_60)

        self.li_61 = QLabel(self.tabWidget_input)
        self.li_61.setObjectName(u"li_61")

        self.verticalLayout_3.addWidget(self.li_61)

        self.li_62 = QLabel(self.tabWidget_input)
        self.li_62.setObjectName(u"li_62")

        self.verticalLayout_3.addWidget(self.li_62)

        self.tabWidget.addTab(self.tabWidget_input, "")
        self.tab_wykres = QWidget()
        self.tab_wykres.setObjectName(u"tab_wykres")
        self.verticalLayout_5 = QVBoxLayout(self.tab_wykres)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.wykres = QGraphicsView(self.tab_wykres)
        self.wykres.setObjectName(u"wykres")
        self.wykres.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.wykres.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout_5.addWidget(self.wykres)

        self.tabWidget.addTab(self.tab_wykres, "")
        self.tab_57_59 = QWidget()
        self.tab_57_59.setObjectName(u"tab_57_59")
        self.verticalLayout_6 = QVBoxLayout(self.tab_57_59)
        self.verticalLayout_6.setSpacing(2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.tab_57_59)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 380, 942))
        self.verticalLayout_7 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setSpacing(2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.gb57 = QGroupBox(self.scrollAreaWidgetContents)
        self.gb57.setObjectName(u"gb57")
        self.formLayout = QFormLayout(self.gb57)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout.setHorizontalSpacing(2)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setContentsMargins(5, 5, 5, 5)
        self.ez57_01 = QLabel(self.gb57)
        self.ez57_01.setObjectName(u"ez57_01")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez57_01)

        self.z57_01 = QLabel(self.gb57)
        self.z57_01.setObjectName(u"z57_01")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z57_01)

        self.ez57_02 = QLabel(self.gb57)
        self.ez57_02.setObjectName(u"ez57_02")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez57_02)

        self.z57_02 = QLabel(self.gb57)
        self.z57_02.setObjectName(u"z57_02")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z57_02)

        self.ez57_03 = QLabel(self.gb57)
        self.ez57_03.setObjectName(u"ez57_03")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez57_03)

        self.z57_03 = QLabel(self.gb57)
        self.z57_03.setObjectName(u"z57_03")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z57_03)

        self.ez57_04 = QLabel(self.gb57)
        self.ez57_04.setObjectName(u"ez57_04")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez57_04)

        self.z57_04 = QLabel(self.gb57)
        self.z57_04.setObjectName(u"z57_04")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z57_04)

        self.ez57_05 = QLabel(self.gb57)
        self.ez57_05.setObjectName(u"ez57_05")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez57_05)

        self.z57_05 = QLabel(self.gb57)
        self.z57_05.setObjectName(u"z57_05")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z57_05)

        self.ez57_06 = QLabel(self.gb57)
        self.ez57_06.setObjectName(u"ez57_06")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez57_06)

        self.z57_06 = QLabel(self.gb57)
        self.z57_06.setObjectName(u"z57_06")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z57_06)

        self.ez57_07 = QLabel(self.gb57)
        self.ez57_07.setObjectName(u"ez57_07")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez57_07)

        self.z57_07 = QLabel(self.gb57)
        self.z57_07.setObjectName(u"z57_07")

        self.formLayout.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z57_07)

        self.ez57_08 = QLabel(self.gb57)
        self.ez57_08.setObjectName(u"ez57_08")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez57_08)

        self.z57_08 = QLabel(self.gb57)
        self.z57_08.setObjectName(u"z57_08")

        self.formLayout.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z57_08)


        self.verticalLayout_7.addWidget(self.gb57)

        self.gb58 = QGroupBox(self.scrollAreaWidgetContents)
        self.gb58.setObjectName(u"gb58")
        self.formLayout_2 = QFormLayout(self.gb58)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_2.setHorizontalSpacing(2)
        self.formLayout_2.setVerticalSpacing(2)
        self.formLayout_2.setContentsMargins(5, 5, 5, 5)
        self.ez58_01 = QLabel(self.gb58)
        self.ez58_01.setObjectName(u"ez58_01")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez58_01)

        self.z58_01 = QLabel(self.gb58)
        self.z58_01.setObjectName(u"z58_01")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z58_01)

        self.ez58_02 = QLabel(self.gb58)
        self.ez58_02.setObjectName(u"ez58_02")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez58_02)

        self.ez58_03 = QLabel(self.gb58)
        self.ez58_03.setObjectName(u"ez58_03")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez58_03)

        self.ez58_04 = QLabel(self.gb58)
        self.ez58_04.setObjectName(u"ez58_04")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez58_04)

        self.z58_02 = QLabel(self.gb58)
        self.z58_02.setObjectName(u"z58_02")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z58_02)

        self.z58_03 = QLabel(self.gb58)
        self.z58_03.setObjectName(u"z58_03")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z58_03)

        self.z58_04 = QLabel(self.gb58)
        self.z58_04.setObjectName(u"z58_04")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z58_04)

        self.ez58_06 = QLabel(self.gb58)
        self.ez58_06.setObjectName(u"ez58_06")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez58_06)

        self.z58_06 = QLabel(self.gb58)
        self.z58_06.setObjectName(u"z58_06")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z58_06)

        self.ez58_07 = QLabel(self.gb58)
        self.ez58_07.setObjectName(u"ez58_07")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez58_07)

        self.ez58_08 = QLabel(self.gb58)
        self.ez58_08.setObjectName(u"ez58_08")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez58_08)

        self.z58_07 = QLabel(self.gb58)
        self.z58_07.setObjectName(u"z58_07")

        self.formLayout_2.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z58_07)

        self.z58_08 = QLabel(self.gb58)
        self.z58_08.setObjectName(u"z58_08")

        self.formLayout_2.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z58_08)

        self.ez58_05 = QLabel(self.gb58)
        self.ez58_05.setObjectName(u"ez58_05")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez58_05)

        self.z58_6 = QLabel(self.gb58)
        self.z58_6.setObjectName(u"z58_6")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z58_6)


        self.verticalLayout_7.addWidget(self.gb58)

        self.gb59 = QGroupBox(self.scrollAreaWidgetContents)
        self.gb59.setObjectName(u"gb59")
        self.formLayout_13 = QFormLayout(self.gb59)
        self.formLayout_13.setObjectName(u"formLayout_13")
        self.formLayout_13.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_13.setHorizontalSpacing(2)
        self.formLayout_13.setVerticalSpacing(2)
        self.formLayout_13.setContentsMargins(5, 5, 5, 5)
        self.ez59_01 = QLabel(self.gb59)
        self.ez59_01.setObjectName(u"ez59_01")

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez59_01)

        self.z59_01 = QLabel(self.gb59)
        self.z59_01.setObjectName(u"z59_01")

        self.formLayout_13.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z59_01)

        self.ez59_02 = QLabel(self.gb59)
        self.ez59_02.setObjectName(u"ez59_02")

        self.formLayout_13.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez59_02)

        self.z59_02 = QLabel(self.gb59)
        self.z59_02.setObjectName(u"z59_02")

        self.formLayout_13.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z59_02)

        self.ez59_03 = QLabel(self.gb59)
        self.ez59_03.setObjectName(u"ez59_03")

        self.formLayout_13.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez59_03)

        self.z59_03 = QLabel(self.gb59)
        self.z59_03.setObjectName(u"z59_03")

        self.formLayout_13.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z59_03)

        self.ez59_04 = QLabel(self.gb59)
        self.ez59_04.setObjectName(u"ez59_04")

        self.formLayout_13.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez59_04)

        self.z59_04 = QLabel(self.gb59)
        self.z59_04.setObjectName(u"z59_04")

        self.formLayout_13.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z59_04)

        self.ez59_05 = QLabel(self.gb59)
        self.ez59_05.setObjectName(u"ez59_05")

        self.formLayout_13.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez59_05)

        self.z59_05 = QLabel(self.gb59)
        self.z59_05.setObjectName(u"z59_05")

        self.formLayout_13.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z59_05)

        self.ez59_06 = QLabel(self.gb59)
        self.ez59_06.setObjectName(u"ez59_06")

        self.formLayout_13.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez59_06)

        self.z59_06 = QLabel(self.gb59)
        self.z59_06.setObjectName(u"z59_06")

        self.formLayout_13.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z59_06)

        self.ez59_07 = QLabel(self.gb59)
        self.ez59_07.setObjectName(u"ez59_07")

        self.formLayout_13.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez59_07)

        self.z59_07 = QLabel(self.gb59)
        self.z59_07.setObjectName(u"z59_07")

        self.formLayout_13.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z59_07)

        self.ez59_08 = QLabel(self.gb59)
        self.ez59_08.setObjectName(u"ez59_08")

        self.formLayout_13.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez59_08)

        self.z59_08 = QLabel(self.gb59)
        self.z59_08.setObjectName(u"z59_08")

        self.formLayout_13.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z59_08)


        self.verticalLayout_7.addWidget(self.gb59)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_6.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_57_59, "")
        self.tab_209_213 = QWidget()
        self.tab_209_213.setObjectName(u"tab_209_213")
        self.verticalLayout_8 = QVBoxLayout(self.tab_209_213)
        self.verticalLayout_8.setSpacing(2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_2 = QScrollArea(self.tab_209_213)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 380, 942))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setSpacing(2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(2, 2, 2, 2)
        self.gb209 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb209.setObjectName(u"gb209")
        self.formLayout_4 = QFormLayout(self.gb209)
        self.formLayout_4.setObjectName(u"formLayout_4")
        self.formLayout_4.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_4.setHorizontalSpacing(2)
        self.formLayout_4.setVerticalSpacing(2)
        self.formLayout_4.setContentsMargins(5, 5, 5, 5)
        self.ez209_01 = QLabel(self.gb209)
        self.ez209_01.setObjectName(u"ez209_01")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez209_01)

        self.z209_01 = QLabel(self.gb209)
        self.z209_01.setObjectName(u"z209_01")

        self.formLayout_4.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z209_01)

        self.ez209_02 = QLabel(self.gb209)
        self.ez209_02.setObjectName(u"ez209_02")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez209_02)

        self.z209_02 = QLabel(self.gb209)
        self.z209_02.setObjectName(u"z209_02")

        self.formLayout_4.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z209_02)

        self.ez209_03 = QLabel(self.gb209)
        self.ez209_03.setObjectName(u"ez209_03")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez209_03)

        self.z209_03 = QLabel(self.gb209)
        self.z209_03.setObjectName(u"z209_03")

        self.formLayout_4.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z209_03)

        self.ez209_04 = QLabel(self.gb209)
        self.ez209_04.setObjectName(u"ez209_04")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez209_04)

        self.z209_04 = QLabel(self.gb209)
        self.z209_04.setObjectName(u"z209_04")

        self.formLayout_4.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z209_04)

        self.ez209_05 = QLabel(self.gb209)
        self.ez209_05.setObjectName(u"ez209_05")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez209_05)

        self.z209_05 = QLabel(self.gb209)
        self.z209_05.setObjectName(u"z209_05")

        self.formLayout_4.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z209_05)

        self.ez209_06 = QLabel(self.gb209)
        self.ez209_06.setObjectName(u"ez209_06")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez209_06)

        self.z209_06 = QLabel(self.gb209)
        self.z209_06.setObjectName(u"z209_06")

        self.formLayout_4.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z209_06)

        self.ez209_07 = QLabel(self.gb209)
        self.ez209_07.setObjectName(u"ez209_07")

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez209_07)

        self.z209_07 = QLabel(self.gb209)
        self.z209_07.setObjectName(u"z209_07")

        self.formLayout_4.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z209_07)

        self.ez209_08 = QLabel(self.gb209)
        self.ez209_08.setObjectName(u"ez209_08")

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez209_08)

        self.z209_08 = QLabel(self.gb209)
        self.z209_08.setObjectName(u"z209_08")

        self.formLayout_4.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z209_08)

        self.ez209_09 = QLabel(self.gb209)
        self.ez209_09.setObjectName(u"ez209_09")

        self.formLayout_4.setWidget(8, QFormLayout.ItemRole.LabelRole, self.ez209_09)

        self.z209_09 = QLabel(self.gb209)
        self.z209_09.setObjectName(u"z209_09")

        self.formLayout_4.setWidget(8, QFormLayout.ItemRole.FieldRole, self.z209_09)

        self.ez209_10 = QLabel(self.gb209)
        self.ez209_10.setObjectName(u"ez209_10")

        self.formLayout_4.setWidget(9, QFormLayout.ItemRole.LabelRole, self.ez209_10)

        self.z209_10 = QLabel(self.gb209)
        self.z209_10.setObjectName(u"z209_10")

        self.formLayout_4.setWidget(9, QFormLayout.ItemRole.FieldRole, self.z209_10)


        self.verticalLayout_9.addWidget(self.gb209)

        self.gb210 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb210.setObjectName(u"gb210")
        self.formLayout_5 = QFormLayout(self.gb210)
        self.formLayout_5.setObjectName(u"formLayout_5")
        self.formLayout_5.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_5.setHorizontalSpacing(2)
        self.formLayout_5.setVerticalSpacing(2)
        self.formLayout_5.setContentsMargins(5, 5, 5, 5)
        self.ez210_01 = QLabel(self.gb210)
        self.ez210_01.setObjectName(u"ez210_01")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez210_01)

        self.z210_01 = QLabel(self.gb210)
        self.z210_01.setObjectName(u"z210_01")

        self.formLayout_5.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z210_01)

        self.ez210_02 = QLabel(self.gb210)
        self.ez210_02.setObjectName(u"ez210_02")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez210_02)

        self.z210_02 = QLabel(self.gb210)
        self.z210_02.setObjectName(u"z210_02")

        self.formLayout_5.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z210_02)

        self.ez210_03 = QLabel(self.gb210)
        self.ez210_03.setObjectName(u"ez210_03")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez210_03)

        self.z210_03 = QLabel(self.gb210)
        self.z210_03.setObjectName(u"z210_03")

        self.formLayout_5.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z210_03)

        self.ez210_04 = QLabel(self.gb210)
        self.ez210_04.setObjectName(u"ez210_04")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez210_04)

        self.z210_04 = QLabel(self.gb210)
        self.z210_04.setObjectName(u"z210_04")

        self.formLayout_5.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z210_04)

        self.ez210_05 = QLabel(self.gb210)
        self.ez210_05.setObjectName(u"ez210_05")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez210_05)

        self.z210_05 = QLabel(self.gb210)
        self.z210_05.setObjectName(u"z210_05")

        self.formLayout_5.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z210_05)

        self.ez210_06 = QLabel(self.gb210)
        self.ez210_06.setObjectName(u"ez210_06")

        self.formLayout_5.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez210_06)

        self.z210_06 = QLabel(self.gb210)
        self.z210_06.setObjectName(u"z210_06")

        self.formLayout_5.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z210_06)


        self.verticalLayout_9.addWidget(self.gb210)

        self.gb211 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb211.setObjectName(u"gb211")
        self.formLayout_6 = QFormLayout(self.gb211)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.formLayout_6.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_6.setHorizontalSpacing(2)
        self.formLayout_6.setVerticalSpacing(2)
        self.formLayout_6.setContentsMargins(5, 5, 5, 5)
        self.ez211_01 = QLabel(self.gb211)
        self.ez211_01.setObjectName(u"ez211_01")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez211_01)

        self.z211_01 = QLabel(self.gb211)
        self.z211_01.setObjectName(u"z211_01")

        self.formLayout_6.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z211_01)

        self.ez211_02 = QLabel(self.gb211)
        self.ez211_02.setObjectName(u"ez211_02")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez211_02)

        self.z211_02 = QLabel(self.gb211)
        self.z211_02.setObjectName(u"z211_02")

        self.formLayout_6.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z211_02)

        self.ez211_03 = QLabel(self.gb211)
        self.ez211_03.setObjectName(u"ez211_03")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez211_03)

        self.z211_03 = QLabel(self.gb211)
        self.z211_03.setObjectName(u"z211_03")

        self.formLayout_6.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z211_03)

        self.ez211_04 = QLabel(self.gb211)
        self.ez211_04.setObjectName(u"ez211_04")

        self.formLayout_6.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez211_04)

        self.z211_04 = QLabel(self.gb211)
        self.z211_04.setObjectName(u"z211_04")

        self.formLayout_6.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z211_04)


        self.verticalLayout_9.addWidget(self.gb211)

        self.gb212 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb212.setObjectName(u"gb212")
        self.formLayout_7 = QFormLayout(self.gb212)
        self.formLayout_7.setObjectName(u"formLayout_7")
        self.formLayout_7.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_7.setHorizontalSpacing(2)
        self.formLayout_7.setVerticalSpacing(2)
        self.formLayout_7.setContentsMargins(5, 5, 5, 5)
        self.ez212_01 = QLabel(self.gb212)
        self.ez212_01.setObjectName(u"ez212_01")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez212_01)

        self.z212_01 = QLabel(self.gb212)
        self.z212_01.setObjectName(u"z212_01")

        self.formLayout_7.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z212_01)

        self.ez212_02 = QLabel(self.gb212)
        self.ez212_02.setObjectName(u"ez212_02")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez212_02)

        self.z212_02 = QLabel(self.gb212)
        self.z212_02.setObjectName(u"z212_02")

        self.formLayout_7.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z212_02)

        self.ez212_03 = QLabel(self.gb212)
        self.ez212_03.setObjectName(u"ez212_03")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez212_03)

        self.z212_03 = QLabel(self.gb212)
        self.z212_03.setObjectName(u"z212_03")

        self.formLayout_7.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z212_03)

        self.ez212_04 = QLabel(self.gb212)
        self.ez212_04.setObjectName(u"ez212_04")

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez212_04)

        self.z212_05 = QLabel(self.gb212)
        self.z212_05.setObjectName(u"z212_05")

        self.formLayout_7.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z212_05)


        self.verticalLayout_9.addWidget(self.gb212)

        self.gb213 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gb213.setObjectName(u"gb213")
        self.formLayout_8 = QFormLayout(self.gb213)
        self.formLayout_8.setObjectName(u"formLayout_8")
        self.formLayout_8.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_8.setHorizontalSpacing(2)
        self.formLayout_8.setVerticalSpacing(2)
        self.formLayout_8.setContentsMargins(5, 5, 5, 5)
        self.ez213_01 = QLabel(self.gb213)
        self.ez213_01.setObjectName(u"ez213_01")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez213_01)

        self.z213_01 = QLabel(self.gb213)
        self.z213_01.setObjectName(u"z213_01")

        self.formLayout_8.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z213_01)

        self.ez213_02 = QLabel(self.gb213)
        self.ez213_02.setObjectName(u"ez213_02")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez213_02)

        self.z213_02 = QLabel(self.gb213)
        self.z213_02.setObjectName(u"z213_02")

        self.formLayout_8.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z213_02)

        self.ez213_03 = QLabel(self.gb213)
        self.ez213_03.setObjectName(u"ez213_03")

        self.formLayout_8.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez213_03)

        self.z213_03 = QLabel(self.gb213)
        self.z213_03.setObjectName(u"z213_03")

        self.formLayout_8.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z213_03)

        self.ez213_04 = QLabel(self.gb213)
        self.ez213_04.setObjectName(u"ez213_04")

        self.formLayout_8.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez213_04)

        self.z213_04 = QLabel(self.gb213)
        self.z213_04.setObjectName(u"z213_04")

        self.formLayout_8.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z213_04)

        self.ez213_05 = QLabel(self.gb213)
        self.ez213_05.setObjectName(u"ez213_05")

        self.formLayout_8.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez213_05)

        self.z213_05 = QLabel(self.gb213)
        self.z213_05.setObjectName(u"z213_05")

        self.formLayout_8.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z213_05)

        self.ez213_06 = QLabel(self.gb213)
        self.ez213_06.setObjectName(u"ez213_06")

        self.formLayout_8.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez213_06)

        self.z213_06 = QLabel(self.gb213)
        self.z213_06.setObjectName(u"z213_06")

        self.formLayout_8.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z213_06)


        self.verticalLayout_9.addWidget(self.gb213)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea_2)

        self.tabWidget.addTab(self.tab_209_213, "")
        self.tab_214_217 = QWidget()
        self.tab_214_217.setObjectName(u"tab_214_217")
        self.verticalLayout_10 = QVBoxLayout(self.tab_214_217)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.scrollArea_3 = QScrollArea(self.tab_214_217)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 394, 942))
        self.verticalLayout_11 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_11.setSpacing(2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(2, 2, 2, 2)
        self.gb214 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.gb214.setObjectName(u"gb214")
        self.formLayout_11 = QFormLayout(self.gb214)
        self.formLayout_11.setObjectName(u"formLayout_11")
        self.formLayout_11.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_11.setHorizontalSpacing(2)
        self.formLayout_11.setVerticalSpacing(2)
        self.formLayout_11.setContentsMargins(5, 5, 5, 5)
        self.ez214_01 = QLabel(self.gb214)
        self.ez214_01.setObjectName(u"ez214_01")

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez214_01)

        self.z214_01 = QLabel(self.gb214)
        self.z214_01.setObjectName(u"z214_01")

        self.formLayout_11.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z214_01)

        self.ez214_02 = QLabel(self.gb214)
        self.ez214_02.setObjectName(u"ez214_02")

        self.formLayout_11.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez214_02)

        self.z214_02 = QLabel(self.gb214)
        self.z214_02.setObjectName(u"z214_02")

        self.formLayout_11.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z214_02)

        self.ez214_03 = QLabel(self.gb214)
        self.ez214_03.setObjectName(u"ez214_03")

        self.formLayout_11.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez214_03)

        self.z214_03 = QLabel(self.gb214)
        self.z214_03.setObjectName(u"z214_03")

        self.formLayout_11.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z214_03)

        self.ez214_04 = QLabel(self.gb214)
        self.ez214_04.setObjectName(u"ez214_04")

        self.formLayout_11.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez214_04)

        self.z214_04 = QLabel(self.gb214)
        self.z214_04.setObjectName(u"z214_04")

        self.formLayout_11.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z214_04)

        self.ez214_05 = QLabel(self.gb214)
        self.ez214_05.setObjectName(u"ez214_05")

        self.formLayout_11.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez214_05)

        self.z214_05 = QLabel(self.gb214)
        self.z214_05.setObjectName(u"z214_05")

        self.formLayout_11.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z214_05)

        self.ez214_06 = QLabel(self.gb214)
        self.ez214_06.setObjectName(u"ez214_06")

        self.formLayout_11.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez214_06)

        self.z214_06 = QLabel(self.gb214)
        self.z214_06.setObjectName(u"z214_06")

        self.formLayout_11.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z214_06)

        self.ez214_07 = QLabel(self.gb214)
        self.ez214_07.setObjectName(u"ez214_07")

        self.formLayout_11.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez214_07)

        self.z214_07 = QLabel(self.gb214)
        self.z214_07.setObjectName(u"z214_07")

        self.formLayout_11.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z214_07)

        self.ez214_08 = QLabel(self.gb214)
        self.ez214_08.setObjectName(u"ez214_08")

        self.formLayout_11.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez214_08)

        self.z214_08 = QLabel(self.gb214)
        self.z214_08.setObjectName(u"z214_08")

        self.formLayout_11.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z214_08)

        self.ez214_09 = QLabel(self.gb214)
        self.ez214_09.setObjectName(u"ez214_09")

        self.formLayout_11.setWidget(8, QFormLayout.ItemRole.LabelRole, self.ez214_09)

        self.z214_09 = QLabel(self.gb214)
        self.z214_09.setObjectName(u"z214_09")

        self.formLayout_11.setWidget(8, QFormLayout.ItemRole.FieldRole, self.z214_09)

        self.ez214_10 = QLabel(self.gb214)
        self.ez214_10.setObjectName(u"ez214_10")

        self.formLayout_11.setWidget(9, QFormLayout.ItemRole.LabelRole, self.ez214_10)

        self.z214_10 = QLabel(self.gb214)
        self.z214_10.setObjectName(u"z214_10")

        self.formLayout_11.setWidget(9, QFormLayout.ItemRole.FieldRole, self.z214_10)


        self.verticalLayout_11.addWidget(self.gb214)

        self.gb215 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.gb215.setObjectName(u"gb215")
        self.formLayout_9 = QFormLayout(self.gb215)
        self.formLayout_9.setObjectName(u"formLayout_9")
        self.formLayout_9.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_9.setHorizontalSpacing(2)
        self.formLayout_9.setVerticalSpacing(2)
        self.formLayout_9.setContentsMargins(5, 5, 5, 5)
        self.ez215_01 = QLabel(self.gb215)
        self.ez215_01.setObjectName(u"ez215_01")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez215_01)

        self.z215_01 = QLabel(self.gb215)
        self.z215_01.setObjectName(u"z215_01")

        self.formLayout_9.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z215_01)

        self.ez215_02 = QLabel(self.gb215)
        self.ez215_02.setObjectName(u"ez215_02")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez215_02)

        self.z215_02 = QLabel(self.gb215)
        self.z215_02.setObjectName(u"z215_02")

        self.formLayout_9.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z215_02)

        self.ez215_03 = QLabel(self.gb215)
        self.ez215_03.setObjectName(u"ez215_03")

        self.formLayout_9.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez215_03)

        self.z215_03 = QLabel(self.gb215)
        self.z215_03.setObjectName(u"z215_03")

        self.formLayout_9.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z215_03)

        self.ez215_04 = QLabel(self.gb215)
        self.ez215_04.setObjectName(u"ez215_04")

        self.formLayout_9.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez215_04)

        self.z215_04 = QLabel(self.gb215)
        self.z215_04.setObjectName(u"z215_04")

        self.formLayout_9.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z215_04)

        self.ez215_05 = QLabel(self.gb215)
        self.ez215_05.setObjectName(u"ez215_05")

        self.formLayout_9.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez215_05)

        self.z215_05 = QLabel(self.gb215)
        self.z215_05.setObjectName(u"z215_05")

        self.formLayout_9.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z215_05)

        self.ez215_06 = QLabel(self.gb215)
        self.ez215_06.setObjectName(u"ez215_06")

        self.formLayout_9.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez215_06)

        self.z215_06 = QLabel(self.gb215)
        self.z215_06.setObjectName(u"z215_06")

        self.formLayout_9.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z215_06)

        self.ez215_07 = QLabel(self.gb215)
        self.ez215_07.setObjectName(u"ez215_07")

        self.formLayout_9.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez215_07)

        self.z215_07 = QLabel(self.gb215)
        self.z215_07.setObjectName(u"z215_07")

        self.formLayout_9.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z215_07)

        self.ez215_08 = QLabel(self.gb215)
        self.ez215_08.setObjectName(u"ez215_08")

        self.formLayout_9.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez215_08)

        self.z215_08 = QLabel(self.gb215)
        self.z215_08.setObjectName(u"z215_08")

        self.formLayout_9.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z215_08)

        self.ez215_09 = QLabel(self.gb215)
        self.ez215_09.setObjectName(u"ez215_09")

        self.formLayout_9.setWidget(8, QFormLayout.ItemRole.LabelRole, self.ez215_09)

        self.z215_09 = QLabel(self.gb215)
        self.z215_09.setObjectName(u"z215_09")

        self.formLayout_9.setWidget(8, QFormLayout.ItemRole.FieldRole, self.z215_09)

        self.ez215_10 = QLabel(self.gb215)
        self.ez215_10.setObjectName(u"ez215_10")

        self.formLayout_9.setWidget(9, QFormLayout.ItemRole.LabelRole, self.ez215_10)

        self.z215_10 = QLabel(self.gb215)
        self.z215_10.setObjectName(u"z215_10")

        self.formLayout_9.setWidget(9, QFormLayout.ItemRole.FieldRole, self.z215_10)


        self.verticalLayout_11.addWidget(self.gb215)

        self.gb216 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.gb216.setObjectName(u"gb216")
        self.formLayout_12 = QFormLayout(self.gb216)
        self.formLayout_12.setObjectName(u"formLayout_12")
        self.formLayout_12.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_12.setHorizontalSpacing(2)
        self.formLayout_12.setVerticalSpacing(2)
        self.formLayout_12.setContentsMargins(5, 5, 5, 5)
        self.ez216_01 = QLabel(self.gb216)
        self.ez216_01.setObjectName(u"ez216_01")

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez216_01)

        self.z216_01 = QLabel(self.gb216)
        self.z216_01.setObjectName(u"z216_01")

        self.formLayout_12.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z216_01)

        self.ez216_02 = QLabel(self.gb216)
        self.ez216_02.setObjectName(u"ez216_02")

        self.formLayout_12.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez216_02)

        self.z216_02 = QLabel(self.gb216)
        self.z216_02.setObjectName(u"z216_02")

        self.formLayout_12.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z216_02)

        self.ez216_03 = QLabel(self.gb216)
        self.ez216_03.setObjectName(u"ez216_03")

        self.formLayout_12.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez216_03)

        self.z216_03 = QLabel(self.gb216)
        self.z216_03.setObjectName(u"z216_03")

        self.formLayout_12.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z216_03)

        self.ez216_04 = QLabel(self.gb216)
        self.ez216_04.setObjectName(u"ez216_04")

        self.formLayout_12.setWidget(3, QFormLayout.ItemRole.LabelRole, self.ez216_04)

        self.z216_04 = QLabel(self.gb216)
        self.z216_04.setObjectName(u"z216_04")

        self.formLayout_12.setWidget(3, QFormLayout.ItemRole.FieldRole, self.z216_04)

        self.ez216_05 = QLabel(self.gb216)
        self.ez216_05.setObjectName(u"ez216_05")

        self.formLayout_12.setWidget(4, QFormLayout.ItemRole.LabelRole, self.ez216_05)

        self.z216_05 = QLabel(self.gb216)
        self.z216_05.setObjectName(u"z216_05")

        self.formLayout_12.setWidget(4, QFormLayout.ItemRole.FieldRole, self.z216_05)

        self.ez216_06 = QLabel(self.gb216)
        self.ez216_06.setObjectName(u"ez216_06")

        self.formLayout_12.setWidget(5, QFormLayout.ItemRole.LabelRole, self.ez216_06)

        self.z216_06 = QLabel(self.gb216)
        self.z216_06.setObjectName(u"z216_06")

        self.formLayout_12.setWidget(5, QFormLayout.ItemRole.FieldRole, self.z216_06)

        self.ez216_07 = QLabel(self.gb216)
        self.ez216_07.setObjectName(u"ez216_07")

        self.formLayout_12.setWidget(6, QFormLayout.ItemRole.LabelRole, self.ez216_07)

        self.z216_07 = QLabel(self.gb216)
        self.z216_07.setObjectName(u"z216_07")

        self.formLayout_12.setWidget(6, QFormLayout.ItemRole.FieldRole, self.z216_07)

        self.ez216_08 = QLabel(self.gb216)
        self.ez216_08.setObjectName(u"ez216_08")

        self.formLayout_12.setWidget(7, QFormLayout.ItemRole.LabelRole, self.ez216_08)

        self.z216_08 = QLabel(self.gb216)
        self.z216_08.setObjectName(u"z216_08")

        self.formLayout_12.setWidget(7, QFormLayout.ItemRole.FieldRole, self.z216_08)

        self.ez216_09 = QLabel(self.gb216)
        self.ez216_09.setObjectName(u"ez216_09")

        self.formLayout_12.setWidget(8, QFormLayout.ItemRole.LabelRole, self.ez216_09)

        self.z216_09 = QLabel(self.gb216)
        self.z216_09.setObjectName(u"z216_09")

        self.formLayout_12.setWidget(8, QFormLayout.ItemRole.FieldRole, self.z216_09)

        self.ez216_10 = QLabel(self.gb216)
        self.ez216_10.setObjectName(u"ez216_10")

        self.formLayout_12.setWidget(9, QFormLayout.ItemRole.LabelRole, self.ez216_10)

        self.z216_10 = QLabel(self.gb216)
        self.z216_10.setObjectName(u"z216_10")

        self.formLayout_12.setWidget(9, QFormLayout.ItemRole.FieldRole, self.z216_10)


        self.verticalLayout_11.addWidget(self.gb216)

        self.gb217 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.gb217.setObjectName(u"gb217")
        self.formLayout_10 = QFormLayout(self.gb217)
        self.formLayout_10.setObjectName(u"formLayout_10")
        self.formLayout_10.setRowWrapPolicy(QFormLayout.WrapLongRows)
        self.formLayout_10.setHorizontalSpacing(2)
        self.formLayout_10.setVerticalSpacing(2)
        self.formLayout_10.setContentsMargins(5, 5, 5, 5)
        self.ez217_01 = QLabel(self.gb217)
        self.ez217_01.setObjectName(u"ez217_01")

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.LabelRole, self.ez217_01)

        self.z217_01 = QLabel(self.gb217)
        self.z217_01.setObjectName(u"z217_01")

        self.formLayout_10.setWidget(0, QFormLayout.ItemRole.FieldRole, self.z217_01)

        self.ez217_02 = QLabel(self.gb217)
        self.ez217_02.setObjectName(u"ez217_02")

        self.formLayout_10.setWidget(1, QFormLayout.ItemRole.LabelRole, self.ez217_02)

        self.z217_02 = QLabel(self.gb217)
        self.z217_02.setObjectName(u"z217_02")

        self.formLayout_10.setWidget(1, QFormLayout.ItemRole.FieldRole, self.z217_02)

        self.ez217_03 = QLabel(self.gb217)
        self.ez217_03.setObjectName(u"ez217_03")

        self.formLayout_10.setWidget(2, QFormLayout.ItemRole.LabelRole, self.ez217_03)

        self.z217_03 = QLabel(self.gb217)
        self.z217_03.setObjectName(u"z217_03")

        self.formLayout_10.setWidget(2, QFormLayout.ItemRole.FieldRole, self.z217_03)


        self.verticalLayout_11.addWidget(self.gb217)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_4)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_10.addWidget(self.scrollArea_3)

        self.tabWidget.addTab(self.tab_214_217, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 3, 1)

        self.frame_3 = QFrame(SalonSypialniaHol)
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

        self.frame_2 = QFrame(SalonSypialniaHol)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pb_2taryfa = QPushButton(self.frame_2)
        self.pb_2taryfa.setObjectName(u"pb_2taryfa")

        self.gridLayout_3.addWidget(self.pb_2taryfa, 0, 5, 1, 1)

        self.pb_24V = QPushButton(self.frame_2)
        self.pb_24V.setObjectName(u"pb_24V")

        self.gridLayout_3.addWidget(self.pb_24V, 0, 8, 1, 1)

        self.pb_czujka1 = QPushButton(self.frame_2)
        self.pb_czujka1.setObjectName(u"pb_czujka1")

        self.gridLayout_3.addWidget(self.pb_czujka1, 0, 6, 1, 1)

        self.pb_czujka2 = QPushButton(self.frame_2)
        self.pb_czujka2.setObjectName(u"pb_czujka2")

        self.gridLayout_3.addWidget(self.pb_czujka2, 0, 7, 1, 1)

        self.pb_noc = QPushButton(self.frame_2)
        self.pb_noc.setObjectName(u"pb_noc")

        self.gridLayout_3.addWidget(self.pb_noc, 0, 3, 1, 1)

        self.pb_zasawar = QPushButton(self.frame_2)
        self.pb_zasawar.setObjectName(u"pb_zasawar")

        self.gridLayout_3.addWidget(self.pb_zasawar, 0, 1, 1, 1)

        self.pb_wieczor = QPushButton(self.frame_2)
        self.pb_wieczor.setObjectName(u"pb_wieczor")

        self.gridLayout_3.addWidget(self.pb_wieczor, 0, 4, 1, 1)

        self.frame_4 = QFrame(self.frame_2)
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


        self.gridLayout_3.addWidget(self.frame_4, 0, 0, 1, 1)


        self.gridLayout_2.addWidget(self.frame_2, 2, 1, 1, 1)


        self.gridLayout_4.addLayout(self.gridLayout_2, 0, 0, 1, 1)


        self.retranslateUi(SalonSypialniaHol)

        self.tabWidget.setCurrentIndex(2)


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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_output), QCoreApplication.translate("SalonSypialniaHol", u"OUTPUT", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabWidget_input), QCoreApplication.translate("SalonSypialniaHol", u"INPUT", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_wykres), QCoreApplication.translate("SalonSypialniaHol", u"Wej\u015bcia/Wyj\u015bcia", None))
        self.gb57.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"57", None))
        self.ez57_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z57_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z57_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z57_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z57_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z57_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z57_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z57_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez57_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z57_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb58.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"58", None))
        self.ez58_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z58_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez58_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.ez58_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.ez58_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z58_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.z58_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.z58_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez58_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z58_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez58_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.ez58_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z58_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.z58_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez58_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z58_6.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb59.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"59", None))
        self.ez59_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z59_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z59_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z59_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z59_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z59_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z59_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z59_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez59_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z59_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_57_59), QCoreApplication.translate("SalonSypialniaHol", u"Z\u0142acza 57,58,59", None))
        self.gb209.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"209", None))
        self.ez209_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z209_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z209_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z209_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z209_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z209_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z209_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z209_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z209_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"9.", None))
        self.z209_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez209_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"10.", None))
        self.z209_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb210.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"210", None))
        self.ez210_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z210_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez210_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z210_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez210_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z210_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez210_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z210_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez210_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z210_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez210_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z210_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb211.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"211", None))
        self.ez211_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z211_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez211_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z211_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez211_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z211_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez211_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z211_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb212.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"212", None))
        self.ez212_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z212_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez212_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z212_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez212_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z212_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez212_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z212_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb213.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"213", None))
        self.ez213_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z213_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez213_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z213_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez213_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z213_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez213_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z213_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez213_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z213_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez213_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z213_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_209_213), QCoreApplication.translate("SalonSypialniaHol", u"Z\u0142\u0105cza 209-213", None))
        self.gb214.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"214", None))
        self.ez214_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z214_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z214_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z214_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z214_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z214_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z214_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z214_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z214_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"9.", None))
        self.z214_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez214_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"10.", None))
        self.z214_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb215.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"215", None))
        self.ez215_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z215_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z215_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z215_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z215_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z215_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z215_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z215_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z215_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"9.", None))
        self.z215_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez215_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"10.", None))
        self.z215_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb216.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"216", None))
        self.ez216_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z216_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z216_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z216_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"4.", None))
        self.z216_04.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"5.", None))
        self.z216_05.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"6.", None))
        self.z216_06.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"7.", None))
        self.z216_07.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"8.", None))
        self.z216_08.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"9.", None))
        self.z216_09.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez216_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"10.", None))
        self.z216_10.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.gb217.setTitle(QCoreApplication.translate("SalonSypialniaHol", u"217", None))
        self.ez217_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"1.", None))
        self.z217_01.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez217_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"2.", None))
        self.z217_02.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.ez217_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"3.", None))
        self.z217_03.setText(QCoreApplication.translate("SalonSypialniaHol", u"-", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_214_217), QCoreApplication.translate("SalonSypialniaHol", u"Z\u0142\u0105cza 214-217", None))
        self.pb_2taryfa.setText(QCoreApplication.translate("SalonSypialniaHol", u"2 taryfa", None))
        self.pb_24V.setText(QCoreApplication.translate("SalonSypialniaHol", u"24V_ON", None))
        self.pb_czujka1.setText(QCoreApplication.translate("SalonSypialniaHol", u"Czujka 1", None))
        self.pb_czujka2.setText(QCoreApplication.translate("SalonSypialniaHol", u"Czujka 2", None))
        self.pb_noc.setText(QCoreApplication.translate("SalonSypialniaHol", u"Noc", None))
        self.pb_zasawar.setText(QCoreApplication.translate("SalonSypialniaHol", u"Zas. awar.", None))
        self.pb_wieczor.setText(QCoreApplication.translate("SalonSypialniaHol", u"Wiecz\u00f3r", None))
        self.pbacm0.setText(QCoreApplication.translate("SalonSypialniaHol", u"Po\u0142\u0105cz z ACM", None))
        self.pbusb0.setText(QCoreApplication.translate("SalonSypialniaHol", u"Po\u0142\u0105cz z USB", None))
    # retranslateUi

