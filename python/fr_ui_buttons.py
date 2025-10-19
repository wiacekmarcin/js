# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'fr_buttons.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QLabel,
    QSizePolicy, QToolButton, QWidget)

class Ui_FrameButton(object):
    def setupUi(self, FrameButton):
        if not FrameButton.objectName():
            FrameButton.setObjectName(u"FrameButton")
        FrameButton.resize(94, 26)
        self.gridLayout = QGridLayout(FrameButton)
        self.gridLayout.setSpacing(1)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pb_both = QToolButton(FrameButton)
        self.pb_both.setObjectName(u"pb_both")
        self.pb_both.setMinimumSize(QSize(10, 15))
        self.pb_both.setMaximumSize(QSize(20, 20))
        font = QFont()
        font.setPointSize(8)
        self.pb_both.setFont(font)

        self.gridLayout.addWidget(self.pb_both, 0, 1, 1, 1)

        self.label = QLabel(FrameButton)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(10, 10))
        self.label.setMaximumSize(QSize(20, 10))
        self.label.setStyleSheet(u"background-color: rgb(26, 95, 180);")

        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)

        self.pb_left = QToolButton(FrameButton)
        self.pb_left.setObjectName(u"pb_left")

        self.gridLayout.addWidget(self.pb_left, 0, 0, 2, 1)

        self.pb_rigth = QToolButton(FrameButton)
        self.pb_rigth.setObjectName(u"pb_rigth")

        self.gridLayout.addWidget(self.pb_rigth, 0, 2, 2, 1)


        self.retranslateUi(FrameButton)

        QMetaObject.connectSlotsByName(FrameButton)
    # setupUi

    def retranslateUi(self, FrameButton):
        FrameButton.setWindowTitle(QCoreApplication.translate("FrameButton", u"Frame", None))
        self.pb_both.setText(QCoreApplication.translate("FrameButton", u"x", None))
        self.label.setText("")
        self.pb_left.setText(QCoreApplication.translate("FrameButton", u"...", None))
        self.pb_rigth.setText(QCoreApplication.translate("FrameButton", u"...", None))
    # retranslateUi

