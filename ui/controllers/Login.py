#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import *
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from db.connection import conexion
from modelos.propietarios_consultas import Propietario
from PySide2.QtCore import QRegExp, QTimer
from PySide2.QtGui import QRegExpValidator


# CLASE PARA EL INICIO DE SESION
class LoginWindow(Login, QWidget):    
    # FUNCION PARA PODER INICIAR
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.propietario = Propietario(conexion()) # LLAMADA A LA BASE DE DATOS Y ASIGNADA A UNA VARIABLE

        # LLAMADO DE INICIO DE SESION                                           # AQUI SE MANDAN LOS DATOS DE LOS TXT
        #self.x = self.ingresar_btn.clicked.connect(lambda:self.iniciar_sesion(self.correo_txt.text(),self.password_txt.text()))
        self.x = self.ingresar_btn.clicked.connect(self.iniciar_sesion)

        # VALIDACIÓN DE DATOS EN LOS QLineEdit
        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))

        # LLAMADO DE LAS VALIDACIONES EN LOS CAMPOS REQUERIDOS
        self.correo_txt.setValidator(email)
        self.password_txt.setValidator(only_password)
    
    
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
            # if correo and password: # CONDICION PARA VERIFICAR EL CORREO Y LA CONTRASEÑA DE LA BD
            #     correo = self.propietario.obtener_correo_propietario(correo,password)
            #     if correo: # CONDICION PARA INICIAR SESION
            #         self.abrir_principal_window()
            #     else:
            #         QMessageBox.critical(self, 'Advertencia', 'Correo y/o contraseña invalidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            if correo and password:
                id_propieatrio = self.propietario.seleccionar_propietario_id_login(correo)
                if id_propieatrio:
                    self.abrir_principal_window(id_propieatrio)
                else:
                    QMessageBox.critical(self, 'Advertencia', 'Correo y/o contraseña invalidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close) 


    # FUNCION PARA EL LLLAMADO DE LA PAGINA PRINCIPAL 
    def abrir_principal_window(self, id_propieatrio):
        self.close()
        window = PrincipalWindow(id_propieatrio)
        window.show()
        self.setWindowFlag(Qt.Window)
    






 

        



                      


        
