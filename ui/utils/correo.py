import string
import secrets
import yagmail

def generar_codigo_verificacion():
    longitud = 5
    caracteres = string.digits  # solo dígitos

    codigo = ''.join(secrets.choice(caracteres) for _ in range(longitud))
    return codigo
    
def enviar_correo(correo):

    codigo_verificacion = generar_codigo_verificacion()

    email = 'diegosalinasvazquez@gmail.com'
    contrasena = 'efjkgppzrikponuo'

    yag = yagmail.SMTP(user=email, password=contrasena)

    destinatario = [correo]
    print(destinatario)
    asunto = ['Código de verificación']
    mensaje = ['Ingresa este código al panel correspondiente: ' + codigo_verificacion]

    try:
        yag.send(destinatario,asunto,mensaje)
        print('Envio correcto del codigo')
        return codigo_verificacion
    
    except:
        print('Hubo un fallo al enviar el codigo')
        return None
    
def verificacion(codigo_verificacion_txt, codigo):

    if codigo_verificacion_txt == codigo:return True
    else: return False