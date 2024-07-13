import os
import subprocess
from .utils import ANSI_COLOR_YELLOW

def show_memory_usage():
    print(f"{ANSI_COLOR_YELLOW}\nMemory Usage:")
    if os.name == 'posix':  # Linux
        command = "free -m"
        memory_info = subprocess.check_output(command, shell=True, text=True).strip()
        print(memory_info)
