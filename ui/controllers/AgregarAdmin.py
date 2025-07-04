# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget,QMessageBox
from views.AgregarAdmin import AgregarPropietario
from PySide2.QtCore import *
from PySide2.QtCore import QRegExp
from PySide2.QtGui import QRegExpValidator
from controllers.Principal import Principal
from controllers.VerificarCorreo import VerificarCorreoWindow
from PySide2 import QtCore
from utils.correo import *
from utils.crear_mensaje_emergente import crear_message_box


# CLASE DE AGREGACION DE propietarioISTRADORES
class AgregarpropietarioWindow(AgregarPropietario,QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.principal = Principal()
        # self.verificar_correo = VerificarCorreoWindow()
        # self.actualizar_tabla = funcion

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_text = QRegExpValidator(QRegExp('^[A-Za-z ]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        self.nombre_propietario_txt.setValidator(only_text)
        self.nombre_propietario_txt.setFocus()
        self.apellido_propietario_txt.setValidator(only_text)
        self.telefono_propietario_txt.setValidator(only_number)
        self.password_propietario_txt.setValidator(only_password)
        self.confirma_contrasenia_txt.setValidator(only_password)


        # LLAMADO DE LA FUNCION AGREGAR propietario Y ENVIO DE LOS DATOS DE LOS TXT 
        self.agregar_admin_btn.clicked.connect(self.agregar_propietario)
        self.cancelar_admin_btn.clicked.connect(self.cancelar_registro)

        self.ventana_abierta = False # IDENTIFICACION DE QUE LA VENTANA ESTA CERRADA

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
        if nombre == '' or apellido == '' or telefono == '' or correo == '' or password == '' or  password2 == '':
            crear_message_box('Error', 'Favor de escribir los datos válidos', 'warning').exec_()
        
        elif password != password2:
            crear_message_box('Error', 'Las contraseñas no coinciden, facor de verificar', 'warning').exec_()
        
        else:

            valor_rol = None

            if rol == 1:
                valor_rol = 1
            elif rol == 2:
                valor_rol = 0


            if valor_rol is not None:       
                if not self.ventana_abierta:
                    codigo = enviar_correo(correo)
                    if codigo is not None:
                        # abrir ventana de codigo
                        self.ventana_abierta=True
                        window = VerificarCorreoWindow(self,[nombre, apellido, telefono, correo, password, rol], codigo, self.close)
                        window.setWindowModality(QtCore.Qt.ApplicationModal)
                        window.destroyed.connect(self.ventana_cerrada)
                        window.show()
                    else:
                        crear_message_box('Ooops, algo ocurrió', 'No se pudo enviar el correo de verificación, intente denuevo', 'error').exec_()

            else:
                crear_message_box('Selecciona un rol', 'Seleccione un rol correctamente', 'warning').exec_()

    def cancelar_registro(self):
        self.close()  

# FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False