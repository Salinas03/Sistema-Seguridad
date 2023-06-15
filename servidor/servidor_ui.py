import socket
import threading
import json
from base_datos.conexion import conexion
from base_datos.equipos_consultas import EquiposConsultas
from base_datos.propietarios_consultas import PropietariosConsultas
from clases.persona import EquipoConectado
from clases.validar_json import is_valid_json

#VARIABLES GLOBALES PARA LA CONFIGURACIÓN DE SOCKETS
FORMAT = 'utf-8'
HEADER = 20480
HOST = socket.gethostbyname(socket.gethostname())
# HOST = '165.22.15.159'

#PUERTOS DE LOS DIFERENTES SOCKETS
PORT = 5050
PORT_NOTI = 5051
PORT_BROAD = 5052
PORT_USUA = 5053

#DIRECCIONES DE LOS DIFERENTES SOCKETS
ADDR = (HOST, PORT)
ADDR_NOTI = (HOST, PORT_NOTI)
ADDR_BROAD = (HOST, PORT_BROAD)
ADDR_USUA = (HOST, PORT_USUA)

#ARREGLOS DE CONEXIONES CON EL SERVIDOR
conexiones_equipos_cliente = []
conexiones_equipos_cliente_mostrar = []

conexiones_equipos_admin = []
conexiones_equipos_admin_notificacion  = []

conexiones_equipos_broadcast = []

#CONFIGURACIÓN INICIAL DE SOCKETS TODO
def crear_sockets():
    try:
        global servidor
        global notificacion
        global broadcasting
        global usuario

        servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        notificacion = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        broadcasting = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        usuario = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    except socket.error as err:
        print(f'Error a la hora de crear el socket... /n {err}')

def vincular_sockets():
    try:
        servidor.bind(ADDR)
        notificacion.bind(ADDR_NOTI)
        broadcasting.bind(ADDR_BROAD)
        usuario.bind(ADDR_USUA)
        
        servidor.listen()
        notificacion.listen()
        broadcasting.listen()
        usuario.listen()

        print(f'HOST {HOST} corriendo en el puerto {PORT}')
        print(f'NOTIFICACION {HOST} corriendo en el puerto {PORT_NOTI}')
        print(f'BROADCASTING {HOST} corriendo en el puerto {PORT_BROAD}')
        print(f'USUARIO {HOST} corriendo en el puero {PORT_USUA}')

        notificacion_thread = threading.Thread(target=aceptar_conexiones_notificacion)
        notificacion_thread.start()
        broadcasting_thread = threading.Thread(target=aceptar_conexiones_broadcast)
        broadcasting_thread.start()

    except socket.error as err:
        print(f'Error al enlazar el socket... /n {err}')
        print('Intentando denuevo...')
        servidor.close()
        notificacion.close()
        broadcasting.close()
        # vincular_socket()

#ACEPTACIÓN DE CONEXIONES TODO
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

            print(f'Conexión con socket de notificaciones: {addr[0]}')

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
            conexiones_equipos_broadcast.append((conn, addr))

            print(f'Conexión con socket de broadcast {addr}')

        except:
            print('Hubo un error al conectar con el canal de broadcasting')
            conn.send('{"success": False, "msg": "Error al aceptar la conexión en broadcasting :("}')

#GUARDAR CONEXIONES DEL SOCKET PRINCIPAL TODO
def guardar_conexiones(conn, addr, hostname, numero_serie):
    #Verificar si el usuario o administrador esta registrado en la base de datos
    resultado = json.loads(EquiposConsultas(conexion()).obtener_equipo_por_nombre_numero_serie(hostname, numero_serie))
    print('Resultado de consulta de obtener equipo por nombre y número de serie')
    print(resultado)

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
        #Verificar si el dispositvo que se esta conectando es un administrador o un usuario dependiendo de la tabla SQL
        resultado = json.loads(EquiposConsultas(conexion()).obtener_equipo_admin_por_nombre_numero_serie(hostname, numero_serie))

        resultado = resultado['data']
        if resultado:
            resultado = resultado[0]

        if not resultado:
            equipo_cliente = EquipoConectado(conn, addr, hostname, numero_serie)
            conexiones_equipos_cliente.append(equipo_cliente)
            print('Conexión con cliente :)')
            conn.send('{"success": true, "msg": "Conexión con servidor exitosa :)"}'.encode())

            usuario_thread = threading.Thread(target=panel_usuario, args=(conn, equipo_cliente))
            usuario_thread.start()

            enviar_notificacion(f'Usuario {hostname} con la IP {addr} se ha conectado')

        else:
            print('Conexión con administrador')
            equipo_admin = EquipoConectado(conn, addr, hostname, numero_serie)
            conexiones_equipos_admin.append(equipo_admin)

            administrador_thread = threading.Thread(target=panel_administrador, args=(conn,equipo_admin))
            administrador_thread.start()

            enviar_notificacion(f'Administrador {hostname} con la IP {addr} se ha conectado')

#PANELES DE CONTROL DE LAS RESPECTIVAS CONEXIONES TODO
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
                print('Operación listar')
                equipos = listar_equipos()
                conn.send(equipos.encode())

            elif 'seleccionar' in operacion:
                print('Operación seleccionar')
                if not conexiones_equipos_cliente:
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
                enviar_notificacion(f'Administrador {administrador_desconexion.get_nombre_host()} desconectado')
                conn.close()
                break
            
            #Operaciones con la base de datos
            elif is_valid_json(operacion):
                print('Petición para base de datos')
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

    if instruccion['tabla'] == 'equipos':
        if operacion == 'insertar':
            data = instruccion['data']
            respuesta_operacion = EquiposConsultas(conexion()).insertar_equipo_computo(data[0], data[1], data[2], data[3])
            if respuesta_operacion['success']:
                broadcast()

            return respuesta_operacion
        
        elif operacion == 'actualizar':
            respuesta_operacion = EquiposConsultas(conexion()).actualizar_equipo_computo(instruccion['id'], instruccion['data'])
            return respuesta_operacion
        
        elif operacion == 'borrar':
            respuesta_operacion = EquiposConsultas(conexion()).borrar_equipo_computo(instruccion['id'])

        elif operacion == 'obtener_equipos_computo':
            return EquiposConsultas(conexion()).obtener_equipos_computo()

        elif operacion == 'obtener_equipo_computo_por_id':
            return EquiposConsultas(conexion()).obtener_equipo_computo_por_id(instruccion['id'])
        
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
            return respuesta_operacion

        elif operacion == 'actualizar':
            respuesta_operacion = PropietariosConsultas(conexion()).actualizar_propietario(instruccion['id'], instruccion['data'])
            return respuesta_operacion

        elif operacion == 'borrar':
            respuesta_operacion = PropietariosConsultas(conexion()).eliminar_propietario(instruccion['id'])
            return respuesta_operacion

        elif operacion == 'obtener_propietarios':
            respuesta_operacion = PropietariosConsultas(conexion()).obtener_propietarios()
            return respuesta_operacion

        elif operacion == 'login':
            data = instruccion['data']
            respuesta_operacion = PropietariosConsultas(conexion()).obtener_propietario(data[0], data[1])
            return respuesta_operacion

        elif operacion == 'obtener_propietario_id':
            respuesta_operacion = PropietariosConsultas(conexion()).seleccionar_propietario_id(instruccion['id'])
        
def panel_usuario(conn, usuario):
    while True:
        try:
            print(f'Entró {usuario.get_nombre_host()} al panel de usuario.')
            #FALLA DE LÓGICA PARA EL RECIBIMIENTO DE MENSAJE TODO -----------------------------------------------------------------------------------------------
            respuesta_usuario = conn.recv(HEADER).decode(FORMAT)
            if respuesta_usuario == 'SALIR':
                borrar_conexion_usuarios(conn)
                enviar_notificacion(f'Usuario {usuario.get_nombre_host()} se ha desconectado')
                conn.close()
                break

        except:         
            borrar_conexion_usuarios(conn)
            enviar_notificacion(f'Usuario {usuario.get_nombre_host()} se ha desconectado')
            conn.close()
            break
          
def panel_notificacion(conn, addr):
    while True:
        try:
            # print('Entrando al panel')
            respuesta_usuario = conn.recv(HEADER).decode(FORMAT)
            if respuesta_usuario == 'SALIR':
                print('Desconexión con el panel de notificación')
                ip = borrar_administradores_notificacion(addr)
                print(f'Administrador con la IP {ip} desconcectado de notificación')
                conn.close()
                break
        except:
            ip = borrar_administradores_notificacion(addr)
            print(f'Desconexión del equipo con la IP {ip}')
            conn.close()
            break

#OPERACIONES QUE PUEDEN REALIZAR LOS ADMINISTRADORES CON LOS EQUIPOS TODO
def listar_equipos():
    #Se tienen que listar los equipos que estan activos 
    #Pero en la UI se tienen que ver tanto activos como inactivos

    #Copiar los equipos de cómputo a la variable de equipos inactivos
    equipos_computo = json.loads(EquiposConsultas(conexion()).obtener_equipos_computo_clientes())
    equipos_computo = equipos_computo['data']
    equipos_inactivos = equipos_computo[:]

    if conexiones_equipos_cliente_mostrar:
        del conexiones_equipos_cliente_mostrar[:]

    #Crar cadena de texto de los equipos activos e inactivos
    for i,conexion_equipo in enumerate(conexiones_equipos_cliente):
        #Mostrar solo aquellas conexiones que estan activas
        try:
            conexion_equipo.get_conexion().send(' '.encode())
            #FALLA DE LÓGICA PARA EL RECIBIMIENTO DE MENSAJE TODO -----------------------------------------------------------------------------------------------
            conexion_equipo.get_conexion().recv(HEADER)
            print('Después de recibir nada')
        except:
            #Las conexiones que no esten activas serán eliminadas
            #El arreglo se recorre al borrar estos elementos (podría estar mal)
            del conexion_equipo[i]
            continue
            
        ip_cliente = conexion_equipo.get_direccion()[0]

        #Obtener los equipos de cómputo inactivos y activos
        for x, equipo_computo in enumerate(equipos_computo):

            if conexion_equipo.get_nombre_host() == equipo_computo[1]:
                equipos_inactivos[x] = None
                equipo = list(equipo_computo)

                #Agregar la IP al cliente activo para mostrar
                equipo.append(ip_cliente)
                conexiones_equipos_cliente_mostrar.append(equipo)

    equipos = [equipos_inactivos, conexiones_equipos_cliente_mostrar]
    equipos = json.dumps(equipos)
    print('Listado realizado')
    return equipos

def conectar_con_equipo(operacion):
    
    try: 
        posicion = operacion.replace('seleccionar', '')
        posicion = int(posicion)
        print(f'Posición: {posicion}')
        objeto_cliente_activo = conexiones_equipos_cliente[posicion]

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

#FUNCIONES DE BORRADO DE CONEXIONES TODO
def borrar_administradores_activos(conn):
    #Borrar administrador del arreglo
    for conexion_admin in conexiones_equipos_admin:
        if conexion_admin.get_conexion() == conn:
            index = conexiones_equipos_admin.index(conexion_admin)
            del conexiones_equipos_admin[index]
            return conexion_admin

def borrar_administradores_notificacion(addr):
    #Borrar arreglo notificación
    for conexion_admin_notificacion in conexiones_equipos_admin_notificacion:
        if conexion_admin_notificacion[1] == addr:
            index = conexiones_equipos_admin_notificacion.index(conexion_admin_notificacion)
            del conexiones_equipos_admin_notificacion[index]
            return notificacion[1] #Regresar IP

def borrar_conexion_usuarios(conn):
    #Borrar arreglo notificación
    for conexion_equipo in conexiones_equipos_cliente:
        if conexion_equipo.get_conexion() == conn:
            index = conexiones_equipos_cliente.index(conexion_equipo)
            del conexiones_equipos_cliente[index]
            return conexion_equipo #Regresar IP

#FUNCIONALIDADES BROADCAST QUE SE ENVIAN A TODOS LOS ADMINISTRADORES TODO
def enviar_notificacion(mensaje):
    try:
        if conexiones_equipos_admin:
            for conexion_admin_notificacion in conexiones_equipos_admin_notificacion: 
                conexion_admin_notificacion[0].send(f'{mensaje}'.encode())
    except:
        print('No se enviaron algunos de los mensajes')

def broadcast():
    try:
        if conexiones_equipos_admin:
            for conexion_broadcast in conexiones_equipos_broadcast: 
                conexion_broadcast[0].send('REFRESH'.encode())
    except:
        print('Fukin shit')

crear_sockets()
vincular_sockets()
aceptar_conexiones()
