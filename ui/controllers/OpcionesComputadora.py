from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2 import QtCore
from views.OpcionesComputadoras import OpcionesComputadora
from utils.abrir_consola import abrir_consola_ejecutar_script
from controllers.Mapa import MapaWindow

import sys
import webbrowser
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
        self.localizacion_btn.clicked.connect(self.mostrar_ubicacion)

        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA


    def llenar_etiquetas(self):
        self.id_lbl.setText(str(self.data[0]))
        self.nombre_lbl.setText(str(self.data[1]))

    def apagar_equipo(self):
        respuesta = admin_socket_ui.escribir_operaciones('apagar')
        print(respuesta)
        if respuesta['success']:
            QMessageBox.information(self, 'Apagado', 'Se realizó la función del apagado de manera correcta', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.close()
        else:
            QMessageBox.critical(self, 'Ooops... Algo ocurrió', 'Hubo un fallo al realizar el apagado del equipo, puede que el equipo se haya desconectado', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 

            #Bandera indicando que ya no va a aplicar la funcionalidad de otro mensaje de salir en el evento de cerrado, porque ya automaticamente esta cayendo en la excepcinon entonces no hace falta que vuelva a enviar salir al servidor de loc contrario se saldria del panel del administrador por lo tanto ya no funciona el panel
            self.bandera = False
            self.close() 

    def suspender_windows(self):
        respuesta = admin_socket_ui.escribir_operaciones('bloquear')
        print(respuesta)
        if respuesta['success']:
            QMessageBox.information(self, 'Suspender', 'Se realizó la función del apagado de manera correcta', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.close()
        else:
            QMessageBox.critical(self, 'Ooops... Algo ocurrió', 'Hubo un fallo al suspender el equipo, puede que el equipo se haya desconectado', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.bandera = False
            self.close()

    def abrir_consola(self):
        respuesta = admin_socket_ui.escribir_operaciones('consola')
        print(respuesta)
        if respuesta['success']:
            consola = respuesta['consola']
            abrir_consola_ejecutar_script(consola)
            print('Proceso realizado')
        else:
            QMessageBox.critical(self, 'Ooops... Algo ocurrió', 'Hubo un fallo al abrir la consola del equipo, puede que el equipo se haya desconectado', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
            self.bandera = False
            self.close()
    
    def mostrar_ubicacion(self):
        url = "https://account.microsoft.com/devices"  # Aquí debes especificar la URL que deseas abrir
        # Abre el enlace en el navegador predeterminado
        webbrowser.open(url)
    
    def ventana_cerrada(self):
        self.ventana_abierta = False
        
