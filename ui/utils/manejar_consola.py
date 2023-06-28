import sys
import socket
sys.path.append('D:/RedesLA/SistemaSeguridad/ui')
from clases.administrador_ui import admin_socket_ui

#Socket para conectar con el proceso principal
socket_subproceso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_subproceso.connect(('127.0.0.1', 7777))

#Recibimiento de prompt para imprimir en el input
consola = socket_subproceso.recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)

operacion = input(consola)

while True:
    try:
        if operacion == 'salir':
            socket_subproceso.send(operacion.encode())
            break

        if len(operacion) > 0:
            socket_subproceso.send(operacion.encode())
            respuesta = socket_subproceso.recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)
            print(respuesta, end='')

        operacion = input()

    except:
        print('Error al enviar el comando')
        break
    
    