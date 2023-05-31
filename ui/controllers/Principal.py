
# IMPORTACION DE LA LIBRERIAS A OCUPAR
from PySide2.QtWidgets import QWidget
from views.Principal import Principal
from controllers.AgregarAdmin import AgregarAdminWindow


class PrincipalWindow(Principal, QWidget):

    # FUNCION PARA INICIO DE LA VENTANA
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        # BOTONES QUE REDIRIGEN A LAS PAGINAS DEL STACKEDWIDGET
        self.home_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_2))
        self.data_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page))
        self.settings_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_3))
        self.user_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_4))

        # PONER LAS MEDIDAS DEL ANCHO DE LAS TABLAS
        self.tabla_computadoras_activas.setColumnWidth(0,560)
        self.tabla_computadoras_activas.setColumnWidth(1,560)
        self.tabla_computadoras_activas.setColumnWidth(2,560)

        self.tabla_computadoras_desactivas.setColumnWidth(0,560)
        self.tabla_computadoras_desactivas.setColumnWidth(1,560)
        self.tabla_computadoras_desactivas.setColumnWidth(2,560)

        self.computadoras_registradas_table.setColumnWidth(0,350)
        self.computadoras_registradas_table.setColumnWidth(1,350)
        self.computadoras_registradas_table.setColumnWidth(2,350)
        self.computadoras_registradas_table.setColumnWidth(3,350)

        self.administradores_tabla.setColumnWidth(0,450)
        self.administradores_tabla.setColumnWidth(1,450)
        self.administradores_tabla.setColumnWidth(2,450)
        self.administradores_tabla.setColumnWidth(3,450)

        # OCULTAR TABLA DE ADMINISTRADORES
        self.ocultar_admin_table.hide()
        self.frame_13.hide()

        # LLAMADO DE LAS FUNCIONES PARA APARECER Y DESAPARECER LA TABLA DE ADMINISTRADORES
        self.mostrar_admin_table.clicked.connect(self.aparecer_tabla_administradores)
        self.ocultar_admin_table.clicked.connect(self.desaparecer_tabla_administradores)

        
        # LLAMADO PARA AGREGAR UN NUEVO ADMINISTRADOR
        self.agregar_admin_btn.clicked.connect(self.abrir_agregar_admin)
        #self.cerrar_sesion_btn.clicked.connect(self.cerrar_sesion) 


    # FUNCION PARA MANDAR LLAMAR LA VENTANA DE AGREGAR ADMIN
    def abrir_agregar_admin(self):
        window = AgregarAdminWindow(self)
        window.show()

    # FUNCION PARA APARECER LA TABLA DE ADMINISRADORES
    def aparecer_tabla_administradores(self):
        self.mostrar_admin_table.hide()
        self.ocultar_admin_table.show()
        self.frame_13.show()

    # FUNCION PARA DESAPARECER LA TABLA DE ADMINISRADORES
    def desaparecer_tabla_administradores(self):
        self.mostrar_admin_table.show()
        self.ocultar_admin_table.hide()
        self.frame_13.hide()