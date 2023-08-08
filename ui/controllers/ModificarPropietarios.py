from PySide2.QtWidgets import *
from views.EditarPropietario import EditarPropietario
from PySide2.QtCore import Qt, QRegExp 
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
from utils.crear_mensaje_emergente import crear_message_box
import json

class ModificarPropietarioWindow(EditarPropietario,QWidget):
    
    def __init__(self ,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()


        only_text = QRegExpValidator(QRegExp('^[A-Za-z ]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        self.nombre_propietario_txt.setValidator(only_text)
        self.nombre_propietario_txt.setFocus()
        self.apellido_propietario_txt.setValidator(only_text)
        self.telefono_propietario_txt.setValidator(only_number)

        self.agregar_admin_btn.clicked.connect(self.editar_propietario)
        self.cancelar_admin_btn.clicked.connect(self.cerrar_ventana)

    def llenar_campos_texto(self):
        
        peticion = {
            'tabla': 'propietarios',
            'operacion': 'obtener_propietario_id',
            'id': self._id
        }

        data = admin_socket_ui.escribir_operaciones(json.dumps(peticion))
        
        if data['success']:
            data = data['data'][0]
            if len(data) >= 1:
                propietario = data
                self.nombre_propietario_txt.setText(propietario[1])
                self.apellido_propietario_txt.setText(propietario[2])
                self.telefono_propietario_txt.setText(propietario[3])
                self.correo_propietario_txt.setText(propietario[4])

                if propietario[5] == 1:
                    self.editar_rol_cmbx.setCurrentIndex(1)

                elif propietario[5] == 0:
                    self.editar_rol_cmbx.setCurrentIndex(2)

            else:
                print('No existe ningún valor')

    def checar_inputs(self):
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()

        errores_count = 0

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == '' :
            crear_message_box('Error', 'Favor de escribir datos válidos', 'warning').exec_()
            errores_count +=1
        elif errores_count == 0:
            return True
                    
    def editar_propietario(self):
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()
        rol = self.editar_rol_cmbx.currentIndex()


        if self.checar_inputs():

            valor_rol = None
            if rol == 1:
                valor_rol = 1
            
            elif rol == 2:
                valor_rol = 0

            if valor_rol is not None:
                data = [nombre,apellido,telefono,correo,valor_rol]

                peticion = {
                    'tabla': 'propietarios',
                    'operacion': 'actualizar',
                    'data': data,
                    'id': self._id
                }

                respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                if respuesta['success']:
                    crear_message_box('Actualización', 'El propietario se actualizó con éxito', 'information').exec_()
                    self.close()

                else:
                    crear_message_box('Ooops... algo ocurrió', 'Hubo un error al realizar la actualización', 'error').exec_()
                    self.close()

            else:
                crear_message_box('Advertencia', 'Seleccione un rol para el propietario', 'warning').exec_()
                self.close()
                
    def cerrar_ventana(self):
        self.close()
                
