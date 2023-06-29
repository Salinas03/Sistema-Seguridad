# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'VerificarCorreo.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class VerificarCorreo(QMainWindow, object):
    def setupUi(self, VerificarCorreo):
        if not VerificarCorreo.objectName():
            VerificarCorreo.setObjectName(u"VerificarCorreo")
        VerificarCorreo.resize(400, 400)
        VerificarCorreo.setMinimumSize(QSize(400, 400))
        VerificarCorreo.setMaximumSize(QSize(400, 400))
        self.centralwidget = QWidget(VerificarCorreo)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.gridLayout_2 = QGridLayout(self.widget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer_3 = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label, 1, 1, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 82, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 2, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 3, 0, 1, 1)

        self.codigo_verificacion_txt = QLineEdit(self.widget)
        self.codigo_verificacion_txt.setObjectName(u"codigo_verificacion_txt")
        self.codigo_verificacion_txt.setMaximumSize(QSize(200, 16777215))

        self.gridLayout_2.addWidget(self.codigo_verificacion_txt, 3, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 3, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 81, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 4, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 5, 0, 1, 1)

        self.verificar_btn = QPushButton(self.widget)
        self.verificar_btn.setObjectName(u"verificar_btn")

        self.gridLayout_2.addWidget(self.verificar_btn, 5, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(79, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 5, 2, 1, 1)


        self.gridLayout.addWidget(self.widget, 0, 0, 1, 1)

        VerificarCorreo.setCentralWidget(self.centralwidget)

        self.retranslateUi(VerificarCorreo)

        QMetaObject.connectSlotsByName(VerificarCorreo)
    # setupUi

    def retranslateUi(self, VerificarCorreo):
        VerificarCorreo.setWindowTitle(QCoreApplication.translate("VerificarCorreo", u"VerificacionCorreo", None))
        self.label.setText(QCoreApplication.translate("VerificarCorreo", u"Ingresa el c\u00f3digo de verifiaci\u00f3n", None))
        self.verificar_btn.setText(QCoreApplication.translate("VerificarCorreo", u"Verificar", None))
    # retranslateUi

