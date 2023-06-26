from PySide2.QtWidgets import *
from PySide2.QtCore import Qt, QRegExp 
from views.EditarPerfil import EditarPerfil

class ModificarPerfil(EditarPerfil, QWidget):
    def __init__(self,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        