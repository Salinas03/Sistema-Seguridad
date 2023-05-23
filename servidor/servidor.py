import socket
import threading
from base_datos import BaseDatos

#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)
#Objeto base de datos
bd = BaseDatos()

#Arreglo de conexiones realizadas en tiempo real
conexiones_activas = []
direcciones_activas = []

#Por el momento solo habra un administrador (Prueba)
conexion_administrador = []

#1er Hilo: Realizar el levantado del canal (socket) y aceptar nuevas conexiones
#obtener información de la base de datos
def crear_socket():
    try:
        global servidor
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_socket():
    try:
        servidor.bind(ADDR)
        servidor.listen()
        print(f'HOST {HOST} corriendo en el puerto {PORT}')
    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        vincular_socket()

def aceptar_conexiones():
    while True:
        try:
            conn, addr = servidor.accept() #Linea que bloquea el flujo del programa
            servidor.setblocking(1) #Evita el tiempo de espera de las conexiones, (el servidor no se cierra)

            #Guardar las conexiones y direcciones del cliente o administrador
            guardar_conexiones(conn,addr)

            print(f'Se ha establecido la conexión con {addr}')

        except:
            print('Error al aceptar la conexión :(')

def guardar_conexiones(conn, addr):

    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtenerEquipoPorNombre(conn.gethostname())
    if not resultado:
        conn.send('Conexión denegada'.encode(FORMAT))
        conn.close()

    #Verificar si el dispositvo que se esta conectando es un administrador o un usuario
    #dependiendo de la tabla SQL
    resultado = bd.obtenerEquiposAdministradorPorNombre(conn.gethostname())
    if not resultado:
        conexiones_activas.append(conn)
        direcciones_activas.append(addr)
    else:
        if not conexion_administrador:
            conexion_administrador.append(conn)
            conexion_administrador.append(addr)
        else:
            conn.send('Conexión denegada, administrador ya conectado'.encode(FORMAT))
            conn.close()


#2do Hilo: Encargado de administrar y manejar las funcionalidades de los usuarios ya existentes
def panel_administrador():
    #Núcleo de la problemática
    #
    conn = None
    addr = None
    bandera = True

    while True:
        if conexion_administrador:
            if bandera:
                conn = conexion_administrador[0]
                addr = conexion_administrador[1]
                conn.send(f'Bienvenido administrador {conn.gethostname()}'.encode())
                bandera = False


            conn.recv(HEADER).decode(FORMAT, errors='ignore') #Bloqueo

            #Si hay conexión con el administrador enviar la mensajería con el mismo
            #El servidor hará lo que el administrador le ordene
            #Realizar las operaciones

def listar_equipos():
    pass

def conectar_con_equipo():
    pass