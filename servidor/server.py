import socket
import threading

#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

#Nombre (identificadores) de los equipos traidos de la base de datos SQL
equipos_existentes = [] 

#Arreglo de conexiones realizadas en tiempo real
conexiones_activas = []
direcciones_activas = []

#1er Hilo: Realizar el levantado del canal (socket) y aceptar nuevas conexiones
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

            #Guardar las conexiones y direcciones del cliente
            conexiones_activas.append(conn)
            direcciones_activas.append(addr)

            print(f'Se ha establecido la conexión con {addr}')

        except:
            print('Error al aceptar la conexión :(')

#2do Hilo: Encargado de administrar y manejar las funcionalidades de los usuarios ya existentes
def panel_operaciones():
    pass

def listar_equipos():
    pass

def conectar_con_equipo():
    pass