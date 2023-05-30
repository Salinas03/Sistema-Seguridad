import mysql.connector

def conexion():
    conexion = mysql.connector.connect(host = 'localhost',
                            database = 'sistema_seguridad',
                            user = 'root',
                            password = '')
    print('Base de datos conectada')
    return conexion