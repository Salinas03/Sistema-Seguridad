import socket
import threading
from queue import Queue
from clases.numero_serie import obtener_numero_serie

class AdministradorSocketUI:
    def __init__(self):
        # 165.22.15.159
        self.FORMAT = "utf-8"
        self.HEADER = 20480
        self.IP = '165.22.15.159'
        self.PORT = 5050
        self.PORT_NOT = 5051
        self.ADDR = (self.IP, self.PORT)
        self.ADDR_NOT = (self.IP, self.PORT_NOT)

        #Configuración de variables para los hilos
        self.NUMERO_HILOS = 1
        self.NUMERO_TAREAS = [1]
        self.queue = Queue()

    def crear_sockets():
        #Creación de sockets, uno para atender el panel de administración y otro para manejar las notificaciones y listados
        global administrador
        global notificacion
        try:
            administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            print('Creación de sockets...')
            return {"success": True, "msg": "Creación de sockets exitosa :)"}

        except:
            return {"success": False, "msg": "Hubo un error al crear los sockets :("}

    def conexion_temporal(self):
        try:
            #Conexión de los sockets con los sockets del administrador
            notificacion.connect(self.ADDR_NOT) #Se conecta con el socket de notificaciones
            administrador.connect(self.ADDR) #Linea de bloqueo de código , se conecta con el ade administrador
            
            #Mensaje de primer conexión con el servidor (conexión temporal)
            respuesta_servidor = administrador.recv(self.HEADER).decode(self.FORMAT)
            
            print(respuesta_servidor) #Imprimir de manera de mensaje emergente

            return respuesta_servidor
        except:
            return {"success": False, "msg": "Error al conectar con el servidor :("}

    def validacion_conexion(self):
        #Obtener el número de seríe del administrador que se va a conectar
        try:
            numero_de_serie = obtener_numero_serie()
            print(f'Número de serie: {numero_de_serie}')

            #Se envia el hostname de la computadora a su vez con el identificador que en este caso será el número de serie
            administrador.send(socket.gethostname().encode())
            administrador.send(numero_de_serie.encode())

            #Mensaje de segunda conexión con el servidor
            #Aqui tanto se puede conectar como no se puede conectar
            respuesta_servidor = administrador.recv(self.HEADER).decode(self.FORMAT)
            print(respuesta_servidor)

            return respuesta_servidor

        except: 
            return {"success": False, "msg": "Error al validar la conexión :("}

    def escribir_operaciones(operacion):
        try:
            administrador.send(operacion.encode())
        except:
            print('Error al enviar el mensaje desde el administrador :(')

    #1er hilo
    def escuchar_respuesta_operaciones(self):
        while True:
            try:
                respuesta_servidor = administrador.recv(self.HEADER).decode(self.FORMAT)
                print(respuesta_servidor)

                if 'Bye' in respuesta_servidor:
                    administrador.close()
                    notificacion.send('SALIR'.encode())
                    notificacion.close()
                    break

                return respuesta_servidor

            except:
                print('Error al recibir mensaje desde el servidor :(')
                administrador.close()
                notificacion.send('SALIR'.encode())
                notificacion.close()
                break
    
    #2do hilo
    def escuchar_notificaciones(self):
        while True:
            try:
                respuesta_servidor_notificacion = notificacion.recv(self.HEADER).decode(self.FORMAT)
                print('Notificación:')
                print(respuesta_servidor_notificacion)

            except:
                notificacion.close()
                print('Error al recibir la notificación')
                break
    
    def crear_threads(self):
        escuchar_operaciones_thread = threading.Thread(target=self.escuchar_respuesta_operaciones)
        escuchar_notificaciones_thread = threading.Thread(target=self.escuchar_notificaciones)
        escuchar_operaciones_thread.start()
        escuchar_notificaciones_thread.start()   

#Global variable scope (testing)
admin_socket_ui = AdministradorSocketUI()