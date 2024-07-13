import os
import subprocess
from .utils import ANSI_COLOR_CYAN, ANSI_COLOR_RED

def show_network_traffic():
    print(f"{ANSI_COLOR_CYAN}\nNetwork Traffic:")
    if os.name == 'posix':  # Linux
        command = "ifconfig"
        try:
            net_info = subprocess.check_output(command, shell=True, text=True).strip()
            print(net_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving network traffic information.")

def show_network_interfaces():
    print(f"{ANSI_COLOR_CYAN}\nNetwork Interfaces:")
    if os.name == 'posix':  # Linux
        command = "ip addr show"
        try:
            net_interfaces_info = subprocess.check_output(command, shell=True, text=True).strip()
            print(net_interfaces_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving network interfaces information.")
