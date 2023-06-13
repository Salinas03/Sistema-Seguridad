
# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget, QMessageBox, QTableWidgetItem, QAbstractItemView, QTableWidget
from PySide2 import QtCore
from views.Principal import Principal
from controllers.AgregarAdmin import AgregarpropietarioWindow
from controllers.AgregarCompus import AgregarCompusWindow
from controllers.OpcionesComputadora import OpcionesCompusWindow
from controllers.ModificarPropietarios import ModificarPropietarioWindow
from modelos.propietarios_consultas import Propietario
from db.connection import conexion
from modelos.equipos_consultas import Equipo


class PrincipalWindow(Principal,QWidget):

    # FUNCION PARA INICIO DE LA VENTANA
    def __init__(self):
        super().__init__(None)
        self.setupUi(self)
        self.conexion = conexion()


        # BOTONES QUE REDIRIGEN A LAS PAGINAS DEL STACKEDWIDGET
        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.compus_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))
        self.admins_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_5))

        # < --------------------- PAGINA PRINCIPAL --------------------- > 

        # CONTROL DE COMPUTADORAS
        self.activar_btn.clicked.connect(self.activar_computadora)
        self.activar_compus_btn.clicked.connect(self.activar_computadoras)
        self.desactivar_btn.clicked.connect(self.desactivar_computadora)
        self.desactivar_compus_btn.clicked.connect(self.desactivar_computadoras)

        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_activas = self.tabla_computadoras_activas.horizontalHeader()
        header_computadoras_activas.setSectionResizeMode(header_computadoras_activas.Stretch)

        header_computadoras_desactivas = self.tabla_computadoras_desactivas.horizontalHeader()
        header_computadoras_desactivas.setSectionResizeMode(header_computadoras_desactivas.Stretch)

        # OCULTAR LOS BOTONES DE ACTIVACION DE Y DESACTIVACION DE COMPUTADORAS
        self.desactivar_btn.setVisible(False)
        self.desactivar_compus_btn.setVisible(False)

        # BlOQUEO DE BOTON OTROS COMANDOS
        self.otros_comandos_btn.setEnabled(False)

        self.otros_comandos_btn.clicked.connect(self.abrir_opciones_computadora)


        # < --------------------- PAGINA COMPUTADORAS REGISTRADAS --------------------- >

        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_registradas_table = self.computadoras_registradas_table.horizontalHeader()
        header_computadoras_registradas_table.setSectionResizeMode(header_computadoras_registradas_table.Stretch)

        # LLAMADO PARA AGREGAR UNA NUEVA COMPUTADORA
        self.agregar_compu_btn.clicked.connect(self.abrir_agregar_compus)
        self.configuracion_tabla_compus()

        # < --------------------- PAGINA ADMINISTRADORES REGISTRADOS --------------------- >

        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_administradores_tabla = self.administradores_tabla.horizontalHeader()
        header_administradores_tabla.setSectionResizeMode(header_administradores_tabla.Stretch)
        # LLAMADO PARA AGREGAR UN NUEVO ADMINISTRADOR
        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)
        self.y = self.eliminar_admin_btn.clicked.connect(self.eliminar_propietario)
        self.x = self.administradores_tabla.itemDoubleClicked.connect(self.modificar_propietarios)
        #self.administradores_tabla.cellDoubleClicked.connect(self.abrir_agregar_admin)      

        self.configuracion_tabla_admins()

        # < --------------------- PAGINA PERFIL --------------------- >
    
        # DESHABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADOR
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)

        self.modificar_perfil_btn.clicked.connect(self.habilitar_datos_admin)

        self.guardar_admin_btn.clicked.connect(self.guardar_datos_perfil)
        
        
        
        # < --------------------- PAGINA EN GENERAL --------------------- >
        
        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

# ////////////////////////// FUNCIONES PAGINA PRINCIPAL //////////////////////////

    def activar_computadora(self):
        self.desactivar_btn.setVisible(True)
        self.desactivar_compus_btn.setVisible(True)

    def activar_computadoras(self):
        self.desactivar_btn.setVisible(True)
        self.desactivar_compus_btn.setVisible(True)
        self.activar_compus_btn.setVisible(False)
        self.activar_btn.setVisible(False)

    def desactivar_computadora(self):
        pass

    def desactivar_computadoras(self):
        self.activar_compus_btn.setVisible(True)
        self.activar_btn.setVisible(True)
        self.desactivar_compus_btn.setVisible(False)
        self.desactivar_btn.setVisible(False)

    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE OPCIONES DE COMPUTADORA
    def abrir_opciones_computadora(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True
            window = OpcionesCompusWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.destroyed.connect(self.ventana_cerrada)
            window.show()

# ////////////////////////// FUNCIONES PAGINA COMPUTADORAS REGISTRADAS //////////////////////////

    # FUNCION PARA MANDAR LLAMAR A LA VENTANA DE AGREGAR COMPUS
    def abrir_agregar_compus(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarCompusWindow(self.datos_compus)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()

    def configuracion_tabla_compus(self):
        column_header = ('id','Nombre de equipo', 'Número de serie', 'Propietario del equipo', 'Rol')
        self.computadoras_registradas_table.setColumnCount(len(column_header))
        self.computadoras_registradas_table.setHorizontalHeaderLabels(column_header)

        self.computadoras_registradas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    
    def datos_compus(self,data):
        self.computadoras_registradas_table.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.computadoras_registradas_table.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))


# ////////////////////////// FUNCIONES PAGINA ADMINISTRADORES REGISTRADOS //////////////////////////

    def configuracion_tabla_admins(self):
            column_headers = ("id", "nombre", "apellidos", "telefono", "correo", "rol")
            self.administradores_tabla.setColumnCount(len(column_headers))
            self.administradores_tabla.setHorizontalHeaderLabels(column_headers)

            self.administradores_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)

    def datos_admins(self,data):
        self.administradores_tabla.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.administradores_tabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
    
    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE AGREGAR ADMIN
    def abrir_agregar_admin(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta: 
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarpropietarioWindow(self.datos_admins)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
        else:
            QMessageBox.warning(self, "Advertencia", "La ventana ya está abierta.")
    
    def modificar_propietarios(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE 
            seleccionar_fila = self.administradores_tabla.selectedItems()
            if seleccionar_fila:
                id_propietarios = seleccionar_fila[0].text()
                window = ModificarPropietarioWindow(self.datos_admins,self,id_propietarios)
                window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
                window.destroyed.connect(self.ventana_cerrada)
                window.show()
        else:
            QMessageBox.warning(self, "Advertencia", "La ventana ya está abierta.")
    
    def eliminar_propietario(self):
        propietario = Propietario(conexion())
        seleccionar_fila = self.administradores_tabla.selectedItems()
        if seleccionar_fila:
            id_propietarios = seleccionar_fila[0].text()
            fila = seleccionar_fila[0].row()

            if propietario.eliminar_propietario(id_propietarios):
                self.administradores_tabla.removeRow(fila)
                QMessageBox.information(self, 'Eliminacion', 'El propietario se elimino con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            
# ////////////////////////// FUNCIONES PAGINA PERFIL //////////////////////////

    # FUNCION PARA HABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADORS
    def habilitar_datos_admin(self):
        self.nombre_txt.setEnabled(True)
        self.apellidos_txt.setEnabled(True)
        self.telefono_txt.setEnabled(True)
        self.correo_txt.setEnabled(True)

    def guardar_datos_perfil(self):
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)
        QMessageBox.warning(self, "Guardado", "Los datos se guardaron correctamente.")



# ////////////////////////// FUNCIONES PARA LAS PAGINAS //////////////////////////
            
    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False
    