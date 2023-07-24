import socket
import threading
import json
from clases import numero_serie

# 165.22.15.159
#Configuración
FORMAT = "utf-8"
HEADER = 20480
# IP = socket.gethostbyname(socket.gethostname())
IP = '165.22.15.159'
PORT = 5050
PORT_NOTI = 5051
ADDR = (IP, PORT)
ADDR_NOTI = (IP, PORT_NOTI)

#Creación de sockets, uno para atender el panel de administración.
administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conexión de los sockets con los sockets del administrador
# notificaciones_admin.connect(ADDR_NOT) #Se conecta con el socket de notificaciones
administrador.connect(ADDR) #Linea de bloqueo de código , se conecta con el ade administrador
notificacion.connect(ADDR_NOTI)

#Mensaje de primer conexión con el servidor (conexión temporal)
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

#Obtener el número de seríe del administrador que se va a conectar
numero_de_serie = numero_serie.obtener_numero_serie()
print(f'Número de serie: {numero_de_serie}')

#Se envia el hostname de la computadora a su vez con el identificador que en este caso será el número de serie
administrador.send(socket.gethostname().encode())
administrador.send(numero_de_serie.encode())

#Mensaje de segunda conexión con el servidor
#Aqui tanto se puede conectar como no se puede conectar
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

def operaciones():
    while True:
        try: 
            entrada_administrador = input(f'Ingrese la operación que desea realizar: \n{administrador.recv(HEADER).decode(FORMAT)}')
            administrador.send(entrada_administrador.encode())        

            respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
                
            print(respuesta_servidor)

            if 'Bye' in respuesta_servidor:
                administrador.close()
                notificacion.send('SALIR'.encode())
                notificacion.close()
                break
                
        
        except:
            print('Hubo un error al conectar con el servidor :(')
            administrador.close()
            notificacion.close()
            break

def escuchar_notificaciones():
    while True:
        try:
            mensaje = notificacion.recv(HEADER).decode(FORMAT)
            print('Notificacion')
            print(mensaje)

        except:
            notificacion.close()
            print('Error al recibir la notificación')
            break

def crear_threads():
    operaciones_thread = threading.Thread(target=operaciones)
    escuchar_notificaciones_thread = threading.Thread(target=escuchar_notificaciones)

    operaciones_thread.start()
    escuchar_notificaciones_thread.start()

crear_threads()