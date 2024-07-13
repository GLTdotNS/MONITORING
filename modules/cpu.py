import os
import subprocess
from .utils import ANSI_COLOR_GREEN

def show_cpu_usage():
    print(f"{ANSI_COLOR_GREEN}\nCPU Usage:")
    if os.name == 'posix':  # Linux
        command = "top -bn1 | grep 'Cpu(s)'"
        cpu_info = subprocess.check_output(command, shell=True, text=True).strip()
        print(cpu_info)
