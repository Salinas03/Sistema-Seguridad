import socket
import threading
import json
from base_datos.conexion import BaseDatos
from clases.persona import PersonaConectada

# 165.22.15.159
#Variables globales para la configuración del socket
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
# HOST = '165.22.15.159'
PORT = 5050
PORT_NOTI = 5051
ADDR = (HOST, PORT)
ADDR_NOTI = (HOST, PORT_NOTI)

#Objeto base de datos
bd = BaseDatos()

#Arreglo de equipos de cómputo de la base de datos
equipos_computo = bd.obtener_equipos_computo()

#Arreglo de conexiones de clientes realizadas en tiempo real
clientes_activos = []
clientes_activos_mostrar = []

#Por el momento solo habra un administrador (Prueba)
administradores_activos = []
administradores_activos_notificacion = []

#CREAR CANALES DEL SERVIDOR Y GUARDAR LAS CONEXIONES REALIZADAS
def crear_socket():
    try:
        global servidor
        global notificacion

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_socket():
    try:
        servidor.bind(ADDR)
        notificacion.bind(ADDR_NOTI)
        servidor.listen()
        notificacion.listen()

        print(f'HOST {HOST} corriendo en el puerto {PORT}')
        print(f'NOTIFICACION {HOST} corriendo en el puerto {PORT_NOTI}')

        notificacion_thread = threading.Thread(target=aceptar_conexiones_notificacion)
        notificacion_thread.start()

    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        servidor.close()
        notificacion.close()
        # vincular_socket()

def aceptar_conexiones():
    #Cerrar todas las conexiones al iniciar el servidor
    for cliente in clientes_activos:
        cliente.get_conexion().close()

    for administrador in administradores_activos:
        administrador.get_conexion().close()

    #Borrar los datos de las conexiónes y direcciones
    del clientes_activos[:]
    del administradores_activos[:]

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
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = bd.obtener_equipo_por_nombre_numero_serie(hostname, numero_serie)
    if not resultado:
        conn.send('{"success": False, "msg": "Conexión denegada >:/"}'.encode())
        conn.close()
    else:
        #Verificar si el dispositvo que se esta conectando es un administrador o un usuario dependiendo de la tabla SQL

        resultado = bd.obtener_equipo_admin_por_nombre_numero_serie(hostname, numero_serie)
        if not resultado:
            cliente = PersonaConectada(conn, addr, hostname, numero_serie)
            clientes_activos.append(cliente)
            print('Conexión con cliente :)')
            conn.send('{"success": True, "msg": "Conexión con servidor exitosa :)"}'.encode())

            usuario_thread = threading.Thread(target=panel_usuario, args=(conn, cliente))
            usuario_thread.start()

            enviar_mensajes(f'Usuario {hostname} con la IP {addr} se ha conectado')

        else:
            administrador = PersonaConectada(conn, addr, hostname, numero_serie)
            administradores_activos.append(administrador)

            administrador_thread = threading.Thread(target=panel_administrador, args=(conn,administrador))
            administrador_thread.start()

            enviar_mensajes(f'Administrador {hostname} con la IP {addr} se ha conectado')

#MANEJAR LAS OPERACIONES DEL ADMINISTRADOR, LISTAR, SELECCIONAR Y SALIR
def panel_administrador(conn, administrador):

    nombre_host = administrador.get_nombre_host()

    #Estar checando si se ha conectado un administrador
    msg = f"Bienvenido administrador {nombre_host} :)"
    respuesta = json.dumps({"success": True, "msg": msg})
    conn.send(respuesta.encode(FORMAT))
                
    print('Conexión exitosa :)')
    print('A sus ordenes administrador...')

    while True:
        try:
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
                administrador_desconexion = borrar_administradores_activos(conn)
                enviar_mensajes(f'Administrador {administrador_desconexion.get_nombre_host()} desconectado')
                conn.close()
                break
            else:
                conn.send('Comando no reconocido'.encode())

        except:
                print('Administrador desconectado espontáneamente...')
                administrador_desconexion = borrar_administradores_activos(conn)
                enviar_mensajes(f'Administrador {administrador_desconexion.get_nombre_host()} desconectado')
                conn.close()
                break
            
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

#MANEJAR OPERACIONES CON LOS USUARIOS
def panel_usuario(conn, usuario):
    while True:
        try:
            print(f'Entró {usuario.get_nombre_host()} al panel de usuario')
            respuesta_usuario = conn.recv(HEADER).decode(FORMAT)
            if respuesta_usuario == 'SALIR':
                enviar_mensajes(f'Usuario {usuario.get_nombre_host()} se ha desconectado')
                conn.close()
                break

        except:         
            enviar_mensajes(f'Usuario {usuario.get_nombre_host()} se ha desconectado')
            conn.close()
            break
   
#MANEJAR EL SOCKET DE NOTIFICACIONES
def aceptar_conexiones_notificacion():
    #Cerrar todas las conexiones al iniciar el servidor
    for administrador_notificacion in administradores_activos_notificacion:
        administrador_notificacion[0].close()

    del administradores_activos_notificacion[:]

    while True:
        try:
            conn, addr = notificacion.accept()
            notificacion.setblocking(1)

            administradores_activos_notificacion.append((conn, addr))

            print(f'Conexión con socket de notificaciones {addr[0]}')

        except:
            print('Hubo un error al conectar con el canal de notificación')
            notificacion.close()

def panel_notificacion(conn):
    while True:
        try:
            print('Entrando al panel')
            respuesta_usuario = conn.recv(HEADER).decode(FORMAT)
            if respuesta_usuario == 'SALIR':
                print('Desconexión con el panel de notificación')
                conn.close()
                break
        except:
            print('Hubo un problema ')
            conn.close()
            break

#FUNCIÓN PARA ENVIAR MENSAJERIA
def enviar_mensajes(mensaje):
    try:
        if administradores_activos:
            for administrador_notificacion in administradores_activos_notificacion: 
                administrador_notificacion[0].send(f'{mensaje}'.encode())
    except:
        print('No se enviaron algunos de los mensajes')

#FUNCIONES PARA BORRAR
def buscar_conexiones_arreglo(arreglo, conexion):
    for elemento in arreglo:
        if elemento.get_conexion() == conexion:
            return elemento
            
    return None

def borrar_administradores_activos(conn):
    #Borrar administrador del arreglo
    administrador_desconexion = buscar_conexiones_arreglo(administradores_activos, conn)
    index = administradores_activos.index(administrador_desconexion)
    del administradores_activos[index]
    return administrador_desconexion

crear_socket()
vincular_socket()
aceptar_conexiones()
