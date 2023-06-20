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
                            )
    print('Base de datos conectada')
    return conexion
