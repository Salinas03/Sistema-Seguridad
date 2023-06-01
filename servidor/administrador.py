import socket
import threading
from queue import Queue

# 165.22.15.159
#Configuración
FORMAT = "utf-8"
HEADER = 20480
IP = '165.22.15.159'
PORT = 5050
ADDR = (IP, PORT)

#Configuración de variables para los hilos
NUMERO_HILOS = 2
NUMERO_TAREAS = [1,2]
queue = Queue()

administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
administrador.connect(ADDR) #Linea de bloqueo de código

#Mensaje de primer conexión con el servidor (conexión temporal)
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

#Se envia el hostname de la computadora o un identificador
administrador.send(socket.gethostname().encode())

#Mensaje de segunda conexión con el servidor
#Aqui tanto se puede conectar como no se puede conectar
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

#PANEL DE CONTROL DEL ADMINISTRADOR, 
# 1.-RECIBIR PROMPT
# 2.-ENVIAR INPUT
# 3.-ESPERAR RESPUESA
# 4.- HACER ALGO CON LA RESPUESTA
def operaciones():
    while True:
        #Enviar la operación
        try: 
            entrada_administrador = input(f'Ingrese la operación que desea realizar: \n{administrador.recv(HEADER).decode(FORMAT)}')
            administrador.send(entrada_administrador.encode())        

            #Recibir lo que el servidor obtenga y mostrarlo
            #ESPERANDO RESPUESTA
            respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
            
            print(respuesta_servidor)

            if 'Bye' in respuesta_servidor:
                administrador.close()
                break
        
        except:
            print('Hubo un error al conectar con el servidor :(')
            administrador.close()
            break

def escuchar_conexiones(mensaje_notificacion):
    while True:
        try:
            print('Este es el mensaje de las notificaciones')
            print(mensaje_notificacion)
        except:
            print('Hubo un error al conectar con el servidor (escuchar conexiones) :(')
            administrador.close()
            break

def crear_hilos():
    for _ in range(NUMERO_HILOS):
        thread = threading.Thread(target=definir_tareas)
        thread.daemon = True
        thread.start()

def crear_tareas():
    #Crear la cola de tareas
    for tarea in NUMERO_TAREAS:
        queue.put(tarea)

    #Iniciar la cola de tareas
    queue.join()

def definir_tareas():
    while True:
        tarea = queue.get()
        if tarea == 1:
            operaciones()

        if tarea == 2:
            escuchar_conexiones()

        queue.task_done()

if 'denegada' not in respuesta_servidor: 
    operaciones()
    # crear_hilos()
    # crear_tareas()