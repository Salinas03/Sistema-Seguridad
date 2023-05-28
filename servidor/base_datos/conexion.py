import mysql.connector
from mysql.connector import Error
from decouple import config

class BaseDatos:
    def __init__ (self):
        try:
            self.conexion = mysql.connector.connect(
                host=config('MYSQLHOST'),
                port=config('MYSQLPORT'),
                user=config('MYSQLUSER'),
                password=config('MYSQLPASSWORD'),
                database=config('MYSQLDATABASE'),
                auth_plugin='mysql_native_password'
            )
            print('Conexión exitosa')

        except Error as err:
            print(f'Error al intentar la conexión {err}')

    def obtener_equipos_computo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE rol={0}')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')

    def obtener_equipos_administradores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE rol={1}')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')

    def obtener_equipo_por_nombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}"')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')

    def obtener_equipo_admin_por_nombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND rol={1}')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')




