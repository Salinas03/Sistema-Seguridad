#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QApplication
from controllers.Login import LoginWindow

# CONDICION PARA LA EJECUCION DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication()
    
    window = LoginWindow()
    window.show()

    app.exec_()