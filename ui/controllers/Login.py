#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from db.connection import conexion
from modelos.propietarios_consultas import Propietario
from PySide2.QtCore import QRegExp, QTimer
from PySide2.QtGui import QRegExpValidator
from clases.administrador_ui import admin_socket_ui
import json

# CLASE PARA EL INICIO DE SESION
class LoginWindow(Login, QWidget):

    # FUNCION PARA PODER INICIAR
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        # LLAMADO DE INICIO DE SESION                                           # AQUI SE MANDAN LOS DATOS DE LOS TXT
        self.x = self.ingresar_btn.clicked.connect(lambda:self.iniciar_sesion(self.correo_txt.text(),self.password_txt.text()))

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))

        # LLAMADO DE LAS VALIDACIONES EN LOS CAMPOS REQUERIDOS
        self.correo_txt.setValidator(email)
        self.password_txt.setValidator(only_password)
        


    # FUNCION PARA EL INICIO DE SESION
    def iniciar_sesion(self, correo, password):
        # CONDICION PARA VALIDAR LOS DATOS DE LOS TXT CON LOS DATOS DE LA BD
        if correo == '' or password == '': # CONDICION PARA VERIFICAR QUE LOS CAMPOS DE TEXTO NO ESTEN VACIOS
                    QMessageBox.warning(self, 'Advertencia', 'Favor de llenar los campos correspondientes', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        elif '@' not in correo: # CONDICION PARA VERIFICAR QUE EXISTA UN @ EN EL CAMPO DE TEXTO CORREO
            QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar @', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        else:
            if correo and password: # CONDICION PARA VERIFICAR EL CORREO Y LA CONTRASEÑA DE LA BD
                respuesta  = admin_socket_ui.crear_sockets()
                if respuesta['success']:
                    print(respuesta['msg'])
                    respuesta = admin_socket_ui.conexion_temporal()
                    if respuesta['success']:    
                        print(respuesta['msg'])
                        respuesta = admin_socket_ui.validacion_conexion()
                        if respuesta['success']:
                            print(respuesta['msg'])

                            peticion = {
                                'tabla': 'propietarios',
                                'operacion': 'login',
                                'data': [correo, password]
                            }

                            respuesta = admin_socket_ui.escribir_operaciones(json.dumps(peticion))

                            if respuesta['data'][0]:
                                self.abrir_principal_window()
                                self.close()
                            else:
                                QMessageBox.critical(self, 'Advertencia', 'Correo y/o contraseña invalidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                            print(respuesta['data'][0])
                        else:
                            print(respuesta['msg']) 
                    else:
                        print(respuesta['msg']) 
                else:
                    print(respuesta['msg']) 
                    
    # FUNCION PARA EL LLLAMADO DE LA PAGINA PRINCIPAL 
    def abrir_principal_window(self):
        self.close()
        window = PrincipalWindow()
        window.show()
        self.setWindowFlag(Qt.Window)
    






 

        



                      


        
