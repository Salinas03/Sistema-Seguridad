from PySide2.QtWidgets import *
from PySide2 import QtWidgets, QtCore, QtWebEngineWidgets
from views.Mapa import Mapa
from PySide2.QtCore import *
import geocoder
import folium

class MapaWindow(Mapa, QWidget):
    def __init__(self, parent = None, ip_publica = None):
        self.ip_publica = ip_publica
        print(self.ip_publica)
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.location()

        if self.location is not False:
            # Crear el widget QWebEngineView
            self.webview = QtWebEngineWidgets.QWebEngineView()
            
            # Configurar la URL inicial
            self.webview.setUrl(QtCore.QUrl("http://127.0.0.1:5500/ui/html/mapa.html"))
            
            # Agregar el widget QWebEngineView a la ventana principal
            self.setCentralWidget(self.webview)
        else:
            print("Error al obtener las coordenadas en el mapa")


    def location(self):
        g = geocoder.ip(self.ip_publica)

        myAddress = g.latlng
        print(myAddress)
                
        if myAddress is not None:
            my_napi = folium.Map(location=myAddress,zoom_start=12)

            folium.CircleMarker(location=myAddress,radius=50, popup="Equipo de computo").add_to(my_napi)

            folium.Marker(myAddress,popup="Equipo de computo").add_to(my_napi)
            my_napi.save("ui/html/mapa.html")
            result = True
        else:
            result = False
            
        print(result)