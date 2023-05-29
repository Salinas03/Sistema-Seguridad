import socket

FORMAT = "utf-8"
HEADER = 20480
IP = '165.22.15.159'
PORT = 5050
ADDR = (IP, PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR) #Linea de bloqueo de código

#Mensaje de primer conexión con el servidor
respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

#Se envia el hostname de la computadora o un identificador
cliente.send(socket.gethostname().encode())

#Mensaje de segunda conexión con el servidor
#Aqui tanto se puede conectar como no se puede conectar
respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)
print('Esperando instrucciones...')

while True:
    respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
    print(respuesta_servidor)
