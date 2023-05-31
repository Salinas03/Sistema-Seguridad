# CLASE PARA LA AGREGACION DE UN NUEVO ADMIN
class Admin():

    #FUNCION PARA PODER INICIAR LA CLASE
    def __init__(self,conexion):
        self.conexion = conexion # CREACION DE LA VARIABLE DE CONEXION

        # CREACION DE LA TABLA administradores SI ES QUE NO EXISTE
        with self.conexion.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS administradores
                        (nombre VARCHAR(50) NOT NULL,
                        apellido VARCHAR(100) NOT NULL,
                        telefono VARCHAR(13) NOT NULL,
                        correo VARCHAR(100) NOT NULL,
                        password VARCHAR(50) NOT NULL)"""
            cursor.execute(sql)
            self.conexion.commit()
    
    # FUNCION PARA BUSCAR EL CORREO Y EL PASSWORD, ESTO PARA EL INICIO DE SESION
    def getAdmin(self, correo, password):
        with self.conexion.cursor() as cursor:
            sql = """SELECT correo FROM administradores WHERE correo = %s AND password = %s"""
            cursor.execute(sql, (correo, password))
            resultado = cursor.fetchall()
            return resultado

    # FUNCION PARA LA INSERCION DE DATOS EN LA TABLA DE ADMINISTRADORES
    def insertar_admin(self, nombre, apellido, telefono, correo, password):
        with self.conexion.cursor() as cursor:
            sql = """INSERT INTO administradores (nombre, apellido, telefono, correo, password) VALUES (%s,%s,%s,%s,%s)"""
            cursor.execute(sql,(nombre, apellido, telefono, correo, password))
            self.conexion.commit()