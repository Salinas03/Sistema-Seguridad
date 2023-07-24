from PySide2.QtWidgets import *
from views.RecuperaPassword import RecuperarContrasenia
from PySide2.QtGui import QRegExpValidator
from utils.correo import *
from utils.correo import verificacion
from db.connection import conexion
from modelos.propietarios_consultas import Propietario

from PySide2.QtCore import * 

class RecuperarPasswordWindow(RecuperarContrasenia,QWidget):
    
    def __init__(self ,parent = None, cambio_de_password = None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.ocultar_segunda_tercera()
        self.cambio_de_password = cambio_de_password

        self.recuperacion_btn.clicked.connect(self.ocultar_segunda_tercera_parte)
        self.recuperacion_codigo_btn.clicked.connect(self.ocultar_primera_segunda_parte)
        self.cambiar_password_btn.clicked.connect(self.cambio_password)

        self.regresar_2_btn.clicked.connect(self.mostrar_primera_parte)
        self.regresar_btn.clicked.connect(self.mostrar_primera_parte)

        only_password = QRegExpValidator(QRegExp('^[A-Za-z0-9.@/_&$%!-]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES

        self.nuevo_password_txt.setValidator(only_password)
        self.confirmar_nuevo_password_txt.setValidator(only_password)

        self.codigo_verificacion = None


    # Inicio
    def ocultar_segunda_tercera(self):
        self.cambio_password_widget.hide()
        self.confirma_codigo_widget.hide()
        self.correo_recuperacion_txt.setFocus()
    
    # Pasar a la segunda parte
    def ocultar_segunda_tercera_parte(self):
        correo = self.correo_recuperacion_txt.text()
        if  correo != '':
            if self.codigo_verificacion is None:
                respuesta = Propietario(conexion()).seleccionar_propietario_correo(correo)

                if respuesta['success']:
                    if respuesta['data']:
                        self.codigo_verificacion = enviar_correo(correo)
            if self.codigo_verificacion is not None:
                self.ingresa_correo_widget.hide()
                self.confirma_codigo_widget.show()
                self.cambio_password_widget.hide()
                self.codigo_recuperacion_txt.setFocus()
                return self.codigo_verificacion
            else:
                QMessageBox.critical(self, 'Oops, algo ocurrio', 'No se pudo enviar el correo de verificacion, intente de nuevo', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                return None
        else:
            QMessageBox.critical(self, 'Error', 'Introduzca un correo en el campo de texto', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            return None
          
    # pasar a la tercera parte 
    def ocultar_primera_segunda_parte(self):
        codigo = self.ocultar_segunda_tercera_parte()
        if codigo is not None:
            codigo_txt = self.codigo_recuperacion_txt.text() 
            if codigo_txt == '':
                QMessageBox.warning(self, 'Error', 'Por favor de poner el codigo de verificación', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            else:
                if verificacion(codigo_txt, codigo): 
                    QMessageBox.information(self, 'Codigo correcto', 'El codigo de verificacion es valido', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                    self.ingresa_correo_widget.hide()
                    self.confirma_codigo_widget.hide()
                    self.cambio_password_widget.show()
                    self.nuevo_password_txt.setFocus()
                else:
                    QMessageBox.warning(self, 'Advertencia', 'El codigo que ingreso no es valido', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                    self.close()
    
    
    # regresar a la primera parte
    def mostrar_primera_parte(self):
        self.ingresa_correo_widget.show()
        self.confirma_codigo_widget.hide()
        self.cambio_password_widget.hide()
        self.codigo_recuperacion_txt.clear()
        self.correo_recuperacion_txt.setFocus()
        self.nuevo_password_txt.clear()
        self.confirmar_nuevo_password_txt.clear()

    def cambio_password(self):
        from controllers.Login import LoginWindow
        nuevo_password = self.nuevo_password_txt.text()
        correo = self.correo_recuperacion_txt.text()
        confirmar_password = self.confirmar_nuevo_password_txt.text()

        print('CORREO')
        print(correo)

        if nuevo_password == '' or confirmar_password == '':
            QMessageBox.warning(self, 'Error', 'Ingresa la contraseña', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

        elif nuevo_password != confirmar_password:
             QMessageBox.warning(self, 'Error', 'Las contraseñas no coinciden', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
        else:
            respuesta = Propietario(conexion()).actualizar_contrasena_propietario(nuevo_password, correo)
            if respuesta['success']:
                QMessageBox.information(self, 'Actualización', 'La recuperación de la contraseña fue existosa', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.close()
                window = LoginWindow(self)
                window.show()
            else:
                print('No se recibio respuesta')

    
    
    # FUNCION PARA DEFINIR QUE LA VENTANA CAMBIE SU ESTADO A FALSE        
    def ventana_cerrada(self):
        self.ventana_abierta = False
        

