import subprocess
import os

def open_console_and_execute_script(script_path):
    # Open a new console window and execute the script
    subprocess.Popen(['start', 'cmd', '/k', 'python', script_path], shell=True)

# Path to the script that says "Hello, World!"
hello_script_path = f'{os.getcwd()}/servidor/testing/hello_world.py'

# Call the function to open console and execute the script
open_console_and_execute_script(hello_script_path)
