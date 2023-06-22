# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarAdmin import AgregarPropietario
from PySide2.QtCore import Qt
from modelos.propietarios_consultas import Propietario
from db.connection import conexion
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from controllers.Principal import Principal

# CLASE DE AGREGACION DE propietarioISTRADORES
class AgregarpropietarioWindow(AgregarPropietario,QWidget):

    def __init__(self, funcion, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.propietario = Propietario(conexion()) # LLAMADO DE LA BD Y ASIGNADA A UNA VARIABLE
        self.principal = Principal()
        self.actualizar_tabla = funcion

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        #email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:gmail|hotmail|msn|yahoo|outlook|live|[.]{1,1})+(?:com|com.mx|net|org|edu|gov|mil|biz|info|name|museum|coop|aero|xxx|)"))

        self.nombre_propietario_txt.setValidator(only_text)
        self.nombre_propietario_txt.setFocus()
        self.apellido_propietario_txt.setValidator(only_text)
        self.telefono_propietario_txt.setValidator(only_number)
        self.correo_propietario_txt.setValidator(email)
        self.password_propietario_txt.setValidator(only_password)
        self.confirma_contrasenia_txt.setValidator(only_password)

        # LLAMADO DE LA FUNCION AGREGAR propietario Y ENVIO DE LOS DATOS DE LOS TXT 
        self.agregar_admin_btn.clicked.connect(lambda:self.agregar_propietario())
        self.cancelar_admin_btn.clicked.connect(self.cancelar_registro)

    # FUNCION PARA AGREGAR ADMIB
    #                   RECEPCION DE DATOS ENVIADOS POR LOS TXT
    def agregar_propietario(self):
        # ASIGNACION DE LOS DATOS A NUEVAS VARIABLES 
        #id = self.id_propietario_txt.text()
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()
        password = self.password_propietario_txt.text()
        password2 = self.confirma_contrasenia_txt.text()
        rol = self.rol_propietario_cmbx.currentText()

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == '' or password == '' or  password2 == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        elif password != password2: 
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden, favor de verificar',QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        elif '@' not in correo:
            QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar @', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        elif '.com' or '.com.mx' or '.net' or '.org' or '.edu' or '.gov' or '.mil' or '.biz' or '.info' or '.name' or '.museum' or '.coop' or '.aero' or '.xxx' not in correo:
            QMessageBox.warning(self, 'Inserta datos validos' , 'Ingresa un correo valido \nRecuerda que deben de llevar un dominio \nEjemplo: .com', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        else:
            self.propietario.insertar_propietario(nombre,apellido,telefono,correo,password,rol)
            QMessageBox.information(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            AgregarPropietario.hide(self)
            self.actualizar_tabla(self.propietario.seleccionar_propietario())

    def cancelar_registro(self):
        self.close()   