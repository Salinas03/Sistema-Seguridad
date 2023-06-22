from PySide2.QtWidgets import *
from views.EditarEquipo import EditarComputadoras
from db.connection import conexion
from modelos.equipos_consultas import Equipo
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
import json

class ModificarEquipoWindow(EditarComputadoras, QWidget):

    def __init__(self ,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()
    
        only_text = QRegExpValidator(QRegExp('^[A-Za-z0-9-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        propietario_text = QRegExpValidator(QRegExp('^[0-9]{1,10}'))
        rol = QRegExpValidator(QRegExp('^[0-1]{1,1}'))

        self.nombre_equipo_txt.setValidator(only_text)
        self.nombre_equipo_txt.setFocus()
        self.num_serie_txt.setValidator(only_text)
        self.propietario_equipo_txt.setValidator(propietario_text)
        self.rol_txt.setValidator(rol)

        self.x = self.modificar_compu_btn.clicked.connect(self.editar_compus)
        self.y = self.cancelar_registro_btn.clicked.connect(self.cancelar_registro)

    def llenar_campos_texto(self):
        peticion = {
            'tabla': 'equipos',
            'operacion': 'obtener_equipo_computo_por_id',
            'id': self._id
        }
        
        #REALIZAR OPERACIONES CON LAS PETICIONES DE LOS SOCKETS
        data = admin_socket_ui.escribir_operaciones(json.dumps(peticion))
        
        if data['success']:
            data = data['data'][0]
            if len(data) >= 1:
                equipo = data
                self.nombre_equipo_txt.setText(equipo[1])
                self.num_serie_txt.setText(equipo[2])
                self.propietario_equipo_txt.setText(str(equipo[3]))
                self.rol_txt.setText(str(equipo[4]))
            else:
                print('No existe ningún valor')
    
    def checar_inputs(self):
        equipo = self.nombre_equipo_txt.text()
        numSerie = self.num_serie_txt.text()
        propietario = self.propietario_equipo_txt.text()
        rol = self.rol_txt.text()

        errores_count = 0

        if equipo == '' or numSerie == '' or propietario == '' or rol == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            errores_count +=1
        elif errores_count == 0:
            return True
    
    def editar_compus(self):
        equipo = self.nombre_equipo_txt.text()
        numSerie = self.num_serie_txt.text()
        propietario = self.propietario_equipo_txt.text()
        rol = self.rol_txt.text()

        peticion = {
            'tabla': 'equipos',
            'operacion': 'actualizar',
            'id': self._id,
            'data': [equipo,numSerie,propietario,rol]
        }

        if self.checar_inputs():
            respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

            print('RESPUESTA DE OPERACIÓN DE ACTUALIZAR')
            print(respuesta)

            if respuesta['success']:
                QMessageBox.information(self, 'Actualización', 'El equipo se actualizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()

    def cancelar_registro(self):
        self.close()     
