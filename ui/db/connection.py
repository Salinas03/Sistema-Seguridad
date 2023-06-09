# IMPORTACION DE LAS LIBRERIAS A OCUPAR
import mysql.connector
# from decouple import config
from dotenv import load_dotenv
import os

load_dotenv()


# FUNCION PARA PODER HACER LA CONEXION A LA BASE DE DATOS
def conexion():
    # CREACION DE LA VARIABLE A EXPORTAR, LA CUAL CONTENDRA LA CONEXION A LA BASE DE DATOS
    conexion = mysql.connector.connect(
                            host = os.getenv('MYSQLHOST'),
                            database = os.getenv('MYSQLDATABASE'),
                            user = os.getenv('MYSQLUSER'),
                            password = os.getenv('MYSQLPASSWORD'),
                            port = os.getenv('MYSQLPORT')
                            # host = 'containers-us-west-35.railway.app',
                            # database = 'railway',
                            # user = 'root',
                            # password = '3yJiRo5XmaoUr8hjNfT8',
                            # port = '6834'
                            )
    print('Base de datos conectada')
    return conexion
