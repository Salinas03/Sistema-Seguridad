import socket
import json
import wmi

class AdministradorSocketUI:
    def __init__(self):
        # 165.22.15.159
        self.FORMAT = "utf-8"
        self.HEADER = 20480
        self.IP = '68.183.143.116'
        # self.IP = '165.22.15.159'
        # self.IP = '165.22.0.170'
        #self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.PORT_NOT = 5051
        self.PORT_BROAD = 5052
        self.PORT_BD = 5054
        self.PORT_CONA = 5055
        self.ADDR = (self.IP, self.PORT)
        self.ADDR_NOT = (self.IP, self.PORT_NOT)
        self.ADDR_BROAD = (self.IP, self.PORT_BROAD)
        self.ADDR_BD = (self.IP, self.PORT_BD)
        self.ADDR_CONA = (self.IP, self.PORT_CONA)
        self.TIMEOUT = 3
        self.MESSAGE_TIMEOUT = 5
        
        #Variables de sockets
        self.administrador = None
        self.notificacion = None
        self.broadcasting = None
        self.operacionesbd = None
        self.conectividad_admin = None

        self.addresses_secundarios = [self.ADDR_NOT, self.ADDR_BROAD, self.ADDR_BD, self.ADDR_CONA]

        #Arreglos en donde se guardan los sockets secundarios y donde se van guardando las conexiones ya realizadas
        self.canales_secundarios = [] 
        self.conexiones_secundarios = []

    def crear_sockets(self):
        #Creación de sockets, uno para atender el panel de administración y otro para manejar las notificaciones y listados
        try:
            self.administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.administrador.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.administrador.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            self.administrador.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)
    
            self.conectividad_admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.conectividad_admin.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.conectividad_admin.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            self.conectividad_admin.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            #Conexiones que requieren estar encendidas
            self.notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.notificacion.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.notificacion.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            self.notificacion.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            self.broadcasting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.broadcasting.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.broadcasting.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            self.broadcasting.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            self.operacionesbd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.operacionesbd.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            self.operacionesbd.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            self.operacionesbd.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            print('Creación de sockets...')
            return {"success": True, "msg": "Creación de sockets exitosa :)"}

        except:
            return {"success": False, "msg": "Hubo un error al crear los sockets :("}

    def conexion_temporal(self):
        try:
            self.administrador.connect(self.ADDR) #Linea de bloqueo de código , se conecta con el socket administrador
            #Mensaje de primer conexión con el servidor (conexión temporal)
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            print(respuesta_servidor)

            return respuesta_servidor
        except:
            self.administrador.close()
            self.notificacion.close()
            self.broadcasting.close()
            self.operacionesbd.close()
            return {"success": False, "msg": "Error al conectar con el servidor :("}
    
    def validacion_conexion(self):
        #Obtener el número de seríe del administrador que se va a conectar
        try:
            numero_de_serie = self.obtener_numero_serie()

            #Se envia el hostname de la computadora a su vez con el identificador que en este caso será el número de serie
            envio_validacion = {
                'nombre_host': socket.gethostname(),
                'numero_serie': numero_de_serie,
                'tipo_programa': 'administrador'
            }

            self.administrador.send(json.dumps(envio_validacion).encode())

            #Mensaje de segunda conexión con el servidor
            #Aqui tanto se puede conectar como no se puede conectar
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            print(respuesta_servidor)

            return respuesta_servidor

        except: 
            self.administrador.close()
            self.notificacion.close()
            self.broadcasting.close()
            self.operacionesbd.close()
            return {"success": False, "msg": "No se pudo realizar la validación de la conexión correctamente"}

    def conexiones_canales_secundarios(self):
        #Hacer el arreglo de los canales secundarios ya craedos
        self.canales_secundarios = [self.notificacion, self.broadcasting, self.operacionesbd, self.conectividad_admin]

        #Realizar las conexiones con los canales secundarios
        for i, canal in enumerate(self.canales_secundarios):
            try:

                canal.settimeout(self.TIMEOUT)
                canal.connect(self.addresses_secundarios[i])
                print(f'Conexion con {self.addresses_secundarios[i]}')
                # self.conexiones_secundarios.append(canal)
            except socket.error as e:
                print(f'Error al conectar con el socket {self.addresses_secundarios[i]}, [ERROR]:{e}')
                break

        #Recibir el mensaje de confirmación de las conexiones realizadas
        try:
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            print('[Respuesta servidor] : ',respuesta_servidor)
            return respuesta_servidor
        except socket.error as e:
            print(f'Hubo un error al conectar con los canales secundarios {e}')
            return {'success': False, 'msg': 'Error al conectar con los canales secundarios'}

    def validacion_canales_secundarios(self):
        #Obtener el número de serie para realizar la validación de las conexiones secundarias
        numero_serie = self.obtener_numero_serie()

        #Enviar los números de series a
        for i, conexion_secundario in enumerate(self.canales_secundarios):
            try:
                conexion_secundario.send(numero_serie.encode())
                print('[Número serie] : ', numero_serie)
            except socket.error as e:
                print(f'Error al conectar con el socket {self.addresses_secundarios[i]}, [ERROR]:{e}')
                break

        try:
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            print(respuesta_servidor)

            if respuesta_servidor['success']:
                for i in range(3):
                    self.canales_secundarios[i].settimeout(None)

            return respuesta_servidor
        except:
            return {'success': False, 'msg': 'Hubo un error al realizar la validación de los canales secundarios'}

    def escribir_operaciones(self, operacion):
        self.administrador.settimeout(None)
        try:
            self.administrador.send(operacion.encode())
        except socket.error as e:
            print(f'Error al enviar el mensaje desde el administrador {e}')
            return None
        
        try:
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            return respuesta_servidor
        except socket.error as e:
            print(f'Error al recibir el mensaje del servidor {e}')
            return None
        
    def escribir_operacion_inicio_sesion(self, operacion):
        self.administrador.settimeout(self.TIMEOUT)

        try:
            self.administrador.send(operacion.encode())
        except socket.error as e:
            print(f'Error al enviar el mensaje desde el administrador {e}')
            # self.administrador.close()
            # self.notificacion.close()
            # self.broadcasting.close()
            # self.operacionesbd.close()
            return None
        
        try:
            respuesta_servidor = json.loads(self.administrador.recv(self.HEADER).decode(self.FORMAT))
            return respuesta_servidor
        except socket.error as e:
            print(f'Error al recibir el mensaje del servidor {e}')
            return None
   
    def get_socket_administrador(self):
        return self.administrador

    def get_socket_notificacion(self):
        return self.notificacion
    
    def get_socket_broadcasting(self):
        return self.broadcasting 

    def get_socket_operacionesbd(self):
        return self.operacionesbd
    
    def get_socket_conectividadadmin(self):
        return self.conectividad_admin

    def cerrado_sockets(self):
        self.administrador.close()
        self.conectividad_admin.close()
        self.notificacion.close()
        self.broadcasting.close()
        self.operacionesbd.close()

    def obtener_numero_serie(self):
        # Connect to the WMI service
        c = wmi.WMI()

        # Query for the serial number
        numero_serie = None
        for bios in c.Win32_BIOS():
            numero_serie = bios.SerialNumber.strip()
            break
        
        return numero_serie

#Global variable scope (testing)
admin_socket_ui = AdministradorSocketUI()