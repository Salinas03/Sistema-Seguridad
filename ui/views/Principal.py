# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal - copia.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from clases.administrador_ui import admin_socket_ui
import socket
import sys
import os

class Principal(QMainWindow, object):

    bandera_salida = True

    def closeEvent(self, event):
        try:
            self.bandera_salida = False
            admin_socket_ui.cerrado_sockets()
            # admin_socket_ui.get_socket_administrador().send('salir'.encode())

        except socket.error as e:
            print(f'Ocurrio un error al realizar la salida {e}')

        event.accept()

    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.resize(1388, 813)
        Principal.setStyleSheet(u"QMainWindow#Principal{\n"
"	background-color: rgb(231, 231, 231);\n"
"}")

        # Rutas de las imágenes
        logo_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/LOGO.svg'
        )
        column_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/column-2.ico'
        )
        home_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/home-cambio-blanco.ico'
        )
        desktop_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/desktop-cambio-blanco.ico'
        )
        admin_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/user-4.ico'
        )
        help_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/question-cambio-blanco.ico'
        )
        arrow_icon_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/arrow-down-left.svg'
        )
        user_4_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/user-4.ico'
        )
        computadora_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/files/ok.png'
        )
        admin_2_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/files/admin2.png'
        )
        actualizar_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/refresh-ccw.svg'
        )

        pin_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/icons/pin-8-24.ico'
        )

        icon = QIcon(logo_path)
        icon1 = QIcon(home_icon_path)
        icon2 = QIcon(desktop_icon_path)
        icon3 = QIcon(admin_icon_path)
        icon4 = QIcon(help_icon_path)
        icon5 = QIcon(arrow_icon_path)
        icon6 = QIcon(user_4_path)
        icon7 = QIcon(actualizar_path)
        icon8 = QIcon(admin_2_path)
        icon9 = QIcon(column_icon_path)
        icon10 = QIcon(pin_path)
        Principal.setWindowIcon(icon)


        self.centralwidget = QWidget(Principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_widget = QWidget(self.frame)
        self.menu_widget.setObjectName(u"menu_widget")
        self.menu_widget.setMinimumSize(QSize(60, 0))
        self.menu_widget.setMaximumSize(QSize(50, 16777215))
        self.menu_widget.setStyleSheet(u"QWidget#menu_widget{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}\n"
"\n"
"QPushButton{\n"
"/*margin-bottom:10px;*/\n"
"background-color:transparent;\n"
"border-radius:3px;\n"
"border: none;\n"
"padding: 8px 0 8px 0;\n"
"color: #788596;\n"
"}\n"
"\n"
"QPushButton::hover{\n"
"background-color:rgba(86,101,115,0.5);\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:rgba(86,101,115,0.5);\n"
"border-top-left-radius: 20px;\n"
"border-left:4px solid rgb(231, 231, 231);\n"
"}\n"
"\n"
"")
        self.verticalLayout_4 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(5, 0, 0, 21)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.menu_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 55))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setPixmap(QPixmap(help_icon_path))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.home_btn = QPushButton(self.menu_widget)
        self.home_btn.setObjectName(u"home_btn")
        self.home_btn.setIcon(icon1)
        self.home_btn.setCheckable(True)
        self.home_btn.setChecked(True)
        self.home_btn.setAutoRepeat(False)
        self.home_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.home_btn)

        self.compus_btn = QPushButton(self.menu_widget)
        self.compus_btn.setObjectName(u"compus_btn")
        self.compus_btn.setIcon(icon2)
        self.compus_btn.setCheckable(True)
        self.compus_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.compus_btn)

        self.admins_btn = QPushButton(self.menu_widget)
        self.admins_btn.setObjectName(u"admins_btn")
        self.admins_btn.setIcon(icon3)
        self.admins_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.admins_btn)

        self.pin_btn = QPushButton(self.menu_widget)
        self.pin_btn.setObjectName(u"pin_btn")
        self.pin_btn.setIcon(icon10)
        self.pin_btn.setCheckable(True)

        self.verticalLayout_3.addWidget(self.pin_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_btn = QPushButton(self.menu_widget)
        self.settings_btn.setObjectName(u"settings_btn")
        self.settings_btn.setIcon(icon4)
        self.settings_btn.setCheckable(True)
        self.settings_btn.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.settings_btn)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.menu_widget)

        self.menu_desplegable_widget = QWidget(self.frame)
        self.menu_desplegable_widget.setObjectName(u"menu_desplegable_widget")
        self.menu_desplegable_widget.setStyleSheet(u"QWidget#menu_desplegable_widget{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}\n"
"\n"
"QLabel{\n"
"color: rgb(255, 255, 255);\n"
"	font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton{\n"
"background-color:transparent;\n"
"border:none;\n"
"border-radius:3px;\n"
"padding: 8px 0 8px 5px;\n"
"text-align:left;\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton::hover{\n"
"background-color:rgba(86,101,115,0.5);\n"
"border-top-left-radius: 20px;\n"
"}\n"
"\n"
"QPushButton::checked{\n"
"background-color:rgba(86,101,115,0.5);\n"
"border-top-left-radius: 20px;\n"
"border-left:4px solid rgb(231, 231, 231);\n"
"}\n"
"\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.menu_desplegable_widget)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(10, 0, 0, 30)
        self.label_18 = QLabel(self.menu_desplegable_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(0, 55))
        self.label_18.setMaximumSize(QSize(16777215, 50))
        self.label_18.setPixmap(QPixmap(help_icon_path))
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_18)

        self.home_texto_btn = QPushButton(self.menu_desplegable_widget)
        self.home_texto_btn.setObjectName(u"home_texto_btn")
        self.home_texto_btn.setIcon(icon1)
        self.home_texto_btn.setCheckable(True)
        self.home_texto_btn.setChecked(True)

        self.verticalLayout_16.addWidget(self.home_texto_btn)

        self.desktop_texto_btn = QPushButton(self.menu_desplegable_widget)
        self.desktop_texto_btn.setObjectName(u"desktop_texto_btn")
        self.desktop_texto_btn.setMinimumSize(QSize(120, 0))
        self.desktop_texto_btn.setMaximumSize(QSize(16777208, 16777215))
        self.desktop_texto_btn.setIcon(icon2)
        self.desktop_texto_btn.setCheckable(True)

        self.verticalLayout_16.addWidget(self.desktop_texto_btn)

        self.admins_texto_btn = QPushButton(self.menu_desplegable_widget)
        self.admins_texto_btn.setObjectName(u"admins_texto_btn")
        self.admins_texto_btn.setIcon(icon3)
        self.admins_texto_btn.setCheckable(True)

        self.verticalLayout_16.addWidget(self.admins_texto_btn)

        self.pin_texto_btn = QPushButton(self.menu_desplegable_widget)
        self.pin_texto_btn.setObjectName(u"pin_texto_btn")
        self.pin_texto_btn.setIcon(icon10)
        self.pin_texto_btn.setCheckable(True)

        self.verticalLayout_16.addWidget(self.pin_texto_btn)

        self.verticalSpacer_13 = QSpacerItem(20, 572, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_13)

        self.settings_texto_btn = QPushButton(self.menu_desplegable_widget)
        self.settings_texto_btn.setObjectName(u"settings_texto_btn")
        self.settings_texto_btn.setIcon(icon4)
        self.settings_texto_btn.setCheckable(True)

        self.verticalLayout_16.addWidget(self.settings_texto_btn)


        self.horizontalLayout.addWidget(self.menu_desplegable_widget)

        self.body_widget = QWidget(self.frame)
        self.body_widget.setObjectName(u"body_widget")
        self.body_widget.setStyleSheet(u"QPushButton#user_btn,#pushButton{\n"
"background-color:transparent;\n"
"}\n"
"\n"
"QPushButton#pushButton{\n"
"border:none;\n"
"text-align:left;\n"
"color:#788596;\n"
"}\n"
"\n"
"QPushButton#user_btn:hover{\n"
"background-color:rgba(86,101,115,0.5);\n"
"border:none;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton#user_btn:checked{\n"
"background-color:rgba(86,101,115,0.5);\n"
"}\n"
"\n"
"QPushButton#guardad_computadora_btn,\n"
"#cancelar_registro_btn,\n"
"#modificar_btn,\n"
"#guardar_btn,\n"
"#cancelar_btn,\n"
"#agregar_admin_btn,\n"
"#modificar_admin_btn,\n"
"#eliminar_admin_btn,\n"
"#agregar_compu_btn,\n"
"#modificar_compu_btn,\n"
"#eliminar_compu_btn,\n"
"#modificar_perfil_btn,\n"
"#guardar_admin_btn{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"border-radius:15px;\n"
"color:white;\n"
"}\n"
"\n"
"QPushButton#guardad_computadora_btn:hover,\n"
"#cancelar_registro_btn:hover,\n"
"#modificar_btn:hover,\n"
"#guardar_btn:hover,\n"
"#cancelar_btn:hover,\n"
"#agregar_admin_btn:hover,\n"
"#modificar_admin_btn:hover,\n"
"#eliminar_admin_btn:hover,\n"
"#agregar_compu_btn:hover,\n"
"#"
                        "modificar_compu_btn:hover,\n"
"#eliminar_compu_btn:hover,\n"
"#modificar_perfil_btn:hover,\n"
"#guardar_admin_btn:hover{\n"
"padding-left:5px;\n"
"padding-top:5px;\n"
"background-color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QPushButton#cerrar_sesion_btn_2{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"border-radius:5px;\n"
"color:white;\n"
"font: 10pt \"MS Shell Dlg 2\";\n"
"}\n"
"\n"
"QPushButton#cerrar_sesion_btn_2:hover{\n"
"padding-left:3px;\n"
"padding-top:3px;\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color:rgba(0,0,0,0);\n"
"border:1px solid rgba(0,0,0,0);\n"
"border-bottom-color:rgba(141,150,140,255);\n"
"padding-bottom:7px;\n"
"color: rgb(140, 140, 140);\n"
"}\n"
"\n"
"QTableWidget#tabla_computadoras_activas::item::selected {\n"
"        background-color: transparent;  /* Eliminar el color de fondo de resaltado */\n"
"          /* Cambiar el puntero a predeterminado */\n"
"        color:black;   \n}"
"QTableWidget#tabla_computadoras_desactivas::item::selected {\n"
"        background-color: transparent;  /* Eliminar el color de fondo de resaltado */\n"
"          /* Cambiar el puntero a predeterminado */\n"
"        color:black;   \n}"
"")
        self.formLayout = QFormLayout(self.body_widget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.body_widget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QSize(1080, 0))
        self.frame_2.setMaximumSize(QSize(50000, 50))
        self.frame_2.setStyleSheet(u"QFrame#frame_2{\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"border-radius: 0 0 15px 1px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setIcon(icon9)
        self.pushButton.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.pushButton)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)

        self.user_btn = QPushButton(self.frame_2)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setMaximumSize(QSize(50, 16777215))
        self.user_btn.setStyleSheet(u"")
        self.user_btn.setIcon(icon6)
        self.user_btn.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.user_btn)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_5)


        self.formLayout.setWidget(0, QFormLayout.SpanningRole, self.frame_2)

        self.frame_3 = QFrame(self.body_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setStyleSheet(u"")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.frame_3)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_6 = QGridLayout(self.page)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_9 = QFrame(self.page)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_9)
        self.verticalLayout_9.setSpacing(7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.widget_5 = QWidget(self.frame_9)
        self.widget_5.setObjectName(u"widget_5")
        self.widget_5.setMaximumSize(QSize(16777215, 60))
        self.verticalLayout_10 = QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_9.addWidget(self.widget_5)

        self.widget_6 = QWidget(self.frame_9)
        self.widget_6.setObjectName(u"widget_6")
        self.widget_6.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.widget_7 = QWidget(self.widget_6)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy)
        self.widget_7.setStyleSheet(u"")
        self.gridLayout_10 = QGridLayout(self.widget_7)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_10.setContentsMargins(20, -1, 50, -1)
        self.frame_11 = QFrame(self.widget_7)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy)
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_20 = QLabel(self.frame_11)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_20)

        self.computadoras_registradas_table = QTableWidget(self.frame_11)
        if (self.computadoras_registradas_table.columnCount() < 5):
            self.computadoras_registradas_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.computadoras_registradas_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.computadoras_registradas_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.computadoras_registradas_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.computadoras_registradas_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.computadoras_registradas_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.computadoras_registradas_table.setObjectName(u"computadoras_registradas_table")

        self.verticalLayout_13.addWidget(self.computadoras_registradas_table)


        self.gridLayout_10.addWidget(self.frame_11, 0, 0, 1, 2)


        self.horizontalLayout_7.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 10, 0)
        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(computadora_path))

        self.verticalLayout_11.addWidget(self.label_14, 0, Qt.AlignHCenter)

        self.verticalSpacer_7 = QSpacerItem(20, 443, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.agregar_compu_btn = QPushButton(self.widget_8)
        self.agregar_compu_btn.setObjectName(u"agregar_compu_btn")
        self.agregar_compu_btn.setMinimumSize(QSize(0, 100))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        font1.setWeight(75)
        self.agregar_compu_btn.setFont(font1)

        self.verticalLayout_11.addWidget(self.agregar_compu_btn)

        self.label_4 = QLabel(self.widget_8)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_11.addWidget(self.label_4)

        self.eliminar_compu_btn = QPushButton(self.widget_8)
        self.eliminar_compu_btn.setObjectName(u"eliminar_compu_btn")
        self.eliminar_compu_btn.setMinimumSize(QSize(0, 50))
        font2 = QFont()
        font2.setBold(True)
        font2.setWeight(75)
        self.eliminar_compu_btn.setFont(font2)

        self.verticalLayout_11.addWidget(self.eliminar_compu_btn)

        self.label_16 = QLabel(self.widget_8)
        self.label_16.setObjectName(u"label_16")

        self.verticalLayout_11.addWidget(self.label_16)

        self.label_17 = QLabel(self.widget_8)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_11.addWidget(self.label_17)


        self.horizontalLayout_7.addWidget(self.widget_8, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.widget_6)


        self.gridLayout_6.addWidget(self.frame_9, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.verticalLayout_12 = QVBoxLayout(self.page_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.widget_9 = QWidget(self.page_3)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setMaximumSize(QSize(16777215, 50))
        self.gridLayout_7 = QGridLayout(self.widget_9)
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget_9)
        self.label_5.setObjectName(u"label_5")
        font3 = QFont()
        font3.setPointSize(26)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_5.setFont(font3)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_5 = QGridLayout(self.widget_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.scrollArea = QScrollArea(self.widget_10)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1200, 598))
        self.gridLayout_8 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_15 = QLabel(self.scrollAreaWidgetContents)
        self.label_15.setObjectName(u"label_15")
        font4 = QFont()
        font4.setPointSize(12)
        self.label_15.setFont(font4)
        self.label_15.setAlignment(Qt.AlignJustify|Qt.AlignTop)
        self.label_15.setWordWrap(True)

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_5.addWidget(self.scrollArea, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_14 = QFrame(self.page_4)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_14)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_6 = QFrame(self.frame_14)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setMinimumSize(QSize(1080, 0))
        self.frame_6.setMaximumSize(QSize(900, 16777215))
        self.frame_6.setStyleSheet(u"QFrame#frame_6{\n"
"background-color: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"color:white;\n"
"border-radius:50px;\n"
"}\n"
"\n"
"QLineEdit#nombre_txt:hover,\n"
"#apellidos_txt:hover,\n"
"#telefono_txt:hover,\n"
"#correo_txt:hover{\n"
"color:white;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_6)
        self.gridLayout_9.setSpacing(0)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 50, 50, 100)
        self.label_13 = QLabel(self.frame_6)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.gridLayout_9.addWidget(self.label_13, 0, 0, 1, 2)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        font5 = QFont()
        font5.setPointSize(14)
        font5.setBold(True)
        font5.setWeight(75)
        self.label_7.setFont(font5)

        self.gridLayout_9.addWidget(self.label_7, 4, 0, 1, 1, Qt.AlignHCenter)

        self.nombre_txt = QLineEdit(self.frame_6)
        self.nombre_txt.setObjectName(u"nombre_txt")
        self.nombre_txt.setMaximumSize(QSize(800, 16777215))
        font6 = QFont()
        font6.setPointSize(14)
        self.nombre_txt.setFont(font6)

        self.gridLayout_9.addWidget(self.nombre_txt, 2, 1, 1, 1)

        self.verticalSpacer_12 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_12, 7, 1, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.gridLayout_9.addWidget(self.label_8, 6, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_11 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_11, 5, 1, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font5)

        self.gridLayout_9.addWidget(self.label_6, 2, 0, 1, 1, Qt.AlignHCenter)

        self.telefono_txt = QLineEdit(self.frame_6)
        self.telefono_txt.setObjectName(u"telefono_txt")
        self.telefono_txt.setMaximumSize(QSize(800, 16777215))
        self.telefono_txt.setFont(font6)

        self.gridLayout_9.addWidget(self.telefono_txt, 6, 1, 1, 1)

        self.correo_txt = QLineEdit(self.frame_6)
        self.correo_txt.setObjectName(u"correo_txt")
        self.correo_txt.setMaximumSize(QSize(800, 16777215))
        self.correo_txt.setFont(font6)

        self.gridLayout_9.addWidget(self.correo_txt, 8, 1, 1, 1)

        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.gridLayout_9.addWidget(self.label_9, 8, 0, 1, 1, Qt.AlignHCenter)

        self.verticalSpacer_10 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_10, 3, 1, 1, 1)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_9, 1, 1, 1, 1)

        self.apellidos_txt = QLineEdit(self.frame_6)
        self.apellidos_txt.setObjectName(u"apellidos_txt")
        self.apellidos_txt.setMaximumSize(QSize(800, 16777215))
        self.apellidos_txt.setFont(font6)

        self.gridLayout_9.addWidget(self.apellidos_txt, 4, 1, 1, 1)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_9.addItem(self.verticalSpacer_6, 9, 1, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_6)

        self.frame_12 = QFrame(self.frame_14)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 200))
        self.frame_12.setStyleSheet(u"")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.gridLayout_13 = QGridLayout(self.frame_12)
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_15 = QFrame(self.frame_12)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setMinimumSize(QSize(1080, 0))
        self.frame_15.setMaximumSize(QSize(1080, 16777215))
        self.frame_15.setStyleSheet(u"")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_15)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.cerrar_sesion_btn_2 = QPushButton(self.frame_15)
        self.cerrar_sesion_btn_2.setObjectName(u"cerrar_sesion_btn_2")
        self.cerrar_sesion_btn_2.setMinimumSize(QSize(120, 40))
        self.cerrar_sesion_btn_2.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_8.addWidget(self.cerrar_sesion_btn_2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)

        self.modificar_perfil_btn = QPushButton(self.frame_15)
        self.modificar_perfil_btn.setObjectName(u"modificar_perfil_btn")
        self.modificar_perfil_btn.setMinimumSize(QSize(200, 60))
        font7 = QFont()
        font7.setPointSize(10)
        self.modificar_perfil_btn.setFont(font7)

        self.horizontalLayout_8.addWidget(self.modificar_perfil_btn)


        self.gridLayout_13.addWidget(self.frame_15, 0, 0, 1, 1)


        self.verticalLayout_15.addWidget(self.frame_12, 0, Qt.AlignRight)


        self.gridLayout_4.addWidget(self.frame_14, 0, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.gridLayout_14 = QGridLayout(self.page_5)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.widget_11 = QWidget(self.page_5)
        self.widget_11.setObjectName(u"widget_11")
        self.verticalLayout_8 = QVBoxLayout(self.widget_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, -1, 50, -1)
        self.frame_13 = QFrame(self.widget_11)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_13)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_21 = QLabel(self.frame_13)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)
        self.label_21.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_21)

        self.administradores_tabla = QTableWidget(self.frame_13)
        if (self.administradores_tabla.columnCount() < 6):
            self.administradores_tabla.setColumnCount(6)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.administradores_tabla.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setBackground(QColor(0, 0, 0, 0));
        self.administradores_tabla.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.administradores_tabla.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.administradores_tabla.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.administradores_tabla.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.administradores_tabla.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        self.administradores_tabla.setObjectName(u"administradores_tabla")
        self.administradores_tabla.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.administradores_tabla.horizontalHeader().setMinimumSectionSize(125)
        self.administradores_tabla.horizontalHeader().setHighlightSections(False)

        self.verticalLayout_7.addWidget(self.administradores_tabla)


        self.verticalLayout_8.addWidget(self.frame_13)


        self.gridLayout_14.addWidget(self.widget_11, 0, 0, 1, 1)

        self.frame_8 = QFrame(self.page_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setMaximumSize(QSize(150, 16777215))
        self.frame_8.setStyleSheet(u"")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_8)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.frame_8)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 150))
        self.label_10.setPixmap(QPixmap(admin_2_path))
        self.label_10.setScaledContents(True)
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_10)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_5)

        self.agregar_admin_btn = QPushButton(self.frame_8)
        self.agregar_admin_btn.setObjectName(u"agregar_admin_btn")
        self.agregar_admin_btn.setMinimumSize(QSize(150, 100))
        self.agregar_admin_btn.setMaximumSize(QSize(150, 16777215))
        font8 = QFont()
        font8.setPointSize(11)
        font8.setBold(True)
        font8.setWeight(75)
        self.agregar_admin_btn.setFont(font8)

        self.verticalLayout_14.addWidget(self.agregar_admin_btn)

        self.label_11 = QLabel(self.frame_8)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)

        self.eliminar_admin_btn = QPushButton(self.frame_8)
        self.eliminar_admin_btn.setObjectName(u"eliminar_admin_btn")
        self.eliminar_admin_btn.setMinimumSize(QSize(0, 50))
        self.eliminar_admin_btn.setMaximumSize(QSize(250, 16777215))
        self.eliminar_admin_btn.setFont(font2)

        self.verticalLayout_14.addWidget(self.eliminar_admin_btn)

        self.label_12 = QLabel(self.frame_8)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_14.addWidget(self.label_12)


        self.gridLayout_14.addWidget(self.frame_8, 0, 1, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_5)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QPushButton#activar_btn,\n"
"#activar_compus_btn,\n"
"#desactivar_btn,\n"
"#desactivar_compus_btn{\n"
"	background-color: transparent;\n"
"}\n"
"\n"
"QPushButton#activar_btn:hover,\n"
"#activar_compus_btn:hover{\n"
"	background-color: rgb(0, 170, 0);\n"
"	color:white;\n"
"	font:15px;\n"
"}\n"
"\n"
"QPushButton#desactivar_btn:hover,\n"
"#desactivar_compus_btn:hover{\n"
"	background-color: rgb(255, 0, 0);\n"
"	color:white;\n"
"	font:15px;\n"
"}\n"
"\n"
"")
        self.horizontalLayout_4 = QHBoxLayout(self.page_2)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.page_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_4)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.widget.setStyleSheet(u"QPushButton#apagar_equipos_btn,#suspender_equipos_btn{\n"
"padding:5px;\n"
"border-radius:10px;\n"
"border:1px solid white;\n"
"color:white;\n"
"padding:7px;\n"
"margin-right:5px;\n"
"background: qlineargradient(x1:0, y1:0, x2:2.5 y2:1, stop:0 #2B3034, stop:1 #1C4968);\n"
"}\n"
"\n"
"QPushButton#apagar_equipos_btn:hover,#suspender_equipos_btn:hover{\n"
"background: qlineargradient(x1:0, y1:0, x2:1 y2:1, stop:0 #251F9B, stop:1 #01A6E1);\n"
"}\n"
"\n"
"QPushButton#apagar_equipos_btn:pressed,#suspender_equipos_btn:pressed{\n"
"	font: 75 9pt \"MS Shell Dlg 2\";\n"
"}")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.actualizar_btn = QPushButton(self.widget)
        self.actualizar_btn.setObjectName(u"actualizar_btn")
        self.actualizar_btn.setIcon(icon7)

        self.horizontalLayout_5.addWidget(self.actualizar_btn)

        self.horizontalSpacer_2 = QSpacerItem(845, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)

        self.suspender_equipos_btn = QPushButton(self.widget)
        self.suspender_equipos_btn.setObjectName(u"suspender_equipos_btn")
        self.suspender_equipos_btn.setMinimumSize(QSize(110, 50))

        self.horizontalLayout_5.addWidget(self.suspender_equipos_btn)

        self.apagar_equipos_btn = QPushButton(self.widget)
        self.apagar_equipos_btn.setObjectName(u"apagar_equipos_btn")
        self.apagar_equipos_btn.setMinimumSize(QSize(110, 50))

        self.horizontalLayout_5.addWidget(self.apagar_equipos_btn)


        self.verticalLayout_6.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabla_computadoras_activas = QTableWidget(self.widget_2)
        if (self.tabla_computadoras_activas.columnCount() < 6):
            self.tabla_computadoras_activas.setColumnCount(6)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        self.tabla_computadoras_activas.setObjectName(u"tabla_computadoras_activas")

        self.gridLayout_2.addWidget(self.tabla_computadoras_activas, 1, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_2)

        self.widget_3 = QWidget(self.frame_4)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setMaximumSize(QSize(16777215, 60))
        self.widget_3.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_3 = QSpacerItem(792, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_6.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.frame_4)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget_4)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tabla_computadoras_desactivas = QTableWidget(self.widget_4)
        if (self.tabla_computadoras_desactivas.columnCount() < 5):
            self.tabla_computadoras_desactivas.setColumnCount(5)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(0, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(1, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(2, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(3, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(4, __qtablewidgetitem21)
        if (self.tabla_computadoras_desactivas.rowCount() < 2):
            self.tabla_computadoras_desactivas.setRowCount(2)
        self.tabla_computadoras_desactivas.setObjectName(u"tabla_computadoras_desactivas")
        self.tabla_computadoras_desactivas.setRowCount(2)

        self.gridLayout_3.addWidget(self.tabla_computadoras_desactivas, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.page_2)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.widget_12 = QWidget(self.page_6)
        self.widget_12.setObjectName(u"widget_12")
        self.widget_12.setGeometry(QRect(380, 250, 120, 80))
        self.stackedWidget.addWidget(self.page_6)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.formLayout.setWidget(1, QFormLayout.SpanningRole, self.frame_3)


        self.horizontalLayout.addWidget(self.body_widget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        self.settings_texto_btn.toggled.connect(self.settings_btn.setChecked)
        self.pushButton.toggled.connect(self.menu_widget.setHidden)
        self.pushButton.toggled.connect(self.menu_desplegable_widget.setVisible)
        self.home_texto_btn.toggled.connect(self.home_btn.setChecked)

        self.desktop_texto_btn.toggled.connect(self.compus_btn.setChecked)
        self.compus_btn.toggled.connect(self.desktop_texto_btn.setChecked)
        self.admins_texto_btn.toggled.connect(self.admins_btn.setChecked)
        self.home_btn.toggled.connect(self.home_texto_btn.setChecked)
        self.admins_btn.toggled.connect(self.admins_texto_btn.setChecked)
        self.pin_btn.toggled.connect(self.pin_texto_btn.setChecked)
        self.pin_texto_btn.toggled.connect(self.pin_btn.setChecked)

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(QCoreApplication.translate("Principal", u"Principal", None))
        self.label.setText("")
        self.home_btn.setText("")
        self.compus_btn.setText("")
        self.admins_btn.setText("")
        self.pin_btn.setText("")
        self.settings_btn.setText("")
        self.label_18.setText("")
        self.home_texto_btn.setText(QCoreApplication.translate("Principal", u"Inicio", None))
        self.desktop_texto_btn.setText(QCoreApplication.translate("Principal", u"Computadoras", None))
        self.admins_texto_btn.setText(QCoreApplication.translate("Principal", u"Propietarios", None))
        self.pin_texto_btn.setText(QCoreApplication.translate("Principal", u"Localizaci\u00f3n", None))
        self.settings_texto_btn.setText(QCoreApplication.translate("Principal", u"Dudas", None))
        self.pushButton.setText("")
        self.label_20.setText(QCoreApplication.translate("Principal", u"TABLA DE COMPUTADORAS REGISTRADAS", None))
        ___qtablewidgetitem = self.computadoras_registradas_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Principal", u"ID", None));
        ___qtablewidgetitem1 = self.computadoras_registradas_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Principal", u"Nombre de quipo", None));
        ___qtablewidgetitem2 = self.computadoras_registradas_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Principal", u"N\u00famero de serie", None));
        ___qtablewidgetitem3 = self.computadoras_registradas_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Principal", u"Propietario del equipo", None));
        ___qtablewidgetitem4 = self.computadoras_registradas_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Principal", u"Rol", None));
        self.label_14.setText("")
        self.agregar_compu_btn.setText(QCoreApplication.translate("Principal", u"Agregar \n"
"Computadora", None))
        self.label_4.setText("")
        self.eliminar_compu_btn.setText(QCoreApplication.translate("Principal", u"Eliminar \n"
"Computadora", None))
        self.label_16.setText("")
        self.label_17.setText("")
        self.label_5.setText(QCoreApplication.translate("Principal", u"Ayuda", None))
        self.label_15.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p align=\"justify\">P\u00e1gina principal</p><p align=\"justify\">-Instalar la segunda aplicaci\u00f3n en la computadora que se va a monitorear. </p><p align=\"justify\">-Asegurese que ambas aplicaciones cuenten con una conexi\u00f3n a internet, si no, el programa no podra ser utilizado correctamente.</p><p align=\"justify\">- Obtener el n\u00famero de serie de la computadora que va a ser registrada, este n\u00famero sera tomado como dato \u00fanico de los equipos de computo y poder distinguirlos con m\u00e1s facilidad.</p><p align=\"justify\">- Para poder registrar una nueva computadora, se debe registrar primeramente en la secci\u00f3n de agregar computadoras.</p><p align=\"justify\">-Si quiere agregar otro comando en la computadoras activas, de doble click en la fila de la computadora que desea controlar.</p><p align=\"justify\">- Hay dos botones en la p\u00e1gina de inicio, los cuales tienen la funci\u00f3n en general de bloqueo o apagado de todos los equipos de computo activos.<br/></p"
                        "><p align=\"justify\">Computadoras</p><p align=\"justify\">- Si requiere modificar alg\u00fan dato de alguna computadora, de doble click en el dato a modificar.</p><p align=\"justify\">- Si se requiere eliminar a una computadora, seleccione la fila y de click en el b\u00f3ton eliminar</p><p align=\"justify\"><br/></p><p align=\"justify\">Propietarios</p><p align=\"justify\">- Si requiere modificar alg\u00fan dato de alg\u00fan propietario, de doble click en la fila del dato a modificar.</p><p align=\"justify\">- Si se requiere eliminar a un propietario, seleccione la fila y de click en el b\u00f3ton eliminar</p><p align=\"justify\"><br/></p><p align=\"justify\">Ubicaci\u00f3n</p><p align=\"justify\">-Para poder localizar un equipo de computo, se debe conocer el correo y contrase\u00f1a de la sesi\u00f3n de la computadora cliente, la cual es la que inicio para el sistema de Windows, ya que los botones de ubicaci\u00f3n tendran la funci\u00f3n de redirigir a una p\u00e1gina oficial de Microsoft para hacer la loc"
                        "alizaci\u00f3n.</p><p align=\"justify\"><br/></p><p align=\"justify\">-Como segunda opci\u00f3n se tiene las coordenas de los equipos de computo, entrando a las opciones de la computadora, dando doble click en la computadora activa, apareceran las coordenadas, el detalle de esta segunda opci\u00f3n es que no tiene una localizaci\u00f3n exacta, pero es muy proxima, con un radio de aproximandamente 1km</p></body></html>", None))
        self.label_13.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:16pt; font-weight:600; color:#ffffff;\">PERFIL ADMINISTRADOR</span></p></body></html>", None))
        self.label_7.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" color:#ffffff;\">Apellidos</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" color:#ffffff;\">Tel\u00e9fono</span></p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" color:#ffffff;\">Nombre</span></p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" color:#ffffff;\">Correo</span></p></body></html>", None))
        self.cerrar_sesion_btn_2.setText(QCoreApplication.translate("Principal", u"Cerrar Sesi\u00f3n", None))
        self.modificar_perfil_btn.setText(QCoreApplication.translate("Principal", u"Modificar \n"
"informaci\u00f3n", None))
        self.label_21.setText(QCoreApplication.translate("Principal", u"TABLA DE PROPIETARIOS REGISRADOS", None))
        ___qtablewidgetitem5 = self.administradores_tabla.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Principal", u"id", None));
        ___qtablewidgetitem6 = self.administradores_tabla.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Principal", u"Nombre", None));
        ___qtablewidgetitem7 = self.administradores_tabla.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Principal", u"Apellidos", None));
        ___qtablewidgetitem8 = self.administradores_tabla.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Principal", u"Telefono", None));
        ___qtablewidgetitem9 = self.administradores_tabla.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Principal", u"Correo", None));
        ___qtablewidgetitem10 = self.administradores_tabla.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Principal", u"Rol", None));
        self.label_10.setText("")
        self.agregar_admin_btn.setText(QCoreApplication.translate("Principal", u"Agregar nuevo \n"
"Administrador", None))
        self.label_11.setText("")
        self.eliminar_admin_btn.setText(QCoreApplication.translate("Principal", u"Eliminar \n"
"Adminstrador", None))
        self.label_12.setText("")
        self.label_2.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:12pt;\">Computadoras </span><span style=\" font-size:12pt; color:#00aa00;\">activas</span></p></body></html>", None))
        self.actualizar_btn.setText("")
        self.suspender_equipos_btn.setText(QCoreApplication.translate("Principal", u"Suspender \n"
"Computadoras", None))
        self.apagar_equipos_btn.setText(QCoreApplication.translate("Principal", u"Apagar \n"
"Computadoras", None))
        ___qtablewidgetitem11 = self.tabla_computadoras_activas.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Principal", u"ID", None));
        ___qtablewidgetitem12 = self.tabla_computadoras_activas.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Principal", u"Nombre del equipo", None));
        ___qtablewidgetitem13 = self.tabla_computadoras_activas.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Principal", u"N\u00famero de serie", None));
        ___qtablewidgetitem14 = self.tabla_computadoras_activas.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("Principal", u"Propietario de equipo", None));
        ___qtablewidgetitem15 = self.tabla_computadoras_activas.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("Principal", u"Rol", None));
        ___qtablewidgetitem16 = self.tabla_computadoras_activas.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("Principal", u"IP", None));
        self.label_3.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:12pt;\">Computadoras </span><span style=\" font-size:12pt; color:#ff0206;\">inactivas</span></p></body></html>", None))
        ___qtablewidgetitem17 = self.tabla_computadoras_desactivas.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("Principal", u"ID", None));
        self.pushButton.setText("")
        self.user_btn.setText("")
    # retranslateUi

