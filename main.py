from modules.cpu import show_cpu_usage
from modules.memory import show_memory_usage
from modules.disk import show_disk_usage
from modules.network import show_network_traffic, show_network_interfaces
from modules.processes import list_processes
from modules.system import show_system_uptime, show_system_load_average, show_system_information
from modules.manage import run_command, restart_system, shutdown_system
from modules.additional import show_directory_disk_usage, show_gpu_information, monitor_system_logs
from modules.utils import ANSI_COLOR_GREEN, ANSI_COLOR_CYAN, ANSI_COLOR_MAGENTA, ANSI_COLOR_YELLOW, ANSI_COLOR_RED, \
    ANSI_COLOR_BLUE, ANSI_COLOR_RESET
import os


def print_menu():
    print("\n=== System Monitoring and Management ===")
    print(f"{ANSI_COLOR_GREEN}1. Show Usage:")
    print(f"  a. CPU Usage")
    print(f"  b. Memory Usage")
    print(f"  c. Disk Usage")
    print(f"{ANSI_COLOR_CYAN}2. Network:")
    print(f"  a. Show Network Traffic")
    print(f"  b. Show Network Interfaces")
    print(f"{ANSI_COLOR_MAGENTA}3. Processes:")
    print(f"  a. List Current Processes")
    print(f"{ANSI_COLOR_YELLOW}4. System:")
    print(f"  a. Show System Uptime")
    print(f"  b. Show System Load Average")
    print(f"  c. Show System Information")
    print(f"{ANSI_COLOR_RED}5. Manage:")
    print(f"  a. Execute Command")
    print(f"  b. Manage System (Restart/Shutdown)")
    print(f"{ANSI_COLOR_BLUE}6. Additional:")
    print(f"  a. Disk Space Usage for Directory")
    print(f"  b. GPU Information")
    print(f"  c. Monitor System Logs")
    print(f"{ANSI_COLOR_RESET}7. Exit")


def main():
    while True:
        print_menu()
        choice = input(f"{ANSI_COLOR_GREEN}Select an option: ")

        if choice == '1':
            sub_choice = input(f"{ANSI_COLOR_GREEN}Select sub-option (a/b/c): ")
            if sub_choice == 'a':
                show_cpu_usage()
            elif sub_choice == 'b':
                show_memory_usage()
            elif sub_choice == 'c':
                show_disk_usage()
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '2':
            sub_choice = input(f"{ANSI_COLOR_CYAN}Select sub-option (a/b): ")
            if sub_choice == 'a':
                show_network_traffic()
            elif sub_choice == 'b':
                show_network_interfaces()
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '3':
            sub_choice = input(f"{ANSI_COLOR_MAGENTA}Select sub-option (a): ")
            if sub_choice == 'a':
                list_processes()
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '4':
            sub_choice = input(f"{ANSI_COLOR_YELLOW}Select sub-option (a/b/c): ")
            if sub_choice == 'a':
                show_system_uptime()
            elif sub_choice == 'b':
                show_system_load_average()
            elif sub_choice == 'c':
                show_system_information()
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '5':
            sub_choice = input(f"{ANSI_COLOR_RED}Select sub-option (a/b): ")
            if sub_choice == 'a':
                run_command()
            elif sub_choice == 'b':
                while True:
                    print(f"{ANSI_COLOR_RED}\nSystem Management Options:")
                    print(f"{ANSI_COLOR_BLUE}a. Restart System")
                    print(f"b. Shutdown System")
                    print(f"{ANSI_COLOR_RESET}c. Back to Main Menu")
                    option = input(f"{ANSI_COLOR_RED}Select an option (a/b/c): ")
                    if option.lower() == 'a':
                        restart_system()
                    elif option.lower() == 'b':
                        shutdown_system()
                    elif option.lower() == 'c':
                        break
                    else:
                        print(f"{ANSI_COLOR_RED}Invalid option. Please try again.")
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '6':
            sub_choice = input(f"{ANSI_COLOR_BLUE}Select sub-option (a/b/c): ")
            if sub_choice == 'a':
                show_directory_disk_usage()
            elif sub_choice == 'b':
                show_gpu_information()
            elif sub_choice == 'c':
                monitor_system_logs()
            else:
                print(f"{ANSI_COLOR_RED}Invalid sub-option.")

        elif choice == '7':
            print(f"{ANSI_COLOR_RED}Exiting...")
            break

        else:
            print(f"{ANSI_COLOR_RED}Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
