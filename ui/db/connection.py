# IMPORTACION DE LAS LIBRERIAS A OCUPAR
import mysql.connector

# FUNCION PARA PODER HACER LA CONEXION A LA BASE DE DATOS
def conexion():
    # CREACION DE LA VARIABLE A EXPORTAR, LA CUAL CONTENDRA LA CONEXION A LA BASE DE DATOS
    conexion = mysql.connector.connect(host = 'localhost',
                            database = 'sistema_seguridad',
                            user = 'root',
                            password = '')
    print('Base de datos conectada')
    return conexion