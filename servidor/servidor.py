import socket
import threading
from queue import Queue
from base_datos import conexion
from clases import persona

# 165.22.15.159
#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = '165.22.15.159'

PORT = 5050
PORT_NOT = 5051

ADDR = (HOST, PORT)
ADDR_NOT = (HOST, PORT_NOT)

#Objeto base de datos
bd = conexion.BaseDatos()

#Configuración de variables para los hilos
NUMERO_HILOS = 3
NUMERO_TAREAS = [1,2,3]
queue = Queue()

#Arreglo de equipos de cómputo de la base de datos
equipos_computo = bd.obtener_equipos_computo()

#Arreglo de conexiones de clientes realizadas en tiempo real
clientes_activos = []

#Por el momento solo habra un administrador (Prueba)
administrador_activo = []

notificacion_conexion = []

#1er Hilo: Realizar el levantado del canal (socket) y aceptar nuevas conexiones
#obtener información de la base de datos
def crear_socket():
    try:
        global servidor
        global notificaciones_socket
        notificaciones_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_socket():
    try:
        notificaciones_socket.bind(ADDR_NOT)
        servidor.bind(ADDR)

        notificaciones_socket.listen()
        servidor.listen()

        print(f'HOST {HOST} corriendo en el puerto {PORT}')
        print(f'NOTIFICACIONES HOST {HOST} corriendo en el puerto {PORT_NOT}')
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
    mensaje = 'mensaje vacio'
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtener_equipo_por_nombre(hostname)
    if not resultado:
        mensaje = f'Conexión denegada a {hostname}'
        conn.send('Conexión denegada >:/'.encode())
        conn.close()
    else:
        #Verificar si el dispositvo que se esta conectando es un administrador o un usuario
        #dependiendo de la tabla SQL
        resultado = bd.obtener_equipo_admin_por_nombre(hostname)
        if not resultado:
            cliente = persona.PersonaConectada(conn, addr, hostname, 'x')
            clientes_activos.append(cliente)
            mensaje = f'El cliente {hostname} se ha conectado'
            print('Conexión con cliente :)')
            conn.send('Conexión con servidor exitosa :)'.encode())
        else:
            if not administrador_activo:
                administrador = persona.PersonaConectada(conn, addr, hostname, 'x')
                administrador_activo.append(administrador)
                #Posibilidad crear otro socket alv
                #Accept connection
            else:
                print('Conexión denegada, administrador ya conectado'.encode())
                mensaje = f'Conexión denegada al administrador {hostname}'
                conn.send('Conexión denegada, administrador ya conectado'.encode())
                conn.close()
    
    #Solo notificar cuando se conecte un usuario
    if administrador_activo:
        if hostname != administrador_activo[0].get_nombre_host():
            notificar_admin_conexiones(mensaje)

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
                conn_admin.send(f'Conexión exitosa :) \nBienvenido administrador {nombre_host} \nSu dirección IP es {addr_admin}'.encode())
                print('Conexión exitosa :)')
                print('A sus ordenes administrador...')
                bandera = False

            try:
                #Enviar el prompt del administrador (esto va a cambiar)
                conn_admin.send('administrador/servidor>'.encode())

                #Esperar instrucción de la computadora administradora
                operacion = conn_admin.recv(HEADER).decode(FORMAT, errors='ignore') #Línea que bloque el código

                #Realizar operaciones de administrador
                if operacion == 'listar':
                    cadena_equipos = listar_equipos()
                    conn_admin.send(cadena_equipos.encode())

                elif 'seleccionar' in operacion:
                    if not clientes_activos:
                        conn_admin.send('No hay dispositivos activos a quienes realizar operaciones :/'.encode())
                    else:
                        cliente_seleccionado = conectar_con_equipo(operacion)
                        if cliente_seleccionado is not None:
                            manejar_operaciones(cliente_seleccionado)

                elif operacion == 'salir':
                    print('Administrador desconectado...')
                    conn_admin.send('Bye bye...'.encode())
                    conn_admin.close()
                    del administrador_activo[0]
                    bandera = True
                else:
                    conn_admin.send('Comando no reconocido'.encode())

            except:
                print('Administrador desconectado espontáneamente...')
                conn_admin.close()
                del administrador_activo[0]
                bandera = True

def listar_equipos():
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
        nombre_host = cliente_activo.get_nombre_host()
        cadena_equipos_activos += str(i) +'  Nombre-host:  ' + str(nombre_host) + '  IP:  ' + str(ip_cliente) + '\n'

        #Obtener los equipos de cómputo inactivos
        for x, equipo_computo in enumerate(equipos_computo):
            #Aqui se tiene que cambiar
            if cliente_activo.get_nombre_host() == equipo_computo[1]:
                equipos_inactivos[x] = None
    
    #Crear cadena de los equipos de cómputo inactivos
    for z, equipo_inactivo in enumerate(equipos_inactivos):
        if equipo_inactivo is not None:
            cadena_equipos_inactivos += str(z) + '  Nombre-Host:  ' + str(equipo_inactivo[1]) + '  MAC:  ' + str(equipo_inactivo[2]) + '\n'
    
    cadena_equipos = cadena_equipos_activos + cadena_equipos_inactivos
    return cadena_equipos

def conectar_con_equipo(operacion):
    #Obtener la variable de conexión del administrador
    admin_conn = administrador_activo[0].get_conexion()
    
    try: 
        posicion = operacion.replace('seleccionar', '')
        posicion = int(posicion)
        print(f'Posición: {posicion}')
        objeto_cliente_activo = clientes_activos[posicion]

        #Notificar al administrador que se hizo la conexión con el dispositivo
        admin_conn.send(f'Conexión con el usuario {objeto_cliente_activo.get_direccion()[0]}'.encode())
        #Notificar
        print(f'Conexión con el usuario {objeto_cliente_activo.get_direccion()[0]}')
        #Regresar objeto de conexión
        return objeto_cliente_activo
    
    except:
        admin_conn.send('Selección no válida :/'.encode())
        print('Selección no válida :/')
        return None
    
def manejar_operaciones(cliente_seleccionado):
    #La variable de conexión es la variable de conexión del usuario con el que se conectó el servidor
    admin_conn = administrador_activo[0].get_conexion()
    while True:
        try:
            #Dibujar prompt para el administrador
            admin_conn.send(f'administrador/{cliente_seleccionado.get_nombre_host()}>'.encode())

            #Tomar la instrucción del administrador
            operacion = admin_conn.recv(HEADER).decode(FORMAT, errors='ignore')

            #Notificar al administrador que el mensaje se ha enviado con éxito
            admin_conn.send(f'Mensaje enviado con éxito'.encode())

            if operacion == 'salir': 
                break

            #Enviar la insturcción al cliente
            cliente_seleccionado.get_conexion().send(operacion.encode())
        
        except:
            
            print('Error al enviar el comando')
            break

#3er Hilo: Encargado de administrar y escuchar cuando un administrador se conecte al canal de notificaciones
#para poder enviar mensajería a través de él
def aceptar_canal_notificaciones():
    while True:
        try:
            conn, addr = notificaciones_socket.accept() #Línea de bloque de código
            notificaciones_socket.setblocking(1)

            notificacion_conexion.append(conn)
            notificacion_conexion.append(addr)
            print('Conexión con socket de notificaciones')
            break
        except:         
            print('Error al aceptar la conexión con el socket de notificaciones')
   
def notificar_admin_conexiones(mensaje):
    try:
        if notificacion_conexion:
            noti_conn = notificacion_conexion[0]
            noti_conn.send(mensaje.encode())
    except:
        print('No se envio el mensaje')

#Creación de hilos y asignación de tareas
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
#3.-El tercer hilo manejará la aceptación de el canal de notificacion
def tarea():
    while True:
        tarea = queue.get()
        if tarea == 1:
            #Crear socket y vincular socket son los dos canales
            crear_socket()
            vincular_socket()   
            aceptar_conexiones()

        if tarea == 2:
            panel_administrador()

        if tarea == 3:
            aceptar_canal_notificaciones()

        queue.task_done()

crear_hilos()
crear_tareas()