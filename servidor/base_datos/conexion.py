import mysql.connector
from mysql.connector import Error
from decouple import config

def conexion():
    try:
        conexion = mysql.connector.connect(
            host=config('MYSQLHOST'),
            port=config('MYSQLPORT'),
            user=config('MYSQLUSER'),
            password=config('MYSQLPASSWORD'),
            database=config('MYSQLDATABASE'),
            auth_plugin='mysql_native_password'
        )
        print('Conexión exitosa con la base de datos MYSQL cloud')

        return conexion

    except Error as err:
        print(f'Error al intentar la conexión {err}')
        return None



