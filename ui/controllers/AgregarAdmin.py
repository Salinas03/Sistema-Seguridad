from PySide2.QtWidgets import QWidget
from views.AgregarAdmin import AgregarAdmin
from PySide2.QtCore import Qt

class AgregarAdminWindow(AgregarAdmin, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

    def mostrar():
        pass