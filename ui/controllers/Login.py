from PySide2.QtWidgets import QWidget, QMessageBox
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow
from db.connection import conexion
from modelos.admin_model import Admin



class LoginWindow(Login, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.admin = Admin(conexion())

        #self.ingresar_btn.clicked.connect(self.abrir_principal_window)
        self.x = self.ingresar_btn.clicked.connect(lambda:self.iniciar_sesion(self.correo_txt.text(),self.password_txt.text()))

    def iniciar_sesion(self, correo, password):
        if correo and password:
            correo = self.admin.getAdmin(correo,password)
            if correo:
                self.abrir_principal_window()
            else:
                QMessageBox.warning(self, 'Error', 'Correo y/o contraseña invalidos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    
    def abrir_principal_window(self):
        self.close()
        window = PrincipalWindow(self)
        window.show()
        self.setWindowFlag(Qt.Window)
 