from PySide2.QtWidgets import QWidget,QMessageBox
from views.OpcionesComputadoras import MainWindow

class OpcionesCompusWindow(MainWindow, QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.comando_widget.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.pushButton_6.hide()
        self.pushButton_7.hide()

