import subprocess
import os
import socket
from clases.administrador_ui import admin_socket_ui

def abrir_consola_ejecutar_script(consola):

    #Creación de socket con el subproceso IPC
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(('127.0.0.1', 7777))
    sock.listen()

    #Abrir una nueva ventana de consola ejecutar el script
    script_path = f'{os.getcwd()}/utils/manejar_consola.py'
    proceso_consola = subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True)

    #Aceptar la conexión con el subproceso
    conn_subproceso, addr = sock.accept()
    print('Conexión con subproceso!!')
    
    #Mandar el prompt del cliente que se va a dibujar en el subproceso
    conn_subproceso.send(consola.encode())

    while True:
        try:
            #Comandos recibidos desde el subproceso de la consola
            msg = conn_subproceso.recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)
            print('Mensaje del subproceso')
            print(msg)

            #Enviar el mensaje al servidor
            admin_socket_ui.get_socket_administrador().send(msg.encode())

            #Si el mensaje enviado por el subproceso es salir y ya no esperamos una respuesta del servidor y salimos del ciclo
            if msg == 'salir':
                break

            #Recibir respuesta del servidor/cliente
            respuesta_servidor_cliente = admin_socket_ui.get_socket_administrador().recv(admin_socket_ui.HEADER).decode(admin_socket_ui.FORMAT)

            if respuesta_servidor_cliente == 'desconectado':
                break

            #Imprimir la respuesta
            print('Respuesta servidor cliente')
            print(respuesta_servidor_cliente)

            #Enviar la respuesta al subproceso
            conn_subproceso.send(respuesta_servidor_cliente.encode())

        except:
            print('Algo paso en el socket de subproceso')
            admin_socket_ui.get_socket_administrador().send('salir'.encode())
            conn_subproceso.close()
            break
    subprocess.Popen(['taskkill', '/F', '/IM', 'cmd.exe'])