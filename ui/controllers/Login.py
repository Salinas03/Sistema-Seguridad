#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from controllers.RecuperaPassword import RecuperarPasswordWindow
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator

import json
from clases.administrador_ui import admin_socket_ui

# CLASE PARA EL INICIO DE SESION
class LoginWindow(Login, QWidget):    
    # FUNCION PARA PODER INICIAR
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # LLAMADO DE INICIO DE SESION                                           # AQUI SE MANDAN LOS DATOS DE LOS TXT
        #self.x = self.ingresar_btn.clicked.connect(lambda:self.iniciar_sesion(self.correo_txt.text(),self.password_txt.text()))
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
                            if 'cliente' not in respuesta['msg']:
                                respuesta_servidor = admin_socket_ui.escribir_operaciones(json.dumps({
                                    'tabla': 'propietarios',
                                    'operacion': 'login',
                                    'data': [correo, password]
                                }))
                                
                                print('[RESPUESTA SERVIDOR]')
                                print(respuesta_servidor)

                                administrador = respuesta_servidor['data']

                                if administrador:
                                    conexion_secundarios = admin_socket_ui.conexiones_canales_secundarios()

                                    if conexion_secundarios['success']:
                                        self.abrir_principal_window(administrador[0])
                                        self.close()
                                    else:
                                        admin_socket_ui.cerrar_conexiones()
                                        QMessageBox.critical(self, 'Advertencia', 'No se pudo realizar la conexión con los canales secundarios', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                                else:
                                    admin_socket_ui.cerrar_conexiones()
                                    QMessageBox.critical(self, 'Advertencia', 'Correo y/o contraseña no válidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                            else: 
                                QMessageBox.critical(self, 'Error', 'Esta intentando ingresar al servidor como administrador desde una  computadora cliente, acción no válida', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
                        else:
                            QMessageBox.critical(self, 'Ooops... algo ocurrió', 'No se pudo realizar la validación de la conexión correctamente', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 
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
        self.close()
        window = RecuperarPasswordWindow(self)
        window.show()
        self.setWindowFlag(Qt.Window)