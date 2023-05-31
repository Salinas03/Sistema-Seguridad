#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget, QMessageBox
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from db.connection import conexion
from modelos.admin_model import Admin


# CLASE PARA EL INICIO DE SESION
class LoginWindow(Login, QWidget):

    # FUNCION PARA PODER INICIAR
    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)
        self.admin = Admin(conexion()) # LLAMADA A LA BASE DE DATOS Y ASIGNADA A UNA VARIABLE

        # LLAMADO DE INICIO DE SESION                                           # AQUI SE MANDAN LOS DATOS DE LOS TXT
        self.x = self.ingresar_btn.clicked.connect(lambda:self.iniciar_sesion(self.correo_txt.text(),self.password_txt.text()))


    # FUNCION PARA EL INICIO DE SESION
    def iniciar_sesion(self, correo, password):
        # CONDICION PARA VALIDAR LOS DATOS DE LOS TXT CON LOS DATOS DE LA BD
        if correo and password:
            correo = self.admin.getAdmin(correo,password)
            if correo:
                self.abrir_principal_window()
            else:
                QMessageBox.warning(self, 'Error', 'Correo y/o contraseña invalidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    # FUNCION PARA EL LLLAMADO DE LA PAGINA PRINCIPAL 
    def abrir_principal_window(self):
        self.close()
        window = PrincipalWindow(self)
        window.show()
        self.setWindowFlag(Qt.Window)






 

        



                      


        
