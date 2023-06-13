from PySide2.QtWidgets import *
from views.EditarPropietario import EditarPropietario
from db.connection import conexion
from modelos.propietarios_consultas import Propietario
from PySide2.QtCore import Qt, QRegExp 
from PySide2.QtGui import QRegExpValidator


class ModificarPropietarioWindow(EditarPropietario,QWidget):
    
    def __init__(self, funcion ,parent = None, _id = None):
        self._id = _id
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowFlag(Qt.Window)
        self.llenar_campos_texto()
        #self.propietario = Propietario(conexion())
        self.actualizar_tabla = funcion


        only_text = QRegExpValidator(QRegExp('^[A-Za-z]{3,50}')) # VALIDACION DE DATOS ALFANUMERICOS DONDE SOLO PUEDE TENER ENTRE 3 Y 100 VALORES
        only_number = QRegExpValidator(QRegExp('^[0-9]{0,10}'))
        #   VALIDACION PARA CAMPO DE CORREO, DONDE SE DEBE PONER UN VALOR ALFANUMERICO, DESPUES LA ACEPTACION DEL @, POR CONSIGUIENTE
        #   OTRO VALOR ALFANUMERICO Y LA ACEPTACION DEL .COM U OTRO DOMINIO
        #email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$"))
        email = QRegExpValidator(QRegExp("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@(?:gmail|hotmail|msn|yahoo|outlook|live|[.]{1,1})+(?:com|com.mx|net|org|edu|gov|mil|biz|info|name|museum|coop|aero|xxx|[a-zA-Z]{2})$"))
        rol = QRegExpValidator(QRegExp('^[0-1]{1,1}'))

        self.nombre_propietario_txt.setValidator(only_text)
        self.nombre_propietario_txt.setFocus()
        self.apellido_propietario_txt.setValidator(only_text)
        self.telefono_propietario_txt.setValidator(only_number)
        self.correo_propietario_txt.setValidator(email)
        self.rol_propietario_txt.setValidator(rol)

        #self.editar_admin_btn.clicked.connect(self.editar_propietario)
        self.agregar_admin_btn.clicked.connect(self.editar_propietario)
        self.cancelar_admin_btn.clicked.connect(self.cerrar_ventana)

    def llenar_campos_texto(self):
        data = Propietario(conexion()).seleccionar_propietario_id(self._id)
        if len(data) >= 1:
            propietario = data[0]
            self.nombre_propietario_txt.setText(propietario[1])
            self.apellido_propietario_txt.setText(propietario[2])
            self.telefono_propietario_txt.setText(propietario[3])
            self.correo_propietario_txt.setText(propietario[4])
            self.rol_propietario_txt.setText(str(propietario[5]))
        else:
            print('No existe ningún valor')

    def checar_inputs(self):
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()
        rol = self.rol_propietario_txt.text()

        errores_count = 0

        # CONDICIONES PARA LA VERIFICACION DE LOS CAMPOS 
        if nombre == '' or apellido == '' or telefono == '' or correo == ''  or rol == '' :
            QMessageBox.warning(self, 'Error', 'Por favor de poner datos validos', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
            errores_count +=1
        elif errores_count == 0:
            return True
                    
    def editar_propietario(self):
        nombre = self.nombre_propietario_txt.text()
        apellido = self.apellido_propietario_txt.text()
        telefono = self.telefono_propietario_txt.text()
        correo = self.correo_propietario_txt.text()
        rol = self.rol_propietario_txt.text()

        data = [nombre,apellido,telefono,correo,rol]

        if self.checar_inputs():
            propietario = Propietario(conexion())
            if propietario.actualizar_propietario(self._id, data):
                QMessageBox.information(self, 'Actualización', 'El propietario se actualizo con exito', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)
                self.actualizar_tabla(propietario.seleccionar_propietario())
                self.close()
            

    def cerrar_ventana(self):
        self.close()
                


