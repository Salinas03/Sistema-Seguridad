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


class Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(800, 800)
        Login.setMinimumSize(QSize(800, 800))
        Login.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(Login)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(11, 11, 791, 781))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
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

        self.verticalLayout.addWidget(self.correo_txt)

        self.correoF_lbl = QLabel(self.frame_body)
        self.correoF_lbl.setObjectName(u"correoF_lbl")
        self.correoF_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.correoF_lbl)

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
        self.password_txt.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_txt)

        self.passwordF_lbl = QLabel(self.frame_body)
        self.passwordF_lbl.setObjectName(u"passwordF_lbl")
        self.passwordF_lbl.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.passwordF_lbl)


        self.gridLayout_3.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_body, 0, Qt.AlignHCenter)

        self.frame_inferior = QFrame(self.frame)
        self.frame_inferior.setObjectName(u"frame_inferior")
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

        self.verticalLayout_2.addWidget(self.ingresar_btn)

        self.pushButton_2 = QPushButton(self.frame_inferior)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"background-color:transparent;")

        self.verticalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout_4.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.verticalLayout_3.addWidget(self.frame_inferior, 0, Qt.AlignHCenter)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:20pt;\">INICIAR SESI\u00d3N</span></p></body></html>", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt;\">Correo</span></p></body></html>", None))
        self.correo_txt.setPlaceholderText(QCoreApplication.translate("Login", u"Correo", None))
        self.correoF_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("Login", u"<html><head/><body><p><span style=\" font-size:14pt;\">Contrase\u00f1a</span></p></body></html>", None))
        self.password_txt.setPlaceholderText(QCoreApplication.translate("Login", u"Contrase\u00f1a", None))
        self.passwordF_lbl.setText("")
        self.ingresar_btn.setText(QCoreApplication.translate("Login", u"Ingresar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Se me olvido la contrase\u00f1a", None))
    # retranslateUi

