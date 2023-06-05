# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OpcionesComputadoras.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class OpcionesComputadora(QMainWindow, object):
    def setupUi(self, OpcionesComputadora):
        if not OpcionesComputadora.objectName():
            OpcionesComputadora.setObjectName(u"OpcionesComputadora")
        OpcionesComputadora.resize(800, 600)
        OpcionesComputadora.setMinimumSize(QSize(800, 600))
        OpcionesComputadora.setMaximumSize(QSize(16777215, 600))
        self.centralwidget = QWidget(OpcionesComputadora)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QFrame#frame{\n"
"	background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(0)
        self.formLayout.setVerticalSpacing(0)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_2 = QSpacerItem(20, 196, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.LabelRole, self.verticalSpacer_2)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(u"./assets/files/desktop-opciones.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label)

        self.verticalSpacer = QSpacerItem(20, 196, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.verticalSpacer)


        self.horizontalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background-color: transparent;\n"
"}\n"
"QWidget#botones_widget,\n"
"#comando_widget{\n"
"background: qlineargradient(x1:0, y1:0, x2:1 y2:1, stop:0 #251F9B, stop:1 #01A6E1);\n"
"}\n"
"\n"
"QWidget#botones_widget,\n"
"#comando_widget{\n"
"border-top-right-radius:30px;\n"
"border-bottom-right-radius:30px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:15px;\n"
"padding:5px;\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color: rgb(234, 234, 234);\n"
"border-radius:10px;\n"
"padding:5px;\n"
"	font: 75 8pt \"MS Shell Dlg 2\";\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 10, 10, 10)
        self.comando_widget = QWidget(self.frame_2)
        self.comando_widget.setObjectName(u"comando_widget")
        self.comando_widget.setStyleSheet(u"QPushButton#ingresar_comandos_btn{\n"
"border:none;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #434645, stop:1 #434645);\n"
"color:white;\n"
"padding-top:10px;\n"
"padding-left:20px;\n"
"padding-right:20px;\n"
"padding-bottom:10px;\n"
"}\n"
"\n"
"QPushButton#ingresar_comandos_btn:hover{\n"
"	background-color: #A1A1A2;\n"
"}\n"
"\n"
"QPushButton#ingresar_comandos_btn:pressed{\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.gridLayout = QGridLayout(self.comando_widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(50, -1, 50, -1)
        self.label_2 = QLabel(self.comando_widget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(226, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.ingresar_comandos_btn = QPushButton(self.comando_widget)
        self.ingresar_comandos_btn.setObjectName(u"ingresar_comandos_btn")
        font1 = QFont()
        font1.setFamily(u"MS Shell Dlg 2")
        font1.setPointSize(8)
        font1.setBold(False)
        font1.setItalic(False)
        font1.setWeight(9)
        self.ingresar_comandos_btn.setFont(font1)

        self.gridLayout.addWidget(self.ingresar_comandos_btn, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(225, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 2, 1, 1)

        self.comandos_txt = QLineEdit(self.comando_widget)
        self.comandos_txt.setObjectName(u"comandos_txt")

        self.gridLayout.addWidget(self.comandos_txt, 1, 0, 1, 3)


        self.verticalLayout.addWidget(self.comando_widget)

        self.botones_widget = QWidget(self.frame_2)
        self.botones_widget.setObjectName(u"botones_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botones_widget.sizePolicy().hasHeightForWidth())
        self.botones_widget.setSizePolicy(sizePolicy1)
        self.botones_widget.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.botones_widget)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(45, 0, 0, 0)
        self.comandos_cbx = QComboBox(self.botones_widget)
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.addItem("")
        self.comandos_cbx.setObjectName(u"comandos_cbx")

        self.gridLayout_2.addWidget(self.comandos_cbx, 1, 1, 1, 2)

        self.pushButton_7 = QPushButton(self.botones_widget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.gridLayout_2.addWidget(self.pushButton_7, 7, 1, 1, 2)

        self.horizontalSpacer_6 = QSpacerItem(166, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_6, 1, 3, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(167, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_4, 1, 0, 1, 1)

        self.label_3 = QLabel(self.botones_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 4)

        self.pushButton_2 = QPushButton(self.botones_widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_2, 2, 1, 1, 2)

        self.pushButton_3 = QPushButton(self.botones_widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        sizePolicy2.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy2)
        self.pushButton_3.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_3, 3, 1, 1, 2)

        self.pushButton_4 = QPushButton(self.botones_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        sizePolicy2.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy2)
        self.pushButton_4.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_4, 4, 1, 1, 2)

        self.pushButton_5 = QPushButton(self.botones_widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        sizePolicy2.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy2)
        self.pushButton_5.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_5, 5, 1, 1, 2)

        self.pushButton_6 = QPushButton(self.botones_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setMinimumSize(QSize(100, 0))

        self.gridLayout_2.addWidget(self.pushButton_6, 6, 1, 1, 2)


        self.verticalLayout.addWidget(self.botones_widget, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2)

        OpcionesComputadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(OpcionesComputadora)

        QMetaObject.connectSlotsByName(OpcionesComputadora)
    # setupUi

    def retranslateUi(self, OpcionesComputadora):
        OpcionesComputadora.setWindowTitle(QCoreApplication.translate("OpcionesComputadora", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("OpcionesComputadora", u"<html><head/><body><p><span style=\" color:#ffffff;\">Ingresa el comando a ejecutar</span></p></body></html>", None))
        self.ingresar_comandos_btn.setText(QCoreApplication.translate("OpcionesComputadora", u"Ingresar", None))
        self.comandos_cbx.setItemText(0, QCoreApplication.translate("OpcionesComputadora", u"-", None))
        self.comandos_cbx.setItemText(1, QCoreApplication.translate("OpcionesComputadora", u"1", None))
        self.comandos_cbx.setItemText(2, QCoreApplication.translate("OpcionesComputadora", u"2", None))
        self.comandos_cbx.setItemText(3, QCoreApplication.translate("OpcionesComputadora", u"3", None))
        self.comandos_cbx.setItemText(4, QCoreApplication.translate("OpcionesComputadora", u"4", None))
        self.comandos_cbx.setItemText(5, QCoreApplication.translate("OpcionesComputadora", u"5", None))
        self.comandos_cbx.setItemText(6, QCoreApplication.translate("OpcionesComputadora", u"Ingresa comando manualmente", None))

        self.pushButton_7.setText(QCoreApplication.translate("OpcionesComputadora", u"Ingresar Comando \n"
"Manualmente", None))
        self.label_3.setText(QCoreApplication.translate("OpcionesComputadora", u"<html><head/><body><p><span style=\" color:#ffffff;\">Selecciona la </span></p><p><span style=\" color:#ffffff;\">opci\u00f3n a ejecutar</span></p></body></html>", None))
        self.pushButton_2.setText(QCoreApplication.translate("OpcionesComputadora", u"1", None))
        self.pushButton_3.setText(QCoreApplication.translate("OpcionesComputadora", u"2", None))
        self.pushButton_4.setText(QCoreApplication.translate("OpcionesComputadora", u"3", None))
        self.pushButton_5.setText(QCoreApplication.translate("OpcionesComputadora", u"4", None))
        self.pushButton_6.setText(QCoreApplication.translate("OpcionesComputadora", u"5", None))
    # retranslateUi

