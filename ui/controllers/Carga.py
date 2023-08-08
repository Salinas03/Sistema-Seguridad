from views.Carga import Carga
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2 import QtCore
from controllers.Principal import PrincipalWindow

COUNTER = 0

class CargaWindow(Carga,QWidget):

    def __init__(self, parent = None, propietario = None, cerrar_login = None):
        self.propietario = propietario
        self.cerrar_login = cerrar_login
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)

        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progreso)

        self.timer.start(35)


    def progreso(self):
        global COUNTER

        self.progressBar.setValue(COUNTER)
        
        if COUNTER > 100:
            self.timer.stop()
            window = PrincipalWindow(self.propietario)
            window.setWindowModality(QtCore.Qt.ApplicationModal)
            window.show()
            self.close()
            self.cerrar_login()

        COUNTER += 6
    