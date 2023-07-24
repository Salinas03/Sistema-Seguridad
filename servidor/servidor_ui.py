import socket
import threading
import json
import atexit
import datetime
import time
from base_datos.conexion import conexion
from base_datos.equipos_consultas import EquiposConsultas
from base_datos.propietarios_consultas import PropietariosConsultas
from clases.equipo_conectado import EquipoConectado
from clases.validar_json import is_valid_json

#VARIABLES GLOBALES PARA LA CONFIGURACIÓN DE SOCKETS
FORMAT = 'utf-8'
HEADER = 20480
#HOST = socket.gethostbyname(socket.gethostname())
# HOST = '68.183.143.116'
HOST = '165.22.15.159'

#PUERTOS DE LOS DIFERENTES SOCKETS
PORT = 5050
PORT_NOTI = 5051
PORT_BROAD = 5052
PORT_CLIEN = 5053
PORT_BD = 5054
PORT_CONA = 5055

#DIRECCIONES DE LOS DIFERENTES SOCKETS
ADDR = (HOST, PORT)
ADDR_NOTI = (HOST, PORT_NOTI)
ADDR_BROAD = (HOST, PORT_BROAD)
ADDR_CLIEN = (HOST, PORT_CLIEN)
ADDR_BD = (HOST, PORT_BD)
ADDR_CONA = (HOST, PORT_CONA)
TIMEOUT = 3
TIME_TO_SEND_MESSAGES = 2

#ARREGLOS DE CONEXIONES CON EL SERVIDOR
conexiones_equipos_cliente = [] #GUARDAR OBJETO DE EQUIPO CONECTADO
conexiones_equipos_cliente_mostrar = [] 
conexiones_equipos_cliente_secundario = []

#ARREGLOS DE CONEXIONES DE ADMINISTRADORES
conexiones_equipos_admin = [] #GUARDAR OBJETO DE EQUIPO CONECTADO
conexiones_conectividad_admin = []
conexiones_equipos_admin_notificacion  = []
conexiones_equipos_broadcast = []
conexiones_equipos_operacionesbd = []

#CONFIGURACIÓN INICIAL DE SOCKETS
def crear_sockets():
    try:
        #VARIABLES GLOBALES DE LOS SOCKETS
        global servidor
        global conectividad_admin
        global notificacion
        global broadcasting
        global operacionesbd
        global cliente

        #CREACIÓN DE DE SOCKETS
        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        conectividad_admin = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conectividad_admin.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        #CONEXIONES QUE SE GUARDARAN EN ARREGLOS LAS CUALES HAY QUE MANTENER ENCENDIDAS
        notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        notificacion.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        broadcasting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        broadcasting.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        operacionesbd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        operacionesbd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_sockets():
    try:
        #CONEXIÓN DE SOCKETS CREADOS ANTERIORMENTE
        servidor.bind(ADDR)
        conectividad_admin.bind(ADDR_CONA)
        notificacion.bind(ADDR_NOTI)
        broadcasting.bind(ADDR_BROAD)
        operacionesbd.bind(ADDR_BD)
        cliente.bind(ADDR_CLIEN)
        
        #ABRIR LOS SOCKETS Y ESCUCHAR LAS PETICIONES DE LAS CONEXIONES
        servidor.listen()
        conectividad_admin.listen()
        cliente.listen()
        notificacion.listen()
        broadcasting.listen()
        operacionesbd.listen()

        print(f'SERVIDOR {HOST} corriendo en el puerto {PORT}')
        print(f'CONECTIVIDAD {HOST} corriendo en el puerto {PORT_CONA}')
        print(f'NOTIFICACION {HOST} corriendo en el puerto {PORT_NOTI}')
        print(f'BROADCASTING {HOST} corriendo en el puerto {PORT_BROAD}')
        print(f'USUARIO {HOST} corriendo en el puerto {PORT_CLIEN}')
        print(f'OPERACIONESBD {HOST} corriendo en el puerto {PORT_BD}')

        #CREACIÓN DE HILOS DE LOS SOCKETS PARA ESCUCHAR LAS CONEXIONES
        # conectividad_thread = threading.Thread(target=)
        cliente_thread = threading.Thread(target=aceptar_conexiones_cliente)
        cliente_thread.start()
        conectividad_thread = threading.Thread(target=aceptar_conexiones_conectividad)
        conectividad_thread.start()
        notificacion_thread = threading.Thread(target=aceptar_conexiones_notificacion)
        notificacion_thread.start()
        broadcasting_thread = threading.Thread(target=aceptar_conexiones_broadcast)
        broadcasting_thread.start()
        operacionesbd_thread = threading.Thread(target=aceptar_conexiones_operacionesbd)
        operacionesbd_thread.start()

    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        servidor.close()
        notificacion.close()
        broadcasting.close()
        operacionesbd.close()
        # vincular_sockets()

def cerrar():
    servidor.close()
    notificacion.close()
    cliente.close()
    broadcasting.close()

#ACEPTACIÓN DE CONEXIONES
def aceptar_conexiones():
    #Cerrar todas las conexiones al iniciar el servidor
    for conexion_equipo  in conexiones_equipos_cliente:
        conexion_equipo.get_conexion().close()

    for conexion_admin in conexiones_equipos_admin:
        conexion_admin.get_conexion().close()

    #Borrar los datos de las conexiónes y direcciones
    del conexiones_equipos_cliente[:]
    del conexiones_equipos_admin[:]
    while True:
        try:
            conn, addr = servidor.accept() #Linea que bloquea el flujo del programa
            servidor.setblocking(1) #Evita el tiempo de espera de las conexiones, (el servidor no se cierra)

            #Conexión temporal establecida para obtener información del cliente que se conecto
            conn.send('{"success": true, "msg": "Conexión temporal establecida..." }'.encode())

            #Se reciben los dos parámetros obligatorios del administrador o cliente para poder
            #verificar si se puede hacer la conexión total con el servidor
            nombre_host = conn.recv(HEADER).decode(FORMAT)
            numero_serie = conn.recv(HEADER).decode(FORMAT)
            print(f'Dispositivo conectado temporalmente: {nombre_host}')

            #Hacer validación si el cliente que se conectó esta en la base de datos o no
            #Si esta en la base de datos se determina si es administrador o cliente
            guardar_conexiones(conn,addr, nombre_host, numero_serie)

        except socket.error as e:
            # conn.send('{"success": false, "msg": "Error al aceptar la conexión :("}'.encode())
            print(f'Error al aceptar la conexión {e}')

def aceptar_conexiones_conectividad():
    for conexion_conectividad in conexiones_conectividad_admin:
        conexion_conectividad[0].close()

    del conexiones_conectividad_admin[:]

    while True:
        try:
            conn, addr = conectividad_admin.accept()
            conectividad_admin.setblocking(1)

            numero_serie = conn.recv(HEADER).decode(FORMAT)
            conn.send('{"success": true, "msg": "Se recibió el número de serie en [conectividadadmin]"}'.encode())
            print('Se recibió el número de serie en [conectividadadmin]')

            conexiones_conectividad_admin.append((conn, addr))
            conectividad_thread = threading.Thread(target=panel_conectividad_admin, args=(conn, addr, numero_serie))
            conectividad_thread.start()

        except socket.error as e:
            print(f'Hubo un error al conectar con el canal de conectividad admin {e}')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en conectividada :("}'.encode())

def aceptar_conexiones_notificacion():
    #Cerrar todas las conexiones al iniciar el servidor
    for conexion_admin_notificacion in conexiones_equipos_admin_notificacion:
        conexion_admin_notificacion[0].close()

    del conexiones_equipos_admin_notificacion[:]

    while True:
        try:
            conn, addr = notificacion.accept()
            notificacion.setblocking(1)

            #CONFIGURACIÓN PARA MANTENER VIVA LA CONEXIÓN DEL SOCKET
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            numero_serie = conn.recv(HEADER).decode(FORMAT)
            conn.send('{"success": true, "msg": "Se recibió el número de serie en [notificación]"}'.encode())
            print('Se recibió el número de serie en [notificación]')

            conexiones_equipos_admin_notificacion.append((conn, addr, numero_serie))
        except socket.error as e:
            print(f'Hubo un error al conectar con el canal de notificación {e}')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en notificación :("}'.encode())
   
def aceptar_conexiones_broadcast():
    for conexion_broadcast in conexiones_equipos_broadcast:
        conexion_broadcast[0].close()

    del conexiones_equipos_broadcast[:]

    while True:
        try:
            conn, addr = broadcasting.accept()
            broadcasting.setblocking(1)

            #CONFIGURACIÓN PARA MANTENER VIVA LA CONEXIÓN
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            numero_serie = conn.recv(HEADER).decode(FORMAT)
            conn.send('{"success": true, "msg": "Se recibió el número de serie en [broadcast]"}'.encode())
            print('Se recibió el número de serie en [broadcast]')

            conexiones_equipos_broadcast.append((conn, addr, numero_serie))
        except socket.error as e:
            print(f'Hubo un error al conectar con el canal de broadcasting {e}')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en broadcasting :("}'.encode())

def aceptar_conexiones_operacionesbd():
    for conexion_operacionbd in conexiones_equipos_operacionesbd:
        conexion_operacionbd[0].close()

    del conexiones_equipos_operacionesbd[:]

    while True:
        try:
            conn, addr = operacionesbd.accept()
            operacionesbd.setblocking(1)

            #CONFIGURACIÓN PARA MANTENER VIVA LA CONEXIÓN
            conn.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 120)
            conn.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 60)

            numero_serie = conn.recv(HEADER).decode(FORMAT)
            conn.send('{"success": true, "msg": "Se recibió el número de serie en [operacionesbd]"}'.encode())
            print('Se recibió el número de serie en [operacionesbd]')

            conexiones_equipos_operacionesbd.append((conn, addr, numero_serie))
        except socket.error as e:
            print(f'Hubo un error al conectar con el canal de operacionesbd {e}')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión de operacionesbd :("}'.encode())

def aceptar_conexiones_cliente():
    for conexion_canal_cliente in conexiones_equipos_cliente_secundario:
        conexion_canal_cliente[0].close()

    del conexiones_equipos_cliente_secundario[:]

    while True:
        try:
            conn, addr = cliente.accept()
            cliente.setblocking(1)

            #Recibir número de serie y guardarlo en el panel del cliente para despues poder borrar el canal principal
            numero_serie = conn.recv(HEADER).decode(FORMAT)

            #Mensaje de verificación de que se ha conectado y enviado el número de serie
            conn.send('{"success": true, "msg": "Se realizó la conexión con el canal secundario"}'.encode())

            print(f'NÚMERO DE SERIE DE CONEXIÓN SECUNDARIA {numero_serie}')

            conexiones_equipos_cliente_secundario.append((conn, addr))

            #Creación del hilo de panel de cliente el cual verifica la conectividad con el (CLIENTE/SERVIDOR)
            panel_cliente_thread = threading.Thread(target=panel_cliente, args=(conn, addr, numero_serie))
            panel_cliente_thread.start()
        except:
            print('Hubo un error al conectar con el canal de cliente')
            borrar_conexion_cliente_secundario(conn)
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en cliente :("}'.encode())

#GUARDAR CONEXIONES DEL SOCKET PRINCIPAL
def guardar_conexiones(conn, addr, hostname, numero_serie):
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = json.loads(EquiposConsultas(conexion()).obtener_equipo_por_nombre_numero_serie(hostname, numero_serie))

    resultado = resultado['data']
    if resultado:
        resultado = resultado[0]

    if not resultado:
        print(f'Se denegó la entrada a {hostname}')
        conn.send('{"success": false, "msg": "Conexión denegada >:/"}'.encode())
        conn.close()

        enviar_notificacion(f'Un dispositivo con la IP {addr} y número de serie {numero_serie} intento entrar al canal sin permisos')
        #Realizar un método para guardar estas conexiones intrusivas en algún otro lado TODO
    else:
        #Verificar si el dispositivo que se esta conectando es un administrador o un usuario dependiendo de la tabla SQL
        resultado = json.loads(EquiposConsultas(conexion()).obtener_equipo_admin_por_nombre_numero_serie(hostname, numero_serie))

        resultado = resultado['data']
        if resultado:
            resultado = resultado[0]

        if not resultado:
            equipo_cliente = EquipoConectado(conn, addr, hostname, numero_serie)
            conexiones_equipos_cliente.append(equipo_cliente)
            print(f'Conexión con cliente a las {datetime.datetime.now()} :)')
            conn.send(json.dumps({'success': True, 'msg': 'Vinculación con servidor exitosa :)'}).encode())

            #Broadcast function
            broadcast()

        else:
            print(f'Administrador {hostname} con la IP {addr} se ha conectado a las {datetime.datetime.now()}')
            equipo_admin = EquipoConectado(conn, addr, hostname, numero_serie)
            conexiones_equipos_admin.append(equipo_admin)

            administrador_thread = threading.Thread(target=panel_administrador, args=(conn,equipo_admin))
            administrador_thread.start()

            enviar_notificacion(f'Administrador {hostname} con la IP {addr} se ha conectado')

#PANELES DE SE REDIRIGEN LAS CONEXIONES PARA ADMINISTRAR EL CANAL
def panel_administrador(conn, administrador):

    nombre_host = administrador.get_nombre_host()

    msg = f"Bienvenido administrador {nombre_host} :)"
    respuesta = json.dumps({"success": True, "msg": msg})
    conn.send(respuesta.encode(FORMAT))
                
    print('Conexión exitosa :)')
    print('A sus ordenes administrador...')

    while True:
        try:

            #Esperar instrucción de la computadora administradora
            operacion = conn.recv(HEADER).decode(FORMAT, errors='ignore') #Línea que bloque el código

            #Realizar operaciones de administrador
            if operacion == 'listar':
                equipos = listar_equipos()
                conn.send(equipos.encode())

            elif 'seleccionar' in operacion:
                if not conexiones_equipos_cliente:
                    conn.send(json.dumps({'success': False, 'msg': 'No hay dispositivos activos a quienes realizar operaciones :/'}).encode())
                else:
                    cliente_seleccionado = conectar_con_equipo(operacion)
                    if cliente_seleccionado is not None:
                        if cliente_seleccionado:
                            #Manejar las operaciones de la selección
                            mensaje = f'Selección con el usuario {cliente_seleccionado.get_nombre_host()}'
                            conn.send(json.dumps({'success': True, 'msg': mensaje}).encode())

                            manejar_operaciones_seleccion(cliente_seleccionado, conn)
                        else:
                            conn.send(json.dumps({'success': False, 'msg': 'La computadora ya esta seleccionada por alguien más, espere un momento...'}).encode())
                    else:
                        conn.send(json.dumps({'success': False, 'msg': 'Selección no válida, computadora inexistente :/'}).encode())

            #Operaciones con la base de datos
            elif is_valid_json(operacion):
                respuesta_operacion = panel_base_datos(operacion)
                conn.send(respuesta_operacion.encode()) #Respetar el request response

            else:
                print(f'Salida del administrador {administrador.get_nombre_host()}, Bye bye...')
                conn.close()
                break
                
        except socket.error as e:
            print(f'EXCPETION [PanelAdministrador]: {e}')
            conn.close()
            break

def panel_conectividad_admin(conn, addr, numero_serie):
    print(f'Entró {numero_serie} al panel de conectividad de administrador')
    conn.settimeout(TIMEOUT)

    while True:
        try:
            time.sleep(TIME_TO_SEND_MESSAGES)
            conn.send('*'.encode())
            conn.recv(HEADER).decode(FORMAT)

        except socket.error as e:
            print(f'EXCEPTION [PanelConectividad]: {e}')

            #Realizar borrado del canal principal
            administrador_desconectado = borrar_administradores_numero_serie(numero_serie)
            print(f'Administrador {administrador_desconectado.get_nombre_host()} desconectado por panel de conectividad')

            #Enviar notificación a los administradores de la desconexión
            enviar_notificacion(f'Administrador {administrador_desconectado.get_nombre_host()} desconectado')

            #Borrado de canales secundarios
            borrar_conectividad_administradores(conn)
            borrar_administradores_notificacion(numero_serie)
            borrar_administradores_broadcasting(numero_serie)
            borrar_administradores_operacionesbd(numero_serie)

            #Cerrar las selecciones en caso de que haya computadoras seleccionadas
            cerrar_selecciones(numero_serie, administrador_desconectado)

            #Realizar un borrado para esta conexión de conectividad
            conn.close()
            break
        
def panel_cliente(conn, addr, numero_serie):
    print(f'Entró {numero_serie} al panel de cliente secundario.')
    conn.settimeout(TIMEOUT)

    while True:
        try:    
            time.sleep(1)
            conn.send('*'.encode())
            conn.recv(HEADER).decode(FORMAT)

        except ConnectionResetError:         
            print(f'Hubo un error al recibir el mensaje en el panel del cliente (ConnectionReset) {datetime.datetime.now()}')
            borrar_conexion_cliente_principal(numero_serie)
            borrar_conexion_cliente_secundario(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break

        except socket.timeout:
            print(f'Hubo un error al recibir el mensaje en el panel del cliente (Timeout) {datetime.datetime.now()}')
            borrar_conexion_cliente_principal(numero_serie)
            borrar_conexion_cliente_secundario(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break

        except:
            print(f'Hubo un error al recibir el mensaje en el panel del cliente (Exception) {datetime.datetime.now()}')
            borrar_conexion_cliente_principal(numero_serie)
            borrar_conexion_cliente_secundario(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break
          
#PANELES DE ADMINISTRACIÓN QUE SE EJECUTAN DEPENDIENDO DE CIERTA OPERACIÓN EN EL PANEL DEL ADMINISTRADOR
def panel_base_datos(instruccion): 
    instruccion = json.loads(instruccion)
    operacion = instruccion['operacion']
    print(instruccion)

    if instruccion['tabla'] == 'equipos':
        if operacion == 'insertar':
            data = instruccion['data']
            nombre_equipo = data[0]
            numero_serie = data[1]

            #Validación de la inserción, checar si ya existe ese nombre de equipo o ese número de serie
            respuesta_operacion = json.loads(EquiposConsultas(conexion()).obtener_equipo_por_nombre(nombre_equipo))
            if respuesta_operacion['success']:
                if respuesta_operacion['data']:
                    return json.dumps({'success': False, 'msg': 'Inserción incorrecta, ya existe un equipo con ese nombre'})
            else:
                return json.dumps({'success': False, 'msg': 'Ocurrió un error al realizar la inserción'})

                
            respuesta_operacion = json.loads(EquiposConsultas(conexion()).obtener_equipo_por_numero_serie(numero_serie))
            if respuesta_operacion['success']:
                if respuesta_operacion['data']:
                    return json.dumps({'success': False, 'msg': 'Inserción incorrecta, ya existe un equipo con ese número de serie'})
            else:
                return json.dumps({'success': False, 'msg': 'Ocurrió un error al realizar la inserción'})

            #Realizar la inserción
            respuesta_operacion = EquiposConsultas(conexion()).insertar_equipo_computo(nombre_equipo, numero_serie, data[2], data[3])
            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_equipos() #Se hace el refrescado de las tablas de la BD
                broadcast() #Se realiza el broadcast lo cual permite actualizar en los equipos inactivos

            return respuesta_operacion
        
        elif operacion == 'actualizar':
            respuesta_operacion = EquiposConsultas(conexion()).actualizar_equipo_computo(int(instruccion['id']), instruccion['data'])

            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_equipos()
                broadcast()

            return respuesta_operacion
        
        elif operacion == 'borrar':
            respuesta_operacion = EquiposConsultas(conexion()).borrar_equipo_computo(int(instruccion['id']))

            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_equipos()
                broadcast()

            return respuesta_operacion

        elif operacion == 'obtener_equipos_computo':
            return EquiposConsultas(conexion()).obtener_equipos_computo()

        elif operacion == 'obtener_equipo_computo_por_id':
            return EquiposConsultas(conexion()).obtener_equipo_computo_por_id(int(instruccion['id']))
        
        elif operacion == 'obtener_equipo_por_nombre_numero_serie':
            data = instruccion['data']
            return EquiposConsultas(conexion()).obtener_equipo_por_nombre_numero_serie(data[0], data[1])
        
        elif operacion == 'obtener_equipo_admin_por_nombre_numero_serie':
            data = instruccion['data']
            return EquiposConsultas(conexion()).obtener_equipo_admin_por_nombre_numero_serie(data[0], data[1])
        
        else:
            return json.dumps({'success': False, 'msg': 'Operación no encontrada'})
            
    elif instruccion['tabla'] == 'propietarios':

        if operacion == 'insertar':
            data = instruccion['data']
            respuesta_operacion = PropietariosConsultas(conexion()).insertar_propietario(data[0], data[1], data[2], data[3], data[4], data[5])
            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_propietarios()

            return respuesta_operacion

        elif operacion == 'actualizar':
            respuesta_operacion = PropietariosConsultas(conexion()).actualizar_propietario(int(instruccion['id']), instruccion['data'])
            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_propietarios()

            return respuesta_operacion

        elif operacion == 'actualizar_perfil':
            respuesta_operacion = PropietariosConsultas(conexion()).actualizar_perfil(int(instruccion['id'], instruccion['data']))
            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_propietarios()

            return respuesta_operacion

        elif operacion == 'borrar':
            respuesta_operacion = PropietariosConsultas(conexion()).eliminar_propietario(int(instruccion['id']))
            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_propietarios()

            return respuesta_operacion

        elif operacion == 'obtener_propietarios':
            respuesta_operacion = PropietariosConsultas(conexion()).obtener_propietarios()
            return respuesta_operacion

        elif operacion == 'login':
            data = instruccion['data']
            #Busqueda para ver si ya existe este usuario que esta tratando de loguearse
            #TODO
            print('Dentro de LOGIN')
            respuesta_operacion = PropietariosConsultas(conexion()).obtener_propietario(data[0], data[1])
            print('RESPUESTA LOGIN')
            print(respuesta_operacion)
            
            return respuesta_operacion

        elif operacion == 'obtener_propietario_id':
            respuesta_operacion = PropietariosConsultas(conexion()).seleccionar_propietario_id(int(instruccion['id']))
            return respuesta_operacion
        
        elif operacion == 'obtener_propietario_correo':
            correo = operacion['data']
            respuesta_operacion = PropietariosConsultas(conexion().obtener_propietario_correos(operacion[correo]))
            return respuesta_operacion

#OPERACIONES QUE PUEDEN REALIZAR LOS ADMINISTRADORES CON LOS EQUIPOS
def listar_equipos():
    #Se tienen que listar los equipos que estan activos 
    #Pero en la UI se tienen que ver tanto activos como inactivos

    #Copiar los equipos de cómputo a la variable de equipos inactivos
    equipos_computo = json.loads(EquiposConsultas(conexion()).obtener_equipos_computo_clientes())
    equipos_computo = equipos_computo['data']
    equipos_inactivos = equipos_computo[:]

    #Borrar elementos del arreglo auxiliar
    if conexiones_equipos_cliente_mostrar:
        del conexiones_equipos_cliente_mostrar[:]

    print('CONEXIONES EQUIPOS CLIENTE')
    print(conexiones_equipos_cliente)

    for i, conexion_equipo in enumerate(conexiones_equipos_cliente[:]):
        bandera = False
        #Mostrar solo aquellas conexiones que estan activas
        conexion_equipo.get_conexion().settimeout(1)
        try:
            #Envio de mensaje vacio para verificar conectividad con dispositivo cada vez que se liste
            conexion_equipo.get_conexion().send(' '.encode())
            conexion_equipo.get_conexion().recv(HEADER)
            bandera = True
        except:
            index = conexiones_equipos_cliente.index(conexion_equipo)
            del conexiones_equipos_cliente[index] #Borrar la conexion del cliente en esa posición en caso de que no haya respuesta
            continue
        
        if bandera:
            ip_cliente = conexion_equipo.get_direccion()[0]
            seleccionado = conexion_equipo.get_seleccionado()

            #Obtener los equipos de cómputo inactivos y activos
            for x, equipo_computo in enumerate(equipos_computo):

                if conexion_equipo.get_nombre_host() == equipo_computo[1]: #equipo_computo[1] = nombre_host
                    equipos_inactivos[x] = None

                    equipo = list(equipo_computo) #Convertir la tupla de los equipos en un arreglo
                    equipo.append(ip_cliente)     #Agregar la IP al arreglo
                    equipo.append(seleccionado)   #Agregar la variable de selección
                    conexiones_equipos_cliente_mostrar.append(equipo)

    equipos = [equipos_inactivos, conexiones_equipos_cliente_mostrar]
    equipos = json.dumps(equipos)
    print('[EQUIPOS ACTIVOS]')
    print(conexiones_equipos_cliente_mostrar)
    print('[EQUIPOS INACTIVOS]')
    print(equipos_inactivos)
    return equipos

def conectar_con_equipo(operacion):
    print('[CONECTAR CON EQUIPO]')
    try: 
        cadena = operacion.replace('seleccionar', '').strip().split(',')
        posicion = int(cadena[0])
        seleccionador = cadena[1]
        
        #Obtener el elemento del arreglo en esa posición
        objeto_cliente_seleccionado = conexiones_equipos_cliente[posicion]

        if objeto_cliente_seleccionado is None:
            return None
        
        #Checar si ya esta seleccionado o no 
        if objeto_cliente_seleccionado.get_seleccionado():
            return False

        #Marcar ese elemento del arreglo en específico como seleccionado
        objeto_cliente_seleccionado.set_seleccionado(True)
        objeto_cliente_seleccionado.set_seleccion_numero_serie(seleccionador)

        print(f'Selección con el usuario {posicion}:{objeto_cliente_seleccionado.get_nombre_host()} por el equipo con el número de serie {seleccionador}')
        return objeto_cliente_seleccionado
    
    except:
        print('Selección no válida :/')
        return None
    
def manejar_operaciones_seleccion(cliente_seleccionado, conn_admin):
    #Tomar la instrucción del administrador
    print('Dentro de manejar operaciones...')
    
    # Verificar si esta en el req/res de la consola o de las operaciones normales
    while True:
        try:
            operacion = conn_admin.recv(HEADER).decode(FORMAT)
            print(f'Operación a realizar {operacion}')

            #Operación de salir de la selección
            if operacion == 'salir':
                
                #Cambiar la selección, que también se cambia dentro del arreglo
                cliente_seleccionado.set_seleccionado(False)
                cliente_seleccionado.set_seleccion_numero_serie('')

                print('Cambio de selección a False')
                print('Se salio de la selección')
                conn_admin.send(json.dumps({'success': True, 'msg': 'Se realizó la salida de selección con éxito'}).encode()) 
                break

            #Abrir consola en caso que se requiere usar manejo de la consola
            if operacion == 'consola':
                cliente_seleccionado.get_conexion().send(operacion.encode())
                cliente_seleccionado.set_consola(True)
                manejar_consola_cliente(cliente_seleccionado, conn_admin)
                print('Se salio de la consola en el servidor')

            #Realizar operaciones de suspensión de computadora o apagado
            else:
                #Enviar la instrucción al cliente
                cliente_seleccionado.get_conexion().send(operacion.encode())

                #Obtener respuesta del cliente
                respuesta_cliente = cliente_seleccionado.get_conexion().recv(HEADER).decode(FORMAT)
                print('Respuesta cliente')
                print(respuesta_cliente)

                #Enviar la respuesta cdel cliente al administrador
                conn_admin.send(respuesta_cliente.encode())

        except:
            print('Error al enviar el comando')
            conn_admin.send(json.dumps({'success': False, 'msg': 'Hubo un error al realizar la operación al equipo'}).encode())
            break

def manejar_consola_cliente(conn_cli, conn_admin):
    print('[MANEJAR CONSOLA admin/servidor/cliente]')
    while True:
        try:
            #Recibir el prompt de la consola la primera vez y despúes esperar las salidas de la consola del cliente
            respuesta_cliente = conn_cli.get_conexion().recv(HEADER).decode(FORMAT)
            print('Respuesta cliente')
            print(respuesta_cliente)

            #Enviar salida del cliente al administrador
            conn_admin.send(respuesta_cliente.encode())

            #Esperar nueva instrucción del administrador para el cliente
            instruccion_admin = conn_admin.recv(HEADER).decode(FORMAT)
            print('Instrucción del administrador al cliente')
            print(instruccion_admin)

            if instruccion_admin == 'salir':
                try:
                    conn_cli.get_conexion().send(instruccion_admin.encode()) #Mandar mensaje de salida de la consola al cliente
                    break
                except:
                    break

            #Enviar instrucción al cliente
            try:
                conn_cli.get_conexion().send(instruccion_admin.encode())
            except socket.error as e:
                print(f'Desconexión del cliente: {e}')
                #Enviar mensaje de desconexión al administrador
                conn_admin.send('desconectado'.encode())
                break

        except socket.error as e:
            print(f'Algo sucedio en la conosola del cliente {e}')
            break

#FUNCIONES DE BORRADO DE CONEXIONES
def borrar_administradores_numero_serie(numero_serie):
    for conexion_admin in conexiones_equipos_admin:
        if conexion_admin.get_identificador() == numero_serie:
            index = conexiones_equipos_admin.index(conexion_admin)
            del conexiones_equipos_admin[index]
            print('[BORRADO DE ADMINISTRADORES ACTIVOS POR NUMERO DE SERIE]')
            return conexion_admin
        
def borrar_conectividad_administradores(conn):
    for conexion_conectividad in conexiones_conectividad_admin[:]:
        if conexion_conectividad[0] == conn:
            index = conexiones_conectividad_admin.index(conexion_conectividad)
            del conexiones_conectividad_admin[index]

    print('[BORRADO DE CONEXIONES DE CONECTIVIDAD ADMINISTRADOR]')

def borrar_administradores_notificacion(numero_serie):
    for conexion_admin_notificacion in conexiones_equipos_admin_notificacion:
        if conexion_admin_notificacion[2] == numero_serie:
            index = conexiones_equipos_admin_notificacion.index(conexion_admin_notificacion)
            del conexiones_equipos_admin_notificacion[index]
            print('[BORRADO DE CONEXIONES DE NOTIFICACIÓN]')
            return conexion_admin_notificacion[1]
        
def borrar_administradores_broadcasting(numero_serie):
    for conexion_broadcast in conexiones_equipos_broadcast:
        if conexion_broadcast[2] == numero_serie:
            index = conexiones_equipos_broadcast.index(conexion_broadcast)
            del conexiones_equipos_broadcast[index]
            print('[BORRADO DE CONEXIONES BROADCASTING]')
            return conexion_broadcast
        
def borrar_administradores_operacionesbd(numero_serie):
    for conexion_operacionbd in conexiones_equipos_operacionesbd:
        if conexion_operacionbd[2] == numero_serie:
            index = conexiones_equipos_operacionesbd.index(conexion_operacionbd)
            del conexiones_equipos_operacionesbd[index]
            print('[BORRADO DE CONEXIONES OPERACIONESBD]')
            return conexion_operacionbd

def borrar_conexion_cliente_principal(numero_serie):
    for conexion_equipo in conexiones_equipos_cliente[:]:
            if conexion_equipo.get_identificador() == numero_serie:
                index = conexiones_equipos_cliente.index(conexion_equipo)
                del conexiones_equipos_cliente[index]
    
    print('[BORRADO DE CONEXIONES CLIENTE PRINCIPAL]')
    
def borrar_conexion_cliente_secundario(conn):    
    for conexion_equipo_secundario in conexiones_equipos_cliente_secundario[:]:
        if conexion_equipo_secundario[0] == conn:
            index = conexiones_equipos_cliente_secundario.index(conexion_equipo_secundario)
            del conexiones_equipos_cliente_secundario[index]

    print('[BORRADO DE CONEXIONES CLIENTE SECUNDARIO]')

def cerrar_selecciones(numero_serie, administrador_desconectado):
    if conexiones_equipos_cliente:
        equipos_seleccionados = list(filter(lambda conexion_equipo : conexion_equipo.get_seleccionado() == True, conexiones_equipos_cliente))

        if equipos_seleccionados:
            equipo_seleccionado = list(filter(lambda equipo_seleccionado : equipo_seleccionado.get_seleccion_numero_serie() == numero_serie, equipos_seleccionados))

            if equipo_seleccionado:
                if len(equipo_seleccionado) == 1:
                    equipo_seleccionado[0].set_seleccionado(False)
                    equipo_seleccionado[0].set_seleccion_numero_serie('')
                    cerrar_consola_seleccion(equipo_seleccionado[0])
                    print(f'RESETEO DE SELECCIÓN DEL EQUIPO {equipo_seleccionado[0].get_nombre_host()}')
                else:
                    for seleccionado in equipo_seleccionado:
                        print(seleccionado.get_nombre_host())
            else:
                print(f'No hay equipos seleccionados por el equipo {administrador_desconectado.get_nombre_host()}')

def cerrar_consola_seleccion(equipo):
    if equipo.get_consola():
        try:
            equipo.get_conexion().send('salir'.encode())
            equipo.set_consola(False)
            print(f'RESETEO DE CONSOLA EQUIPO {equipo.get_nombre_host()}')
        except socket.error as e:
            print(f'No se pudo enviar el mensaje de salida de consola [desconexión administrador] {e}')
            print('Intentando denuevo...')
            
            try:
                equipo.get_conexion().send('salir'.encode())
            except socket.error as e:
                print(f'{e}')

#FUNCIONALIDADES BROADCAST QUE SE ENVIAN A TODOS LOS ADMINISTRADORES
def enviar_notificacion(mensaje):
    print('[NOTIFICACIÓN]')
    
    if conexiones_equipos_admin:
        for conexion_admin_notificacion in conexiones_equipos_admin_notificacion: 
            try:
                conexion_admin_notificacion[0].send(f'{mensaje}'.encode())
            except socket.error as e:
                print(f'Error al enviar el mensaje de notificación {e}')

    print('[ENVIO DE NOTIFICACIONES]')

def broadcast():
    print('[BROADCASTING]')
    equipos_activos_inactivos = listar_equipos()

    if conexiones_equipos_admin:
        print('[Conexiones equipos broadcast]')
        for broadcast in conexiones_equipos_broadcast:
            print(broadcast[2])

        for conexion_broadcast in conexiones_equipos_broadcast: 
            try:
                conexion_broadcast[0].send(equipos_activos_inactivos.encode())
            except (socket.error) as e:
                print(f'Error al enviar el mensaje de broadcast {e}')
    
        
    print('[ENVIO DE BROADCAST]')

def refrescar_tabla_equipos():
    peticion_equipos = {
        'tabla': 'equipos',
        'operacion': 'obtener_equipos_computo'
    }

    equipos_computo = panel_base_datos(json.dumps(peticion_equipos))
    equipos_computo = json.loads(equipos_computo)

    respuesta = {
        "tabla": "equipos",
        "data": equipos_computo['data']
    }

    if conexiones_equipos_admin:
        print('[Conexiones equipos operacionesBD]')
        for operacionbd in conexiones_equipos_operacionesbd:
            print(operacionbd[2])
            
        for conexion_operacionesbd in conexiones_equipos_operacionesbd:
            try:
                conexion_operacionesbd[0].send(json.dumps(respuesta).encode())
            except (socket.error) as e:
                print(f'Error al enviar el mensaje de refrescar tablas {e}')

    print('[REFRESCADO TABLA EQUIPOS]')
    
def refrescar_tabla_propietarios():
    peticion_propietarios = {
        'tabla':'propietarios',
        'operacion': 'obtener_propietarios'
    }

    propietarios = panel_base_datos(json.dumps(peticion_propietarios))
    propietarios = json.loads(propietarios)

    respuesta = {
        'tabla': 'propietarios',
        'data': propietarios['data']
    }

    try:
        if conexiones_equipos_admin:
            for conexion_operacionesbd in conexiones_equipos_operacionesbd:
                conexion_operacionesbd[0].send(json.dumps(respuesta).encode())

    except:
        print('Error al refrescar las tablas de propietarios')

    print('[REFRESCADO TABLA PROPIETARIOS]')

atexit.register(cerrar)
crear_sockets()
vincular_sockets()
aceptar_conexiones()