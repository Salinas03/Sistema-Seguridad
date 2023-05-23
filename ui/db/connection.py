from mysql import connector

config = {
    'user' : 'root',
    'passwors' : '',
    'host' : 'localhost',
    'database' : 'sistema_seguridad'

}

def crear_conexion():
    conn = None
    try:
        conn = connector.connect(**config)
    except connector.Error as err:
        print('Error en la conexion: {err.msg}')
    return conn
    