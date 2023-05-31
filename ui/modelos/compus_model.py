class Compus():

    def __init__(self, conexion):
        self.conexion = conexion

        with self.conexion.cursor() as cursor:
            sql = """CREATE TABLE IF NOT EXISTS computadoras
                        (persona VARCHAR(150) NOT NULL,
                        computadora VARCHAR(100) NOT NULL,
                        fecha_entrega VARCHAR(50) NOT NULL,
                        mac_address VARCHAR(50) NOT NUL)"""
            cursor.execute(sql)
            self.conexion.commit()
    
    def insertarCompus(self):
        pass