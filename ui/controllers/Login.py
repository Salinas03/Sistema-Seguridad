#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from controllers.RecuperaPassword import RecuperarPasswordWindow
from controllers.Carga import CargaWindow
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from PySide2 import QtCore 


import json
from clases.administrador_ui import admin_socket_ui

# CLASE PARA EL INICIO DE SESION
class LoginWindow(Login, QWidget):    
    # FUNCION PARA PODER INICIAR
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

        # LLAMADO DE INICIO DE SESION                                           # AQUI SE MANDAN LOS DATOS DE LOS TXT
        self.ingresar_btn.clicked.connect(self.iniciar_sesion)

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))

        # LLAMADO DE LAS VALIDACIONES EN LOS CAMPOS REQUERIDOS
        self.correo_txt.setValidator(email)
        self.password_txt.setValidator(only_password)

        self.recuperar_contrasenia_btn.clicked.connect(self.abrir_recuperar_password)
        self.pushButton.clicked.connect(self.cambio_visible_password)
        self.correo_txt.setFocus()
     
    # FUNCION PARA EL INICIO DE SESION
    def iniciar_sesion(self):
        correo = self.correo_txt.text()
        password = self.password_txt.text()
        # CONDICION PARA VALIDAR LOS DATOS DE LOS TXT CON LOS DATOS DE LA BD
        if correo == '' or password == '': # CONDICION PARA VERIFICAR QUE LOS CAMPOS DE TEXTO NO ESTEN VACIOS
            QMessageBox.warning(self, 'Advertencia', 'Favor de llenar los campos correspondientes', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        elif '@' not in correo: # CONDICION PARA VERIFICAR QUE EXISTA UN @ EN EL CAMPO DE TEXTO CORREO
            QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar @', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        else:
            if correo and password:
                respuesta = admin_socket_ui.crear_sockets()
                if respuesta['success']:
                    print(respuesta['msg'])
                    respuesta = admin_socket_ui.conexion_temporal()
                    if respuesta['success']:
                        print(respuesta['msg'])
                        respuesta = admin_socket_ui.validacion_conexion()
                        if respuesta['success']:
                            #Operación del inicio de sesión que crea la sesión, conexión y validación con canales secundarios
                            respuesta_servidor = admin_socket_ui.escribir_operacion_inicio_sesion(json.dumps({
                                'operacion': 'login',
                                'data': [correo, password, admin_socket_ui.obtener_numero_serie()]
                            }))

                            #Checar si no da un NONE
                            print('[RESPUESTA SERVIDOR]')
                            print(respuesta_servidor)

                            if respuesta_servidor is not None:
                                if respuesta_servidor['success']:
                                    conexion_secundarios = admin_socket_ui.conexiones_canales_secundarios()
                                    print(conexion_secundarios)
                                    if conexion_secundarios['success']:
                                            
                                        validacion_secundarios = admin_socket_ui.validacion_canales_secundarios()
                                        if validacion_secundarios['success']:
                                            administrador_logueado = respuesta_servidor['data']
                                            print(administrador_logueado)
                                            window = CargaWindow(self, administrador_logueado, self.close)
                                            #window.setWindowModality(QtCore.Qt.ApplicationModal)
                                            window.show()
                                        else:
                                            admin_socket_ui.cerrado_sockets()
                                            QMessageBox.critical(self, 'Advertencia', 'No se pudo realizar la validación con los canales secundarios', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                                            self.close() 
                                    else:
                                        admin_socket_ui.cerrado_sockets()
                                        QMessageBox.critical(self, 'Advertencia', 'No se pudo realizar la conexión con los canales secundarios', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                                        self.close() 
                                else:
                                    admin_socket_ui.cerrado_sockets()
                                    QMessageBox.critical(self, 'Advertencia', respuesta_servidor['msg'], QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                            else:
                                QMessageBox.critical(self, 'Advertencia', 'Hubo un error al realizar el inicio de sesión', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 

                        else:
                            QMessageBox.critical(self, 'Advertencia', respuesta['msg'], QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                    else:
                        QMessageBox.critical(self, 'Ooops... algo ocurrió', 'No se pudo realizar la conexión temporal con el servidor', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                else:
                    QMessageBox.critical(self, 'Ooops... algo ocurrió', 'No se pudieron crear los sockets de manera correcta', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 

    # FUNCION PARA EL LLLAMADO DE LA PAGINA PRINCIPAL 
    def abrir_principal_window(self, id_propieatrio):
        self.close()
        window = PrincipalWindow(id_propieatrio)
        window.show()
        self.setWindowFlag(Qt.Window)
    
    def abrir_recuperar_password(self):
        if not self.ventana_abierta:
            self.ventana_abierta:True
            window = RecuperarPasswordWindow(self)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.destroyed.connect(self.ventana_cerrada)
            window.show()
            self.setWindowFlag(Qt.Window)
    
    def cambio_visible_password(self):
        if self.password_txt.echoMode() == QLineEdit.Password:
            self.password_txt.setEchoMode(QLineEdit.Normal)
        else:
            self.password_txt.setEchoMode(QLineEdit.Password)

    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False
