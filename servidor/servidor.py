import socket
import threading
from queue import Queue
from base_datos import conexion
from clases import persona

#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (HOST, PORT)

#Objeto base de datos
bd = conexion.BaseDatos()

#Configuración de variables para los hilos
NUMERO_HILOS = 2
NUMERO_TAREAS = [1,2]
queue = Queue()

#Arreglo de equipos de cómputo de la base de datos
equipos_computo = bd.obtener_equipos_computo()

#Arreglo de conexiones de clientes realizadas en tiempo real
clientes_activos = []

#Por el momento solo habra un administrador (Prueba)
administrador_activo = []

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
    #Cerrar todas las conexiones al iniciar el servidor
    for cliente in clientes_activos:
        cliente.get_conexion().close()

    #Borrar los datos de las conexiónes y direcciones
    del clientes_activos[:]

    while True:
        try:
            conn, addr = servidor.accept() #Linea que bloquea el flujo del programa
            servidor.setblocking(1) #Evita el tiempo de espera de las conexiones, (el servidor no se cierra)

            #Conexión temporal establecida para obtener información del cliente que se conecto
            conn.send('Conexión temporal establecida...'.encode())
            nombre_host = conn.recv(HEADER).decode(FORMAT)
            print(f'Dispositivo conectado temporalmente: {nombre_host}')
            #Hacer validación si el cliente que se conecto esta en la base de datos o no
            #Si esta en l abase de datos se determina si es administrador o cliente
            guardar_conexiones(conn,addr, nombre_host)

        except:
            print('Error al aceptar la conexión :(')

def guardar_conexiones(conn, addr, hostname):
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtener_equipo_por_nombre(hostname)
    if not resultado:
        conn.send('Conexión denegada'.encode(FORMAT))
        conn.close()

    #Verificar si el dispositvo que se esta conectando es un administrador o un usuario
    #dependiendo de la tabla SQL
    resultado = bd.obtener_equipo_admin_por_nombre(hostname)
    if not resultado:
        cliente = persona.PersonaConectada(conn, addr, hostname, 'x')
        clientes_activos.append(cliente)
        print('Conexión con cliente :)')
        conn.send('Conexión con servidor exitosa :)'.encode())
    else:
        if not administrador_activo:
            administrador = persona.PersonaConectada(conn, addr, hostname, 'x')
            administrador_activo.append(administrador)
        else:
            conn.send('Conexión denegada, administrador ya conectado'.encode(FORMAT))
            conn.close()


#2do Hilo: Encargado de administrar y manejar las funcionalidades de los usuarios ya existentes
#desde la computadora del administrador
def panel_administrador():
    #Núcleo de la problemática
    bandera = True

    while True:
        #Estar checando si se ha conectado un administrador
        if administrador_activo:
            if bandera:
                conn_admin = administrador_activo[0].get_conexion()
                addr_admin = administrador_activo[0].get_direccion()
                nombre_host = administrador_activo[0].get_nombre_host()
                conn_admin.send(f'Conexión exitosa :) \n Bienvenido administrador {nombre_host} \n Su dirección IP es {addr_admin}'.encode())
                print('Conexión exitosa :)')
                print('A sus ordenes administrador...')
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

    cadena_equipos_activos = 'ACTIVOS \n'
    cadena_equipos_inactivos = 'INACTIVOS \n'

    #Copiar los equipos de cómputo a la variable de equipos inactivos
    equipos_inactivos = equipos_computo[:]

    #Crar cadena de texto de los equipos activos e inactivos
    for i,cliente_activo in enumerate(clientes_activos):
        #Mostrar solo aquellas conexiones que estan activas
        try:
            cliente_activo.get_conexion().send(' '.encode())
            cliente_activo.get_conexion().recv(HEADER)

        except:
            #Las conexiones que no esten activas serán eliminadas
            #El arreglo se recorre al borrar estos elementos (podría estar mal)
            del clientes_activos[i]
            continue
        
        ip_cliente = cliente_activo.get_direccion()[0]
        puerto_tcp = cliente_activo.get_direccion()[1]
        cadena_equipos_activos += str(i) +'  IP:  ' + str(ip_cliente) + '  TCP_PORT:  ' + str(puerto_tcp) + '\n'

        #Obtener los equipos de cómputo inactivos
        for x, equipo_computo in enumerate(equipos_computo):
            #Aqui se tiene que cambiar
            if cliente_activo.get_nombre_host() == equipo_computo[1]:
                equipos_inactivos[x] = None
    
    #Crear cadena de los equipos de cómputo inactivos
    for z, equipo_inactivo in enumerate(equipos_inactivos):
        if equipo_inactivo is not None:
            cadena_equipos_inactivos += str(z) + '  IP:  ' + str(equipo_inactivo[0]) + '  TCP_PORT:  ' + str(equipo_inactivo[1]) + '\n'
    
    cadena_equipos = cadena_equipos_activos + cadena_equipos_inactivos
    conexion_admin.send(cadena_equipos.encode())
    
def conectar_con_equipo():
    pass

def manejar_operaciones():
    pass

def crear_hilos(): 
    for _ in range(NUMERO_HILOS):
        thread = threading.Thread(target=tarea)
        #Cuando el hilo se cierre se tiene que cerrar en todo el programa
        thread.daemon = True
        #Iniciar hilo
        thread.start()

def crear_tareas():
    #Crear la cola de tareas
    for tarea in NUMERO_TAREAS:
        queue.put(tarea)

    #Iniciar la cola de tareas
    queue.join()

#Asignar las tareas que estan en la cola
#1.-El primer hilo encenderá el canal del socket y manejará las conexiones que se vayan realizando
#2.-El segundo hilo manejará las manejará los comandos del administrador y clientes ya conectados
def tarea():
    while True:
        tarea = queue.get()
        if tarea == 1:
            crear_socket()
            vincular_socket()
            aceptar_conexiones()

        if tarea == 2:
            panel_administrador()

        queue.task_done()

crear_hilos()
crear_tareas()