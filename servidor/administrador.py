import socket

FORMAT = "utf-8"
HEADER = 20480
IP = '165.22.15.159'
PORT = 5050
ADDR = (IP, PORT)

administrador = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
administrador.connect(ADDR) #Linea de bloqueo de código

#Mensaje de primer conexión con el servidor
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

#Se envia el hostname de la computadora o un identificador
administrador.send(socket.gethostname().encode())

#Mensaje de segunda conexión con el servidor
#Aqui tanto se puede conectar como no se puede conectar
respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

while True:
    #Enviar la operación
    entrada_administrador = input('Ingrese la operación que desea realizar: \n>')
    administrador.send(entrada_administrador.encode())

    #Recibir lo que el servidor obtenga y mostrarlo
    respuesta_servidor = administrador.recv(HEADER).decode(FORMAT)
    print(respuesta_servidor)


    