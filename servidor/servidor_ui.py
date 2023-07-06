import socket
import threading
import json
import atexit
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
PORT_SEL = 5055

#DIRECCIONES DE LOS DIFERENTES SOCKETS
ADDR = (HOST, PORT)
ADDR_NOTI = (HOST, PORT_NOTI)
ADDR_BROAD = (HOST, PORT_BROAD)
ADDR_CLIEN = (HOST, PORT_CLIEN)
ADDR_SEL = (HOST, PORT_SEL)
ADDR_BD = (HOST, PORT_BD)
TIMEOUT = 2

#ARREGLOS DE CONEXIONES CON EL SERVIDOR
conexiones_equipos_cliente = []
conexiones_equipos_cliente_mostrar = []
conexiones_equipos_cliente_secundario = []

conexiones_equipos_admin = []
conexiones_equipos_admin_notificacion  = []
conexiones_equipos_broadcast = []
conexiones_equipos_operacionesbd = []
conexiones_equipos_seleccion = []

#CONFIGURACIÓN INICIAL DE SOCKETS
def crear_sockets():
    try:
        global servidor
        global notificacion
        global broadcasting
        global operacionesbd
        global seleccion
        global cliente

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        broadcasting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        operacionesbd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        seleccion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_sockets():
    try:
        servidor.bind(ADDR)
        notificacion.bind(ADDR_NOTI)
        broadcasting.bind(ADDR_BROAD)
        operacionesbd.bind(ADDR_BD)
        cliente.bind(ADDR_CLIEN)
        seleccion.bind(ADDR_SEL)
        
        servidor.listen()
        notificacion.listen()
        broadcasting.listen()
        operacionesbd.listen()
        cliente.listen()
        seleccion.listen()

        print(f'HOST {HOST} corriendo en el puerto {PORT}')
        print(f'NOTIFICACION {HOST} corriendo en el puerto {PORT_NOTI}')
        print(f'BROADCASTING {HOST} corriendo en el puerto {PORT_BROAD}')
        print(f'USUARIO {HOST} corriendo en el puerto {PORT_CLIEN}')
        print(f'OPERACIONESBD {HOST} corriendo en el puerto {PORT_BD}')
        print(f'SELECCIÓN {HOST} corriendo en el puerto {PORT_SEL}')

        #CREACIÓN DE HILOS
        notificacion_thread = threading.Thread(target=aceptar_conexiones_notificacion)
        notificacion_thread.start()
        broadcasting_thread = threading.Thread(target=aceptar_conexiones_broadcast)
        broadcasting_thread.start()
        cliente_thread = threading.Thread(target=aceptar_conexiones_cliente)
        cliente_thread.start()
        operacionesbd_thread = threading.Thread(target=aceptar_conexiones_operacionesbd)
        operacionesbd_thread.start()
        seleccion_thread = threading.Thread(target=aceptar_conexiones_seleccion)
        seleccion_thread.start()

    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        servidor.close()
        notificacion.close()
        broadcasting.close()
        operacionesbd.close()
        seleccion.close()
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

        except:
            # conn.send('{"success": false, "msg": "Error al aceptar la conexión :("}'.encode())
            print('Error al aceptar la conexión :(')

def aceptar_conexiones_notificacion():
    #Cerrar todas las conexiones al iniciar el servidor
    for conexion_admin_notificacion in conexiones_equipos_admin_notificacion:
        conexion_admin_notificacion[0].close()

    del conexiones_equipos_admin_notificacion[:]

    while True:
        try:
            conn, addr = notificacion.accept()
            notificacion.setblocking(1)

            conexiones_equipos_admin_notificacion.append((conn, addr))
            
            panel_notificacon_thread = threading.Thread(target=panel_notificacion, args=(conn,addr))
            panel_notificacon_thread.start()
        except:
            print('Hubo un error al conectar con el canal de notificación')
            conn.send('{"success": False, "msg": "Error al aceptar la conexión en notificación :("}')
   
def aceptar_conexiones_broadcast():
    for conexion_broadcast in conexiones_equipos_broadcast:
        conexion_broadcast[0].close()

    del conexiones_equipos_broadcast[:]

    while True:
        try:
            conn, addr = broadcasting.accept()
            broadcasting.setblocking(1)

            conexiones_equipos_broadcast.append((conn, addr))

            conexiones_broadcast_thread = threading.Thread(target=panel_broadcasting, args=(conn, addr))
            conexiones_broadcast_thread.start()
        except:
            print('Hubo un error al conectar con el canal de broadcasting')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en broadcasting :("}')

def aceptar_conexiones_operacionesbd():
    while True:
        try:
            conn, addr = operacionesbd.accept()
            operacionesbd.setblocking(1)

            conexiones_equipos_operacionesbd.append((conn, addr))

            conexiones_operacionesbd_thread = threading.Thread(target=panel_operacionesbd, args=(conn, addr))
            conexiones_operacionesbd_thread.start()
        except:
            print('Hubo un error al conectar con el canal de operacionesbd')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión de operacionesbd :("}')

def aceptar_conexiones_cliente():
    for conexion_canal_cliente in conexiones_equipos_cliente_secundario:
        conexion_canal_cliente[0].close()

    del conexiones_equipos_cliente_secundario[:]

    while True:
        try:
            conn, addr = cliente.accept()
            cliente.setblocking(1)
            conexiones_equipos_cliente_secundario.append((conn, addr))
            panel_cliente_thread = threading.Thread(target=panel_cliente, args=(conn, addr))
            panel_cliente_thread.start()
        except:
            print('Hubo un error al conectar con el canal de cliente')
            borrar_conexion_usuarios(conn)
            conn.send('{"success": false, "msg": "Error al aceptar la conexión en cliente :("}'.encode())

def aceptar_conexiones_seleccion():
    for conexion_seleccion in conexiones_equipos_seleccion:
        conexion_seleccion[0].close()

    del conexiones_equipos_seleccion[:]

    while True:
        try:
            conn, addr = seleccion.accept()
            seleccion.setblocking(1)
            conexiones_equipos_seleccion.append((conn,addr))
            #abrir panel de conexión

        except:
            print('Hubo un error al conectar con el canal de selección')
            conn.send('{"success": false, "msg": "Error al aceptar la conexión con canal de selección :("}'.encode())

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
            print('Conexión con cliente :)')
            print(conexiones_equipos_cliente)
            conn.send(json.dumps({'success': True, 'msg': 'Conexión de cliente con servidor exitosa :)'}).encode())

            #Broadcast function
            broadcast()

        else:
            print('Conexión con administrador')
            equipo_admin = EquipoConectado(conn, addr, hostname, numero_serie)
            conexiones_equipos_admin.append(equipo_admin)

            administrador_thread = threading.Thread(target=panel_administrador, args=(conn,equipo_admin))
            administrador_thread.start()

            enviar_notificacion(f'Administrador {hostname} con la IP {addr} se ha conectado')

#PANELES DE CONTROL DE LAS RESPECTIVAS CONEXIONES
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
                            mensaje = f'Selección con el usuario {cliente_seleccionado.get_direccion()[0]}'
                            conn.send(json.dumps({'success': True, 'msg': mensaje}).encode())

                            manejar_operaciones_seleccion(cliente_seleccionado, conn)
                        else:
                            conn.send(json.dumps({'success': False, 'msg': 'La computadora ya esta seleccionada por alguien más, espere un momento...'}).encode())
                    else:
                        conn.send(json.dumps({'success': False, 'msg': 'Selección no válida, computadora inexistente :/'}).encode())

            elif operacion == 'salir':
                print('Administrador desconectado...')
                conn.send('Bye bye...'.encode())
                administrador_desconexion = borrar_administradores_activos(conn)
                enviar_notificacion(f'Administrador {administrador_desconexion.get_nombre_host()} desconectado')
                conn.close()
                break
            
            #Operaciones con la base de datos
            elif is_valid_json(operacion):
                respuesta_operacion = panel_base_datos(operacion)
                conn.send(respuesta_operacion.encode()) #Respetar el request response

            else:
                print('Comando no reconocido')
                conn.send('Comando no reconocido'.encode())

        except:
            print('Administrador desconectado espontáneamente...')
            administrador_desconexion = borrar_administradores_activos(conn)
            enviar_notificacion(f'Administrador {administrador_desconexion.get_nombre_host()} desconectado')
            conn.close()
            break

def panel_base_datos(instruccion): 
    instruccion = json.loads(instruccion)
    operacion = instruccion['operacion']
    print(instruccion)

    if instruccion['tabla'] == 'equipos':
        if operacion == 'insertar':
            data = instruccion['data']
            respuesta_operacion = EquiposConsultas(conexion()).insertar_equipo_computo(data[0], data[1], data[2], data[3])

            validar = json.loads(respuesta_operacion)

            if validar['success']:
                refrescar_tabla_equipos()
                broadcast()

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

def panel_cliente(conn, addr):
    print(f'Entró {addr} al panel de cliente.')
    conn.settimeout(TIMEOUT)

    while True:
        try:    
            conn.send('*'.encode())
            conn.recv(HEADER).decode(FORMAT)

        except ConnectionResetError:         
            print('Hubo un error al recibir el mensaje en el panel del cliente (ConnectionReset)')
            borrar_conexion_usuarios(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break

        except socket.timeout:
            print('Hubo un error al recibir el mensaje en el panel del cliente (Timeout)')
            borrar_conexion_usuarios(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break

        except:
            print('Hubo un error al recibir el mensaje en el panel del cliente (Exception)')
            borrar_conexion_usuarios(conn)
            enviar_notificacion(f'Usuario {addr} se ha desconectado')
            broadcast()
            conn.close()
            break
          
def panel_notificacion(conn, addr):
    while True:
        try:
            print('Entró al panel de notificación')
            conn.recv(HEADER).decode(FORMAT)
        except ConnectionResetError:
            ip = borrar_administradores_notificacion(addr)
            print(f'Desconexión del panel de notificación')
            conn.close()
            break

def panel_broadcasting(conn, addr):
    while True:
        try:
            print('Entró al panel de broadcasting')
            conn.recv(HEADER).decode(FORMAT)

        except ConnectionResetError:
            borrar_administradores_broadcasting(addr)
            print('Desconexión del canal de broadcasting')
            conn.close()
            break

def panel_operacionesbd(conn, addr):
    while True:
        try:
            print('Entró al panel de operacionesBD')
            conn.recv(HEADER).decode(FORMAT)

        except ConnectionResetError:
            borrar_administradores_operacionesbd(addr)
            print('Desconexión del canal de operacionesbd')
            conn.close()
            break

def panel_seleccion(conn, addr):
    while True:
        try:
            print('Entró al panel de selección')
            conn.recv(HEADER).decode(FORMAT)

        except ConnectionResetError:
            borrar_administradores_seleccion(addr)
            print('Desconexión del canal de selección')
            conn.close()
            break

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

    for i, conexion_equipo in enumerate(conexiones_equipos_cliente[:]):
        bandera = False
        #Mostrar solo aquellas conexiones que estan activas
        conexion_equipo.get_conexion().settimeout(1)
        try:
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
        posicion = operacion.replace('seleccionar', '')
        posicion = int(posicion)
        print(f'Posición: {posicion}')
        
        #Obtener el elemento del arreglo en esa posición
        objeto_cliente_seleccionado = conexiones_equipos_cliente[posicion]

        if objeto_cliente_seleccionado is None:
            return None
        
        #Checar si ya esta seleccionado o no 
        if objeto_cliente_seleccionado.get_seleccionado():
            return False

        #Marcar ese elemento del arreglo en específico como seleccionado
        conexiones_equipos_cliente[posicion].set_seleccionado(True)
        print(f'Nombre Host: {objeto_cliente_seleccionado.get_nombre_host()} Ha cambiado a True la selección')

        print(f'Conexión con el usuario {objeto_cliente_seleccionado.get_direccion()[0]}')
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
                #Buscar el elemento seleccionado en el arreglo y cambiar su selección

                for i in range(len(conexiones_equipos_cliente)):
                    print(conexiones_equipos_cliente[i].get_seleccionado())
                    if conexiones_equipos_cliente[i] == cliente_seleccionado:
                        index_seleccionado = conexiones_equipos_cliente.index(cliente_seleccionado)
                        conexiones_equipos_cliente[index_seleccionado].set_seleccionado(False)

                print('Cambio de selección a False')
                for i in range(len(conexiones_equipos_cliente)):
                    print(f'Nombre host: {conexiones_equipos_cliente[i].get_nombre_host()} Selección: {conexiones_equipos_cliente[i].get_seleccionado()}')

                conn_admin.send(json.dumps({'success': True, 'msg': 'Se realizó la salida de la consola con éxito'}).encode()) 
                break

            #Abrir consola en caso que se requiere usar manejo de la consola
            if operacion == 'consola':
                cliente_seleccionado.get_conexion().send(operacion.encode())
                manejar_consola_cliente(cliente_seleccionado, conn_admin)
                print('Se salio de la consola en el servidor')

            else:
                #Enviar la insturcción al cliente
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
                conn_cli.get_conexion().send(instruccion_admin.encode()) #Mandar mensaje de salida de la consola al cliente
                break

            #Enviar instrucción al cliente
            conn_cli.get_conexion().send(instruccion_admin.encode())
        except:
            conn_cli.get_conexion().send('salir'.encode()) #Mandar mensaje de salida de la consola al cliente
            break

#FUNCIONES DE BORRADO DE CONEXIONES
def borrar_administradores_activos(conn):
    for conexion_admin in conexiones_equipos_admin:
        if conexion_admin.get_conexion() == conn:
            index = conexiones_equipos_admin.index(conexion_admin)
            del conexiones_equipos_admin[index]
            print('[BORRADO DE ADMINISTRADORES ACTIVOS]')
            return conexion_admin
        
def borrar_administradores_notificacion(addr):
    for conexion_admin_notificacion in conexiones_equipos_admin_notificacion:
        if conexion_admin_notificacion[1] == addr:
            index = conexiones_equipos_admin_notificacion.index(conexion_admin_notificacion)
            del conexiones_equipos_admin_notificacion[index]
            print('[BORRADO DE CONEXIONES DE NOTIFICACIÓN]')
            return conexion_admin_notificacion[1] #Regresar IP
        
def borrar_administradores_broadcasting(addr):
    for conexion_broadcast in conexiones_equipos_broadcast:
        if conexion_broadcast[1] == addr:
            index = conexiones_equipos_broadcast.index(conexion_broadcast)
            del conexiones_equipos_broadcast[index]
            print('[BORRADO DE CONEXIONES BROADCASTING]')
            return conexion_broadcast
        
def borrar_administradores_operacionesbd(addr):
    for conexion_operacionbd in conexiones_equipos_operacionesbd:
        if conexion_operacionbd[1] == addr:
            index = conexiones_equipos_operacionesbd.index(conexion_operacionbd)
            del conexiones_equipos_operacionesbd[index]
            print('[BORRADO DE CONEXIONES OPERACIONESBD]')
            return conexion_operacionbd

def borrar_administradores_seleccion(addr):
    for conexion_seleccion in conexiones_equipos_seleccion:
        if conexion_seleccion[1] == addr:
            index = conexiones_equipos_operacionesbd.index(conexion_seleccion)
            del conexiones_equipos_operacionesbd[index]
            print('[BORRADO DE CONEXIONES SELECCIÓN]')
            return conexion_seleccion   

def borrar_conexion_usuarios(conn):    
    for conexion_equipo in conexiones_equipos_cliente[:]:
        if conexion_equipo.get_conexion() == conn:
            index = conexiones_equipos_cliente.index(conexion_equipo)
            del conexiones_equipos_cliente[index]

    for conexion_equipo_secundario in conexiones_equipos_cliente_secundario[:]:
        if conexion_equipo_secundario[0] == conn:
            index = conexiones_equipos_cliente_secundario.index(conexion_equipo_secundario)
            del conexiones_equipos_cliente_secundario[index]

    print('[BORRADO DE CONEXIONES CLIENTE PRINCIPAL]')

#FUNCIONALIDADES BROADCAST QUE SE ENVIAN A TODOS LOS ADMINISTRADORES
def enviar_notificacion(mensaje):
    print('[NOTIFICACIÓN]')
    print(f'Mensaje enviado: {mensaje}')
    try:
        if conexiones_equipos_admin:
            for conexion_admin_notificacion in conexiones_equipos_admin_notificacion: 
                conexion_admin_notificacion[0].send(f'{mensaje}'.encode())
    except:
        print('No se enviaron algunos de los mensajes')

def broadcast():
    print('[BROADCASTING]')
    equipos_activos_inactivos = listar_equipos()
    try:
        if conexiones_equipos_admin:
            for conexion_broadcast in conexiones_equipos_broadcast: 
                conexion_broadcast[0].send(equipos_activos_inactivos.encode())
    except:
        print('Error al enviar el mensaje de broadcast')
        
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

    try:
        if conexiones_equipos_admin:
            for conexion_operacionesbd in conexiones_equipos_operacionesbd:
                conexion_operacionesbd[0].send(json.dumps(respuesta).encode())
    except:
        print('Error al refrescar las tablas de los equipos')

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

def enviar_seleccion(id):
    try:
        if conexiones_equipos_admin:
            for conexion_seleccion in conexiones_equipos_seleccion:
                conexion_seleccion[0].send(id.encode())

    except:
        print('Hubo un error al enviar quien se ha seleccionado')

def enviar_mensaje_cliente(conn):
    try:
        conn.send('*'.encode())
        print('Se envio el mensaje al cliente')
        respuesta = conn.recv(HEADER).decode(FORMAT)
        print('Se recibio el mensaje del cliente')

        return {'success': True, 'msg': 'Cliente seleccionado activo'}
    except:
        borrar_conexion_usuarios(conn)
        return {'success': True, 'msg': 'Cliente seleccionado inactivo'}

atexit.register(cerrar)
crear_sockets()
vincular_sockets()
aceptar_conexiones()
