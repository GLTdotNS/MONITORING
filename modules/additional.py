import os
import subprocess
from .utils import ANSI_COLOR_BLUE, ANSI_COLOR_RED

def show_directory_disk_usage():
    directory = input(f"{ANSI_COLOR_BLUE}\nEnter directory path: ")
    if os.path.exists(directory):
        command = f"du -sh {directory}"
        try:
            disk_usage_info = subprocess.check_output(command, shell=True, text=True).strip()
            print(f"{ANSI_COLOR_BLUE}\nDisk Usage for {directory}:")
            print(disk_usage_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving disk usage information.")
    else:
        print(f"{ANSI_COLOR_RED}Directory does not exist.")

def show_gpu_information():
    print(f"{ANSI_COLOR_MAGENTA}\nGPU Information:")
    if os.name == 'posix':  # Linux
        command = "lspci | grep -i vga"
        try:
            gpu_info = subprocess.check_output(command, shell=True, text=True).strip()
            print(gpu_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving GPU information.")

def monitor_system_logs():
    print(f"{ANSI_COLOR_YELLOW}\nSystem Logs:")
    if os.name == 'posix':  # Linux
        command = "tail -n 20 /var/log/syslog"
        try:
            logs_info = subprocess.check_output(command, shell=True, text=True).strip()
            print(logs_info)
        except subprocess.CalledProcessError:
            print(f"{ANSI_COLOR_RED}Error retrieving system logs.")
