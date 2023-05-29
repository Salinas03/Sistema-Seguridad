import socket
import threading
from base_datos import conexion

#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)
#Objeto base de datos
bd = conexion.BaseDatos()

#Arreglo de equipos de cómputo de la base de datos
equipos_computo = bd.obtener_equipos_computo()

#Arreglo de conexiones realizadas en tiempo real
conexiones_activas = []
direcciones_activas = []

#Por el momento solo habra un administrador (Prueba)
conexion_administrador = []

#1er Hilo: Realizar el levantado del canal (socket) y aceptar nuevas conexiones
#obtener información de la base de datos
def crear_socket():
    try:
        global servidor
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_socket():
    try:
        servidor.bind(ADDR)
        servidor.listen()
        print(f'HOST {HOST} corriendo en el puerto {PORT}')
    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        vincular_socket()

def aceptar_conexiones():
    while True:
        try:
            conn, addr = servidor.accept() #Linea que bloquea el flujo del programa
            servidor.setblocking(1) #Evita el tiempo de espera de las conexiones, (el servidor no se cierra)

            #Guardar las conexiones y direcciones del cliente o administrador
            guardar_conexiones(conn,addr)

            print(f'Se ha establecido la conexión con {addr}')

        except:
            print('Error al aceptar la conexión :(')

def guardar_conexiones(conn, addr):

    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtener_equipo_por_nombre(conn.gethostname())
    if not resultado:
        conn.send('Conexión denegada'.encode(FORMAT))
        conn.close()

    #Verificar si el dispositvo que se esta conectando es un administrador o un usuario
    #dependiendo de la tabla SQL
    resultado = bd.obtener_equipo_admin_por_nombre(conn.gethostname())
    if not resultado:
        conexiones_activas.append(conn)
        direcciones_activas.append(addr)
    else:
        if not conexion_administrador:
            conexion_administrador.append(conn)
            conexion_administrador.append(addr)
        else:
            conn.send('Conexión denegada, administrador ya conectado'.encode(FORMAT))
            conn.close()


#2do Hilo: Encargado de administrar y manejar las funcionalidades de los usuarios ya existentes
#desde la computadora del administrador
def panel_administrador():
    #Núcleo de la problemática
    conn_admin = None
    addr_admin = None
    bandera = True

    while True:
        #Estar checando si se ha conectado un administrador
        if conexion_administrador:
            if bandera:
                conn_admin = conexion_administrador[0]
                addr_admin = conexion_administrador[1]

                conn_admin.send('Conexión exitosa :)'.encode())
                conn_admin.send(f'Bienvenido administrador {conn_admin.gethostname()}'.encode())
                conn_admin.send(f'Su dirección IP es {addr_admin}')
                bandera = False

            #Esperar instrucción de la computadora administradora
            operacion = conn_admin.recv(HEADER).decode(FORMAT, errors='ignore') #Línea que bloque el código

            #Realizar operaciones de administrador
            if operacion == 'listar':
                listar_equipos(conn_admin)
            else:
                conn_admin.send('Comando no reconocido'.encode())

def listar_equipos(conexion_admin):
    #Se tienen que listar los equipos que estan activos 
    #Pero en la UI se tienen que ver tanto activos como inactivos

    cadena_equipos_activos = ''
    cadena_equipos_inactivos = ''
    equipos_inactivos = equipos_computo[:]

    #Crar cadena de texto de los equipos activos e inactivos
    for i,conexion_activa in enumerate(conexiones_activas):
        #Mostrar solo aquellas conexiones que estan activas
        try:
            conexion_activa.send(' '.encode())
            conexion_activa.recv(HEADER)

        except:
            #Las conexiones que no esten activas serán eliminadas
            #El arreglo se recorre al borrar estos elementos (podría estar mal)
            del conexiones_activas[i]
            del direcciones_activas[i]
            continue
        
        cadena_equipos_activos = str(i) + '  IP:  ' + str(conexiones_activas[i][0]) + '  TCP_PORT:  ' + str(direcciones_activas[i][1]) + '\n'

        #Obtener los equipos de cómputo inactivos
        for x, equipo_computo in enumerate(equipos_computo):
            if conexion_activa.gethostname() == equipo_computo[1]:
                equipos_inactivos[x] = None
    
    #Crear cadena de los equipos de cómputo inactivos
    for z, equipo_inactivo in enumerate(equipos_inactivos):
        if equipo_inactivo is not None:
            cadena_equipos_inactivos = str(z) + '  IP:  ' + str(equipo_inactivo[0]) + '  TCP_PORT:  ' + str(equipo_inactivo[1]) + '\n'

    conexion_admin.send(cadena_equipos_activos.encode())
    conexion_admin.send(cadena_equipos_inactivos.encode())
    
def conectar_con_equipo():
    pass

def manejar_operaciones():
    pass