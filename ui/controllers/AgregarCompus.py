from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarComputadoras import AgregarComputadoras
from modelos.compus_model import Compus
from PySide2.QtCore import Qt
from db.connection import conexion
from PySide2.QtCore import QRegExp, QTimer
from PySide2.QtGui import QRegExpValidator

class AgregarCompusWindow(AgregarComputadoras, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_text = QRegExpValidator(QRegExp('^[A-Za-z-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9.]{7,50}'))
        only_fecha = QRegExpValidator(QRegExp('^[0-9-/]{10,10}'))


        self.persona_cargo_txt.setValidator(only_text)
        self.computadora_txt.setValidator(only_text)
        self.dia_txt.setValidator(only_fecha)
        self.ip_txt.setValidator(only_number)

        self.x = self.guardar_compu_btn.clicked.connect(lambda:self.agregar_compus(self.persona_cargo_txt.text(), 
                                                                                   self.computadora_txt.text(), 
                                                                                   self.dia_txt.text(), 
                                                                                   self.ip_txt.text()))
        self.y = self.cancelar_registro_btn.clicked.connect(self.cancelar_registro)


    def agregar_compus(self, persona, computadora, dia, macaddress):
            persona = self.persona_cargo_txt.text()
            computadora = self.computadora_txt.text()
            dia = self.dia_txt.text()
            macaddress = self.ip_txt.text()

            if persona == '' or computadora == '' or dia == '' or macaddress == '':
                QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

            else:
                self.persona_cargo_txt.clear()
                self.computadora_txt.clear()
                self.dia_txt.clear()
                self.ip_txt.clear()
                QMessageBox.warning(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()   

    def cancelar_registro(self):
        self.close()     

        