#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QApplication
from controllers.Login import LoginWindow
from controllers.Principal import PrincipalWindow
from controllers.AgregarAdmin import  AgregarAdminWindow
from controllers.AgregarCompus import AgregarCompusWindow
from controllers.OpcionesComputadora import OpcionesCompusWindow

# CONDICION PARA LA EJECUCION DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication()

    window = OpcionesCompusWindow()
    window.show()

    app.exec_() 