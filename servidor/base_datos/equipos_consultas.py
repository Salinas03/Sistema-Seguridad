from mysql.connector import Error
import json

class EquiposConsultas():

    def __init__(self, conexion):
        self.conexion = conexion
    
    def obtener_equipos_computo(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # cursor.execute(f"SELECT * FROM equipos")
                cursor.execute(f"SELECT e.id_equipo, e.area_equipo, e.caracteristica_equipo , e.nombre_equipo, e.numero_serie_equipo, CONCAT(p.nombre_propietario, ' ', p.apellido_propietario) as propietario_equipo,CASE WHEN e.rol = 1 THEN 'administrador'WHEN e.rol = 0 THEN'cliente' END as rol FROM equipos as e JOIN propietarios as p ON e.propietario_equipo = p.id_propietarios ORDER BY e.rol DESC")
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al intentar la obtener los equipos de cómputo {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener los equipos de cómputo {err}'})

    def obtener_equipos_computo_clientes(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                # cursor.execute(f"SELECT * FROM equipos WHERE rol={0}")
                cursor.execute(f"SELECT e.area_equipo, e.caracteristica_equipo, e.nombre_equipo, e.numero_serie_equipo, CONCAT(p.nombre_propietario, ' ', p.apellido_propietario) as propietario_equipo,CASE WHEN e.rol = 1 THEN 'administrador'WHEN e.rol = 0 THEN'cliente' END as rol FROM equipos as e JOIN propietarios as p ON e.propietario_equipo = p.id_propietarios WHERE e.rol={0} ORDER BY e.rol DESC")
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al intentar la obtener los equipos de cómputo {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener los equipos de cómputo {err}'})

    def obtener_equipo_computo_por_id(self, id_equipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE id_equipo="{id_equipo}"')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al intentar la obtener los equipos de cómputo por id {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener los equipos de cómputo {err}'})

    def obtener_equipos_administradores(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE rol={1}')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al intentar la conexión {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener los equipos administradores {err}'})
    
    def obtener_equipo_por_nombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}"')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener equipo por nombre {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el equipo por nombre {err}'})

    def obtener_equipo_por_numero_serie(self, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE numero_serie_equipo="{numero_serie}"')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener equipo por nombre {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el equipo por nombre {err}'})

    def obtener_equipo_por_nombre_numero_serie(self, nombre, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND numero_serie_equipo="{numero_serie}"')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener equipo por nombre y número de serie {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el equipo por nombre y número de serie {err}'})

    def obtener_equipo_admin_por_nombre(self, nombre):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND rol={1}')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener equipo administrador por nombre {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el equipo administrador por nombre {err}'})

    def obtener_equipo_admin_por_nombre_numero_serie(self, nombre, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT * FROM equipos WHERE nombre_equipo="{nombre}" AND numero_serie_equipo="{numero_serie}" AND rol={1}')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener equipo administrador por nombre y número de serie {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el equipo administrador por nombre y número de serie {err}'})

    def obtener_propietario_numero_serie(self, numero_serie):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                print(f'SELECT propietario_equipo FROM equipos WHERE numero_serie_equipo={numero_serie}')
                query = 'SELECT propietario_equipo FROM equipos WHERE numero_serie_equipo= %s'
                cursor.execute(query, (numero_serie,))
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al obtener el propietario de equipo administrador por número de serie {err}')
                return json.dumps({'success': False, 'msg': f'Error al obtener el propietario de equipo administrador por número de serie {err}'})

    def insertar_equipo_computo(self, nombre_equipo, num_serie, propietario, rol, area, caracteristica):
        if self.conexion.is_connected():
            try:
                cursor= self.conexion.cursor()
                sql = "INSERT INTO equipos (nombre_equipo,numero_serie_equipo,propietario_equipo,rol,area_equipo, caracteristica_equipo) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (f"{nombre_equipo}",f"{num_serie}",f"{propietario}",f"{rol}",f"{area}",f"{caracteristica}")
                cursor.execute(sql, val)
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se realizó la inserción correctamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al realizar la inserción'})

    def actualizar_equipo_computo(self, id_equipo, data):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f'UPDATE equipos SET nombre_equipo = %s,numero_serie_equipo = %s,propietario_equipo=%s,rol=%s, area_equipo=%s, caracteristica_equipo=%s WHERE id_equipo={id_equipo}'
                cursor.execute(sql, data)
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se realizó la actualización correctamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al realizar la actualización'})

    def borrar_equipo_computo(self, id_equipo):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f'DELETE FROM equipos WHERE id_equipo={id_equipo}'
                cursor.execute(sql)
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se realizó la eliminación correctamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al realizar la eliminación'})