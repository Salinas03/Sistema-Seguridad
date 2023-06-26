from PySide2.QtWidgets import QWidget,QMessageBox, QPushButton
from views.OpcionesComputadoras import OpcionesComputadora
from clases.administrador_ui import admin_socket_ui
from utils.abrir_consola import abrir_consola_ejecutar_script

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self, parent = None, _id = None, numSerie = None):
        self._id = _id
        self.numSerie= numSerie
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_etiquetas()
        self.consola_btn = self.pushButton_6
        
        self.apagar_equipo_btn.clicked.connect(self.apagar_equipo)
        self.supender_windows_equipo_btn.clicked.connect(self.suspender_windows)
        self.bloquear_protector_equipo_btn.clicked.connect(self.bloquear_protector)
        self.consola_btn.clicked.connect(self.abrir_consola)

    def llenar_etiquetas(self):
        self.id_lbl.setText(str(self._id))
        self.nombre_lbl.setText(str(self.numSerie))

    def apagar_equipo(self):
        print('Apagar')
        respuesta = admin_socket_ui.escribir_operaciones('apagar')
        print(respuesta)
        if respuesta['success']:
            QMessageBox.information(self, 'Apagado', 'Se realizó la función del apagado de manera correcta', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.close()
        else:
            QMessageBox.critical(self, 'Ooops... Algo ocurrió', 'Hubo un fallo al realizar el apagado del equipo', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 

    def suspender_windows(self):
        print('suspender')
        respuesta = admin_socket_ui.escribir_operaciones('bloquear')
        print(respuesta)
        if respuesta['success']:
            QMessageBox.information(self, 'Suspender', 'Se realizó la función del apagado de manera correcta', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.close()
        else:
            QMessageBox.critical(self, 'Ooops... Algo ocurrió', 'Hubo un fallo al suspender el equipo', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 

    def bloquear_protector(self):
        print('Bloqueo protector')

    def abrir_consola(self):
        print('Abrir consola')
        abrir_consola_ejecutar_script()
        
