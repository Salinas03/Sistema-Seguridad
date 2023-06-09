from mysql.connector import Error

class Equipo():

    def __init__(self, conexion):
        self.conexion = conexion
    
    def insertarCompus(self):
        pass

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

    def obtener_equipo_por_nombre_numero_serie(self, nombre, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND numero_serie_equipo="{numero_serie}"')
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

    def obtener_equipo_admin_por_nombre_numero_serie(self, nombre, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND numero_serie_equipo="{numero_serie}" AND rol={1}')
                resultado = cursor.fetchall()
                return resultado
            except Error as err:
                print(f'Error al intentar la conexión {err}')
    
    def seleccionar_compus(self):
        try:
            cursor = self.conexion.cursor()
            cursor.execute(f'SELECT id_equipo,nombre_equipo,numero_serie_equipo,propietario_equipo,rol FROM equipos')
            resultado = cursor.fetchall()
            return resultado
        except Error as err:
            print(f'Error al intentar la conexion {err}')
    

    def insertar_compus(self, equipo, numSerie, propietario, rol):
        if self.conexion.is_connected():
            try:
                cursor= self.conexion.cursor()
                sql = "INSERT INTO equipos (nombre_equipo,numero_serie_equipo,propietario_equipo,rol) VALUES (%s,%s,%s,%s)"
                val = (f"{equipo}",f"{numSerie}",f"{propietario}",f"{rol}")
                cursor.execute(sql, val)
                self.conexion.commit()

            except Error as err:
                print(f'Error al intentar la conexion {err}')


