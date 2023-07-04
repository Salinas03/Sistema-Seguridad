from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QRegExp 
from views.EditarPerfil import EditarPerfil
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
import json

class ModificarPerfilWindow(EditarPerfil, QWidget):
    def __init__(self,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()

        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))

        self.nombre_perfil_editar_txt.setValidator(only_text)
        self.nombre_perfil_editar_txt.setFocus()
        self.apellidos_perfil_editar_txt.setValidator(only_text)
        self.telefono_perfil_editar_txt.setValidator(only_number)
        
        self.Modificar_perfil_btn.clicked.connect(self.editar_perfil)
        self.cancelar_perfil_btn.clicked.connect(self.cancelar_modificacion)

    
    def llenar_campos_texto(self):
        peticion = {
            'tabla': 'propietarios',
            'operacion':'obtener_propietario_id',
            'id': self._id
        }

        data = admin_socket_ui.escribir_operaciones(json.dumps(peticion))


        if data['success']:
            data = data['data'][0]
            if len(data) >= 1:
                propietario = data
                self.nombre_perfil_editar_txt.setText(propietario[1])
                self.apellidos_perfil_editar_txt.setText(propietario[2])
                self.telefono_perfil_editar_txt.setText(int(propietario[3]))
                self.correo_perfil_editar_txt.setText(propietario[4])

            else:
                print('No existe nigun valor')
        
    def checar_inputs(self):
        nombre = self.nombre_perfil_editar_txt.text()
        apellido = self.apellidos_perfil_editar_txt.text()
        telefono = self.telefono_perfil_editar_txt.text()
        correo = self.correo_perfil_editar_txt.text()

        errores_count = 0

        if nombre == '' or apellido == '' or telefono == '' or correo == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            errores_count += 1
        elif errores_count == 0:
            return True
    
    def editar_perfil(self):
        nombre = self.nombre_perfil_editar_txt.text()
        apellido = self.apellidos_perfil_editar_txt.text()
        telefono = self.telefono_perfil_editar_txt.text()
        correo = self.correo_perfil_editar_txt.text()

        if self.checar_inputs():
            data = [nombre,apellido,telefono,correo]

            peticion = {
                'tabla': 'propietarios',
                'operacion':'actualizar',
                'data':data,
                'id':self._id
            }

            respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

            if respuesta['success']:
                QMessageBox.information(self, 'Actualización', 'El propietario se actualizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()

            else:
                QMessageBox.critical(self, 'Ooops... algo ocurrio', 'Hubo un error al realizar la actualización', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()
        else:
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un rol para el propietario', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            self.close()
    
    def cancelar_modificacion(self):
        self.close()
 
        