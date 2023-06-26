import subprocess
import os

def abrir_consola_ejecutar_script():
    # Open a new console window and execute the script
    script_path = f'{os.getcwd()}/ui/utils/manejar_consola.py'
    subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True)

