
# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView
from PySide2 import QtCore
from PySide2.QtCore import Qt
from views.Principal import Principal
from controllers.AgregarAdmin import AgregarAdminWindow
from controllers.AgregarCompus import AgregarCompusWindow
from controllers.OpcionesComputadora import OpcionesCompusWindow
from modelos.admin_model import Admin
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator


class PrincipalWindow(Principal,Admin,QWidget):

    # FUNCION PARA INICIO DE LA VENTANA
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # BOTONES QUE REDIRIGEN A LAS PAGINAS DEL STACKEDWIDGET
        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.compus_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))
        self.admins_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_5))


        # PONER LAS MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_activas = self.tabla_computadoras_activas.horizontalHeader()
        header_computadoras_activas.setSectionResizeMode(header_computadoras_activas.Stretch)

        header_computadoras_desactivas = self.tabla_computadoras_desactivas.horizontalHeader()
        header_computadoras_desactivas.setSectionResizeMode(header_computadoras_desactivas.Stretch)

        header_computadoras_registradas_table = self.computadoras_registradas_table.horizontalHeader()
        header_computadoras_registradas_table.setSectionResizeMode(header_computadoras_registradas_table.Stretch)

        header_administradores_tabla = self.administradores_tabla.horizontalHeader()
        header_administradores_tabla.setSectionResizeMode(header_administradores_tabla.Stretch)
    
        # OCULTAR LOS BOTONES DE ACTIVACION DE Y DESACTIVACION DE COMPUTADORAS
        self.activar_btn.hide()
        self.desactivar_btn.hide()
        self.desactivar_compus_btn.hide()

        # DESHABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADOR
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)
        
        # LLAMADO PARA AGREGAR UN NUEVO ADMINISTRADOR
        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)
        # LLAMADO PARA AGREGAR UNA NUEVA COMPUTADORA
        self.agregar_compu_btn.clicked.connect(self.abrir_agregar_compus)
        
        self.otros_comandos_btn.clicked.connect(self.abrir_opciones_computadora)

        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

        self.modificar_perfil_btn.clicked.connect(self.habilitar_datos_admin)

        self.configuracion_tabla_admins()
        self.datos_admins(self.seleccionar_admins())

        self.guardar_admin_btn.clicked.connect(self.guardar_datos_perfil)


    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE AGREGAR ADMIN
    def abrir_agregar_admin(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta: 
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarAdminWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
        else:
            QMessageBox.warning(self, "Advertencia", "La ventana ya está abierta.")
    
    # FUNCION PARA MANDAR LLAMAR A LA VENTANA DE AGREGAR COMPUS
    def abrir_agregar_compus(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarCompusWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
    
    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE OPCIONES DE COMPUTADORA
    def abrir_opciones_computadora(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True
            window = OpcionesCompusWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
            
    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False

    # CONDICION PARA HABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADORS
    def habilitar_datos_admin(self):
        self.nombre_txt.setEnabled(True)
        self.apellidos_txt.setEnabled(True)
        self.telefono_txt.setEnabled(True)
        self.correo_txt.setEnabled(True)
    
    def configuracion_tabla_admins(self):
        column_headers = ("nombre", "apellido", "telefono", "correo")
        self.administradores_tabla.setColumnCount(len(column_headers))
        self.administradores_tabla.setHorizontalHeaderLabels(column_headers)

        self.administradores_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

    def datos_admins(self,data):
        self.administradores_tabla.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.administradores_tabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
    
    def guardar_datos_perfil(self):
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)
        QMessageBox.warning(self, "Guardado", "Los datos se guardaron correctamente.")
  
    




