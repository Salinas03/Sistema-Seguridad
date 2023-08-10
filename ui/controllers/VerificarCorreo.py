from views.VerificarCorreo import VerificarCorreo
from PySide2.QtWidgets import *
from PySide2.QtCore import Qt
from clases.administrador_ui import admin_socket_ui
from utils.correo import verificacion
from utils.crear_mensaje_emergente import crear_message_box
import json

class VerificarCorreoWindow(VerificarCorreo, QWidget):
    def __init__(self, parent=None, data = None, codigo = None, cerrar_insertar = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.data = data
        self.codigo = codigo
        self.verificar_btn.clicked.connect(self.insertar_propietario)
        self.cerrar_insertar = cerrar_insertar

    def insertar_propietario(self):
        codigo_txt = self.codigo_verificacion_txt.text()
        if codigo_txt == '':
            crear_message_box('Advertencia','Ingrese el codigo de verificacion','warning').exec_()
            #QMessageBox.warning(self, 'Advertencia', 'Ingrese el codigo de verificacion', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        else: 
            if verificacion(codigo_txt, self.codigo):
                #QMessageBox.information(self, 'Codigo correcto', 'El codigo de verificacion es valido', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                crear_message_box('Codigo correcto','El codigo de verificacion es valido','information').exec_()

                peticion = {
                    'tabla': 'propietarios',
                    'operacion': 'insertar',
                    'data': self.data
                }

                respuesta_insertar = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                if respuesta_insertar['success']:
                    #QMessageBox.information(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                    crear_message_box('Registro','El registro se hizo con exito','information').exec_()
                    self.close()
                    self.cerrar_insertar()
                    
                else:
                    #QMessageBox.critical(self, 'Oops, algo ocurrio', 'Hubo un problema al realizar el registro', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                    crear_message_box('Oops, algo ocurrio','Hubo un problema al realizar el registro','critical').exec_()
                    self.close()

            else:
                crear_message_box('Advertencia','El codigo que ingreso no es valido','warning').exec_()
                #QMessageBox.warning(self, 'Advertencia', 'El codigo que ingreso no es valido', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()


                



    