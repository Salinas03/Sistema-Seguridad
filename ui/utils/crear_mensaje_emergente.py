from PySide2.QtWidgets import QMessageBox

def crear_message_box(titulo, texto, tipo):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(titulo)
    msg_box.setText(texto)
    msg_box.setStandardButtons(QMessageBox.Close)


    if tipo == 'information':
        msg_box.setIcon(QMessageBox.Information)
    elif tipo == 'error':
        msg_box.setIcon(QMessageBox.Critical)
    elif tipo == 'warning':
        msg_box.setIcon(QMessageBox.Warning)

    return msg_box