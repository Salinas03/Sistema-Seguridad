# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RecuperaPassword.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class RecuperarContrasenia(QMainWindow, object):
    def setupUi(self, RecuperarContrasenia):
        if not RecuperarContrasenia.objectName():
            RecuperarContrasenia.setObjectName(u"RecuperarContrasenia")
        RecuperarContrasenia.resize(600, 600)
        RecuperarContrasenia.setMinimumSize(QSize(600, 600))
        RecuperarContrasenia.setMaximumSize(QSize(600, 600))
        RecuperarContrasenia.setStyleSheet(u"QPushButton#cambiar_password_btn,#recuperacion_codigo_btn,#recuperacion_btn{\n"
"    text-decoration: none;\n"
"    width:50%;\n"
"    padding:10px;\n"
"    border: 1px solid black;\n"
"    border-radius:10px;\n"
"    text-decoration: none;\n"
"    color:black;\n"
"    font-weight: bold;\n"
"    text-align: center;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton#cambiar_password_btn:hover,#recuperacion_codigo_btn:hover,#recuperacion_btn:hover{\n"
"    background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);;\n"
"    color:white;\n"
"}\n"
"\n"
"QPushButton#regresar_btn,#regresar_2_btn{\n"
"border:none;\n"
"padding:5px;\n"
"background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);;\n"
"}\n"
"\n"
"QPushButton#regresar_btn:hover,#regresar_2_btn:hover{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QLabel{\n"
"margin:20px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border:1px solid rgba(0,0,0,0);\n"
"background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B303"
                        "4, stop:1 #1C4968);\n"
"border-radius:10px;\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"color:rgb(255,255,255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding:7px;\n"
"}")
        self.centralwidget = QWidget(RecuperarContrasenia)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ingresa_correo_widget = QWidget(self.frame)
        self.ingresa_correo_widget.setObjectName(u"ingresa_correo_widget")
        self.ingresa_correo_widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.ingresa_correo_widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalSpacer = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.recuperacion_btn = QPushButton(self.ingresa_correo_widget)
        self.recuperacion_btn.setObjectName(u"recuperacion_btn")

        self.gridLayout_2.addWidget(self.recuperacion_btn, 4, 1, 1, 1)

        self.label = QLabel(self.ingresa_correo_widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 3, 1, 1, 1)

        self.correo_recuperacion_txt = QLineEdit(self.ingresa_correo_widget)
        self.correo_recuperacion_txt.setObjectName(u"correo_recuperacion_txt")
        self.correo_recuperacion_txt.setMinimumSize(QSize(330, 0))

        self.gridLayout_2.addWidget(self.correo_recuperacion_txt, 2, 1, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_4, 0, 1, 1, 1)


        self.verticalLayout.addWidget(self.ingresa_correo_widget)

        self.confirma_codigo_widget = QWidget(self.frame)
        self.confirma_codigo_widget.setObjectName(u"confirma_codigo_widget")
        self.confirma_codigo_widget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.confirma_codigo_widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.codigo_recuperacion_txt = QLineEdit(self.confirma_codigo_widget)
        self.codigo_recuperacion_txt.setObjectName(u"codigo_recuperacion_txt")

        self.gridLayout_3.addWidget(self.codigo_recuperacion_txt, 2, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_2, 3, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(175, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_3, 2, 0, 1, 1)

        self.recuperacion_codigo_btn = QPushButton(self.confirma_codigo_widget)
        self.recuperacion_codigo_btn.setObjectName(u"recuperacion_codigo_btn")

        self.gridLayout_3.addWidget(self.recuperacion_codigo_btn, 4, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(175, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_3.addItem(self.horizontalSpacer_4, 2, 2, 1, 1)

        self.label_2 = QLabel(self.confirma_codigo_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.label_2, 1, 1, 1, 1)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_3.addItem(self.verticalSpacer_5, 0, 1, 1, 1)

        self.regresar_btn = QPushButton(self.confirma_codigo_widget)
        self.regresar_btn.setObjectName(u"regresar_btn")
        self.regresar_btn.setMaximumSize(QSize(30, 16777215))
        icon = QIcon()
        icon.addFile(u"./ui/assets/icons/arrow-2.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.regresar_btn.setIcon(icon)

        self.gridLayout_3.addWidget(self.regresar_btn, 4, 0, 1, 1)


        self.verticalLayout.addWidget(self.confirma_codigo_widget)

        self.cambio_password_widget = QWidget(self.frame)
        self.cambio_password_widget.setObjectName(u"cambio_password_widget")
        self.cambio_password_widget.setStyleSheet(u"")
        self.gridLayout_4 = QGridLayout(self.cambio_password_widget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_3 = QLabel(self.cambio_password_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_3, 1, 1, 1, 1)

        self.nuevo_password_txt = QLineEdit(self.cambio_password_widget)
        self.nuevo_password_txt.setObjectName(u"nuevo_password_txt")

        self.gridLayout_4.addWidget(self.nuevo_password_txt, 2, 1, 1, 1)

        self.confirmar_nuevo_password_txt = QLineEdit(self.cambio_password_widget)
        self.confirmar_nuevo_password_txt.setObjectName(u"confirmar_nuevo_password_txt")

        self.gridLayout_4.addWidget(self.confirmar_nuevo_password_txt, 4, 1, 1, 1)

        self.horizontalSpacer_5 = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_5, 2, 0, 1, 1)

        self.cambiar_password_btn = QPushButton(self.cambio_password_widget)
        self.cambiar_password_btn.setObjectName(u"cambiar_password_btn")

        self.gridLayout_4.addWidget(self.cambiar_password_btn, 6, 1, 1, 1)

        self.label_4 = QLabel(self.cambio_password_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.label_4, 3, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 5, 1, 1, 1)

        self.horizontalSpacer_6 = QSpacerItem(177, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_4.addItem(self.horizontalSpacer_6, 2, 2, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_6, 0, 1, 1, 1)

        self.regresar_2_btn = QPushButton(self.cambio_password_widget)
        self.regresar_2_btn.setObjectName(u"regresar_2_btn")
        self.regresar_2_btn.setMaximumSize(QSize(30, 16777215))
        self.regresar_2_btn.setIcon(icon)

        self.gridLayout_4.addWidget(self.regresar_2_btn, 6, 0, 1, 1)


        self.verticalLayout.addWidget(self.cambio_password_widget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        RecuperarContrasenia.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(RecuperarContrasenia)
        self.statusBar.setObjectName(u"statusBar")
        RecuperarContrasenia.setStatusBar(self.statusBar)

        self.retranslateUi(RecuperarContrasenia)

        QMetaObject.connectSlotsByName(RecuperarContrasenia)
    # setupUi

    def retranslateUi(self, RecuperarContrasenia):
        RecuperarContrasenia.setWindowTitle(QCoreApplication.translate("RecuperarContrasenia", u"Recuperar Contrase\u00f1a", None))
        self.recuperacion_btn.setText(QCoreApplication.translate("RecuperarContrasenia", u"Siguiente", None))
        self.label.setText(QCoreApplication.translate("RecuperarContrasenia", u"Ingresa tu correo ", None))
        self.recuperacion_codigo_btn.setText(QCoreApplication.translate("RecuperarContrasenia", u"Recuperar", None))
        self.label_2.setText(QCoreApplication.translate("RecuperarContrasenia", u"Ingresa el c\u00f3digo de verficiaci\u00f3n", None))
        self.regresar_btn.setText("")
        self.label_3.setText(QCoreApplication.translate("RecuperarContrasenia", u"Ingresa la contrase\u00f1a", None))
        self.cambiar_password_btn.setText(QCoreApplication.translate("RecuperarContrasenia", u"Cambiar", None))
        self.label_4.setText(QCoreApplication.translate("RecuperarContrasenia", u"Confirma la contrase\u00f1a", None))
        self.regresar_2_btn.setText("")
    # retranslateUi

