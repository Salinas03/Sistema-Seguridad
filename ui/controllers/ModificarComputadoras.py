from PySide2.QtWidgets import *
from views.EditarEquipo import EditarComputadoras
from db.connection import conexion
from modelos.equipos_consultas import Equipo
from PySide2.QtCore import Qt, QRegExp
from PySide2.QtGui import QRegExpValidator


class ModificarEquipoWindow(EditarComputadoras, QWidget):

    def __init__(self, funcion ,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()
        self.actualizar_tabla = funcion
    
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
        data = Equipo(conexion()).seleccionar_equipo_id(self._id)

        if len(data) >= 1:
            equipo = data[0]
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

        data = [equipo,numSerie,propietario,rol]

        if self.checar_inputs():
            equipo = Equipo(conexion())
            if equipo.actualizar_equipo(self._id, data):
                QMessageBox.information(self, 'Actualización', 'El equipo se actualizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.actualizar_tabla(equipo.seleccionar_compus())
                self.close()

    def cancelar_registro(self):
        self.close()     
