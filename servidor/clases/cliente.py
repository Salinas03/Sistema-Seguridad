import socket
import json
import wmi

class ClienteSocket:
    def __init__(self):
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