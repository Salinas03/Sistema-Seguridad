from PySide2.QtWidgets import QApplication
from controllers.Login import LoginWindow
from controllers.Principal import PrincipalWindow
from controllers.AgregarAdmin import  AgregarAdminWindow

if __name__ == "__main__":
    app = QApplication()

    window = LoginWindow()
    window.show()

    app.exec_()