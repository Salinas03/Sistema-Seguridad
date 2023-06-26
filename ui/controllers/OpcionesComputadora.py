from PySide2.QtWidgets import QWidget,QMessageBox, QPushButton
from views.OpcionesComputadoras import OpcionesComputadora
from modelos.equipos_consultas import Equipo
from db.connection import conexion

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self, parent = None, _id = None, numSerie = None):
        self._id = _id
        self.numSerie= numSerie
        super().__init__(parent)
        self.setupUi(self)
        
        self.llenar_etiquetas()

    def llenar_etiquetas(self):
        self.id_lbl.setText(str(self._id))
        self.nombre_lbl.setText(str(self.numSerie))

        
    

