from PySide2.QtWidgets import QWidget,QMessageBox, QPushButton
from views.OpcionesComputadoras import OpcionesComputadora
from modelos.equipos_consultas import Equipo
from db.connection import conexion

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self, parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        
        self.llenar_etiquetas()

    def llenar_etiquetas(self):
        data = Equipo(conexion()).seleccionar_equipo_id(self._id)

        if len(data) >=1:
            equipo = data[0]
            self.id_lbl.setText(str(equipo[0]))
            self.nombre_lbl.setText(str(equipo[1]))
        else:
            print('No existe ningun valor')

        
    

