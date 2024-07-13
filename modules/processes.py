import os
import subprocess
from .utils import ANSI_COLOR_MAGENTA

def list_processes():
    print(f"{ANSI_COLOR_MAGENTA}\nCurrent Processes:")
    if os.name == 'posix':  # Linux
        command = "ps -eo pid,comm,user"
        process_info = subprocess.check_output(command, shell=True, text=True).strip()
        print(process_info)
