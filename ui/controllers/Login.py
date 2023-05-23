from PySide2.QtWidgets import QWidget
from views.Login import Login
from views.Principal import Principal

class Login(QWidget, Login):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def open_principal_window(self):
        pass

    def iniciar_sesion(self):
        
        self.passwordF_lbl.setText('')
        self.correoF_lbl.setText('')
        user_entry = self.correo_txt.text()
        password_entry = self.password_txt.text()

        user_entry = str("'" + user_entry + "'")
        password_entry = str("'" + password_entry + "'")

        dato1 = self.d1.busca_user(user_entry)
        dato2 = self.d2.busca_password(password_entry)

        if dato1 == [] and dato2 == []:
            self.passwordF_lbl.setText('Contraseña incorrecta')
            self.correoF_lbl.setText('Correo incorrecto')
        else:
            if dato1 == []:
                self.correoF_lbl.setText('Correo incorrecto')
            else:
                dato1 = dato1[0][1]
            
            if dato2 == []:
              self.passwordF_lbl.setText('Contraseña incorrecta')
            else:
                dato2 = dato2[0][2]

            if dato1 != [] and dato2 != []:
                self.hide()
                self.window = Principal()
                self.window.show()


class Principal(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
                      


        
