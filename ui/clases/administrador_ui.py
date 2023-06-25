import socket
import json
import wmi

class AdministradorSocketUI:
    def __init__(self):
        # 165.22.15.159
        self.FORMAT = "utf-8"
        self.HEADER = 20480
        # self.IP = '68.183.143.116'
        self.IP = '165.22.15.159'
        #self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.PORT_NOT = 5051
        self.PORT_BROAD = 5052
        self.PORT_BD = 5054
        self.ADDR = (self.IP, self.PORT)
        self.ADDR_NOT = (self.IP, self.PORT_NOT)
        self.ADDR_BROAD = (self.IP, self.PORT_BROAD)
        self.ADDR_BD = (self.IP, self.PORT_BD)

    def crear_sockets(self):
        #Creación de sockets, uno para atender el panel de administración y otro para manejar las notificaciones y listados
        global administrador
        global notificacion
        global broadcasting
        global operacionesbd
        try:
            administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            broadcasting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            operacionesbd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            print('Creación de sockets...')
            return {"success": True, "msg": "Creación de sockets exitosa :)"}

        except:
            return {"success": False, "msg": "Hubo un error al crear los sockets :("}

    def conexion_temporal(self):
        try:
            #Conexión de los sockets con los sockets del administrador
            notificacion.connect(self.ADDR_NOT) #Se conecta con el socket de notificaciones
            administrador.connect(self.ADDR) #Linea de bloqueo de código , se conecta con el socket administrador
            broadcasting.connect(self.ADDR_BROAD)
            operacionesbd.connect(self.ADDR_BD)
                    
            #Mensaje de primer conexión con el servidor (conexión temporal)
            respuesta_servidor = json.loads(administrador.recv(self.HEADER).decode(self.FORMAT))
            print(respuesta_servidor)

            return respuesta_servidor
        except:
            notificacion.close()
            administrador.close()
            broadcasting.close()
            operacionesbd.close()
            return {"success": False, "msg": "Error al conectar con el servidor :("}

    def validacion_conexion(self):
        #Obtener el número de seríe del administrador que se va a conectar
        try:
            numero_de_serie = self.obtener_numero_serie()
            print(f'Número de serie: {numero_de_serie}')

            #Se envia el hostname de la computadora a su vez con el identificador que en este caso será el número de serie
            administrador.send(socket.gethostname().encode())
            administrador.send(numero_de_serie.encode())

            #Mensaje de segunda conexión con el servidor
            #Aqui tanto se puede conectar como no se puede conectar
            respuesta_servidor = json.loads(administrador.recv(self.HEADER).decode(self.FORMAT))
            print(respuesta_servidor)

            return respuesta_servidor

        except: 
            notificacion.close()
            administrador.close()
            broadcasting.close()
            operacionesbd.close()
            return {"success": False, "msg": "Error al validar la conexión :("}

    def escribir_operaciones(self, operacion):
        try:
            administrador.send(operacion.encode())
            respuesta_servidor = json.loads(administrador.recv(self.HEADER).decode(self.FORMAT))
            return respuesta_servidor
        except:
            print('Error al enviar el mensaje desde el administrador :(')
            administrador.close()
            notificacion.close()
            broadcasting.close()
            operacionesbd.close()
            return None

    def get_socket_administrador(self):
        return administrador

    def get_socket_notificacion(self):
        return notificacion
    
    def get_socket_broadcasting(self):
        return broadcasting 
    
    def get_socket_operacionesbd(self):
        return operacionesbd

    def obtener_numero_serie(self):
        # Connect to the WMI service
        c = wmi.WMI()

        # Query for the serial number
        numero_serie = None
        for bios in c.Win32_BIOS():
            numero_serie = bios.SerialNumber.strip()
            break
        
        return numero_serie

    def cerrar_conexiones(self):
        notificacion.close()
        administrador.close()
        broadcasting.close()
        operacionesbd.close()

#Global variable scope (testing)
admin_socket_ui = AdministradorSocketUI()