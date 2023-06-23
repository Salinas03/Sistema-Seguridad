# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditarEquipo.ui'
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


class EditarComputadoras(QMainWindow, object):
    def setupUi(self, EditarComputadoras):
        if not EditarComputadoras.objectName():
            EditarComputadoras.setObjectName(u"EditarComputadoras")

        self.peticion_propietarios = {
            'tabla': 'propietarios',
            'operacion': 'obtener_propietarios'
        }

        self.propietarios = admin_socket_ui.escribir_operaciones(json.dumps(self.peticion_propietarios))

        EditarComputadoras.resize(700, 500)
        EditarComputadoras.setMinimumSize(QSize(700, 500))
        EditarComputadoras.setMaximumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u"./ui/assets/icons/LOGO.svg", QSize(), QIcon.Normal, QIcon.Off)
        EditarComputadoras.setWindowIcon(icon)
        self.centralwidget = QWidget(EditarComputadoras)
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

        self.nombre_equipo_txt = QLineEdit(self.frame_2)
        self.nombre_equipo_txt.setObjectName(u"nombre_equipo_txt")
        font2 = QFont()
        font2.setPointSize(12)
        self.nombre_equipo_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.nombre_equipo_txt, 0, 1, 1, 1)

        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setFont(font1)

        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)

        self.num_serie_txt = QLineEdit(self.frame_2)
        self.num_serie_txt.setObjectName(u"num_serie_txt")
        self.num_serie_txt.setFont(font2)

        self.gridLayout_3.addWidget(self.num_serie_txt, 1, 1, 1, 1)

        self.label_12 = QLabel(self.frame_2)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setFont(font1)

        self.gridLayout_3.addWidget(self.label_12, 2, 0, 1, 1)

        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 50))
        self.label_13.setFont(font1)

        self.gridLayout_3.addWidget(self.label_13, 3, 0, 1, 1)

        self.edita_propietario_cmbx = QComboBox(self.frame_2)
        self.edita_propietario_cmbx.setObjectName(u"edita_propietario_cmbx")
        self.edita_propietario_cmbx.addItem('')
        if self.propietarios['success']:
            for _ in range(len(self.propietarios['data'])):
                self.edita_propietario_cmbx.addItem("")

        self.gridLayout_3.addWidget(self.edita_propietario_cmbx, 2, 1, 1, 1)

        #Combobox de ROL
        self.edita_rol_cmbx = QComboBox(self.frame_2)
        self.edita_rol_cmbx.setObjectName(u"edita_rol_cmbx")
        self.edita_rol_cmbx.addItem('')
        self.edita_rol_cmbx.addItem('')
        self.edita_rol_cmbx.addItem('')

        self.gridLayout_3.addWidget(self.edita_rol_cmbx, 3, 1, 1, 1)


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

        self.modificar_compu_btn = QPushButton(self.frame_4)
        self.modificar_compu_btn.setObjectName(u"modificar_compu_btn")

        self.horizontalLayout.addWidget(self.modificar_compu_btn)


        self.verticalLayout.addWidget(self.frame_4, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        EditarComputadoras.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditarComputadoras)

        QMetaObject.connectSlotsByName(EditarComputadoras)
    # setupUi

    def retranslateUi(self, EditarComputadoras):
        EditarComputadoras.setWindowTitle(QCoreApplication.translate("EditarComputadoras", u"Editar equipo de computo", None))
        self.label.setText(QCoreApplication.translate("EditarComputadoras", u"Editar Computadoras", None))
        self.label_10.setText(QCoreApplication.translate("EditarComputadoras", u"Nombre del equipo", None))
        self.nombre_equipo_txt.setPlaceholderText(QCoreApplication.translate("EditarComputadoras", u"Nombre del equipo", None))
        self.label_11.setText(QCoreApplication.translate("EditarComputadoras", u"N\u00famero de serie", None))
        self.num_serie_txt.setPlaceholderText(QCoreApplication.translate("EditarComputadoras", u"N\u00famero de serie", None))
        self.label_12.setText(QCoreApplication.translate("EditarComputadoras", u"Propietario del equipo", None))
        self.label_13.setText(QCoreApplication.translate("EditarComputadoras", u"Rol", None))
        self.cancelar_registro_btn.setText(QCoreApplication.translate("EditarComputadoras", u"Cancelar", None))
        self.modificar_compu_btn.setText(QCoreApplication.translate("EditarComputadoras", u"Modificar", None))
        
        self.edita_propietario_cmbx.setItemText(0, QCoreApplication.translate('Seleccionar', u'Selecciona un rol', None))

         #Desplegar la información
        if self.propietarios['success']:
            propietarios = self.propietarios['data']
            for i, propietario in enumerate(propietarios): 
                self.edita_propietario_cmbx.setItemText(i+1, QCoreApplication.translate("AgregarComputadoras", f"{propietario[0]}.-{propietario[1]} [{propietario[4]}]", None))

        self.edita_rol_cmbx.setItemText(0, QCoreApplication.translate("Seleccionar", u"Selecciona un rol", None))
        self.edita_rol_cmbx.setItemText(1, QCoreApplication.translate("Cliente", u"Administrador", None))
        self.edita_rol_cmbx.setItemText(2, QCoreApplication.translate("Administrador", u"Cliente", None))
        # self.edita_rol_cmbx.setCurrentIndex(1)
    

