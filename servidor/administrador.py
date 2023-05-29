import socket

FORMAT = "utf-8"
HEADER = 20480
IP = socket.gethostbyname(socket.gethostname())
PORT = 5050
ADDR = (IP, PORT)

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(ADDR) #Linea de bloqueo de código

#Mensaje de primer conexión con el servidor
respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

while True:

    #Enviar la operación
    entrada_cliente = input('Ingrese la operación que desea realizar')
    cliente.send(entrada_cliente.encode())

    #Recibir lo que el servidor obtenga y mostrarlo


    