# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlpeOgX.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import ressurce_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(450, 438)
        MainWindow.setMinimumSize(QSize(450, 438))
        MainWindow.setStyleSheet(u"QWidget#centralwidget{\n"
"Backgound-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget#centralwidget{\n"
"background-color: qlineargradient(spread:pad, x1:0.460455, y1:0.648, x2:0.466, y2:0.994318, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255))\n"
"}\n"
"\n"
"QLabel {\n"
"font-size: 35px;\n"
"font-weight: bold;\n"
"color: white;\n"
"\n"
"}\n"
"\n"
"QPushButton{\n"
" font-size: 20px;\n"
" color: black;\n"
" min-height: 45px;\n"
" border-radius: 20px;\n"
" background-color: white;\n"
"\n"
"}")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 20, 431, 71))
        self.label.setAlignment(Qt.AlignCenter)
        self.frame_yes = QFrame(self.centralwidget)
        self.frame_yes.setObjectName(u"frame_yes")
        self.frame_yes.setGeometry(QRect(60, 190, 141, 81))
        self.frame_yes.setFrameShape(QFrame.NoFrame)
        self.frame_yes.setFrameShadow(QFrame.Raised)
        self.frame_yes.setMidLineWidth(0)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_yes)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.button_yes = QPushButton(self.frame_yes)
        self.button_yes.setObjectName(u"button_yes")

        self.horizontalLayout_2.addWidget(self.button_yes)

        self.frame_no = QFrame(self.centralwidget)
        self.frame_no.setObjectName(u"frame_no")
        self.frame_no.setGeometry(QRect(250, 190, 141, 81))
        self.frame_no.setLayoutDirection(Qt.LeftToRight)
        self.frame_no.setFrameShape(QFrame.NoFrame)
        self.frame_no.setFrameShadow(QFrame.Raised)
        self.frame_no.setMidLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame_no)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.button_no = QPushButton(self.frame_no)
        self.button_no.setObjectName(u"button_no")

        self.horizontalLayout.addWidget(self.button_no)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 110, 281, 241))
        self.label_2.setPixmap(QPixmap(u":/images/coracao.png"))
        self.label_2.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quer Namorar Comigo?", None))
        self.button_yes.setText(QCoreApplication.translate("MainWindow", u"Sim", None))
        self.button_no.setText(QCoreApplication.translate("MainWindow", u"N\u00e3o", None))
        self.label_2.setText("")
    # retranslateUi

