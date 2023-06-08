from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarComputadoras import AgregarComputadoras
from PySide2.QtCore import Qt
from modelos.equipos_consultas import Equipo
from db.connection import conexion
from PySide2.QtCore import QRegExp, QTimer
from PySide2.QtGui import QRegExpValidator

class AgregarCompusWindow(AgregarComputadoras, QWidget):
    def __init__(self, function):
        super().__init__(None)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.equipo = Equipo(conexion())

        self.actualizar_tabla = function

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_text = QRegExpValidator(QRegExp('^[A-Za-z0-9-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        propietario_text = QRegExpValidator(QRegExp('^[0-9]{1,10}'))
        rol = QRegExpValidator(QRegExp('^[0-1]{1,1}'))

        # only_number = QRegExpValidator(QRegExp('^[0-9.]{7,50}'))
        # only_fecha = QRegExpValidator(QRegExp('^[0-9-/]{10,10}'))

        self.nombre_equipo_txt.setValidator(only_text)
        self.nombre_equipo_txt.setFocus()
        self.num_serie_txt.setValidator(only_text)
        self.propietario_equipo_txt.setValidator(propietario_text)
        self.rol_txt.setValidator(rol)

        self.x = self.guardar_compu_btn.clicked.connect(lambda:self.agregar_compus(self.nombre_equipo_txt.text(), 
                                                                                   self.num_serie_txt.text(), 
                                                                                   self.propietario_equipo_txt.text(), 
                                                                                   self.rol_txt.text()))
        self.y = self.cancelar_registro_btn.clicked.connect(self.cancelar_registro)


    def agregar_compus(self, equipo, numSerie, propietario, rol):
            equipo = self.nombre_equipo_txt.text()
            numSerie = self.num_serie_txt.text()
            propietario = self.propietario_equipo_txt.text()
            rol = self.rol_txt.text()

            if equipo == '' or numSerie == '' or propietario == '' or rol == '':
                QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

            else:
                self.equipo.insertar_compus(equipo,numSerie,propietario,rol)
                self.nombre_equipo_txt.clear()
                self.num_serie_txt.clear()
                self.propietario_equipo_txt.clear()
                self.rol_txt.clear()
                QMessageBox.warning(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.actualizar_tabla(self.equipo.seleccionar_compus())
                self.close()   

    def cancelar_registro(self):
        self.close()     

        