import socket
import json
import wmi
import os

class ClienteSocket:
    def __init__(self, ip):
        self.FORMAT = "utf-8"
        self.HEADER = 20480
        # self.IP = '68.183.143.116'
        self.IP = ip
        # self.IP = '165.22.0.170'
        #self.IP = socket.gethostbyname(socket.gethostname())
        self.PORT = 5050
        self.PORT_CLIENTE = 5053
        self.ADDR = (self.IP, self.PORT)
        self.ADDR_CLIENTE = (self.IP, self.PORT_CLIENTE)
        self.TIMEOUT = 4
        self.TIMEOUT_SECUNDARIO = 4
        self.BASE_DIR = 'C:/Cliente/output'

    def crear_sockets(self):
        global cliente
        global cliente_secundario

        try:
            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            cliente.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            cliente.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            cliente_secundario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            cliente_secundario.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            cliente_secundario.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            cliente_secundario.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            #Establecer los TIMOUTS de los sockets
            cliente.settimeout(self.TIMEOUT)
            cliente_secundario.settimeout(self.TIMEOUT)

            return {"success": True, "msg": "Creación de sockets exitosa :)"}
        
        except socket.error as e:
            print(f'Error al crear los sockets {e}')
            return {"success": False, "msg": "Hubo un error al crear los sockets :("}

    def conexion_temporal(self):
        try:
            cliente.connect(self.ADDR)
            respuesta_servidor = json.loads(cliente.recv(self.HEADER).decode(self.FORMAT))
            return respuesta_servidor
        
        except socket.timeout:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Error al realizar la conexión temporal (SocketTimeout)'}

        except:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'No se pudo realizar la conexión temporal'}

    def validacion_conexion(self):
        try:
            numero_de_serie = self.obtener_numero_serie()

            envio_validacion = {
                'nombre_host': socket.gethostname(),
                'numero_serie': numero_de_serie,
                'tipo_programa': 'cliente'
            }

            cliente.send(json.dumps(envio_validacion).encode())

            respuesta_servidor = json.loads(cliente.recv(self.HEADER).decode(self.FORMAT))
            return respuesta_servidor
        
        except socket.timeout:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Error al validar la conexión (SocketTimeout)'}

        except:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Error al validar la conexión :('}

    def conexion_canal_secundario(self):
        try:
            #Conexión con cliente
            cliente_secundario.connect(self.ADDR_CLIENTE)

            #Envio de número de serie y esperar respuesta
            numero_serie = self.obtener_numero_serie()
            cliente_secundario.send(numero_serie.encode())
            respuesta = json.loads(cliente_secundario.recv(self.HEADER).decode(self.FORMAT))

            return respuesta
        
        except socket.timeout:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Hubo un error al conectar con el canal secundario y enviar el número de serie'}
        
        except:
            cliente.close()
            cliente_secundario.close()
            return {'success': False, 'msg': 'Hubo un error al conectar con el canal secundario y enviar el número de serie'}

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

# cliente_socket = ClienteSocket(ip)