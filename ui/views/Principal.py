# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Principal.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Principal(QMainWindow, object):
    def setupUi(self, Principal):
        if not Principal.objectName():
            Principal.setObjectName(u"Principal")
        Principal.resize(1241, 848)
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
        self.menu_widget.setStyleSheet(u"background-color: rgb(214, 214, 214);")
        self.verticalLayout_4 = QVBoxLayout(self.menu_widget)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label = QLabel(self.menu_widget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(0, 55))
        self.label.setMaximumSize(QSize(16777215, 50))
        self.label.setPixmap(QPixmap(u"./assets/icons/align-justify.svg"))
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.label)

        self.home_btn = QPushButton(self.menu_widget)
        self.home_btn.setObjectName(u"home_btn")
        icon = QIcon()
        icon.addFile(u"./assets/icons/home-3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.home_btn.setIcon(icon)
        self.home_btn.setCheckable(False)
        self.home_btn.setChecked(False)
        self.home_btn.setAutoRepeat(False)
        self.home_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.home_btn)

        self.data_btn = QPushButton(self.menu_widget)
        self.data_btn.setObjectName(u"data_btn")
        icon1 = QIcon()
        icon1.addFile(u"./assets/icons/database-3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.data_btn.setIcon(icon1)
        self.data_btn.setCheckable(False)
        self.data_btn.setAutoExclusive(False)

        self.verticalLayout_3.addWidget(self.data_btn)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.settings_btn = QPushButton(self.menu_widget)
        self.settings_btn.setObjectName(u"settings_btn")
        icon2 = QIcon()
        icon2.addFile(u"./assets/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_btn.setIcon(icon2)
        self.settings_btn.setCheckable(False)
        self.settings_btn.setAutoExclusive(False)

        self.verticalLayout_2.addWidget(self.settings_btn)

        self.pushButton_4 = QPushButton(self.menu_widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon3 = QIcon()
        icon3.addFile(u"./assets/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)

        self.verticalLayout_2.addWidget(self.pushButton_4)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)


        self.horizontalLayout.addWidget(self.menu_widget)

        self.body_widget = QWidget(self.frame)
        self.body_widget.setObjectName(u"body_widget")
        self.body_widget.setStyleSheet(u"QPushButton#guardad_computadora_btn,\n"
"#cancelar_registro_btn,\n"
"#modificar_btn,\n"
"#guardar_btn,\n"
"#cancelar_btn,\n"
"#agregar_admin_btn,\n"
"#user_btn{\n"
"background-color: transparent;\n"
"\n"
"}\n"
"\n"
"QPushButton#guardad_computadora_btn:hover,\n"
"#cancelar_registro_btn:hover,\n"
"#modificar_btn:hover,\n"
"#guardar_btn:hover,\n"
"#cancelar_btn:hover,\n"
"#agregar_admin_btn:hover,\n"
"#user_btn:hover{\n"
"border:1px solid #2372B4;\n"
"border-radius:10px;\n"
"background-color: rgba(0, 85, 255,0.5);\n"
"color:white;\n"
"font:15px;\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.body_widget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.body_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 50))
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(1150, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.user_btn = QPushButton(self.frame_2)
        self.user_btn.setObjectName(u"user_btn")
        self.user_btn.setStyleSheet(u"")
        icon4 = QIcon()
        icon4.addFile(u"./assets/icons/user-5.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.user_btn.setIcon(icon4)

        self.horizontalLayout_2.addWidget(self.user_btn)


        self.verticalLayout.addWidget(self.frame_2)

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
        self.label_4 = QLabel(self.widget_5)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.label_4)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer_8)


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
        self.widget_7.setStyleSheet(u"")
        self.formLayout = QFormLayout(self.widget_7)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(100, -1, 50, -1)
        self.label_10 = QLabel(self.widget_7)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(0, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_10)

        self.persona_cargo_txt = QLineEdit(self.widget_7)
        self.persona_cargo_txt.setObjectName(u"persona_cargo_txt")
        font1 = QFont()
        font1.setPointSize(12)
        self.persona_cargo_txt.setFont(font1)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.persona_cargo_txt)

        self.label_11 = QLabel(self.widget_7)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMinimumSize(QSize(0, 50))
        self.label_11.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_11)

        self.computadora_txt = QLineEdit(self.widget_7)
        self.computadora_txt.setObjectName(u"computadora_txt")
        self.computadora_txt.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.computadora_txt)

        self.label_12 = QLabel(self.widget_7)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(0, 50))
        self.label_12.setFont(font)

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_12)

        self.dia_txt = QLineEdit(self.widget_7)
        self.dia_txt.setObjectName(u"dia_txt")
        self.dia_txt.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.dia_txt)

        self.label_13 = QLabel(self.widget_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setMinimumSize(QSize(0, 50))
        self.label_13.setFont(font)

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_13)

        self.ip_txt = QLineEdit(self.widget_7)
        self.ip_txt.setObjectName(u"ip_txt")
        self.ip_txt.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.ip_txt)


        self.horizontalLayout_7.addWidget(self.widget_7)

        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setStyleSheet(u"")
        self.verticalLayout_11 = QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_14 = QLabel(self.widget_8)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"./assets/files/ok.png"))

        self.verticalLayout_11.addWidget(self.label_14)

        self.verticalSpacer_7 = QSpacerItem(20, 443, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_11.addItem(self.verticalSpacer_7)

        self.guardad_computadora_btn = QPushButton(self.widget_8)
        self.guardad_computadora_btn.setObjectName(u"guardad_computadora_btn")
        self.guardad_computadora_btn.setMinimumSize(QSize(0, 50))
        icon5 = QIcon()
        icon5.addFile(u"./assets/icons/save-3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.guardad_computadora_btn.setIcon(icon5)

        self.verticalLayout_11.addWidget(self.guardad_computadora_btn)

        self.cancelar_registro_btn = QPushButton(self.widget_8)
        self.cancelar_registro_btn.setObjectName(u"cancelar_registro_btn")
        icon6 = QIcon()
        icon6.addFile(u"./assets/icons/cancel-3.ico", QSize(), QIcon.Normal, QIcon.Off)
        self.cancelar_registro_btn.setIcon(icon6)

        self.verticalLayout_11.addWidget(self.cancelar_registro_btn)


        self.horizontalLayout_7.addWidget(self.widget_8)


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
        font2 = QFont()
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_5.setFont(font2)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.gridLayout_7.addWidget(self.label_5, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_9)

        self.widget_10 = QWidget(self.page_3)
        self.widget_10.setObjectName(u"widget_10")
        self.gridLayout_8 = QGridLayout(self.widget_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(50, 60, -1, -1)
        self.label_15 = QLabel(self.widget_10)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setAlignment(Qt.AlignJustify|Qt.AlignTop)

        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)


        self.verticalLayout_12.addWidget(self.widget_10)

        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.gridLayout_4 = QGridLayout(self.page_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.frame_6 = QFrame(self.page_4)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_6)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(50, 0, 50, 0)
        self.label_9 = QLabel(self.frame_6)
        self.label_9.setObjectName(u"label_9")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        font3.setWeight(75)
        self.label_9.setFont(font3)

        self.gridLayout_5.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font3)

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 1)

        self.nombre_txt = QLineEdit(self.frame_6)
        self.nombre_txt.setObjectName(u"nombre_txt")
        font4 = QFont()
        font4.setPointSize(14)
        self.nombre_txt.setFont(font4)

        self.gridLayout_5.addWidget(self.nombre_txt, 0, 1, 1, 1)

        self.apellidos_txt = QLineEdit(self.frame_6)
        self.apellidos_txt.setObjectName(u"apellidos_txt")
        self.apellidos_txt.setFont(font4)

        self.gridLayout_5.addWidget(self.apellidos_txt, 2, 1, 1, 1)

        self.telefono_txt = QLineEdit(self.frame_6)
        self.telefono_txt.setObjectName(u"telefono_txt")
        self.telefono_txt.setFont(font4)

        self.gridLayout_5.addWidget(self.telefono_txt, 3, 1, 1, 1)

        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font3)

        self.gridLayout_5.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_8 = QLabel(self.frame_6)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font3)

        self.gridLayout_5.addWidget(self.label_8, 3, 0, 1, 1)

        self.correo_txt = QLineEdit(self.frame_6)
        self.correo_txt.setObjectName(u"correo_txt")
        self.correo_txt.setFont(font4)

        self.gridLayout_5.addWidget(self.correo_txt, 4, 1, 1, 1)


        self.gridLayout_4.addWidget(self.frame_6, 0, 0, 1, 2)

        self.frame_8 = QFrame(self.page_4)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.agregar_admin_btn = QPushButton(self.frame_8)
        self.agregar_admin_btn.setObjectName(u"agregar_admin_btn")
        self.agregar_admin_btn.setMinimumSize(QSize(150, 150))
        self.agregar_admin_btn.setMaximumSize(QSize(150, 16777215))
        self.agregar_admin_btn.setFont(font)

        self.verticalLayout_8.addWidget(self.agregar_admin_btn)


        self.gridLayout_4.addWidget(self.frame_8, 3, 0, 1, 1, Qt.AlignRight|Qt.AlignBottom)

        self.frame_7 = QFrame(self.page_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(150, 16777215))
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_7)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 30)
        self.modificar_btn = QPushButton(self.frame_7)
        self.modificar_btn.setObjectName(u"modificar_btn")

        self.verticalLayout_7.addWidget(self.modificar_btn)

        self.guardar_btn = QPushButton(self.frame_7)
        self.guardar_btn.setObjectName(u"guardar_btn")
        icon7 = QIcon()
        icon7.addFile(u"./assets/icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.guardar_btn.setIcon(icon7)

        self.verticalLayout_7.addWidget(self.guardar_btn)

        self.cancelar_btn = QPushButton(self.frame_7)
        self.cancelar_btn.setObjectName(u"cancelar_btn")
        self.cancelar_btn.setIcon(icon6)

        self.verticalLayout_7.addWidget(self.cancelar_btn)


        self.gridLayout_4.addWidget(self.frame_7, 3, 1, 1, 1, Qt.AlignBottom)

        self.frame_10 = QFrame(self.page_4)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMinimumSize(QSize(700, 0))
        self.frame_10.setMaximumSize(QSize(16777215, 50))
        self.frame_10.setStyleSheet(u"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_10)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.cerrar_sesion_btn = QPushButton(self.frame_10)
        self.cerrar_sesion_btn.setObjectName(u"cerrar_sesion_btn")

        self.gridLayout_9.addWidget(self.cerrar_sesion_btn, 0, 0, 1, 1)


        self.gridLayout_4.addWidget(self.frame_10, 4, 0, 1, 1, Qt.AlignHCenter)

        self.stackedWidget.addWidget(self.page_4)
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
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.widget = QWidget(self.frame_4)
        self.widget.setObjectName(u"widget")
        self.widget.setMaximumSize(QSize(16777215, 60))
        self.widget.setStyleSheet(u"")
        self.horizontalLayout_5 = QHBoxLayout(self.widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_5.addWidget(self.label_2)

        self.horizontalSpacer_2 = QSpacerItem(845, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_6.addWidget(self.widget)

        self.widget_2 = QWidget(self.frame_4)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(self.widget_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabla_computadoras_activas = QTableWidget(self.widget_2)
        if (self.tabla_computadoras_activas.columnCount() < 3):
            self.tabla_computadoras_activas.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tabla_computadoras_activas.setHorizontalHeaderItem(2, __qtablewidgetitem2)
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
        if (self.tabla_computadoras_desactivas.columnCount() < 3):
            self.tabla_computadoras_desactivas.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tabla_computadoras_desactivas.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tabla_computadoras_desactivas.setObjectName(u"tabla_computadoras_desactivas")

        self.gridLayout_3.addWidget(self.tabla_computadoras_desactivas, 0, 0, 1, 1)


        self.verticalLayout_6.addWidget(self.widget_4)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.page_2)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(100, 16777215))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer_3 = QSpacerItem(20, 174, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_3)

        self.activar_btn = QPushButton(self.frame_5)
        self.activar_btn.setObjectName(u"activar_btn")
        self.activar_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.activar_btn)

        self.activar_compus_btn = QPushButton(self.frame_5)
        self.activar_compus_btn.setObjectName(u"activar_compus_btn")
        self.activar_compus_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.activar_compus_btn)

        self.verticalSpacer_2 = QSpacerItem(20, 174, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.desactivar_btn = QPushButton(self.frame_5)
        self.desactivar_btn.setObjectName(u"desactivar_btn")
        self.desactivar_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.desactivar_btn)

        self.desactivar_compus_btn = QPushButton(self.frame_5)
        self.desactivar_compus_btn.setObjectName(u"desactivar_compus_btn")
        self.desactivar_compus_btn.setMinimumSize(QSize(0, 50))

        self.verticalLayout_5.addWidget(self.desactivar_compus_btn)

        self.verticalSpacer_4 = QSpacerItem(20, 174, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_4)


        self.horizontalLayout_4.addWidget(self.frame_5)

        self.stackedWidget.addWidget(self.page_2)

        self.horizontalLayout_3.addWidget(self.stackedWidget)


        self.verticalLayout.addWidget(self.frame_3)


        self.horizontalLayout.addWidget(self.body_widget)


        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        Principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(Principal)
        self.pushButton_4.clicked.connect(Principal.close)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(Principal)
    # setupUi

    def retranslateUi(self, Principal):
        Principal.setWindowTitle(QCoreApplication.translate("Principal", u"MainWindow", None))
        self.label.setText("")
        self.home_btn.setText("")
        self.data_btn.setText("")
        self.settings_btn.setText("")
        self.pushButton_4.setText("")
        self.user_btn.setText("")
        self.label_4.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">AGREGAR COMPUTADORAS</span></p></body></html>", None))
        self.label_10.setText(QCoreApplication.translate("Principal", u"Persona a cargo", None))
        self.persona_cargo_txt.setPlaceholderText(QCoreApplication.translate("Principal", u"Nombre de la persona que va a estar a cargo de la computadora", None))
        self.label_11.setText(QCoreApplication.translate("Principal", u"Computadora", None))
        self.computadora_txt.setPlaceholderText(QCoreApplication.translate("Principal", u"Nombre de la computadora - Modelo", None))
        self.label_12.setText(QCoreApplication.translate("Principal", u"D\u00eda de entrega", None))
        self.dia_txt.setPlaceholderText(QCoreApplication.translate("Principal", u"dd-mm-yyyy", None))
        self.label_13.setText(QCoreApplication.translate("Principal", u"IP", None))
        self.ip_txt.setPlaceholderText(QCoreApplication.translate("Principal", u"0.0.0.0", None))
        self.label_14.setText("")
        self.guardad_computadora_btn.setText("")
        self.cancelar_registro_btn.setText("")
        self.label_5.setText(QCoreApplication.translate("Principal", u"Ayuda", None))
        self.label_15.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p>- Obtener la MAC ADRESS de la computadora que va a ser registrada. </p><p><br/></p><p>- Para poder registrar una nueva computadora, se debe registrar primeramente en la secci\u00f3n de agregar </p><p>computadoras. </p><p><br/></p><p>-Instalar la segunda aplicaci\u00f3n en la computadora que se va a monitorear. </p><p><br/></p><p>-Asegurese que ambas aplicaciones cuenten con una conexi\u00f3n a internet, si no, el programa no podra ser utilizado </p><p>correctamente.</p></body></html>", None))
        self.label_9.setText(QCoreApplication.translate("Principal", u"Correo", None))
        self.label_6.setText(QCoreApplication.translate("Principal", u"Nombre", None))
        self.label_7.setText(QCoreApplication.translate("Principal", u"Apellidos", None))
        self.label_8.setText(QCoreApplication.translate("Principal", u"Tel\u00e9fono", None))
        self.agregar_admin_btn.setText(QCoreApplication.translate("Principal", u"Agregar nuevo \n"
"Administrador", None))
        self.modificar_btn.setText(QCoreApplication.translate("Principal", u"Modificar informaci\u00f3n", None))
        self.guardar_btn.setText("")
        self.cancelar_btn.setText("")
        self.cerrar_sesion_btn.setText(QCoreApplication.translate("Principal", u"Cerrar Sesi\u00f3n", None))
        self.label_2.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:12pt;\">Computadoras </span><span style=\" font-size:12pt; color:#00aa00;\">activas</span></p></body></html>", None))
        ___qtablewidgetitem = self.tabla_computadoras_activas.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Principal", u"Desktop", None));
        ___qtablewidgetitem1 = self.tabla_computadoras_activas.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Principal", u"Nombre", None));
        ___qtablewidgetitem2 = self.tabla_computadoras_activas.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Principal", u"IP", None));
        self.label_3.setText(QCoreApplication.translate("Principal", u"<html><head/><body><p><span style=\" font-size:12pt;\">Computadoras </span><span style=\" font-size:12pt; color:#ff0206;\">desactivadas</span></p></body></html>", None))
        ___qtablewidgetitem3 = self.tabla_computadoras_desactivas.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Principal", u"Desktop", None));
        ___qtablewidgetitem4 = self.tabla_computadoras_desactivas.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Principal", u"Nombre", None));
        ___qtablewidgetitem5 = self.tabla_computadoras_desactivas.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Principal", u"IP", None));
        self.activar_btn.setText(QCoreApplication.translate("Principal", u"Activar", None))
        self.activar_compus_btn.setText(QCoreApplication.translate("Principal", u"Activar \n"
"Computadoras", None))
        self.desactivar_btn.setText(QCoreApplication.translate("Principal", u"Desactivar", None))
        self.desactivar_compus_btn.setText(QCoreApplication.translate("Principal", u"Desactivar \n"
"Computadoras", None))
    # retranslateUi

