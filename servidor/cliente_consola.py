import socket
import os
from clases import numero_serie

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

#Se envia el hostname de la computadora y el número de serie
numero_de_serie = numero_serie.obtener_numero_serie()
cliente.send(socket.gethostname().encode())
cliente.send(numero_de_serie.encode())

#Mensaje de segunda conexión con el servidor
#Aqui tanto se puede conectar como no se puede conectar
respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
print(respuesta_servidor)

if 'denegada' in respuesta_servidor:
    cliente.close()

else:
    print('Esperando instrucciones...')

    while True:
        try:
            respuesta_servidor = cliente.recv(HEADER).decode(FORMAT)
            if respuesta_servidor == ' ':
                cliente.send(' '.encode())

            else:
                try:
                    print(f'Instrucción a aplicar {respuesta_servidor}')

                    if respuesta_servidor == 'apagar' or respuesta_servidor == 'bloquear':
                        os.system(f'{os.getcwd()}/comandos/{respuesta_servidor}.bat')

                    elif respuesta_servidor == 'cmd':   
                        #Realizar proceso del cmd
                        print('Abrir consola')
                        pass
                    
                    else:
                        print('Instruccion no encontrada')

                except:
                    print('Hubo un error al aplicar la instrucción aplicada')
        except:
            print('Ocurrió un error')
            cliente.send('SALIR'.encode())
            cliente.close()
            break