from PySide2.QtWidgets import *
from views.EditarEquipo import EditarComputadoras
from db.connection import conexion
from modelos.equipos_consultas import Equipo
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
from utils.crear_mensaje_emergente import crear_message_box
import json

class ModificarEquipoWindow(EditarComputadoras, QWidget):

    def __init__(self ,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()
    
        only_text = QRegExpValidator(QRegExp('^[A-Za-z0-9-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES

        self.nombre_equipo_txt.setValidator(only_text)
        self.nombre_equipo_txt.setFocus()
        self.num_serie_txt.setValidator(only_text)
        # self.propietario_equipo_txt.setValidator(propietario_text)
        # self.rol_txt.setValidator(rol)

        self.x = self.modificar_compu_btn.clicked.connect(self.editar_compus)
        self.y = self.cancelar_registro_btn.clicked.connect(self.cancelar_registro)

    def llenar_campos_texto(self):
        peticion = {
            'tabla': 'equipos',
            'operacion': 'obtener_equipo_computo_por_id',
            'id': self._id
        }
        
        data = admin_socket_ui.escribir_operaciones(json.dumps(peticion))
        if data['success']:
            data = data['data'][0]
            if len(data) >= 1:
                equipo = data
                #Llenado de datos con los datos de propietario por ID
                self.nombre_equipo_txt.setText(equipo[1])
                self.num_serie_txt.setText(equipo[2])
                indice = self.establecer_indices_combobox(equipo[3])
                self.edita_propietario_cmbx.setCurrentIndex(indice)

                if equipo[4] == '1':
                    self.edita_rol_cmbx.setCurrentIndex(1)
                elif equipo[4] == '0':
                    self.edita_rol_cmbx.setCurrentIndex(2)
                
            else:
                print('No existe ningún valor')
    
    def establecer_indices_combobox(self, id_propietario):
        propietarios = self.propietarios['data']
        for i, propietario in enumerate(propietarios):
            if propietario[0] == id_propietario:
                return i + 1

    def checar_inputs(self):
        equipo = self.nombre_equipo_txt.text()
        numSerie = self.num_serie_txt.text()
        propietario = self.propietario_equipo_txt.text()
        rol = self.rol_txt.text()

        errores_count = 0

        if equipo == '' or numSerie == '' or propietario == '' or rol == '':
            crear_message_box('Error', 'Favor de escribir datos válidos', 'warning').exec_()
            errores_count +=1
        elif errores_count == 0:
            return True
    
    def editar_compus(self):
        equipo = self.nombre_equipo_txt.text()
        numSerie = self.num_serie_txt.text()
        propietario = self.edita_propietario_cmbx.currentText().split('.')[0]
        rol = self.edita_rol_cmbx.currentIndex()

        if equipo == '' or numSerie == '':
            crear_message_box('Error', 'Favor de escribir datos válidos', 'warning').exec_()

        else:
            valor_rol = None

            if rol == 1:  # Administrador
                valor_rol = 1
            elif rol == 2:  # Cliente
                valor_rol = 0

            if propietario[0] != 'S':
                if valor_rol is not None:
                     
                    peticion = {
                        'tabla': 'equipos',
                        'operacion': 'actualizar',
                        'id': self._id,
                        'data': [equipo,numSerie,propietario,valor_rol]
                    }
                     
                    respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                    if respuesta['success']:
                        self.nombre_equipo_txt.clear()
                        self.num_serie_txt.clear()
                        crear_message_box('Actualización hecha con éxito', 'La actualización se ha realizado exitosamente', 'information').exec_()
                        self.close() 

                    else:
                        crear_message_box('Ooops... algo ocurrió', 'Hubo un error al actualizar', 'error').exec_()
                        self.close() 

                else:
                    crear_message_box('Advertencia', 'Seleccione un rol para el equipo', 'warning').exec_()
            else: 
                crear_message_box('Advertencia', 'Seleccione un propietario del equipo', 'warning').exec_()
            

    def cancelar_registro(self):
        self.close()     
