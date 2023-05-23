import mysql.connector
from mysql.connector import Error

class BaseDatos:
    def __init__ (self):
        try:
            self.conexion = mysql.connector.connect(
                host='localhost',
                port='3306',
                user='root',
                password='root',
                database='sistema_seguridad',
                auth_plugin='mysql_native_password'
            )
            print('Conexión exitosa')

        except Error as err:
            print(f'Error al intentar la conexión {err}')

    def obtenerEquipos(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute('SELECT * FROM equipos')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')

    def obtenerEquipoPorNombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}"')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')

    def obtenerEquiposAdministradorPorNombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND rol={1}')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')




