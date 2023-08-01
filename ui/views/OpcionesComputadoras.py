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
from clases.administrador_ui import admin_socket_ui
import os


class OpcionesComputadora(QMainWindow, object):

    bandera = True

    def closeEvent(self, event):
        print('Cerrado de selección')

        if self.bandera:
            try:
                #Esta salir es salir de las operaciones de selección pero esta la excepción que salga del panel de administrador
                admin_socket_ui.escribir_operaciones('salir')
            except:
                print('No se pudo enviar el mensaje de salir, porque probablemente el dispositivo se haya desonectado')

        self.bandera = True
        event.accept()

    def decidir_cerrado(self, bandera):
        return bandera

    def setupUi(self, OpcionesComputadora):
        if not OpcionesComputadora.objectName():
            OpcionesComputadora.setObjectName(u"OpcionesComputadora")
        OpcionesComputadora.resize(800, 600)
        OpcionesComputadora.setMinimumSize(QSize(800, 600))
        OpcionesComputadora.setMaximumSize(QSize(16777215, 600))
        icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/LOGO.svg'
        )
        desktop_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/files/desktop-opciones.png'
        )
        icon = QIcon(icon_path)
        OpcionesComputadora.setWindowIcon(icon)
        OpcionesComputadora.setStyleSheet(u"QMainWindow#OpcionesComputadora{\n"
"	/*background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #080f43, stop:1 #1d1e26);*/\n"
"background-color:qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}")
        self.centralwidget = QWidget(OpcionesComputadora)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"QLabel#id_lbl,#nombre_lbl,#latitud_txt,#longitud_txt,#label_2,#label_5,#ip_txt{\n"
"	color: rgb(255, 255, 255);\n"
"	font: 75 10pt \"MS Shell Dlg 2\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame)
        self.formLayout.setObjectName(u"formLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 32, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(0, QFormLayout.SpanningRole, self.verticalSpacer_2)

        self.verticalSpacer_3 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(2, QFormLayout.SpanningRole, self.verticalSpacer_3)

        self.nombre_lbl = QLabel(self.frame)
        self.nombre_lbl.setObjectName(u"nombre_lbl")
        self.nombre_lbl.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.nombre_lbl)

        self.verticalSpacer_4 = QSpacerItem(20, 33, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(4, QFormLayout.SpanningRole, self.verticalSpacer_4)

        self.ip_txt = QLabel(self.frame)
        self.ip_txt.setObjectName(u"ip_txt")
        self.ip_txt.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(5, QFormLayout.SpanningRole, self.ip_txt)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(6, QFormLayout.SpanningRole, self.verticalSpacer_5)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setPixmap(QPixmap(desktop_path))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(7, QFormLayout.SpanningRole, self.label)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(9, QFormLayout.LabelRole, self.label_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(8, QFormLayout.LabelRole, self.verticalSpacer)

        self.latitud_txt = QLabel(self.frame)
        self.latitud_txt.setObjectName(u"latitud_txt")
        self.latitud_txt.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(9, QFormLayout.FieldRole, self.latitud_txt)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(10, QFormLayout.LabelRole, self.verticalSpacer_6)

        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(11, QFormLayout.LabelRole, self.label_5)

        self.longitud_txt = QLabel(self.frame)
        self.longitud_txt.setObjectName(u"longitud_txt")
        self.longitud_txt.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(11, QFormLayout.FieldRole, self.longitud_txt)

        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(12, QFormLayout.LabelRole, self.verticalSpacer_7)

        self.id_lbl = QLabel(self.frame)
        self.id_lbl.setObjectName(u"id_lbl")
        self.id_lbl.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.id_lbl)


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
"	background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1.5, y2:3, stop:0 #c0c0c0, stop:1 #000000);\n"
"}\n"
"\n"
"QWidget#botones_widget,\n"
"#comando_widget{\n"
"border-radius:30px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:15px;\n"
"padding:5px;\n"
"}\n"
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
"}\n"
"\n"
"QComboBox{\n"
"font-size: 12px;\n"
"padding:10px;\n"
"font-weight: bold;\n"
"background-color: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);;\n"
"color:white;\n"
"border:non"
                        "e;\n"
"}\n"
"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(20, 10, 10, 10)
        self.botones_widget = QWidget(self.frame_2)
        self.botones_widget.setObjectName(u"botones_widget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.botones_widget.sizePolicy().hasHeightForWidth())
        self.botones_widget.setSizePolicy(sizePolicy1)
        self.botones_widget.setMinimumSize(QSize(537, 0))
        self.botones_widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.botones_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(80, 0, 80, 0)
        self.label_3 = QLabel(self.botones_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label_3)

        self.apagar_equipo_btn = QPushButton(self.botones_widget)
        self.apagar_equipo_btn.setObjectName(u"apagar_equipo_btn")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.apagar_equipo_btn.sizePolicy().hasHeightForWidth())
        self.apagar_equipo_btn.setSizePolicy(sizePolicy2)
        self.apagar_equipo_btn.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.apagar_equipo_btn)

        self.supender_windows_equipo_btn = QPushButton(self.botones_widget)
        self.supender_windows_equipo_btn.setObjectName(u"supender_windows_equipo_btn")
        sizePolicy2.setHeightForWidth(self.supender_windows_equipo_btn.sizePolicy().hasHeightForWidth())
        self.supender_windows_equipo_btn.setSizePolicy(sizePolicy2)
        self.supender_windows_equipo_btn.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.supender_windows_equipo_btn)

        self.localizacion_btn = QPushButton(self.botones_widget)
        self.localizacion_btn.setObjectName(u"localizacion_btn")
        sizePolicy2.setHeightForWidth(self.localizacion_btn.sizePolicy().hasHeightForWidth())
        self.localizacion_btn.setSizePolicy(sizePolicy2)
        self.localizacion_btn.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.localizacion_btn)

        self.pushButton_6 = QPushButton(self.botones_widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        sizePolicy2.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy2)
        self.pushButton_6.setMinimumSize(QSize(100, 0))

        self.verticalLayout_3.addWidget(self.pushButton_6)


        self.verticalLayout.addWidget(self.botones_widget, 0, Qt.AlignHCenter)


        self.horizontalLayout.addWidget(self.frame_2)

        OpcionesComputadora.setCentralWidget(self.centralwidget)

        self.retranslateUi(OpcionesComputadora)

        QMetaObject.connectSlotsByName(OpcionesComputadora)
    # setupUi

    def retranslateUi(self, OpcionesComputadora):
        OpcionesComputadora.setWindowTitle(QCoreApplication.translate("OpcionesComputadora", u"Opciones de la computadora", None))
        self.nombre_lbl.setText("")
        self.ip_txt.setText("")
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("OpcionesComputadora", u"Latitud", None))
        self.latitud_txt.setText("")
        self.label_5.setText(QCoreApplication.translate("OpcionesComputadora", u"Longitud", None))
        self.longitud_txt.setText("")
        self.id_lbl.setText("")
        self.label_3.setText(QCoreApplication.translate("OpcionesComputadora", u"<html><head/><body><p><span style=\" font-weight:600;\">Selecciona la opci\u00f3n a </span></p><p><span style=\" font-weight:600;\">ejecutar</span></p></body></html>", None))
        self.apagar_equipo_btn.setText(QCoreApplication.translate("OpcionesComputadora", u"Apagar equipo", None))
        self.supender_windows_equipo_btn.setText(QCoreApplication.translate("OpcionesComputadora", u"Suspender - bloqueo de windows", None))
        self.localizacion_btn.setText(QCoreApplication.translate("OpcionesComputadora", u"Localizaci\u00f3n", None))
        self.pushButton_6.setText(QCoreApplication.translate("OpcionesComputadora", u"T\u00e9rmial de comandos", None))
    # retranslateUi

