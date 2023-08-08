#IMPORTACION DE LAS LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QApplication
from controllers.IngresarIP import IngresoipWindow

# CONDICION PARA LA EJECUCION DEL PROGRAMA
if __name__ == "__main__":
    app = QApplication()
    
    window = IngresoipWindow()
    window.show()

    app.exec_()