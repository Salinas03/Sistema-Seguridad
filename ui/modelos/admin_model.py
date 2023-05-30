class Admin():

    def __init__(self,conexion):
        self.conexion = conexion
        with self.conexion.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS administradores
                        (nombre VARCHAR(50) NOT NULL,
                        apellido VARCHAR(100) NOT NULL,
                        telefono VARCHAR(13) NOT NULL,
                        correo VARCHAR(100) NOT NULL,
                        password VARCHAR(50) NOT NULL)"""
            cursor.execute(sql)
            self.conexion.commit()
    
    def getAdmin(self, correo, password):
        with self.conexion.cursor() as cursor:
            sql = """SELECT correo FROM administradores WHERE correo = %s AND password = %s"""
            cursor.execute(sql, (correo, password))
            resultado = cursor.fetchall()
            return resultado
