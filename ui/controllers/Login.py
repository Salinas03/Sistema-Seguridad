from PySide2.QtWidgets import QWidget
from views.Login import Login
from PySide2.QtCore import Qt
from controllers.Principal import PrincipalWindow


class LoginWindow(Login, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.ingresar_btn.clicked.connect(self.abrir_principal_window)

    def abrir_principal_window(self):
        self.close()
        window = PrincipalWindow(self)
        window.show()
        self.setWindowFlag(Qt.Window)


    def iniciar_sesion(self):
        pass
 