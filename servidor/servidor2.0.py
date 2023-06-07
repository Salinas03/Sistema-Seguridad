import socket
import threading
import json
from queue import Queue
from base_datos.conexion import BaseDatos
from clases.persona import PersonaConectada

# 165.22.15.159
#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())

PORT = 5050
PORT_NOT = 5051

ADDR = (HOST, PORT)
ADDR_NOT = (HOST, PORT_NOT)

#Objeto base de datos
bd = BaseDatos()

#Configuración de variables para los hilos
NUMERO_HILOS = 2
NUMERO_TAREAS = [1,2]
queue = Queue()

#Arreglo de equipos de cómputo de la base de datos
equipos_computo = bd.obtener_equipos_computo()

#Arreglo de conexiones de clientes realizadas en tiempo real
clientes_activos = []
clientes_activos_mostrar = []

#Por el momento solo habra un administrador (Prueba)
administrador_activo = []

notificacion_conexion = []

#1er Hilo: Realizar el levantado del canal (socket) y aceptar nuevas conexiones
#obtener información de la base de datos
def crear_socket():
    try:
        global servidor
        global notificaciones

        notificaciones = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_socket():
    try:
        notificaciones.bind(ADDR_NOT)
        servidor.bind(ADDR)

        notificaciones.listen()
        servidor.listen()

        print(f'HOST {HOST} corriendo en el puerto {PORT}')
        print(f'NOTIFICACIONES HOST {HOST} corriendo en el puerto {PORT_NOT}')
    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        notificaciones.close()
        servidor.close()
        # vincular_socket()

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
            conn.send('{"success": True, "msg": "Conexión temporal establecida..."}'.encode())

            #Se reciben los dos parámetros obligatorios del administrador o cliente para poder
            #verificar si se puede hacer la conexión total con el servidor
            nombre_host = conn.recv(HEADER).decode(FORMAT)
            numero_serie = conn.recv(HEADER).decode(FORMAT)
            print(f'Dispositivo conectado temporalmente: {nombre_host}')

            #Hacer validación si el cliente que se conecto esta en la base de datos o no
            #Si esta en la base de datos se determina si es administrador o cliente
            guardar_conexiones(conn,addr, nombre_host, numero_serie)

        except:
            conn.send('{"success": False, "msg": "Error al aceptar la conexión :("}')
            print('Error al aceptar la conexión :(')

def guardar_conexiones(conn, addr, hostname, numero_serie):
    mensaje = 'mensaje vacio'
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtener_equipo_por_nombre_numero_serie(hostname, numero_serie)
    if not resultado:
        mensaje = f'Conexión denegada a {hostname}'
        conn.send('{"success": False, "msg": "Conexión denegada >:/"}'.encode())
        conn.close()
    else:
        #Verificar si el dispositvo que se esta conectando es un administrador o un usuario
        #dependiendo de la tabla SQL
        resultado = bd.obtener_equipo_admin_por_nombre_numero_serie(hostname, numero_serie)
        if not resultado:
            cliente = PersonaConectada(conn, addr, hostname, numero_serie)
            clientes_activos.append(cliente)
            mensaje = f'El cliente {hostname} se ha conectado'
            print('Conexión con cliente :)')
            conn.send('{"success": True, "msg": "Conexión con servidor exitosa :)"}'.encode())

            #Crear nuevo hilo para escuchar los usuarios
            # usuario_thread = threading.Thread(target=escuchar_desconexiones, args=(conn, addr))
            # usuario_thread.start()
        else:
            administrador = PersonaConectada(conn, addr, hostname, numero_serie)
            administrador_activo.append(administrador)
                
            administrador_thread = threading.Thread(target=panel_administrador, args=(conn, addr,administrador))
            administrador_thread.start()
            # if not administrador_activo:
            #     administrador = PersonaConectada(conn, addr, hostname, numero_serie)
            #     administrador_activo.append(administrador)
                
            #     administrador_thread = threading.Thread(target=panel_administrador, args=(conn, addr, administrador))
            #     administrador_thread.start()
            # else:
            #     print('Conexión denegada, administrador ya conectado'.encode())
            #     mensaje = f'Conexión denegada al administrador {hostname}'
            #     conn.send('{"success": False, "msg": "Conexión denegada, administrador ya conectado"}'.encode())
            #     conn.close()
    
    #Solo notificar cuando se conecte un usuario
    # if administrador_activo:
    #     if hostname != administrador_activo[0].get_nombre_host():
    #         notificar_admin_conexiones(f'{mensaje} \n IP: {addr} \n Número de serie: {numero_serie}')

#2do Hilo: Encargado de administrar y manejar las funcionalidades de los usuarios ya existentes
#desde la computadora del administrador
def panel_administrador(conn, addr, administrador):

    nombre_host = administrador.get_nombre_host()

    #Estar checando si se ha conectado un administrador
    msg = f"Conexión exitosa :) \nBienvenido administrador {nombre_host} \nSu dirección IP es {addr}"
    conn.send('{"success": True, "msg": "PUTA MIERDA"}'.encode(FORMAT))
                
    print('Conexión exitosa :)')
    print('A sus ordenes administrador...')

    while True:
        try:
            #Enviar el prompt del administrador (esto va a cambiar)
            conn.send('administrador/servidor>'.encode())

            #Esperar instrucción de la computadora administradora
            operacion = conn.recv(HEADER).decode(FORMAT, errors='ignore') #Línea que bloque el código

            #Realizar operaciones de administrador
            if operacion == 'listar':
                cadena_equipos = listar_equipos()
                conn.send(cadena_equipos.encode())

            elif 'seleccionar' in operacion:
                if not clientes_activos:
                    conn.send('No hay dispositivos activos a quienes realizar operaciones :/'.encode())
                else:
                    cliente_seleccionado = conectar_con_equipo(operacion)
                    if cliente_seleccionado is not None:
                        conn.send(f'Conexión con el usuario {cliente_seleccionado.get_direccion()[0]}'.encode())
                        manejar_operaciones(cliente_seleccionado, conn)
                    else:
                        conn.send('Selección no válida :/'.encode())


            elif operacion == 'salir':
                print('Administrador desconectado...')
                conn.send('Bye bye...'.encode())
                conn.close()
                index = administrador_activo.index(conn)

                del administrador_activo[index]
            else:
                conn.send('Comando no reconocido'.encode())

        except:
                print('Administrador desconectado espontáneamente...')
                conn.close()
                index = administrador_activo.index(conn)
                del administrador_activo[index]
            
def listar_equipos():
    #Se tienen que listar los equipos que estan activos 
    #Pero en la UI se tienen que ver tanto activos como inactivos

    cadena_equipos_activos = 'ACTIVOS \n'
    cadena_equipos_inactivos = 'INACTIVOS \n'

    #Copiar los equipos de cómputo a la variable de equipos inactivos
    equipos_inactivos = equipos_computo[:]
    if clientes_activos_mostrar:
        del clientes_activos_mostrar[:]

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

        #Obtener los equipos de cómputo inactivos y activos
        for x, equipo_computo in enumerate(equipos_computo):

            if cliente_activo.get_nombre_host() == equipo_computo[1]:
                equipos_inactivos[x] = None
                equipo = list(equipo_computo)
                equipo.append(ip_cliente)
                clientes_activos_mostrar.append(equipo)
    
    #Crear cadena de los equipos de cómputo inactivos
    for z, equipo_inactivo in enumerate(equipos_inactivos):
        if equipo_inactivo is not None:
            cadena_equipos_inactivos += str(z) + '  ID:  ' + str(equipo_inactivo[0]) + '  NOMBRE EQUIPO:  ' + str(equipo_inactivo[1]) +  '  NÚMERO SERIE: ' + str(equipo_inactivo[2]) + '  ID PROPIETARIO:   ' + str(equipo_inactivo[3]) +  '\n'

    #Crear cadena de los equipos de cómputo activos
    for j, cliente_activo_mostrar in enumerate(clientes_activos_mostrar):
        cadena_equipos_activos += str(j) + '  ID:  ' + str(cliente_activo_mostrar[0]) + '  NOMBRE EQUIPO:  ' + str(cliente_activo_mostrar[1]) +  '  NÚMERO SERIE: ' + str(cliente_activo_mostrar[2]) + '  ID PROPIETARIO:   ' + str(cliente_activo_mostrar[3]) + '  IP:   ' + str(cliente_activo_mostrar[5]) +'\n'
    
    cadena_equipos = cadena_equipos_activos + cadena_equipos_inactivos
    equipos = [equipos_inactivos, clientes_activos_mostrar]
    equipos = json.dumps(equipos)
    # return equipos
    return cadena_equipos

def conectar_con_equipo(operacion):
    
    try: 
        posicion = operacion.replace('seleccionar', '')
        posicion = int(posicion)
        print(f'Posición: {posicion}')
        objeto_cliente_activo = clientes_activos[posicion]

        print(f'Conexión con el usuario {objeto_cliente_activo.get_direccion()[0]}')
        
        return objeto_cliente_activo
    
    except:
        print('Selección no válida :/')
        return None
    
def manejar_operaciones(cliente_seleccionado, conn_admin):

    while True:
        try:
            #Dibujar prompt para el administrador
            conn_admin.send(f'administrador/{cliente_seleccionado.get_nombre_host()}>'.encode())

            #Tomar la instrucción del administrador
            operacion = conn_admin.recv(HEADER).decode(FORMAT, errors='ignore')

            #Notificar al administrador que el mensaje se ha enviado con éxito
            conn_admin.send(f'Mensaje enviado con éxito'.encode())

            if operacion == 'salir': 
                break

            #Enviar la insturcción al cliente
            cliente_seleccionado.get_conexion().send(operacion.encode())

            #Obtener respuesta del cliente
            # . . .
        except:
            
            print('Error al enviar el comando')
            break

#3er Hilo: Encargado de administrar y escuchar cuando un administrador se conecte al canal de notificaciones
#para poder enviar mensajería a través de él
def aceptar_canal_notificaciones():
    while True:
        try:
            # print('fakiu')
            conn, addr = notificaciones.accept() #Línea de bloque de código
            notificaciones.setblocking(1)

            notificacion_conexion.append(conn)
            notificacion_conexion.append(addr)
            print('Conexión con socket de notificaciones')
            # break
        except:         
            print('Error al aceptar la conexión con el socket de notificaciones')
            notificaciones.close()
            # break
   
def notificar_admin_conexiones(mensaje):
    try:
        if notificacion_conexion:
            #Obtener variable de conexión
            noti_conn = notificacion_conexion[0]

            #Listar los equipos
            equipos = listar_equipos()

            noti_conn.send(mensaje.encode())
            noti_conn.send(equipos.encode())
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
#2.-El segundo hilo manejará la aceptación de el canal de notificacion
def tarea():
    while True:
        tarea = queue.get()
        if tarea == 1:
            #Crear socket y vincular socket son los dos canales
            crear_socket()
            vincular_socket()   
            aceptar_conexiones()

        if tarea == 2:
            pass
            # aceptar_canal_notificaciones()

        queue.task_done()

crear_hilos()
crear_tareas()