from PySide2.QtWidgets import QWidget
from views.Principal import Principal
from PySide2.QtWidgets import QMainWindow
from controllers.AgregarAdmin import AgregarAdminWindow
#from controllers.Login import LoginWindow
#from PySide2.QtCore import Qt


class PrincipalWindow(Principal, QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.data_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))

        self.tabla_computadoras_activas.setColumnWidth(0,560)
        self.tabla_computadoras_activas.setColumnWidth(1,560)
        self.tabla_computadoras_activas.setColumnWidth(2,560)

        self.tabla_computadoras_desactivas.setColumnWidth(0,560)
        self.tabla_computadoras_desactivas.setColumnWidth(1,560)
        self.tabla_computadoras_desactivas.setColumnWidth(2,560)

        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)
        #self.cerrar_sesion_btn.clicked.connect(self.cerrar_sesion) 


    def abrir_agregar_admin(self):
        window = AgregarAdminWindow(self)
        window.show()
    
    # def cerrar_sesion(self):
    #     self.close()
    #     window = LoginWindow(self)
    #     window.show()
    #     self.setWindowFlag(Qt.Window)
