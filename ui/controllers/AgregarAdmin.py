# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarAdmin import AgregarAdmin
from PySide2.QtCore import Qt
from modelos.admin_model import Admin
from db.connection import conexion
from PySide2.QtCore import QRegExp, QTimer
from PySide2.QtGui import QRegExpValidator

# CLASE DE AGREGACION DE ADMINISTRADORES
class AgregarAdminWindow(AgregarAdmin, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.admin = Admin(conexion()) # LLAMADO DE LA BD Y ASIGNADA A UNA VARIABLE

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))

        self.nombre_admin_txt.setValidator(only_text)
        self.apellido_admin_txt.setValidator(only_text)
        self.telefono_admin_txt.setValidator(only_number)
        self.correo_admin_txt.setValidator(email)
        self.password_admin_txt.setValidator(only_password)
        self.confirma_contrasenia_btn.setValidator(only_password)

        # LLAMADO DE LA FUNCION AGREGAR ADMIN Y ENVIO DE LOS DATOS DE LOS TXT 
        self.y = self.agregar_admin_btn.clicked.connect(lambda:self.agregar_admin(self.nombre_admin_txt.text(),
                                                                                  self.apellido_admin_txt.text(),
                                                                                  self.telefono_admin_txt.text(),
                                                                                  self.correo_admin_txt.text(),
                                                                                   self.password_admin_txt.text()))
        self.cancelar_admin_btn.clicked.connect(self.cancelar_registro)

    # FUNCION PARA AGREGAR ADMIB
    #                   RECEPCION DE DATOS ENVIADOS POR LOS TXT
    def agregar_admin(self,nombre, apellido, telefono, correo, password):
        # ASIGNACION DE LOS DATOS A NUEVAS VARIABLES 
        nombre = self.nombre_admin_txt.text()
        apellido = self.apellido_admin_txt.text()
        telefono = self.telefono_admin_txt.text()
        correo = self.correo_admin_txt.text()
        password = self.password_admin_txt.text()
        password2 = self.confirma_contrasenia_btn.text()

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == '' or password == '' or password2 == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        elif password != password2:
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden, favor de verificar',QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        else:
            self.admin.insertar_admin(nombre, apellido, telefono, correo, password)
            AgregarAdmin.hide(self)
            QMessageBox.warning(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)


    def cancelar_registro(self):
        self.close()    