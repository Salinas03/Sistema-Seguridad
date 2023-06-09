from PySide2.QtWidgets import QWidget,QMessageBox, QPushButton
from views.OpcionesComputadoras import OpcionesComputadora

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self,):
        super().__init__(None)
        self.setupUi(self)

        self.comando_widget.hide()

        self.comandos_cbx.currentIndexChanged.connect(self.seleccionar_comandos)

        self.pushButton_7.clicked.connect(self.mostrar_comandos_manualmente)

        for button in self.findChildren(QPushButton):
            button.setVisible(False)
            self.ingresar_comandos_btn.show()

    def seleccionar_comandos(self, index):
        # Ocultar todos los botones
        for button in self.findChildren(QPushButton):
            button.setVisible(False)
            self.ingresar_comandos_btn.show()
            self.comando_widget.hide()

        # Obtener el nombre del botón correspondiente al índice seleccionado y mostrarlo
        button_name = f"pushButton_{index + 1}"
        button = self.findChild(QPushButton, button_name)
        button.setVisible(True)

    def mostrar_comandos_manualmente(self):
        self.comando_widget.show()

        
    

