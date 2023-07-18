# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import os


class Login(QMainWindow, object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(800, 800)
        Login.setMinimumSize(QSize(800, 800))
        Login.setMaximumSize(QSize(800, 800))

        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/LOGO.svg'
        )
        icon = QIcon(icon_path)
        Login.setWindowIcon(icon)

        Login.setStyleSheet(u"\n"
"QMainWindow#Login{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}")
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(100, 100, 100, 100)
        self.frame_superior = QFrame(self.frame)
        self.frame_superior.setObjectName(u"frame_superior")
        self.frame_superior.setFrameShape(QFrame.StyledPanel)
        self.frame_superior.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_superior)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_superior)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_superior)

        self.frame_body = QFrame(self.frame)
        self.frame_body.setObjectName(u"frame_body")
        self.frame_body.setStyleSheet(u"QLineEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"color:rgb(255,255,255);\n"
"padding-bottom:7px;\n"
"}\n"
"")
        self.frame_body.setFrameShape(QFrame.StyledPanel)
        self.frame_body.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_body)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.frame_body)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(0, 80))
        self.label_2.setMaximumSize(QSize(16777215, 80))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        self.correo_txt = QLineEdit(self.frame_body)
        self.correo_txt.setObjectName(u"correo_txt")
        self.correo_txt.setMinimumSize(QSize(400, 0))
        self.correo_txt.setMaximumSize(QSize(300, 16777215))
        font = QFont()
        font.setPointSize(10)
        self.correo_txt.setFont(font)

        self.verticalLayout.addWidget(self.correo_txt)

        self.label_3 = QLabel(self.frame_body)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(0, 80))
        self.label_3.setMaximumSize(QSize(16777215, 80))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_3)

        self.password_txt = QLineEdit(self.frame_body)
        self.password_txt.setObjectName(u"password_txt")
        self.password_txt.setMinimumSize(QSize(400, 0))
        self.password_txt.setMaximumSize(QSize(300, 16777215))
        self.password_txt.setFont(font)
        self.password_txt.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_txt)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_body, 0, Qt.AlignHCenter)

        self.frame_inferior = QFrame(self.frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
        self.frame_inferior.setStyleSheet(u"QPushButton#recuperar_contrasenia_btn{\n"
"color:white;\n"
"background-color:transparent;\n"
"}\n"
"QPushButton#recuperar_contrasenia_btn:hover{\n"
"color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton#ingresar_btn{\n"
"border:none;\n"
"color: rgb(0,0,0);\n"
"background-color: #D2CFCC ;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#ingresar_btn:hover { \n"
"	background-color: rgb(149, 149, 149);\n"
"}\n"
"\n"
"QPushButton#ingresar_btn:pressed { \n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"	background-color: rgb(149, 149, 149);\n"
"}\n"
"\n"
"")
        self.frame_inferior.setFrameShape(QFrame.StyledPanel)
        self.frame_inferior.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.frame_inferior)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ingresar_btn = QPushButton(self.frame_inferior)
        self.ingresar_btn.setObjectName(u"ingresar_btn")
        self.ingresar_btn.setMinimumSize(QSize(0, 40))
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(10)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.ingresar_btn.setFont(font1)
        self.ingresar_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.ingresar_btn)

        self.label_4 = QLabel(self.frame_inferior)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))

        self.verticalLayout_2.addWidget(self.label_4)

        self.recuperar_contrasenia_btn = QPushButton(self.frame_inferior)
        self.recuperar_contrasenia_btn.setObjectName(u"recuperar_contrasenia_btn")
        self.recuperar_contrasenia_btn.setStyleSheet(u"")

        self.verticalLayout_2.addWidget(self.recuperar_contrasenia_btn)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_inferior, 0, Qt.AlignHCenter)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Login.setCentralWidget(self.centralwidget)

        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Login", None))
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:20pt; font-weight:600; color:#ffffff;\">INICIAR SESI\u00d3N</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Correo</span></p></body></html>", None))
        self.correo_txt.setPlaceholderText(QCoreApplication.translate("Login", u"Correo", None))
        self.label_3.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt; color:#ffffff;\">Contrase\u00f1a</span></p></body></html>", None))
        self.password_txt.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.ingresar_btn.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.label_4.setText("")
        self.recuperar_contrasenia_btn.setText(QCoreApplication.translate("Login", u"Se me olvido la contrase\u00f1a", None))
    # retranslateUi

