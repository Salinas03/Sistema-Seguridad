# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarAdmin import AgregarPropietario
from PySide2.QtCore import Qt
from db.connection import conexion
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from controllers.Principal import Principal
from clases.administrador_ui import admin_socket_ui
import json

# CLASE DE AGREGACION DE propietarioISTRADORES
class AgregarpropietarioWindow(AgregarPropietario,QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.principal = Principal()
        # self.actualizar_tabla = funcion

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        #email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:gmail|hotmail|msn|yahoo|outlook|live|[.]{1,1})+(?:com|com.mx|net|org|edu|gov|mil|biz|info|name|museum|coop|aero|xxx|)"))
        rol = QRegExpValidator(QRegExp('^[0-1]{1,1}'))

        self.nombre_propietario_txt.setValidator(only_text)
        self.nombre_propietario_txt.setFocus()
        self.apellido_propietario_txt.setValidator(only_text)
        self.telefono_propietario_txt.setValidator(only_number)
        self.correo_propietario_txt.setValidator(email)
        self.password_propietario_txt.setValidator(only_password)
        self.confirma_contrasenia_txt.setValidator(only_password)
        # self.rol_propietario_txt.setValidator(rol)

        # LLAMADO DE LA FUNCION AGREGAR propietario Y ENVIO DE LOS DATOS DE LOS TXT 
        self.agregar_admin_btn.clicked.connect(self.agregar_propietario)
        self.y = self.cancelar_admin_btn.clicked.connect(self.cancelar_registro)

    # FUNCION PARA AGREGAR ADMIB
    #                   RECEPCION DE DATOS ENVIADOS POR LOS TXT
    def agregar_propietario(self):
        # ASIGNACION DE LOS DATOS A NUEVAS VARIABLES 
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()
        password = self.password_propietario_txt.text()
        password2 = self.confirma_contrasenia_txt.text()

        rol = self.rol_propietario_cmbx.currentIndex()

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == '' or password == '' or  password2 == '' or rol == '' :
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        elif password != password2: 
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden, favor de verificar',QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        # elif '@' not in correo:
        #     QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar @', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        # elif '.com' or '.com.mx' or '.net' or '.org' or '.edu' or '.gov' or '.mil' or '.biz' or '.info' or '.name' or '.museum' or '.coop' or '.aero' or '.xxx' not in correo:
        #     QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar un dominio \nEjemplo: .com', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        else:

            valor_rol = None

            if rol == 1:
                valor_rol = 1
            elif rol == 2:
                valor_rol = 0

            if valor_rol is not None:

                peticion = {
                    'tabla': 'propietarios',
                    'operacion': 'insertar',
                    'data': [nombre, apellido, telefono, correo, password, valor_rol]
                }

                respuesta_insertar = admin_socket_ui.escribir_operaciones(json.dumps(peticion))
                
                if respuesta_insertar['success']:
                    self.nombre_propietario_txt.clear()
                    self.apellido_propietario_txt.clear()
                    self.telefono_propietario_txt.clear()
                    self.correo_propietario_txt.clear()
                    self.password_propietario_txt.clear()

                    QMessageBox.information(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                    AgregarPropietario.hide(self)

                else:
                    QMessageBox.critical(self, 'Oops, algo ocurrio', 'Hubo un problema al realizar el registro', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

            else:
                QMessageBox.warning(self, 'Selecciona un rol' , 'Seleccione un rol correctamente', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def cancelar_registro(self):
        self.close()   