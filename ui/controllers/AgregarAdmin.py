from PySide2.QtWidgets import QWidget
from views.AgregarAdmin import AgregarAdmin

class AgregarAdmin(AgregarAdmin, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def mostrar():
        pass