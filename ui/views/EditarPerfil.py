# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EditarPerfil.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class EditarPerfil(QMainWindow, object):
    def setupUi(self, EditarPerfil):
        if not EditarPerfil.objectName():
            EditarPerfil.setObjectName(u"EditarPerfil")
        EditarPerfil.resize(800, 500)
        EditarPerfil.setMinimumSize(QSize(800, 500))
        EditarPerfil.setMaximumSize(QSize(800, 500))
        self.centralwidget = QWidget(EditarPerfil)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(50, -1, 50, -1)
        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label)

        self.nombre_perfil_editar_txt = QLineEdit(self.frame_2)
        self.nombre_perfil_editar_txt.setObjectName(u"nombre_perfil_editar_txt")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.nombre_perfil_editar_txt)

        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.label_2)

        self.apellidos_perfil_editar_txt = QLineEdit(self.frame_2)
        self.apellidos_perfil_editar_txt.setObjectName(u"apellidos_perfil_editar_txt")

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.apellidos_perfil_editar_txt)

        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.label_3)

        self.telefono_perfil_editar_txt = QLineEdit(self.frame_2)
        self.telefono_perfil_editar_txt.setObjectName(u"telefono_perfil_editar_txt")

        self.formLayout.setWidget(6, QFormLayout.FieldRole, self.telefono_perfil_editar_txt)

        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.label_4)

        self.correo_perfil_editar_txt = QLineEdit(self.frame_2)
        self.correo_perfil_editar_txt.setObjectName(u"correo_perfil_editar_txt")

        self.formLayout.setWidget(8, QFormLayout.FieldRole, self.correo_perfil_editar_txt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(3, QFormLayout.FieldRole, self.verticalSpacer)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(7, QFormLayout.FieldRole, self.verticalSpacer_3)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(9, QFormLayout.FieldRole, self.verticalSpacer_4)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(1, QFormLayout.FieldRole, self.verticalSpacer_5)

        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_5.setFont(font1)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.label_5)


        self.verticalLayout.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.cancelar_perfil_btn = QPushButton(self.frame_3)
        self.cancelar_perfil_btn.setObjectName(u"cancelar_perfil_btn")

        self.horizontalLayout.addWidget(self.cancelar_perfil_btn)

        self.Modificar_perfil_btn = QPushButton(self.frame_3)
        self.Modificar_perfil_btn.setObjectName(u"Modificar_perfil_btn")

        self.horizontalLayout.addWidget(self.Modificar_perfil_btn)


        self.verticalLayout.addWidget(self.frame_3, 0, Qt.AlignRight|Qt.AlignBottom)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        EditarPerfil.setCentralWidget(self.centralwidget)

        self.retranslateUi(EditarPerfil)

        QMetaObject.connectSlotsByName(EditarPerfil)
    # setupUi

    def retranslateUi(self, EditarPerfil):
        EditarPerfil.setWindowTitle(QCoreApplication.translate("EditarPerfil", u"Editar Perfil", None))
        self.label.setText(QCoreApplication.translate("EditarPerfil", u"Nombre", None))
        self.label_2.setText(QCoreApplication.translate("EditarPerfil", u"Apellidos", None))
        self.label_3.setText(QCoreApplication.translate("EditarPerfil", u"Tel\u00e9fono", None))
        self.label_4.setText(QCoreApplication.translate("EditarPerfil", u"Correo", None))
        self.label_5.setText(QCoreApplication.translate("EditarPerfil", u"Modificar perfil de administrador", None))
        self.cancelar_perfil_btn.setText(QCoreApplication.translate("EditarPerfil", u"Cancelar", None))
        self.Modificar_perfil_btn.setText(QCoreApplication.translate("EditarPerfil", u"Modificar", None))
    # retranslateUi

