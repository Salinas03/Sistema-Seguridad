# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AgregarAdmin.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class AgregarAdmin(QMainWindow, object):
    def setupUi(self, AgregarAdmin):
        if not AgregarAdmin.objectName():
            AgregarAdmin.setObjectName(u"AgregarAdmin")
        AgregarAdmin.resize(700, 500)
        AgregarAdmin.setMinimumSize(QSize(700, 500))
        AgregarAdmin.setMaximumSize(QSize(700, 500))
        self.centralwidget = QWidget(AgregarAdmin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 180))
        self.widget.setStyleSheet(u"")
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 80))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_2)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 50))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame = QFrame(self.widget)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(16777215, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.widget_3 = QWidget(self.widget_2)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(69, -1, 100, -1)
        self.telefono_admin_txt = QLineEdit(self.widget_3)
        self.telefono_admin_txt.setObjectName(u"telefono_admin_txt")
        font1 = QFont()
        font1.setPointSize(12)
        self.telefono_admin_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.telefono_admin_txt, 2, 2, 1, 1)

        self.apellido_admin_txt = QLineEdit(self.widget_3)
        self.apellido_admin_txt.setObjectName(u"apellido_admin_txt")
        self.apellido_admin_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.apellido_admin_txt, 1, 2, 1, 1)

        self.password_admin_txt = QLineEdit(self.widget_3)
        self.password_admin_txt.setObjectName(u"password_admin_txt")
        self.password_admin_txt.setFont(font1)
        self.password_admin_txt.setEchoMode(QLineEdit.Password)

        self.gridLayout_3.addWidget(self.password_admin_txt, 4, 2, 1, 1)

        self.nombre_admin_txt = QLineEdit(self.widget_3)
        self.nombre_admin_txt.setObjectName(u"nombre_admin_txt")
        self.nombre_admin_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.nombre_admin_txt, 0, 2, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.correo_admin_txt = QLineEdit(self.widget_3)
        self.correo_admin_txt.setObjectName(u"correo_admin_txt")
        self.correo_admin_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.correo_admin_txt, 3, 2, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 4, 0, 1, 1)

        self.confirma_contrasenia_btn = QLineEdit(self.widget_3)
        self.confirma_contrasenia_btn.setObjectName(u"confirma_contrasenia_btn")
        self.confirma_contrasenia_btn.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.gridLayout_3.addWidget(self.confirma_contrasenia_btn, 5, 2, 1, 1)

        self.label_7 = QLabel(self.widget_3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(0, 30))
        self.label_7.setFont(font1)

        self.gridLayout_3.addWidget(self.label_7, 5, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setMinimumSize(QSize(0, 150))
        self.widget_4.setMaximumSize(QSize(16777215, 150))
        self.widget_4.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.widget_4)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 90, 10, 0)
        self.cancelar_admin_btn = QPushButton(self.widget_4)
        self.cancelar_admin_btn.setObjectName(u"cancelar_admin_btn")

        self.horizontalLayout.addWidget(self.cancelar_admin_btn)

        self.agregar_admin_btn = QPushButton(self.widget_4)
        self.agregar_admin_btn.setObjectName(u"agregar_admin_btn")

        self.horizontalLayout.addWidget(self.agregar_admin_btn)


        self.verticalLayout_3.addWidget(self.widget_4, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.widget_2)

        AgregarAdmin.setCentralWidget(self.centralwidget)

        self.retranslateUi(AgregarAdmin)

        QMetaObject.connectSlotsByName(AgregarAdmin)
    # setupUi

    def retranslateUi(self, AgregarAdmin):
        AgregarAdmin.setWindowTitle(QCoreApplication.translate("AgregarAdmin", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("AgregarAdmin", u"Agregar Administrador", None))
        self.label_2.setText(QCoreApplication.translate("AgregarAdmin", u"<html><head/><body><p><span style=\" font-size:10pt; font-weight:600; color:#ff0000;\">ADVERTENCIA</span><span style=\" font-size:10pt;\">: Si agregar a un administrador, debes de saber que el tambien tendra </span></p><p><span style=\" font-size:10pt;\">acceso a las computadoras que se hayan registrado, esto para el acceso remoto</span></p><p><span style=\" font-size:10pt;\">a ellas.</span></p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("AgregarAdmin", u"Nombre", None))
        self.label_6.setText(QCoreApplication.translate("AgregarAdmin", u"Correo", None))
        self.label_4.setText(QCoreApplication.translate("AgregarAdmin", u"Apellidos", None))
        self.label_5.setText(QCoreApplication.translate("AgregarAdmin", u"Tel\u00e9fono", None))
        self.label_11.setText(QCoreApplication.translate("AgregarAdmin", u"Contrase\u00f1a", None))
        self.label_7.setText(QCoreApplication.translate("AgregarAdmin", u"Confirma Contrase\u00f1a", None))
        self.cancelar_admin_btn.setText(QCoreApplication.translate("AgregarAdmin", u"Cancelar", None))
        self.agregar_admin_btn.setText(QCoreApplication.translate("AgregarAdmin", u"Agregar", None))
    # retranslateUi

