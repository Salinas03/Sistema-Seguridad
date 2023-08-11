import sys
import socket
import os

HEADER = 20480
FORMAT = 'utf-8'

#Socket para conectar con el proceso principal
socket_subproceso = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_subproceso.connect(('127.0.0.1', 7777))

#Recibimiento de prompt para imprimir en el input
consola = socket_subproceso.recv(HEADER).decode(FORMAT)

#Recibir input del administrador la primera vez que se abra la consola
operacion = input(consola)

while True:
    try:
        if operacion == 'salir':
            socket_subproceso.send(operacion.encode())
            socket_subproceso.close()
            break

        if len(operacion) > 0:
            socket_subproceso.send(operacion.encode())
            respuesta = socket_subproceso.recv(HEADER).decode(FORMAT)
            print(respuesta, end='')

        #Recibir input del administrador de manera continua
        operacion = input()

    except:
        print('Error al enviar el comando')
        socket_subproceso.send('salir'.encode())
        socket_subproceso.close()
        break
