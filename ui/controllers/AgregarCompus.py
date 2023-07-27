from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarComputadoras import AgregarComputadoras
from PySide2.QtCore import *
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
from utils.crear_mensaje_emergente import crear_message_box
import json

class AgregarCompusWindow(AgregarComputadoras, QWidget):
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_text = QRegExpValidator(QRegExp('^[A-Za-z0-9- ]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 
        self.nombre_equipo_txt.setValidator(only_text)
        self.nombre_equipo_txt.setFocus()
        self.num_serie_txt.setValidator(only_text)

        self.x = self.guardar_compu_btn.clicked.connect(self.agregar_compus)
        self.y = self.cancelar_registro_btn.clicked.connect(self.cancelar_registro)

    def agregar_compus(self):
        equipo = self.nombre_equipo_txt.text()
        numSerie = self.num_serie_txt.text()

        id_propietario = None
        cadena = self.propietario_cmbx.currentText()
        if '.' in cadena:
            id_propietario = cadena.split('.')[0]

        rol = self.rol_cmbx.currentIndex()

        if equipo == '' or numSerie == '' or rol == None:
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        else:
            valor_rol = None

            if rol == 1:  # Administrador
                valor_rol = 1
            elif rol == 2:  # Cliente
                valor_rol = 0

            if id_propietario is not None:
                if valor_rol is not None:
                    objeto_insertar = {
                        'tabla': 'equipos',
                        'operacion': 'insertar',
                        'data': [equipo, numSerie, id_propietario, valor_rol]     
                    }

                    respuesta = admin_socket_ui.escribir_operaciones(json.dumps(objeto_insertar))
                        
                    if respuesta['success']:
                        self.nombre_equipo_txt.clear()
                        self.num_serie_txt.clear()
                        crear_message_box('Registro realizado con éxito', 'El registro se hizó con éxito', 'information').exec_()
                        self.close()  

                    else:
                        crear_message_box('Ooops... algo ocurrió', respuesta['msg'], 'error').exec_()
                else:
                    crear_message_box('Advertencia', 'Seleccione un rol para el equipo', 'warning').exec_()
            else:
                crear_message_box('Advertencia', 'Seleccione un propietario del equipo', 'warning').exec_()


    def cancelar_registro(self):
        self.close()     

        