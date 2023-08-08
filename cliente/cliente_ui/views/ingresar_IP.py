# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ingresar_IPXQajpF.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class MainWindow(QMainWindow, object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(500, 600)
        MainWindow.setMinimumSize(QSize(500, 600))
        MainWindow.setMaximumSize(QSize(500, 600))
        MainWindow.setStyleSheet(u"QMainWindow{\n"
"background-color:rgb(231, 231, 231);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QLabel{\n"
"	font: 75 20pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"	background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2B3034, stop: 1 #1C4968);\n"
"	border-bottom-color:1px solid #ffffff;\n"
"	color: #ffffff;\n"
"	padding-bottom:7px;\n"
"	font: 14pt \"MS Shell Dlg 2\";\n"
"	padding:5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"padding:5px;\n"
"border-radius:10px;\n"
"border:1px solid white;\n"
"color:white;\n"
"margin-right:5px;\n"
"background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1, stop: 0 #2B3034, stop: 1 #1C4968);}\n"
"QPushButton:hover{\n"
"background: qlineargradient(x1:0, y1:0, x2:1 y2:1, stop:0 #251F9B, stop:1 #01A6E1);\n"
"}")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(50, -1, 50, -1)
        self.ip_txt = QLineEdit(self.frame_2)
        self.ip_txt.setObjectName(u"ip_txt")

        self.verticalLayout_4.addWidget(self.ip_txt)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(150, -1, 150, -1)
        self.ingresar_ip_btn = QPushButton(self.frame_3)
        self.ingresar_ip_btn.setObjectName(u"ingresar_ip_btn")

        self.verticalLayout_5.addWidget(self.ingresar_ip_btn)


        self.verticalLayout.addWidget(self.frame_3)


        self.verticalLayout_2.addWidget(self.widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ingreso de la IP", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Ingresa la IP", None))
        self.ingresar_ip_btn.setText(QCoreApplication.translate("MainWindow", u"Ingresar", None))
    # retranslateUi

