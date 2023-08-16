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
from clases.administrador_ui import admin_socket_ui
import json
import os

class AgregarComputadoras(QMainWindow, object):
    def setupUi(self, AgregarComputadoras):
        if not AgregarComputadoras.objectName():
            AgregarComputadoras.setObjectName(u"AgregarComputadoras")

                 
        self.peticion_propietarios = {
            'tabla': 'propietarios',
            'operacion': 'obtener_propietarios'
        }

        self.propietarios = admin_socket_ui.escribir_operaciones(json.dumps(self.peticion_propietarios))

        AgregarComputadoras.resize(700, 500)
        AgregarComputadoras.setMinimumSize(QSize(700, 500))
        AgregarComputadoras.setMaximumSize(QSize(700, 500))
        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/LOGO.svg'
        )
        icon = QIcon(icon_path)
        AgregarComputadoras.setWindowIcon(icon)
        AgregarComputadoras.setStyleSheet(u"QLineEdit,QComboBox{\n"
"border:1px solid rgba(0,0,0,0);\n"
"background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"border-radius:10px;\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"color:rgb(255,255,255);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding:7px;\n"
"}\n"
"\n"
"\n"
"QPushButton{\n"
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
"QPushButton:hover{\n"
"    background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);;\n"
"    color:white;\n"
"}")
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
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 50))
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 5, 0, 1, 1)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.propietario_cmbx = QComboBox(self.frame_2)
        self.propietario_cmbx.addItem("")
        if self.propietarios['success']:
            for _ in range(len(self.propietarios['data'])):
                self.propietario_cmbx.addItem("")
        self.propietario_cmbx.setObjectName(u"propietario_cmbx")

        self.gridLayout_3.addWidget(self.propietario_cmbx, 4, 1, 1, 1)

        self.label_10 = QLabel(self.frame_2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        self.label_10.setFont(font1)

        self.gridLayout_3.addWidget(self.label_10, 2, 0, 1, 1)

        self.rol_cmbx = QComboBox(self.frame_2)
        self.rol_cmbx.addItem("")
        self.rol_cmbx.addItem("")
        self.rol_cmbx.addItem("")
        self.rol_cmbx.setObjectName(u"rol_cmbx")

        self.gridLayout_3.addWidget(self.rol_cmbx, 5, 1, 1, 1)

        self.nombre_equipo_txt = QLineEdit(self.frame_2)
        self.nombre_equipo_txt.setObjectName(u"nombre_equipo_txt")
        font2 = QFont()
        font2.setFamily(u"MS Shell Dlg 2")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setWeight(9)
        self.nombre_equipo_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.nombre_equipo_txt, 2, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 3, 0, 1, 1)

        self.num_serie_txt = QLineEdit(self.frame_2)
        self.num_serie_txt.setObjectName(u"num_serie_txt")
        self.num_serie_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.num_serie_txt, 3, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 4, 0, 1, 1)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.area_equipo_txt = QLineEdit(self.frame_2)
        self.area_equipo_txt.setObjectName(u"area_equipo_txt")

        self.gridLayout_3.addWidget(self.area_equipo_txt, 0, 1, 1, 1)

        self.caracteristica_equipo_txt = QLineEdit(self.frame_2)
        self.caracteristica_equipo_txt.setObjectName(u"caracteristica_equipo_txt")

        self.gridLayout_3.addWidget(self.caracteristica_equipo_txt, 1, 1, 1, 1)


        self.verticalLayout.addWidget(self.frame_2)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

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
        AgregarComputadoras.setWindowTitle(QCoreApplication.translate("AgregarComputadoras", u"Agregar computadoras", None))
        self.label.setText(QCoreApplication.translate("AgregarComputadoras", u"Agregar Computadoras", None))
        self.label_13.setText(QCoreApplication.translate("AgregarComputadoras", u"Rol", None))
        self.label_3.setText(QCoreApplication.translate("AgregarComputadoras", u"\u00c1rea", None))
        self.propietario_cmbx.setItemText(0, QCoreApplication.translate("AgregarComputadoras", u"Selecciona Propietario", None))

        self.label_10.setText(QCoreApplication.translate("AgregarComputadoras", u"Nombre del equipo", None))
        self.rol_cmbx.setItemText(0, QCoreApplication.translate("AgregarComputadoras", u"Selecciona un rol", None))
        self.rol_cmbx.setItemText(1, QCoreApplication.translate("AgregarComputadoras", u"Administrador", None))
        self.rol_cmbx.setItemText(2, QCoreApplication.translate("AgregarComputadoras", u"Cliente", None))

        self.nombre_equipo_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"Nombre del equipo", None))
        self.label_11.setText(QCoreApplication.translate("AgregarComputadoras", u"N\u00famero de serie", None))
        self.num_serie_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"N\u00famero de serie", None))
        self.label_12.setText(QCoreApplication.translate("AgregarComputadoras", u"Propietario del equipo", None))
        self.label_4.setText(QCoreApplication.translate("AgregarComputadoras", u"Caracter\u00edstica", None))


        self.propietario_cmbx.setItemText(0, QCoreApplication.translate("AgregarComputadoras", u"Selecciona Propietario", None))
        #Desplegar la información
        if self.propietarios['success']:
            propietarios = self.propietarios['data']

            for i, propietario in enumerate(propietarios): 
                self.propietario_cmbx.setItemText(i+1, QCoreApplication.translate("AgregarComputadoras", f"{propietario[0]}.-{propietario[1]} [{propietario[4]}]", None))
    

        self.rol_cmbx.setItemText(0, QCoreApplication.translate("AgregarComputadoras", u"Selecciona un rol", None))
        self.rol_cmbx.setItemText(1, QCoreApplication.translate("AgregarComputadoras", u"Administrador", None))
        self.rol_cmbx.setItemText(2, QCoreApplication.translate("AgregarComputadoras", u"Cliente", None))
        self.area_equipo_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"\u00c1rea del equipo", None))
        self.caracteristica_equipo_txt.setPlaceholderText(QCoreApplication.translate("AgregarComputadoras", u"Caracter\u00edstia del equipo", None))
        self.label_2.setText(QCoreApplication.translate("AgregarComputadoras", u"<html><head/><body><p><br/></p></body></html>", None))
        self.cancelar_registro_btn.setText(QCoreApplication.translate("AgregarComputadoras", u"Cancelar", None))
        self.guardar_compu_btn.setText(QCoreApplication.translate("AgregarComputadoras", u"Aceptar", None))
    # retranslateUi

