import os
import subprocess
import json
from PySide2.QtWidgets import *
from views.ingresar_IP import MainWindow


class IngresoipWindow(MainWindow, QWidget):

    def __init__(self, parent = None):
        super().__init__(parent)
        self.setupUi(self)

        self.ingresar_ip_btn.clicked.connect(self.recepcionIP)


    def recepcionIP(self):
        ip = self.ip_txt.text()
        if ip != '':
            print(ip)
            self.crear_ip(ip)
        else:
            QMessageBox.warning(self, 'Advertencia', 'Favor de llenar los campos correspondientes', QMessageBox.StandardButton.Close,QMessageBox.StandardButton.Close)

    def crear_ip(self,ip):
        data = {"ip" : ip}
        data_json = json.dumps(data)
        path = f'{os.getcwd()}/data.json'

        # Write the JSON data to the file
        with open(path, "w") as json_file:
            json_file.write(data_json)



        script_path = f'{os.getcwd()}\\cliente_ui.py'

        try:
            startupinfo = subprocess.STARTUPINFO()
            startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
            subprocess.Popen(['python', script_path, ip],shell=True,startupinfo=startupinfo)
        except subprocess.SubprocessError as e:
            print(f'Error al correr el script {e}')




