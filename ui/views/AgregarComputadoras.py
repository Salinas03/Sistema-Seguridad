# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarComputadoras.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AgregarComputadoras(QMainWindow, object):
    def setupUi(self, AgregarComputadoras):
        if not AgregarComputadoras.objectName():
            AgregarComputadoras.setObjectName(u"AgregarComputadoras")
        AgregarComputadoras.resize(700, 500)
        AgregarComputadoras.setMinimumSize(QSize(700, 500))
        AgregarComputadoras.setMaximumSize(QSize(700, 500))
        self.centralwidget = QWidget(AgregarComputadoras)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(16777215, 40))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.frame_3)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)

        self.persona_cargo_txt = QLineEdit(self.frame_2)
        self.persona_cargo_txt.setObjectName(u"persona_cargo_txt")
        font2 = QFont()
        font2.setPointSize(12)
        self.persona_cargo_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.persona_cargo_txt, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.computadora_txt = QLineEdit(self.frame_2)
        self.computadora_txt.setObjectName(u"computadora_txt")
        self.computadora_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.computadora_txt, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.dia_txt = QLineEdit(self.frame_2)
        self.dia_txt.setObjectName(u"dia_txt")
        self.dia_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.dia_txt, 2, 1, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 50))
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)

        self.ip_txt = QLineEdit(self.frame_2)
        self.ip_txt.setObjectName(u"ip_txt")
        self.ip_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.ip_txt, 3, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_4 = QFrame(self.frame)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_4)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelar_registro_btn = QPushButton(self.frame_4)
        self.cancelar_registro_btn.setObjectName(u"cancelar_registro_btn")

        self.horizontalLayout.addWidget(self.cancelar_registro_btn)

        self.guardar_compu_btn = QPushButton(self.frame_4)
        self.guardar_compu_btn.setObjectName(u"guardar_compu_btn")

        self.horizontalLayout.addWidget(self.guardar_compu_btn)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        AgregarComputadoras.setCentralWidget(self.centralwidget)

        self.retranslateUi(AgregarComputadoras)

        QMetaObject.connectSlotsByName(AgregarComputadoras)
    # setupUi

    def retranslateUi(self, AgregarComputadoras):
        AgregarComputadoras.setWindowTitle(QCoreApplication.translate("AgregarComputadoras", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AgregarComputadoras", u"Agregar Computadoras", None))
        self.label_10.setText(QCoreApplication.translate("AgregarComputadoras", u"Persona a cargo", None))
        self.persona_cargo_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"Nombre de la persona que va a estar a cargo de la computadora", None))
        self.label_11.setText(QCoreApplication.translate("AgregarComputadoras", u"Computadora", None))
        self.computadora_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"Nombre de la computadora - Modelo", None))
        self.label_12.setText(QCoreApplication.translate("AgregarComputadoras", u"D\u00eda de entrega", None))
        self.dia_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"dd-mm-yyyy", None))
        self.label_13.setText(QCoreApplication.translate("AgregarComputadoras", u"MAC ADDRESS", None))
        self.ip_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"0.0.0.0", None))
        self.cancelar_registro_btn.setText(QCoreApplication.translate("AgregarComputadoras", u"Cancelar", None))
        self.guardar_compu_btn.setText(QCoreApplication.translate("AgregarComputadoras", u"Aceptar", None))
    # retranslateUi

