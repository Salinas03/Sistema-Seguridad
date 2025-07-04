# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from PySide2 import QtCore
from views.Principal import Principal
from controllers.AgregarAdmin import AgregarpropietarioWindow
from controllers.AgregarCompus import AgregarCompusWindow
from controllers.OpcionesComputadora import OpcionesCompusWindow
from controllers.ModificarPropietarios import ModificarPropietarioWindow
from controllers.ModificarComputadoras import ModificarEquipoWindow
from controllers.ModificarPerfil import ModificarPerfilWindow
from py2_msgboxes import msg_boxes
from PySide2.QtCore import *
from PySide2.QtGui import QRegExpValidator, QPixmap, QIcon
import os
#TODO Librerias agregadas para la implementación de tablas dinámicas
import json
import threading
import time
import socket
from clases.administrador_ui import admin_socket_ui
from clases.administrador_sesion import AdministradorSesion
from utils.crear_mensaje_emergente import crear_message_box
import webbrowser


class PrincipalWindow(Principal,QWidget):

    # CONSTRUCTOR PARA INICIO DE LA VENTANA
                # RECEPCION DEL ID QUE ENVIA
                # EL LOGIN
    def __init__(self,data_admin):
        super().__init__(None)
        self.setupUi(self)

        #CREACIÓN DE OBJETO DE ADMINISTRADOR PARA DESPLEGAR SU INFORMACIÓN EN EL FORMULARIO
        self.administrador = AdministradorSesion(data_admin)

    ###################################################################################################################################
    ###################################################################################################################################
    #
    #       FUNCIONES QUE SE EJECUTAN CUANDO DE EJECUTA LA VENTANA PRINCIPAL
    #
    ###################################################################################################################################
    ###################################################################################################################################

            # Obtener la lista de botones de tu interfaz gráfica
        buttons = [
            self.home_btn, 
            self.home_texto_btn, 
            self.compus_btn, 
            self.desktop_texto_btn, 
            self.admins_btn, 
            self.admins_texto_btn, 
            self.settings_btn, 
            self.settings_texto_btn,
            self.pin_btn,
            self.pin_texto_btn 
        ]

                   # Hacer que los botones sean checkables
        for button in buttons:
            button.setCheckable(True)

            # Conectar eventos clicked de los botones a la función boton_activo
        for button in buttons:
            button.clicked.connect(self.boton_activo)

        # BOTONES QUE REDIRIGEN A LAS PAGINAS DEL STACKEDWIDGET
        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.home_btn.setChecked(True)
        self.home_btn.setFocus()
        self.compus_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))
        self.admins_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_5))
        self.pin_btn.clicked.connect(self.mostrar_ubicacion)

        self.home_texto_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.home_texto_btn.setChecked(True)
        self.desktop_texto_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_texto_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.admins_texto_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_5))

        
        self.actualizar_btn.clicked.connect(self.actualizar_tabla_activos_inactivos)
        self.pin_texto_btn.clicked.connect(self.mostrar_ubicacion)

        self.suspender_equipos_btn.clicked.connect(self.suspender_equipos_general)
        self.apagar_equipos_btn.clicked.connect(self.apagar_equipos_general)

        # < --------------------- PAGINA PRINCIPAL --------------------- >

        self.menu_desplegable_widget.hide()

        tabla_de_computadoras_activas = QTableWidget()
        tabla_de_computadoras_activas.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_activas = self.tabla_computadoras_activas.horizontalHeader()
        header_computadoras_activas.setSectionResizeMode(header_computadoras_activas.Stretch)

        header_computadoras_desactivas = self.tabla_computadoras_desactivas.horizontalHeader()
        header_computadoras_desactivas.setSectionResizeMode(header_computadoras_desactivas.Stretch)

        # < --------------------- PAGINA COMPUTADORAS ACTIVAS E INACTIVAS--------------------- >
        
        header_computadoras_activas_tabla = self.tabla_computadoras_activas.horizontalHeader()
        header_computadoras_activas_tabla.setSectionResizeMode(header_computadoras_activas_tabla.Stretch)
        self.configuracion_tabla_equipos_activos()

        header_computadoras_inactivas_tabla = self.tabla_computadoras_desactivas.horizontalHeader()
        header_computadoras_inactivas_tabla.setSectionResizeMode(header_computadoras_inactivas_tabla.Stretch)
        self.configuracion_tabla_equipos_inactivos()
        
        self.tabla_computadoras_activas.itemDoubleClicked.connect(self.abrir_opciones_computadora)


        # < --------------------- PAGINA COMPUTADORAS REGISTRADAS --------------------- >

        self.botones_eliminar = [self.eliminar_admin_btn, self.eliminar_compu_btn]

        for button in self.botones_eliminar:
            self.apply_hover_effect_computadoras(button)


        self.eliminar_compu_btn.setEnabled(False)
        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_computadoras_registradas_table = self.computadoras_registradas_table.horizontalHeader()
        header_computadoras_registradas_table.setSectionResizeMode(header_computadoras_registradas_table.Stretch)


        self.agregar_compu_btn.clicked.connect(self.abrir_agregar_compus) # LLAMADO PARA AGREGAR NUEVA COMPUTADORA

        # LLAMADO PARA LA INSERCION DE DATOS EN LA TABLA DE COMPUTADORAS
        self.configuracion_tabla_compus()
        self.computadoras_registradas_table.cellPressed.connect(self.habilitar_eliminar_compus)

        self.eliminar_compu_btn.clicked.connect(self.eliminar_equipo) # LLAMADO PARA LA ELIMINACION DE COMPUTADORAS

        # LLAMADO PARA LA MODIFICACION DE LA COMPUTADORAS, HACIENDO DOBLE CLICK SOBRE LA COMPUTADORA SELECCIONADA EN LA TABLA
        self.computadoras_registradas_table.itemDoubleClicked.connect(self.modificar_equipos)
        
        # HABILITACION DE BOTON PARA ELIMINAR, CUANDO UNA FILA DE LA TABLA SE HAYA SELECCIONADO
        self.computadoras_registradas_table.selectionModel().currentChanged.connect(self.actualizar_estado_boton_compu)

        # < --------------------- PAGINA ADMINISTRADORES REGISTRADOS --------------------- >

        self.botones_agregar = [self.agregar_admin_btn, self.agregar_compu_btn]

        for button in self.botones_agregar:
            self.apply_hover_effect(button)

        self.eliminar_admin_btn.setEnabled(False)
        # MEDIDAS DEL ANCHO DE LAS TABLAS
        header_administradores_tabla = self.administradores_tabla.horizontalHeader()
        header_administradores_tabla.setSectionResizeMode(header_administradores_tabla.Stretch)

        # LLAMADO PARA AGREGAR UN NUEVO ADMINISTRADOR
        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)

        self.y = self.eliminar_admin_btn.clicked.connect(self.eliminar_propietario) # LLAMADO PARA LA ELIMINACION DE PROPIETARIOS

        # LLAMADO PARA LA MODIFICACION DE PROPIETARIOS, HACIENDO DOBLE CLICK EN LA FILA SELECCIONADA DE LA TABLA
        self.x = self.administradores_tabla.itemDoubleClicked.connect(self.modificar_propietarios)

        # LLAMADO PARA LA INSERCION DE DATOS EN LA TABLA DE PROPIETARIOS
        self.configuracion_tabla_admins()
        self.administradores_tabla.cellPressed.connect(self.habilitar_eliminar_propietario)

        # HABILITAR EL BOTON DE ELIMINAR CUANDO SELECCIONE UNA FILA DE LA TABLA PROPIETARIO
        self.administradores_tabla.cellPressed.connect(self.habilitar_eliminar_propietario)

        # < --------------------- PAGINA PERFIL --------------------- >

        self.llenar_campos_administrador()

        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))
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

        self.modificar_perfil_btn.clicked.connect(self.abrir_modificar_perfil) # LLAMADO PARA LA MODIFICACION DE LOS DATOS DEL PERFIL
        self.cerrar_sesion_btn_2.clicked.connect(self.cerrar_sesion) # LLAMADO PARA CERRAR SESION 
        self.actualizar_tabla_equipos_btn.clicked.connect(self.actualizar_tabla_equipos)
        self.actualizar_tabla_propietarios_btn.clicked.connect(self.actualizar_tabla_propietarios)
        
        # < --------------------- PAGINA EN GENERAL --------------------- >
        
        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

        #RENDERIZADO DE TABLAS POR MEDIO DE PETICIONES ------------------------------------------------------
        self.bandera_internet = True
        # self.conectar_canal_conectividad()

        #Crear hilo de conectividad
        self.thread_conectividad = threading.Thread(target=self.escuchar_conectividad)
        self.thread_conectividad.daemon = True
        self.thread_conectividad.start()

        #Crear hilo de notificaciones
        self.thread_notificacion = threading.Thread(target=self.escuchar_notificaciones)
        self.thread_notificacion.daemon = True
        self.thread_notificacion.start()

        #Crear hilo para escuchar la conexión a internet
        self.thread_conexion_internet = threading.Thread(target=self.escuchar_conexion_internet)
        self.thread_conexion_internet.daemon = True
        self.thread_conexion_internet.start()

        self.peticion_equipos = {
            'tabla': 'equipos',
            'operacion': 'obtener_equipos_computo'
        }

        self.peticion_propietarios = {
            'tabla': 'propietarios',
            'operacion': 'obtener_propietarios'
        }

        #Obtener por primera vez los equipos activos e inactivos
        equipos_activos_inactivos = admin_socket_ui.escribir_operaciones('listar')
        print(equipos_activos_inactivos)
        print(equipos_activos_inactivos)

        if equipos_activos_inactivos:
            self.desplegar_datos_equipos_inactivos(equipos_activos_inactivos[0])
            self.desplegar_datos_equipos_activos(equipos_activos_inactivos[1])
            self.thread_equipos_activos_inactivos = threading.Thread(target=self.escuchar_cambios_equipos_activos_inactivos)
            self.thread_equipos_activos_inactivos.daemon = True
            self.thread_equipos_activos_inactivos.start()

        #Obtener por primera vez los equipos de cómputo de la BD_SQL
        equipos_computo = admin_socket_ui.escribir_operaciones(json.dumps(self.peticion_equipos))
        if equipos_computo['success']:
            self.datos_compus(equipos_computo['data'])    
            self.thread_escuchar_cambios_tablasbd = threading.Thread(target=self.escuchar_cambios_tablasbd)
            self.thread_escuchar_cambios_tablasbd.daemon = True
            self.thread_escuchar_cambios_tablasbd.start()

        #Obtener por primera vez los propietarios
        propietarios = admin_socket_ui.escribir_operaciones(json.dumps(self.peticion_propietarios))
        if propietarios['success']:
            self.datos_admins(propietarios['data'])            
          
        ###################################################################################################################################
        ###################################################################################################################################
        #
        #       FIN DE LAS FUNCIONES QUE SE EJECUTAN CUANDO DE EJECUTA LA VENTANA PRINCIPAL
        #
        ###################################################################################################################################
        ###################################################################################################################################


        ###################################################################################################################################
        ###################################################################################################################################
        #
        #       FUNCIONES SECUNDARIAS, DEPENDEN DEL LLAMADO DE LAS INICIALES
        #
        ###################################################################################################################################
        ###################################################################################################################################

    # ////////////////////////// FUNCIONES PAGINA PRINCIPAL TODO//////////////////////////

    def boton_checked(self, checked):
        if checked:
            self.home_btn.setFocus()

    def boton_activo(self):
        sender = self.sender()
        for button in sender.parent().findChildren(QPushButton):
            if button is not sender:
                button.setChecked(False)
            else:
                button.setChecked(True)
                
    def mostrar_ubicacion(self):
        resp = msg_boxes.precaucion_msg('ADVERTENCIA','¿Desea buscar las ubicación de algún dispositivo?')

        if resp == QMessageBox.Yes:
                url = "https://account.microsoft.com/devices"  # Aquí debes especificar la URL que deseas abrir
                # Abre el enlace en el navegador predeterminado
                webbrowser.open(url)

    def configuracion_tabla_equipos_activos(self):
        column_headers_tablas_equipos_activos = ('Área', 'Características','Nombre del equipo', 'Número de serie', 'Propietario del equipo', 'Rol', 'IP')   
        self.tabla_computadoras_activas.setColumnCount(len(column_headers_tablas_equipos_activos))
        self.tabla_computadoras_activas.setHorizontalHeaderLabels(column_headers_tablas_equipos_activos)
        self.tabla_computadoras_activas.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tabla_computadoras_activas.setSelectionBehavior(QAbstractItemView.SelectRows)# EVENTO QUE SELECCIONA TODA LA FILA
        self.tabla_computadoras_activas.verticalHeader().setVisible(False) # Ocultar el header vertical

    def configuracion_tabla_equipos_inactivos(self):
        column_headers_tabla_equipos_inactivos = ('Área', 'Características','Nombre del equipo', 'Número de serie', 'Propietario del equipo', 'Rol')
        self.tabla_computadoras_desactivas.setColumnCount(len(column_headers_tabla_equipos_inactivos))
        self.tabla_computadoras_desactivas.setHorizontalHeaderLabels(column_headers_tabla_equipos_inactivos)

        self.tabla_computadoras_desactivas.setEditTriggers(QAbstractItemView.NoEditTriggers) #Eliminar la edicion de la tabla
        self.tabla_computadoras_desactivas.setSelectionBehavior(QAbstractItemView.SelectRows) #Seleccionar toda la fila
        self.tabla_computadoras_desactivas.setSelectionMode(QAbstractItemView.SingleSelection) #Seleccionar solo una fila
        self.tabla_computadoras_desactivas.verticalHeader().setVisible(False) # Ocultar el header 

    @QtCore.Slot()
    def _mostrar_mensaje(self):
        QMessageBox.critical(
            self, 'Desonexión de internet', 'Ocurrió algo con el su red wifi, intente denuevo por favor', 
            QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close
        ) 
        self.close()
    
    def mostrar_mensaje(self):
        try:
            QtCore.QMetaObject.invokeMethod(self, '_mostrar_mensaje', Qt.QueuedConnection)

        except:
            print('Hubo un error al evocar la función de desconexión de internet')

    @QtCore.Slot()
    def _mostrar_mensaje_desconectividad(self):
        QMessageBox.critical(
            self, 'Desconexión del servidor', 'Ocurrió algo con la conexión con el servidor, intente denuevo :)', 
            QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close
        ) 
        self.close()

    def mostrar_mensaje_desconectividad(self):
        try:
            QtCore.QMetaObject.invokeMethod(self, '_mostrar_mensaje_desconectividad', Qt.QueuedConnection)

        except:
            print('Hubo un error al evocar la función de desconexión de conectividad')

    def verificar_conexion_internet(self):
        try:
            socket.create_connection(('www.google.com', 80))
            return True
        
        except OSError:
            return False

    def desplegar_datos_equipos_activos(self, data):
        # data = [ID, nombre_equipo, numero_serie, propietario, Rol, IP, seleccionado]
        self.tabla_computadoras_activas.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                item = QTableWidgetItem(str(cell))
                self.tabla_computadoras_activas.setItem(index_row, index_cell, item)
        
    def desplegar_datos_equipos_inactivos(self, data):
        self.tabla_computadoras_desactivas.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            if row is not None:
                for (index_cell, cell) in enumerate(row):
                    self.tabla_computadoras_desactivas.showRow(index_row)
                    self.tabla_computadoras_desactivas.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
            else: 
                self.tabla_computadoras_desactivas.hideRow(index_row)

    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE OPCIONES DE COMPUTADORA
    def abrir_opciones_computadora(self):
        
        if not self.ventana_abierta:
            self.ventana_abierta:True
            seleccionar_fila = self.tabla_computadoras_activas.selectedItems()
            if seleccionar_fila:
                index = seleccionar_fila[0].row()

                respuesta = admin_socket_ui.escribir_operaciones(f'seleccionar {index},{admin_socket_ui.obtener_numero_serie()}')
                
                if respuesta['success']:
                    id_propietarios = seleccionar_fila[0].text()
                    numero_serie = seleccionar_fila[3].text()
                    ip_publica = seleccionar_fila[6].text()
                    data = [id_propietarios,numero_serie,ip_publica]
                    window = OpcionesCompusWindow(self,data)
                    window.setWindowModality(QtCore.Qt.ApplicationModal)
                    window.destroyed.connect(self.ventana_cerrada)
                    window.show()
                else:
                    crear_message_box('Selección no válida', respuesta['msg'], 'information').exec_()
                
            else:
                crear_message_box('Advertencia', 'La ventana ya esta abierta', 'warning').exec_()
# ////////////////////////// FUNCIONES PAGINA COMPUTADORAS REGISTRADAS //////////////////////////

    def apply_hover_effect_computadoras(self, button):
        button.enterEvent = lambda event, button=button: self.on_enter_event_computadoras(event, button)
        button.leaveEvent = lambda event, button=button: self.on_leave_event_computadoras(event, button)

    def on_enter_event_computadoras(self, event, button):
        image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/files/clear.png'
        )
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            new_width = button.width() // 2
            new_height = button.height() // 2
            pixmap = pixmap.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            # Guardamos el texto original en el atributo del botón
            if not hasattr(button, 'original_text'):
                button.original_text = button.text()

            button.setIcon(pixmap)
            button.setIconSize(pixmap.size())
            button.setText("")  # Configura el texto del botón en una cadena vacía

    def on_leave_event_computadoras(self, event, button):
         # Volver a mostrar el texto al salir del hover
        if hasattr(button, 'original_text'):
            button.setText(button.original_text)  # Restaura el texto original del botón
        button.setIcon(QIcon())  # Configura un QIcon vacío para eliminar la imagen

    # FUNCION PARA MANDAR LLAMAR A LA VENTANA DE AGREGAR COMPUS
    def abrir_agregar_compus(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarCompusWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()

    # FUNCION PARA COLOCAR LAF CONFIGURACIONES PARA LA TABLA 
    def configuracion_tabla_compus(self):
        column_headers_tabla_compus = ('ID', 'Área','Característica','Nombre de equipo', 'Número de serie', 'Propietario del equipo', 'Rol')
        self.computadoras_registradas_table.setColumnCount(len(column_headers_tabla_compus))
        self.computadoras_registradas_table.setHorizontalHeaderLabels(column_headers_tabla_compus)

        self.computadoras_registradas_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.computadoras_registradas_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.computadoras_registradas_table.verticalHeader().setVisible(False) # Ocultar el header vertical
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
                window = ModificarEquipoWindow(self,id_equipo)
                window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
                window.destroyed.connect(self.ventana_cerrada)
                window.show()
            else:
               crear_message_box('Advertencia', 'La ventana ya esta abierta', 'warning').exec_()
    
    def eliminar_equipo(self):
        seleccionar_fila = self.computadoras_registradas_table.selectedItems()

        resp = msg_boxes.warning_msg('ADVERTENCIA', '¿Estas seguro de eliminar esta computadora?')
        if resp == QMessageBox.Yes:
            if seleccionar_fila:
                id_equipo = seleccionar_fila[0].text()
                fila = seleccionar_fila[0].row()

                peticion = {
                    'tabla': 'equipos',
                    'operacion': 'borrar',
                    'id': id_equipo
                }

                respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                if respuesta['success']:
                    crear_message_box('Eliminación realizada con éxito', 'El equipo de cómputo se eliminó con éxito', 'information').exec_()
                else:
                    crear_message_box('Ooops... algo sucedió', 'Ocurrió un error al realizar la eliminación', 'error').exec_()

    def habilitar_eliminar_compus(self):
        self.eliminar_compu_btn.setEnabled(True)
    
    # FUNCION PARA HABILITAR EL BOTON DE ELIMINAR EQUIPOS DE COMPUTO
    def actualizar_estado_boton_compu(self,current: QModelIndex, previous: QModelIndex):
        if current.isValid():
            self.eliminar_compu_btn.setEnabled(True)
        else:
            self.eliminar_compu_btn.setEnabled(False)   

# ////////////////////////// FUNCIONES PAGINA ADMINISTRADORES REGISTRADOS //////////////////////////

    def apply_hover_effect(self, button):
        button.enterEvent = lambda event, button=button: self.on_enter_event(event, button)
        button.leaveEvent = lambda event, button=button: self.on_leave_event(event, button)

    def on_enter_event(self, event, button):
        image_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            '../assets/files/more.png'
        )
        if os.path.exists(image_path):
            pixmap = QPixmap(image_path)
            new_width = button.width() // 2
            new_height = button.height() // 2
            pixmap = pixmap.scaled(new_width, new_height, QtCore.Qt.KeepAspectRatio, QtCore.Qt.SmoothTransformation)
            # Guardamos el texto original en el atributo del botón
            if not hasattr(button, 'original_text'):
                button.original_text = button.text()

            button.setIcon(pixmap)
            button.setIconSize(pixmap.size())
            button.setText("")  # Configura el texto del botón en una cadena vacía

    def on_leave_event(self, event, button):
         # Volver a mostrar el texto al salir del hover
        if hasattr(button, 'original_text'):
            button.setText(button.original_text)  # Restaura el texto original del botón
        button.setIcon(QIcon())  # Configura un QIcon vacío para eliminar la imagen


# FUNCION PARA MANDAR LLAMAR LA VENTANA DE AGREGAR ADMIN
    def abrir_agregar_admin(self):
        # CONDICION PARA SABER SI LA VENTANA ESTA ABIERTA
        if not self.ventana_abierta: 
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE
            window = AgregarpropietarioWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
        else:
            crear_message_box('Advertencia', 'La ventana ya esta abierta', 'warning').exec_()
    
    def configuracion_tabla_admins(self):
            column_headers_tabla_admins = ("id", "nombre", "apellidos", "telefono", "correo", "rol")
            self.administradores_tabla.setColumnCount(len(column_headers_tabla_admins))
            self.administradores_tabla.setHorizontalHeaderLabels(column_headers_tabla_admins)
            self.administradores_tabla.setSelectionMode(QAbstractItemView.SingleSelection)
            self.administradores_tabla.setSelectionBehavior(QAbstractItemView.SelectRows)
            self.administradores_tabla.verticalHeader().setVisible(False) # Ocultar el header vertical

    def datos_admins(self,data):
        self.administradores_tabla.setRowCount(len(data))
        for (index_row, row) in enumerate(data):
            for (index_cell, cell) in enumerate(row):
                if row[0] != self.administrador.get_id_admin():
                    self.administradores_tabla.showRow(index_row)
                    self.administradores_tabla.setItem(index_row, index_cell, QTableWidgetItem(str(cell)))
                else:
                    self.administradores_tabla.hideRow(index_row)

    def modificar_propietarios(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE 
            seleccionar_fila = self.administradores_tabla.selectedItems()
            if seleccionar_fila:
                id_propietarios = seleccionar_fila[0].text()
                window = ModificarPropietarioWindow(self,id_propietarios)
                window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
                window.destroyed.connect(self.ventana_cerrada)
                window.show()
        else:
            crear_message_box('Advertencia', 'La ventana ya esta abierta', 'warning').exec_()
    
    def eliminar_propietario(self):

        seleccionar_fila = self.administradores_tabla.selectedItems()
        
        resp = msg_boxes.warning_msg('Advertencia', '¿Estas seguro de eliminar este propietario?')
        if resp == QMessageBox.Yes:
            if seleccionar_fila:
                id_propietarios = seleccionar_fila[0].text()
                fila = seleccionar_fila[0].row()

                peticion = {
                    'tabla': 'propietarios',
                    'operacion': 'borrar',
                    'id': id_propietarios
                }

                respuesta_borrado = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                if respuesta_borrado['success']:
                    crear_message_box('Eliminación', 'El propietario se eliminó con éxito', 'information').exec_()

                else:
                    crear_message_box('Ooops... algo ocurrió', 'Hubo algún error al realizar la eliminación', 'information').exec_()

    def habilitar_eliminar_propietario(self):
        self.eliminar_admin_btn.setEnabled(True)   
    
# ////////////////////////// FUNCIONES PAGINA PERFIL //////////////////////////

    def llenar_campos_administrador(self):
        self.nombre_txt.setText(self.administrador.get_nombre_admin())
        self.apellidos_txt.setText(self.administrador.get_apellido_admin())
        self.telefono_txt.setText(self.administrador.get_tel_admin())
        self.correo_txt.setText(self.administrador.get_correo_admin())

    def abrir_modificar_perfil(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True # CAMBIO DE LA VENTANA A TRUE 
            window = ModificarPerfilWindow(self,self.administrador, self.llenar_campos_administrador)
            window.setWindowModality(QtCore.Qt.ApplicationModal) # BLOQUEO DE LA VENTANA PRINCIPAL
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
        else:
            crear_message_box('Advertencia', 'La ventana ya esta abierta', 'warning').exec_()


# ////////////////////////// FUNCIONES PARA LAS PAGINAS //////////////////////////

    def actualizar_tabla_equipos(self):
        respuesta = admin_socket_ui.escribir_operaciones('refrescar_equipos')
        if respuesta:
            crear_message_box('Refrescado de tablas', 'Se han refrescado las tabla de los equipos exitosamente', 'information').exec_()
        else:
            crear_message_box('Error al refrescar', 'Hubo un error al refrescar la tabla de los equipos', 'error').exec_()


    def actualizar_tabla_propietarios(self):
        respuesta = admin_socket_ui.escribir_operaciones('refrescar_propietarios')
        if respuesta:
            crear_message_box('Refrescado de tablas', 'Se han refrescado las tabla de los propietarios exitosamente', 'information').exec_()
        else:
            crear_message_box('Error al refrescar', 'Hubo un error al refrescar la tabla de los propietarios', 'error').exec_()
            
    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False

    # FUNCION PARA CERRAR SESION
    def cerrar_sesion(self):
        # ESTA IMPORTACION SE PONE AQUI, YA QUE HACE UN BUCLE INFINITO AL MOMENTO DEL LLAMADO DE LA PAGINA LOGIN
        from controllers.Login import LoginWindow
        self.close()
        window = LoginWindow(self)
        window.show()

    def conectar_canal_conectividad(self):
        try:
            #Conectar con socket de conectividad
            admin_socket_ui.get_socket_conectividadadmin().connect(admin_socket_ui.ADDR_CONA)

            #Enviar numero de serie
            numero_serie = admin_socket_ui.obtener_numero_serie()
            admin_socket_ui.get_socket_conectividadadmin().send(numero_serie.encode())
            respuesta = admin_socket_ui.get_socket_conectividadadmin().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)
            print(respuesta)

            self.thread_conectividad = threading.Thread(target=self.escuchar_conectividad)
            self.thread_conectividad.start()
        except socket.error as e:
            print(f'Hubo un error al conectar con el canal de conectividad {e}')
            self.close()

    def cerrar_procesos_hilos(self):
        try:
            self.thread_equipos_activos_inactivos.join()
            self.thread_notificacion.join()
            self.thread_escuchar_cambios_tablasbd.join()
            self.bandera_internet = False
            self.thread_conexion_internet.join()
        except threading.ThreadError as e:
            print(f'Hubo un error al realizar el cerrado de los HILOS {e}')

    def actualizar_tabla_activos_inactivos(self):
        equipos_activos_inactivos = admin_socket_ui.escribir_operaciones('listar')
        if equipos_activos_inactivos:
            self.desplegar_datos_equipos_inactivos(equipos_activos_inactivos[0])
            self.desplegar_datos_equipos_activos(equipos_activos_inactivos[1])
            crear_message_box('Refrescado de tablas', 'Se han refrescado las tablas exitosamente', 'information').exec_()

    def suspender_equipos_general(self):
        res = msg_boxes.precaucion_msg('Advertencia', '¿Estas seguro que quieres suspender todos los equipos?')
        
        if res == QMessageBox.Yes:
            respuesta_servidor = admin_socket_ui.escribir_operaciones('bloquear')
            print(respuesta_servidor)

            if respuesta_servidor == None:
                crear_message_box('Error', 'Hubo un error al bloquear los equipos de manera general', 'error').exec_()
            else:
                if respuesta_servidor['success']:
                    crear_message_box('Operación exitosa', respuesta_servidor['msg'], 'information').exec_()
                else:
                    if isinstance(respuesta_servidor['msg'], str):
                        crear_message_box('Advertencia', respuesta_servidor['msg'], 'warning').exec_()
                    else:
                        crear_message_box('Advertencia/Error', 'No se pudo realizar el apagado a los siguientes clientes '+respuesta_servidor['msg'], 'error').exec_()

    def apagar_equipos_general(self):
        res = msg_boxes.precaucion_msg('Advertencia', '¿Estas seguro que quieres apagar todos los equipos?')
        
        if res == QMessageBox.Yes:
            respuesta_servidor = admin_socket_ui.escribir_operaciones('apagar')
            print(respuesta_servidor)

            if respuesta_servidor == None:
                crear_message_box('Error', 'Hubo un error al apagar los equipos de manera general', 'error').exec_()
            else:
                if respuesta_servidor['success']:
                    crear_message_box('Operación exitosa', respuesta_servidor['msg'], 'information').exec_()
                else:
                    if isinstance(respuesta_servidor['msg'], str):
                        crear_message_box('Advertencia', respuesta_servidor['msg'], 'warning').exec_()
                    else:
                        crear_message_box('Advertencia/Error', 'No se pudo realizar el apagado a los siguientes clientes '+respuesta_servidor['msg'], 'error').exec_()

# ////////////////////////// FUNCIONES PARA ESCUCHAR CAMBIOS EN LA BASE DE DATOS TODO//////////////////////////

    def escuchar_conectividad(self):
        admin_socket_ui.get_socket_conectividadadmin().settimeout(admin_socket_ui.MESSAGE_TIMEOUT)
        while True:
            try:
                mensaje = admin_socket_ui.get_socket_conectividadadmin().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)
                admin_socket_ui.get_socket_conectividadadmin().send('*'.encode())

            except socket.error as e:
                print(f'Ocurrio un error en el canal de conectividad {e}')
                if self.bandera_salida:
                    self.mostrar_mensaje_desconectividad()
                break

        #Cerrar los procesos de los hilos       
        print('Salida de procesos [escuchar conectividad]') 
        admin_socket_ui.cerrado_sockets()
        self.cerrar_procesos_hilos()

    def escuchar_cambios_equipos_activos_inactivos(self):
        print('Escuchar cuando se conecten o desconecten usuarios | Canal: Broadcasting')
        while True:
            try:
                equipos_activos_inactivos = json.loads(admin_socket_ui.get_socket_broadcasting().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT))
                self.desplegar_datos_equipos_inactivos(equipos_activos_inactivos[0])
                self.desplegar_datos_equipos_activos(equipos_activos_inactivos[1])
                print('[ACTUALIZACIÓN DE EQUIPOS ACTIVOS E INACTIVOS]')

            except ConnectionResetError as e:
                print(f'Hubo un problema al recibir los equipos activos e inactivos {e}')
                break

            except socket.error as e:
                admin_socket_ui.get_socket_broadcasting().close()
                print(f'Ocurrió un error en el socket de broadcast {e}')
                break

    def escuchar_notificaciones(self):
        print('Escuchar cuando se haga una notificación | Canal: Notificación')
        while True:
            try:
                notificacion = admin_socket_ui.get_socket_notificacion().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)
                print(f'Mensaje de notificación enviado por el servidor | {notificacion}')

            except ConnectionResetError as e:
                print(f'Hubo un problema al recibir las notificacaciones {e}')
                break

            except socket.error as e:
                print(f'Ocurrió un error en el socket de notificación {e}')
                break

    def escuchar_cambios_tablasbd(self):
        print('Escuchar cambios en la BD | Canal: OperacionesBD')
        while True:
            try:
                datos = json.loads(admin_socket_ui.get_socket_operacionesbd().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT))

                print(f'[SE OBTUVIERON LOS DATOS DE ESCUCHAR CAMBIOS EN LAS TABLAS EQUIPOS/PROPIETARIOS]')
                print(datos)
                print("")

                if datos['tabla'] == 'equipos':
                    self.datos_compus(datos['data'])

                else:
                    self.datos_admins(datos['data'])

            except ConnectionResetError as e:
                admin_socket_ui.get_socket_operacionesbd().close()
                print(f'Hubo un problema al recibir los datos de operacionesBD {e}')
                break

            except socket.error as e:
                print(f'Ocurrió un error en el socket de operacionesBD {e}')
                break

    def escuchar_conexion_internet(self):
        while self.bandera_internet:
            if not self.verificar_conexion_internet():
                print('Se fue el internet')
                self.mostrar_mensaje()
                break

            time.sleep(1)