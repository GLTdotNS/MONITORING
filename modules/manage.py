import os
import subprocess
from .utils import ANSI_COLOR_RED

def run_command():
    command = input(f"{ANSI_COLOR_RED}\nEnter command to execute: ")
    try:
        output = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(output.stdout)
    except subprocess.CalledProcessError as e:
        print(f"{ANSI_COLOR_RED}Error executing command:", e)

def restart_system():
    if os.name == 'posix':  # Linux
        try:
            subprocess.run("sudo shutdown -r now", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{ANSI_COLOR_RED}Error restarting system:", e)

def shutdown_system():
    if os.name == 'posix':  # Linux
        try:
            subprocess.run("sudo shutdown -h now", shell=True, check=True)
        except subprocess.CalledProcessError as e:
            print(f"{ANSI_COLOR_RED}Error shutting down system:", e)
