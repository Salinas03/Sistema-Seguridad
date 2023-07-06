# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mapa.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Mapa(QMainWindow, object):
    def setupUi(self, Mapa):
        if not Mapa.objectName():
            Mapa.setObjectName(u"Mapa")
        Mapa.resize(800, 628)
        self.centralwidget = QWidget(Mapa)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")

        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        Mapa.setCentralWidget(self.centralwidget)

        self.retranslateUi(Mapa)

        QMetaObject.connectSlotsByName(Mapa)
    # setupUi

    def retranslateUi(self, Mapa):
        Mapa.setWindowTitle(QCoreApplication.translate("Mapa", u"Mapa", None))
    # retranslateUi

