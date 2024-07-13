import os
import subprocess
from .utils import ANSI_COLOR_YELLOW, ANSI_COLOR_RED

def show_system_uptime():
    print(f"{ANSI_COLOR_YELLOW}\nSystem Uptime:")
    if os.name == 'posix':  # Linux
        try:
            uptime_info = subprocess.check_output("uptime", shell=True, text=True).strip()
            print(uptime_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving system uptime information.")

def show_system_load_average():
    print(f"{ANSI_COLOR_YELLOW}\nSystem Load Average:")
    if os.name == 'posix':  # Linux
        try:
            load_avg_info = subprocess.check_output("uptime", shell=True, text=True).strip()
            print(load_avg_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving system load average information.")

def show_system_information():
    print(f"{ANSI_COLOR_MAGENTA}\nSystem Information:")
    if os.name == 'posix':  # Linux
        try:
            sys_info = subprocess.check_output("uname -a", shell=True, text=True).strip()
            print(sys_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving system information.")
