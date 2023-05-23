from PySide2.QtWidgets import QApplication
from controllers.Login import Login
from controllers.Principal import Principal

if __name__ == "__main__":
    app = QApplication()
    window = Principal()
    window.show()

    app.exec_()