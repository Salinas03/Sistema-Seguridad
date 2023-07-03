import socket
import json
import threading
import os
import subprocess
import time
from clases.cliente import cliente_socket

#Función de dos hilos que corren en el programa
def manejar_canal_cliente():
    while True:
        try:
            print('Manejar canal de cliente')
            respuesta_servidor = cliente_socket.get_socket_cliente().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
            if respuesta_servidor == ' ':
                cliente_socket.get_socket_cliente().send(' '.encode())
                print('Se envió mensaje vacio')
            else:
                try:
                    print(f'Instrucción a aplicar {respuesta_servidor}')

                    if respuesta_servidor == 'apagar':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Apagado realizado exitosamente'}).encode())
                        os.system(f'{os.getcwd()}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'bloquear':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Bloqueo de windows realizado exitosamente'}).encode())
                        os.system(f'{os.getcwd()}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'desbloquear':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Bloqueo de windows realizado exitosamente'}).encode())
                        os.system(f'{os.getcwd()}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'consola':
                        print('Abrir consola')
                        current_wd = f'{os.getcwd()}>'
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'consola': current_wd}).encode())

                        manejar_comandos_consola()
                        print('Salir de manejar comandos')

                    else:
                        print('Instruccion no encontrada')

                except:
                    mensaje_respuesta = json.dumps({'success': False, 'msg': 'Hubo un error al ejecutar la instrucción mandada'})
                    print(mensaje_respuesta)
                    cliente_socket.get_socket_cliente().send(mensaje_respuesta.encode())
        except (socket.error, socket.timeout) as err:

            #SE HACE LA ESEPCIÓN DE QUE SI SE VA EL INTERNET
            if isinstance(err, (socket.error, socket.timeout)):
                print('Desconexión de internet del canal principal')
                cliente_socket.get_socket_cliente().close()
                cliente_socket.get_socket_cliente_secundario().close()
                #CREAR UNA FUNCIÓN DE RECONEXIÓN TODO
                break
            else:
                print('Ocurrió un error en el canal cliente principal')
                cliente_socket.get_socket_cliente().close()
                cliente_socket.get_socket_cliente_secundario().close()
                break

#Función que permite al servidor saber si el cliente sigue activo
def manejar_canal_cliente_secundario():
    cliente_socket.get_socket_cliente_secundario().settimeout(5)
    while True:
        try:
            mensaje = cliente_socket.get_socket_cliente_secundario().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
            # print(f'Mensaje del servidor {mensaje}')
            cliente_socket.get_socket_cliente_secundario().send('*'.encode())
            
        except:
            print('Ocurrio un error en el canal cliente secunadrio')
            cliente_socket.get_socket_cliente().close()
            cliente_socket.get_socket_cliente_secundario().close()
            break

#Función que maneja los comandos de la consola con respecto al administrador
def manejar_comandos_consola():
    while True:
        try:
            comando = cliente_socket.get_socket_cliente().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
            print(f'Operación a realizar {comando}')
            if comando == 'salir':
                print('Dentro del if de salir')
                break

            if comando[:2] == 'cd':
                os.chdir(comando[3:])

            if len(comando) > 0:
                cmd = subprocess.Popen(comando[:],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = output_bytes.decode(cliente_socket.FORMAT, errors='ignore')
                current_wd = f'{os.getcwd()}>'
                cliente_socket.get_socket_cliente().send(str.encode(output_str + current_wd))

        except:
            print('Ocurrio en la función de manejar comandos en la consola')
            break

#Función principal
def main():
    respuesta = cliente_socket.crear_sockets()
    if respuesta['success']:
        print(respuesta['msg'])
        respuesta = cliente_socket.conexion_temporal()
        print(respuesta)    
        if respuesta['success']:
            print(respuesta['msg'])
            respuesta = cliente_socket.validacion_conexion()
            if respuesta['success']:
                #Conexión con el canal secundario despúes de la validación del socket principal
                if cliente_socket.conexion_canal_secundario():
                    cliente_thread = threading.Thread(target=manejar_canal_cliente)
                    cliente_thread.start()
                    cliente_secundario_thread = threading.Thread(target=manejar_canal_cliente_secundario)
                    cliente_secundario_thread.start()
                    print('Esperando instrucciones ...')

                else: 
                    print('Hubo un error al conectar con el canal secundario')
            else:
                print(respuesta['msg'])
        else:
            print(respuesta['msg'])
    else:
        print(respuesta['msg'])

#Función para verificar la conexión a internet de la misma
def verificar_conexion_internet():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

#Realizar conexión la primera vez
def realizar_conexion():
    if verificar_conexion_internet():
        try:
            main()
        except:
            print('Algo sucedio en el programa principal, intentando reconexión...')
            time.sleep(30)
            realizar_conexion()
    else:
        print('Intentando conexión')
        time.sleep(30)
        realizar_conexion()

realizar_conexion()