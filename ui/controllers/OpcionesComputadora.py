from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2 import QtCore
from views.OpcionesComputadoras import OpcionesComputadora
from utils.abrir_consola import abrir_consola_ejecutar_script
from controllers.Mapa import MapaWindow

import sys
sys.path.append('D:/RedesLA/SistemaSeguridad/ui')
from clases.administrador_ui import admin_socket_ui

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self, parent = None, data = None):
        self.data = data
        print(data)
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_etiquetas()
        self.consola_btn = self.pushButton_6
        
        self.apagar_equipo_btn.clicked.connect(self.apagar_equipo)
        self.supender_windows_equipo_btn.clicked.connect(self.suspender_windows)
        self.consola_btn.clicked.connect(self.abrir_consola)

        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA


    def llenar_etiquetas(self):
        self.id_lbl.setText(str(self.data[0]))
        self.nombre_lbl.setText(str(self.data[1]))
        

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

    def abrir_consola(self):
        print('Abrir consola')
        respuesta = admin_socket_ui.escribir_operaciones('consola')
        print(respuesta)

        if respuesta['success']:
            consola = respuesta['consola']
            abrir_consola_ejecutar_script(consola)

        print('Proceso realizado')
    
    def mostrar_ubicacion(self):
        ip_publica = str(self.data[2])
        if not self.ventana_abierta:
            self.ventana_abierta:True
            window = MapaWindow(self,ip_publica)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
        else:
            QMessageBox.warning(self, "Advertencia", "La ventana ya está abierta.")


    
    def ventana_cerrada(self):
        self.ventana_abierta = False
        
