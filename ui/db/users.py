from mysql import connector
from db.connection import crear_conexion

class registro_user():
    def insert_user(data):
        conn = crear_conexion
        sql = """INSERT INTO user (nombre,apellidos,telefono,correo,password)
                    VALUES(%s, %s, %s, %s, %s)"""
        
        try:
            cur = conn.cursor()
            cur.execute(sql, data)
            conn.commit()
            print('Nuevo usuario agregado')
            return True
        except connector.Error as e:
            print("Error inserting new user: " + str(e))
        finally:
            if conn:
                cur.close()
                conn.close()

    def busca_user(self, users):
        conn = crear_conexion()
        sql = "SELECT * FROM user WHERE correo = {}".format(users)
        conn.execute(sql)
        usersx = conn.fetchall()
        conn.close()
        return usersx

    def busca_password(self, password):
        conn = crear_conexion()
        sql = "SELECT * FROM user WHERE password = {}".format(password)
        conn.execute(sql)
        passwordx = conn.fetchall()
        conn.close()
        return passwordx

