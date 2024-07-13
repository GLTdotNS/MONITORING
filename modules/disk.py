import os
import subprocess
from .utils import ANSI_COLOR_BLUE

def show_disk_usage():
    print(f"{ANSI_COLOR_BLUE}\nDisk Usage:")
    if os.name == 'posix':  # Linux
        command = "df -h"
        disk_info = subprocess.check_output(command, shell=True, text=True).strip()
        print(disk_info)
