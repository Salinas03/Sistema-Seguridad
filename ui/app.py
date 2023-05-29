from PySide2.QtWidgets import QApplication
from controllers.Login import Login
from controllers.Principal import Principal
from controllers.AgregarAdmin import  AgregarAdmin

if __name__ == "__main__":
    app = QApplication()
    #window = Principal()
    window = Login()
    window.show()

    app.exec_()