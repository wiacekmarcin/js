# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'kalkulator_wejsc_salon.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFrame, QGridLayout, QLineEdit, QSizePolicy,
    QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.labelsgrid = QGridLayout(self.frame)
        self.labelsgrid.setSpacing(2)
        self.labelsgrid.setObjectName(u"labelsgrid")
        self.labelsgrid.setContentsMargins(1, 2, 1, 2)

        self.gridLayout.addWidget(self.frame, 2, 0, 1, 4)

        self.b48_63 = QLineEdit(Dialog)
        self.b48_63.setObjectName(u"b48_63")

        self.gridLayout.addWidget(self.b48_63, 1, 0, 1, 1)

        self.b16_31 = QLineEdit(Dialog)
        self.b16_31.setObjectName(u"b16_31")

        self.gridLayout.addWidget(self.b16_31, 1, 2, 1, 1)

        self.b32_47 = QLineEdit(Dialog)
        self.b32_47.setObjectName(u"b32_47")

        self.gridLayout.addWidget(self.b32_47, 1, 1, 1, 1)

        self.b00_15 = QLineEdit(Dialog)
        self.b00_15.setObjectName(u"b00_15")

        self.gridLayout.addWidget(self.b00_15, 1, 3, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.StandardButton.Cancel|QDialogButtonBox.StandardButton.Ok)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 4)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 0, 1, 4)

        QWidget.setTabOrder(self.lineEdit, self.b48_63)
        QWidget.setTabOrder(self.b48_63, self.b32_47)
        QWidget.setTabOrder(self.b32_47, self.b16_31)
        QWidget.setTabOrder(self.b16_31, self.b00_15)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
    # retranslateUi

