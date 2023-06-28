import socket
import json
import wmi
import threading
import os
import subprocess
import time

class ClienteSocket:
    def _init_(self):
        self.FORMAT = "utf-8"
        self.HEADER = 20480
        # self.IP = '68.183.143.116'
        self.IP = '165.22.15.159'
        #self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.PORT_CLIENTE = 5053
        self.ADDR = (self.IP, self.PORT)
        self.ADDR_CLIENTE = (self.IP, self.PORT_CLIENTE)

    def crear_sockets(self):
        global cliente
        global cliente_secundario

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_secundario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            print('Creación de sockets...')
            return {"success": True, "msg": "Creación de sockets exitosa :)"}
        
        except:
            return {"success": False, "msg": "Hubo un error al crear los sockets :("}

    def conexion_temporal(self):
        try:

            cliente.connect(self.ADDR)

            respuesta_servidor = json.loads(cliente.recv(self.HEADER).decode(self.FORMAT))

            return respuesta_servidor
    
        except:
            cliente.close()
            cliente_secundario.close()

    def conexion_canal_secundario(self):
        try:
            cliente_secundario.connect(self.ADDR_CLIENTE)
            return True

        except:
            cliente.close()
            cliente_secundario.close()
            return False

    def validacion_conexion(self):
        try:
            numero_de_serie = self.obtener_numero_serie()
            cliente.send(socket.gethostname().encode())
            cliente.send(numero_de_serie.encode())

            respuesta_servidor = json.loads(cliente.recv(self.HEADER).decode(self.FORMAT))

            print(respuesta_servidor)

            return respuesta_servidor
        
        except:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Error al validar la conexión :('}

    def get_socket_cliente(self):
        return cliente
    
    def get_socket_cliente_secundario(self):
        return cliente_secundario

    def obtener_numero_serie(self):
        # Connect to the WMI service
        c = wmi.WMI()

        # Query for the serial number
        numero_serie = None
        for bios in c.Win32_BIOS():
            numero_serie = bios.SerialNumber.strip()
            break
        
        return numero_serie


cliente_socket = ClienteSocket()

def manejar_canal_cliente():
     while True:
        try:
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

def manejar_comandos_consola():
    while True:
        comando = cliente_socket.get_socket_cliente().recv(cliente_socket.HEADER).decode(cliente_socket.FORMAT)
        if comando == 'salir':
            break

        if comando[:2] == 'cd':
            os.chdir(comando[3:])

        if len(comando) > 0:
            cmd = subprocess.Popen(comando[:],shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            output_bytes = cmd.stdout.read() + cmd.stderr.read()
            output_str = output_bytes.decode(cliente_socket.FORMAT, errors='ignore')
            current_wd = f'{os.getcwd()}>'
            cliente_socket.get_socket_cliente().send(str.encode(output_str + current_wd))

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