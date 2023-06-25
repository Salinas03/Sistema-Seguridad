from mysql.connector import Error
import json

class PropietariosConsultas:
    
    def __init__(self,conexion):
        self.conexion = conexion 
    
    def obtener_propietario(self, correo, password):
        with self.conexion.cursor() as cursor:
            try:
                sql = """SELECT * FROM propietarios WHERE correo_propietario = %s AND contrasena_propietario = %s"""
                cursor.execute(sql, (correo, password))
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                return json.dumps({'success': False, 'msg': 'Hubo un error al obtener los propietarios por correo y contraseña'})

    def insertar_propietario(self, nombre, apellido, telefono, correo, password, rol):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = "INSERT INTO propietarios (nombre_propietario,apellido_propietario,telefono_propietario,correo_propietario,contrasena_propietario,rol) VALUES (%s,%s,%s,%s,%s,%s)"
                val = (f"{nombre}",f"{apellido}",f"{telefono}",f"{correo}",f"{password}",f"{rol}")
                cursor.execute(sql, val)
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se realizó la inserción exitosamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al realizar la inserción'})
    
    def obtener_propietarios(self):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                cursor.execute(f'SELECT id_propietarios,nombre_propietario,apellido_propietario,telefono_propietario,correo_propietario,rol FROM propietarios')
                resultado = cursor.fetchall()
                return json.dumps({'success': True, 'data': resultado})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al obtener los propietarios'})

    def actualizar_propietario(self, id_propietarios, data):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"""UPDATE propietarios SET nombre_propietario = %s,apellido_propietario = %s,telefono_propietario=%s,correo_propietario=%s,rol=%s WHERE id_propietarios={id_propietarios}"""
                cursor.execute(sql, data)
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se ha actualizado la tabla exitosamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al actualizar la tabla de propietarios'})

    def seleccionar_propietario_id(self, id_propietarios):
        try:
            cursor = self.conexion.cursor()
            sql = f'SELECT id_propietarios,nombre_propietario,apellido_propietario,telefono_propietario,correo_propietario,rol FROM propietarios WHERE id_propietarios = {id_propietarios}'
            cursor.execute(sql)
            resultado = cursor.fetchall()  # Obtener los resultados de la consulta
            #cursor.close()  # Cerrar el cursor después de obtener los resultados
            return json.dumps({'success': True, 'data': resultado})
            #self.conexion.commit()
        except Error as err:
            print(f'Error al intentar la conexion {err}')
            return json.dumps({'success': False, 'msg': 'Hubo un error al obtener el propietario por id'})
        
    def eliminar_propietario(self,id_propietarios):
        if self.conexion.is_connected():
            try:
                cursor = self.conexion.cursor()
                sql = f"""DELETE FROM propietarios WHERE id_propietarios = %s"""
                cursor.execute(sql, (id_propietarios,))
                cursor.close()
                self.conexion.commit()
                return json.dumps({'success': True, 'msg': 'Se realizó la eliminación exitosamente'})
            except Error as err:
                print(f'Error al intentar la conexion {err}')
                return json.dumps({'success': False, 'msg': 'Hubo un error al eliminar'})