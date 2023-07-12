# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Carga.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Carga(QMainWindow, object):
    def setupUi(self, Carga):
        if not Carga.objectName():
            Carga.setObjectName(u"Carga")
        Carga.resize(500, 200)
        Carga.setMaximumSize(QSize(500, 200))
        Carga.setStyleSheet(u"QWidget#fondo_widget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius:10px;\n"
"}\n"
"\n"
"QProgressBar{\n"
"	background-color:rgb(200,200,200);\n"
"	color:rgb(0,0,0);\n"
"	border-style:solid;\n"
"	border-radius:10px;\n"
"	text-align:center;\n"
"}\n"
"\n"
"QProgressBar::chunk{\n"
"	border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(43, 48, 52, 255), stop:1 rgba(212, 212, 212, 255));\n"
"}")
        self.centralwidget = QWidget(Carga)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.fondo_widget = QWidget(self.centralwidget)
        self.fondo_widget.setObjectName(u"fondo_widget")
        self.verticalLayout = QVBoxLayout(self.fondo_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(11, -1, -1, -1)
        self.label = QLabel(self.fondo_widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.progressBar = QProgressBar(self.fondo_widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)


        self.gridLayout.addWidget(self.fondo_widget, 0, 0, 1, 1)

        Carga.setCentralWidget(self.centralwidget)

        self.retranslateUi(Carga)

        QMetaObject.connectSlotsByName(Carga)
    # setupUi

    def retranslateUi(self, Carga):
        Carga.setWindowTitle(QCoreApplication.translate("Carga", u"Carga", None))
        self.label.setText(QCoreApplication.translate("Carga", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600;\">Cargando...</span></p></body></html>", None))
    # retranslateUi

