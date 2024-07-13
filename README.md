# Monitoring

![GitHub](https://img.shields.io/github/license/GLTdotNS/MONITORING)

## Overview

Monitoring is a command-line interface (CLI) tool designed for system monitoring and management on Linux-based operating systems. It provides various functionalities such as CPU, memory, and disk usage monitoring, network traffic analysis, process management, system information retrieval, and system control operations like executing commands, restarting, and shutting down.

## Architecture

The project is structured into modules, each focusing on specific system monitoring and management tasks:

- **main.py**: Contains the main program loop and menu system for user interaction.
  
- **modules/**
  - **cpu.py**: Functions for displaying CPU usage.
  - **memory.py**: Functions for displaying memory usage.
  - **disk.py**: Functions for displaying disk usage.
  - **network.py**: Functions for displaying network traffic and interfaces.
  - **processes.py**: Functions for listing current processes.
  - **system.py**: Functions for displaying system uptime, load average, and information.
  - **manage.py**: Functions for managing the system, including executing commands, restarting, and shutting down.
  - **additional.py**: Additional functions for displaying disk usage for specific directories, GPU information, and monitoring system logs.
  - **utils.py**: Utility functions and ANSI color constants used for formatting output.

## Features

- **System Monitoring**:
  - CPU, memory, and disk usage.
  - Network traffic and interfaces.
  - Current running processes.
  - System uptime, load average, and general information.

- **System Management**:
  - Execute custom commands.
  - Restart and shutdown the system.

- **Additional Features**:
  - Monitor disk usage for specific directories.
  - Display GPU information.
  - Monitor system logs.

## Installation

### Prerequisites

- Python 3.x
- Linux-based operating system (tested on Ubuntu)

### Clone

Clone the repository to your local machine:

git clone https://github.com/GLTdotNS/Monitoring.git
cd Monitoring



Usage
Navigate to the project directory and run main.py:

``bash
Copy code
python main.py
Follow the on-screen instructions to navigate through different options and sub-options.

Contributing
Contributions are welcome! Please fork the repository and submit pull requests.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgments
Hat tip to anyone whose code was used.


Project Link: https://github.com/GLTdotNS/Monitoring

This text incorporates the structure and content from the previous README.md file and includes standard sections such as Overview, Architecture, Features, Installation, Usage, Contributing, License, Acknowledgments, and Contact. If you need any adjustments or further details, feel free to let me know!









# MONITORING
# MONITORING
