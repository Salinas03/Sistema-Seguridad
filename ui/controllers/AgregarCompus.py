from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarComputadoras import AgregarComputadoras
from modelos.compus_model import Compus
from PySide2.QtCore import Qt
from db.connection import conexion

class AgregarCompusWindow(AgregarComputadoras, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)