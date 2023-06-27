# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditarPropietario.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditarPropietario(QMainWindow, object):
    def setupUi(self, EditarPropietario):
        if not EditarPropietario.objectName():
            EditarPropietario.setObjectName(u"EditarPropietario")
        EditarPropietario.resize(700, 500)
        EditarPropietario.setMinimumSize(QSize(700, 500))
        EditarPropietario.setMaximumSize(QSize(700, 500))
        icon = QIcon()
        icon.addFile(u"./ui/assets/icons/LOGO.svg", QSize(), QIcon.Normal, QIcon.Off)
        EditarPropietario.setWindowIcon(icon)
        EditarPropietario.setStyleSheet(u"QMainWindow{\n"
"background:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}\n"
"\n"
"QLineEdit,QComboBox{\n"
"border:1px solid rgba(0,0,0,0);\n"
"background-color: rgb(216, 216, 216);\n"
"border-radius:10px;\n"
"border-bottom-color:rgba(255,255,255,255);\n"
"color:rgb(0,0,0);\n"
"font: 75 10pt \"MS Shell Dlg 2\";\n"
"padding:7px;\n"
"}\n"
"\n"
"QLabel{\n"
"color:white;\n"
"}")
        self.centralwidget = QWidget(EditarPropietario)
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
        self.widget_3.setMinimumSize(QSize(0, 345))
        self.widget_3.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_3)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(69, -1, 100, -1)
        self.telefono_propietario_txt = QLineEdit(self.widget_3)
        self.telefono_propietario_txt.setObjectName(u"telefono_propietario_txt")
        font1 = QFont()
        font1.setPointSize(12)
        self.telefono_propietario_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.telefono_propietario_txt, 2, 2, 1, 1)

        self.correo_propietario_txt = QLineEdit(self.widget_3)
        self.correo_propietario_txt.setObjectName(u"correo_propietario_txt")
        self.correo_propietario_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.correo_propietario_txt, 3, 2, 1, 1)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)

        self.nombre_propietario_txt = QLineEdit(self.widget_3)
        self.nombre_propietario_txt.setObjectName(u"nombre_propietario_txt")
        self.nombre_propietario_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.nombre_propietario_txt, 0, 2, 1, 1)

        self.label_5 = QLabel(self.widget_3)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.gridLayout_3.addWidget(self.label_5, 2, 0, 1, 1)

        self.label_8 = QLabel(self.widget_3)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.gridLayout_3.addWidget(self.label_8, 4, 0, 1, 1)

        self.label_6 = QLabel(self.widget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.gridLayout_3.addWidget(self.label_6, 3, 0, 1, 1)

        self.apellido_propietario_txt = QLineEdit(self.widget_3)
        self.apellido_propietario_txt.setObjectName(u"apellido_propietario_txt")
        self.apellido_propietario_txt.setFont(font1)

        self.gridLayout_3.addWidget(self.apellido_propietario_txt, 1, 2, 1, 1)

        self.editar_rol_cmbx = QComboBox(self.widget_3)
        self.editar_rol_cmbx.addItem('')
        self.editar_rol_cmbx.addItem('')
        self.editar_rol_cmbx.addItem('')
        self.editar_rol_cmbx.setObjectName(u"editar_rol_cmbx")

        self.gridLayout_3.addWidget(self.editar_rol_cmbx, 4, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_4.sizePolicy().hasHeightForWidth())
        self.widget_4.setSizePolicy(sizePolicy)
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

        EditarPropietario.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditarPropietario)

        QMetaObject.connectSlotsByName(EditarPropietario)
    # setupUi

    def retranslateUi(self, EditarPropietario):
        EditarPropietario.setWindowTitle(QCoreApplication.translate("EditarPropietario", u"Editar propietario", None))
        self.label.setText(QCoreApplication.translate("EditarPropietario", u"Modificar Propietario o Administrador", None))
        self.label_4.setText(QCoreApplication.translate("EditarPropietario", u"Apellidos", None))
        self.label_3.setText(QCoreApplication.translate("EditarPropietario", u"Nombre", None))
        self.label_5.setText(QCoreApplication.translate("EditarPropietario", u"Tel\u00e9fono", None))
        self.label_8.setText(QCoreApplication.translate("EditarPropietario", u"Rol", None))
        self.label_6.setText(QCoreApplication.translate("EditarPropietario", u"Correo", None))
        self.cancelar_admin_btn.setText(QCoreApplication.translate("EditarPropietario", u"Cancelar", None))
        self.agregar_admin_btn.setText(QCoreApplication.translate("EditarPropietario", u"Modificar", None))

        self.editar_rol_cmbx.setItemText(0, QCoreApplication.translate("ActualizarPropietarios", u"Selecciona un rol", None))
        self.editar_rol_cmbx.setItemText(1, QCoreApplication.translate("ActualizarPropietarios", u"Administrador", None))
        self.editar_rol_cmbx.setItemText(2, QCoreApplication.translate("ActualizarPropietarios", u"Cliente", None))

    # retranslateUi

