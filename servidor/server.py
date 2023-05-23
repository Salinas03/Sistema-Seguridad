import socket
import threading

#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

conexiones = []
direcciones = []

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

def aceptar_solicitudes():
    while True:
        try:
            conn, addr = servidor.accept() #Linea que bloquea el flujo del programa
            servidor.setblocking(1) #Evita el tiempo de espera de las conexiones, (el servidor no se cierra)

            #Guardar las conexiones y direcciones del cliente
            conexiones.append(conn)
            direcciones.append(addr)

            print(f'Se ha establecido la conexión con {addr}')

        except:
            print('Error al aceptar la conexión :(')