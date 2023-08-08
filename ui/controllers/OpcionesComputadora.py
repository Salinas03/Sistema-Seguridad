from PySide2.QtWidgets import QWidget,QMessageBox
from PySide2 import QtCore
from views.OpcionesComputadoras import OpcionesComputadora
from utils.abrir_consola import abrir_consola_ejecutar_script
import sys
import webbrowser
sys.path.append('D:/RedesLA/SistemaSeguridad/ui')
from clases.administrador_ui import admin_socket_ui
from utils.crear_mensaje_emergente import crear_message_box
import geocoder
from py2_msgboxes import msg_boxes

class OpcionesCompusWindow(OpcionesComputadora, QWidget):
    def __init__(self, parent = None, data = None):
        self.data = data
        print(data)
        super().__init__(parent)
        self.setupUi(self)
        self.llenar_etiquetas()
        self.coordenadas()
        self.consola_btn = self.pushButton_6
        
        self.apagar_equipo_btn.clicked.connect(self.apagar_equipo)
        self.supender_windows_equipo_btn.clicked.connect(self.suspender_windows)
        self.consola_btn.clicked.connect(self.abrir_consola)
        self.localizacion_btn.clicked.connect(self.mostrar_ubicacion)

        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

    def llenar_etiquetas(self):
        self.id_lbl.setText(str(self.data[0]))
        self.nombre_lbl.setText(str(self.data[1]))
        self.ip_txt.setText(str(self.data[2]))

    def apagar_equipo(self):
        res = msg_boxes.warning_msg('Advertencia','¿Seguro que desea apagar el equipo de computo?')
        if res == QMessageBox.Yes:
            respuesta = admin_socket_ui.escribir_operaciones('apagar')
            print(respuesta)
            if respuesta['success']:
                crear_message_box('Apagado', 'Se realizó la función del apagado de manera correcta', 'information')
                self.close()
            else:
                crear_message_box('Ooops... Algo ocurrió', 'Hubo un fallo al realizar el apagado del equipo, puede que el equipo se haya desconectado', 'error')

                #Bandera indicando que ya no va a aplicar la funcionalidad de otro mensaje de salir en el evento de cerrado, porque ya automaticamente esta cayendo en la excepcinon entonces no hace falta que vuelva a enviar salir al servidor de loc contrario se saldria del panel del administrador por lo tanto ya no funciona el panel
                self.bandera = False
                self.close() 

    def suspender_windows(self):
        res = msg_boxes.warning_msg('Advertencia','¿Seguro que desea bloquear el equipo de computo?')
        if res == QMessageBox.Yes:
            respuesta = admin_socket_ui.escribir_operaciones('bloquear')
            print(respuesta)
            if respuesta['success']:
                crear_message_box('Suspender', 'Se realizó la función de suspensión de windows de manera exitosa', 'information').exec_()
                self.close()
            else:
                crear_message_box('Ooops... Algo ocurrió', 'Hubo un fallo al suspender el equipo, puede que el equipo se haya desconectado', 'error')
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
            crear_message_box('Ooops... Algo ocurrió', 'Hubo un fallo al abrir la consola del equipo, puede que el equipo se haya desconectado', 'error')
            self.bandera = False
            self.close()
    
    def mostrar_ubicacion(self):
        url = "https://account.microsoft.com/devices"  # Aquí debes especificar la URL que deseas abrir
        # Abre el enlace en el navegador predeterminado
        webbrowser.open(url)

    def coordenadas(self):
        g = geocoder.ip(self.data[2])
        myaddress = g.latlng

        if myaddress:
            latitude = myaddress[0]
            longitude = myaddress[1]

            self.latitud_txt.setText(str(latitude))
            print(f'Latitud: {latitude}')
            self.longitud_txt.setText(str(longitude))
            print(f'Longitud: {longitude}')
        else:
            print('No se pudo obtener la ubicación.')
    
    def ventana_cerrada(self):
        self.ventana_abierta = False
        