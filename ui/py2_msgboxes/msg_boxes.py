from PySide2.QtWidgets import *
from PySide2.QtGui import QIcon

class MsgBox(QMessageBox):
    def __init__(self, title, text):
        super().__init__()
        self.setWindowTitle(title)
        self.setText(text)

    def set_custom_icon(self,icon):
        self.setIconPixmap(icon)
        q_icon = QIcon(icon)
        self.setWindowIcon(q_icon)

    def set_si_no_buttons(self):
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

def warning_msg(title, text):
    icon = 'py2_msgboxes/icons/eliminar.png'    
    msg_box = MsgBox(title, text)
    msg_box.set_custom_icon(icon)
    msg_box.set_si_no_buttons()
    resp = msg_box.exec_()
    return resp