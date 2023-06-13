# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from PySide2 import QtCore
from views.Principal import Principal
from controllers.AgregarAdmin import AgregarpropietarioWindow
from controllers.AgregarCompus import AgregarCompusWindow
from controllers.OpcionesComputadora import OpcionesCompusWindow
from controllers.ModificarPropietarios import ModificarPropietarioWindow
from controllers.ModificarComputadoras import ModificarEquipoWindow
from modelos.propietarios_consultas import Propietario
from py2_msgboxes import msg_boxes
from db.connection import conexion
from modelos.equipos_consultas import Equipo
from PySide2.QtCore import QRegExp 
from PySide2.QtGui import QRegExpValidator


class PrincipalWindow(Principal,QWidget):

    # FUNCION PARA INICIO DE LA VENTANA
    def __init__(self,_id = 12):
        self._id = _id
        super().__init__(None)
        self.setupUi(self)
        self.conexion = conexion()
        self.equipo = Equipo(self.conexion)
        self.propietario = Propietario(self.conexion)

        self.llenar_campos_texto()


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
        self.otros_comandos_btn.setVisible(False)

        self.otros_comandos_btn.clicked.connect(self.abrir_opciones_computadora)


        # < --------------------- PAGINA COMPUTADORAS REGISTRADAS --------------------- >
        self.eliminar_compu_btn.setEnabled(False)
        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_registradas_table = self.computadoras_registradas_table.horizontalHeader()
        header_computadoras_registradas_table.setSectionResizeMode(header_computadoras_registradas_table.Stretch)
        self.agregar_compu_btn.clicked.connect(self.abrir_agregar_compus)
        self.a = self.eliminar_compu_btn.clicked.connect(self.eliminar_equipo)
        self.b = self.computadoras_registradas_table.itemDoubleClicked.connect(self.modificar_equipos)
        
        self.configuracion_tabla_compus()
        self.datos_compus(self.equipo.seleccionar_compus())

        self.computadoras_registradas_table.cellPressed.connect(self.habilitar_eliminar_compus)


        # < --------------------- PAGINA ADMINISTRADORES REGISTRADOS --------------------- >

        self.eliminar_admin_btn.setEnabled(False)
        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_administradores_tabla = self.administradores_tabla.horizontalHeader()
        header_administradores_tabla.setSectionResizeMode(header_administradores_tabla.Stretch)
        # LLAMADO PARA AGREGAR UN NUEVO ADMINISTRADOR
        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)
        self.y = self.eliminar_admin_btn.clicked.connect(self.eliminar_propietario)
        self.x = self.administradores_tabla.itemDoubleClicked.connect(self.modificar_propietarios)

        self.configuracion_tabla_admins()
        self.datos_admins(self.propietario.seleccionar_propietario())

        self.administradores_tabla.cellPressed.connect(self.habilitar_eliminar_propietario)

        # < --------------------- PAGINA PERFIL --------------------- >

        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:gmail|hotmail|msn|yahoo|outlook|live|[.]{1,1})+(?:com|com.mx|net|org|edu|gov|mil|biz|info|name|museum|coop|aero|xxx|[a-zA-Z]{2})$"))
        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        
        self.nombre_txt.setValidator(only_text)
        self.apellidos_txt.setValidator(only_text)
        self.telefono_txt.setValidator(only_number)
        self.correo_txt.setValidator(email)

        # DESHABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADOR
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)
        self.guardar_admin_btn.setEnabled(False)

        self.modificar_perfil_btn.clicked.connect(self.modificar_perfil)

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

    # FUNCION PARA COLOCAR LAF CONFIGURACIONES PARA LA TABLA 
    def configuracion_tabla_compus(self):
        column_header = ('id','Nombre de equipo', 'Número de serie', 'Propietario del equipo', 'Rol')
        self.computadoras_registradas_table.setColumnCount(len(column_header))
        self.computadoras_registradas_table.setHorizontalHeaderLabels(column_header)

        self.computadoras_registradas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
    # FUNCION PARA VERIFICAR LA CANTIDAD DE FILAS QUE VA A TENER LA TABLA
    # ES LA QUE RENDERIZA LA TABLA
    def datos_compus(self,data): 
        self.computadoras_registradas_table.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                self.computadoras_registradas_table.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))

    def modificar_equipos(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True
            seleccionar_fila = self.computadoras_registradas_table.selectedItems()
            if seleccionar_fila:
                id_equipo = seleccionar_fila[0].text()
                window = ModificarEquipoWindow(self.datos_compus,self,id_equipo)
                window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
                window.destroyed.connect(self.ventana_cerrada)
                window.show()
            else:
               QMessageBox.warning(self, "Advertencia", "La ventana ya está abierta.") 
    
    def eliminar_equipo(self):
        equipo = Equipo(conexion())
        seleccionar_fila = self.computadoras_registradas_table.selectedItems()

        resp = msg_boxes.warning_msg('Seguro?', 'Estas seguro de eliminar esta computadora?')
        if resp == QMessageBox.Yes:
            if seleccionar_fila:
                id_equipo = seleccionar_fila[0].text()
                fila = seleccionar_fila[0].row()

                if equipo.eliminar_equipo(id_equipo):
                    self.computadoras_registradas_table.removeRow(fila)
                    QMessageBox.information(self, 'Eliminacion', 'El equipo de computo se elimino con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def habilitar_eliminar_compus(self):
        self.eliminar_compu_btn.setEnabled(True)
 

# ////////////////////////// FUNCIONES PAGINA ADMINISTRADORES REGISTRADOS //////////////////////////

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
        resp = msg_boxes.warning_msg('Seguro?', 'Estas seguro de eliminar este propietario?')
        if resp == QMessageBox.Yes:
            if seleccionar_fila:
                id_propietarios = seleccionar_fila[0].text()
                fila = seleccionar_fila[0].row()

                if propietario.eliminar_propietario(id_propietarios):
                    self.administradores_tabla.removeRow(fila)
                    QMessageBox.information(self, 'Eliminacion', 'El propietario se elimino con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def habilitar_eliminar_propietario(self):
        self.eliminar_admin_btn.setEnabled(True)           
# ////////////////////////// FUNCIONES PAGINA PERFIL //////////////////////////


    def llenar_campos_texto(self):
        data  = Propietario(conexion()).seleccionar_propietario_id(self._id)
        if data is not None and len(data) >=1:
            propietario = data[0]
            self.nombre_txt.setText(propietario[1])
            self.apellidos_txt.setText(propietario[2])
            self.telefono_txt.setText(propietario[3])
            self.correo_txt.setText(propietario[4])
        else:
            print('No existe ningún valor')

    def checar_inputs(self):
        nombre = self.nombre_txt.text()
        apellido = self.apellidos_txt.text()
        telefono = self.telefono_txt.text()
        correo = self.correo_txt.text()
        errores_count = 0

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            errores_count +=1
        elif errores_count == 0:
            return True
    
    # FUNCION PARA HABILITAR LOS CAMPOS DE PERFIL DE ADMINISTRADORS
    def modificar_perfil(self):
        self.nombre_txt.setEnabled(True)
        self.apellidos_txt.setEnabled(True)
        self.telefono_txt.setEnabled(True)
        self.correo_txt.setEnabled(True)
        self.guardar_admin_btn.setEnabled(True)
        self.modificar_perfil_btn.setEnabled(False)

    def guardar_datos_perfil(self):
        self.modificar_perfil_btn.setEnabled(True)
        self.guardar_admin_btn.setEnabled(False)
        self.nombre_txt.setEnabled(False)
        self.apellidos_txt.setEnabled(False)
        self.telefono_txt.setEnabled(False)
        self.correo_txt.setEnabled(False)
        nombre = self.nombre_txt.text()
        apellido = self.apellidos_txt.text()
        telefono = self.telefono_txt.text()
        correo = self.correo_txt.text()

        data = [nombre,apellido,telefono,correo]

        if self.checar_inputs():
            propietario = Propietario(conexion())
            if propietario.actualizar_perfil(self._id, data):
                QMessageBox.information(self, 'Actualización', 'El propietario se actualizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()
        QMessageBox.warning(self, "Guardado", "Los datos se guardaron correctamente.")


    #def llenar_campos_texto_perfil(self):
        data = Propietario(conexion()).seleccionar_datos_perfil(self._id)


# ////////////////////////// FUNCIONES PARA LAS PAGINAS //////////////////////////
            
    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False
    