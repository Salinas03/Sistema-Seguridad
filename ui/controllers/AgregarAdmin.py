from PySide2.QtWidgets import QWidget,QDialog,QLabel,QLineEdit,QMessageBox
from views.AgregarAdmin import AgregarAdmin
from PySide2.QtCore import Qt
from db.administradores import registro_user


class AgregarAdminWindow(AgregarAdmin, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.agregar_admin_btn.clicked.connect(self.agregar_admin)
        self.cancelar_admin_btn.clicked.connect(self.cancelar_registro)


    def agregar_admin(self):
        nombre = self.nombre_admin_txt.text()
        apellido = self.apellido_admin_txt.text()
        telefono = self.telefono_admin_txt.text()
        correo = self.correo_admin_txt.text()
        password = self.password_admin_txt.text()
        password2 = self.confirma_contrasenia_btn.text()

        if nombre == '' or apellido == '' or telefono == '' or correo == '' or password == '' or password2 == '':
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        elif password != password2:
            QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden, favor de verificar',QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        
        else:
            self.registro_usuario = registro_user()
            QMessageBox.warning(self, 'Registro', 'El registro se hizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def cancelar_registro(self):
        self.close()    