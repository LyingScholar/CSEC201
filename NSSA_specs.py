#!/usr/bin/env python3

import os
import platform
import subprocess
import socket
import datetime

# Michael B.
# 2024-09-22

def clear_terminal():
    try:
        os.system('clear')
    except SyntaxError:
        os.system('cls')


def execute_command(command):
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout.strip()


def get_system_info():
    
    info = {}
    
    info['date'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    info['hostname'] = socket.gethostname()
    info['domain_suffix'] = execute_command('hostname -d')
    info['ipv4_address'] = execute_command("hostname -I | awk '{print $1}'")
    info['default_gateway'] = execute_command("ip route | grep default | awk '{print $3}'")
    info['network_mask'] = execute_command("ifconfig | grep -w inet | awk '{print $4}'")
    info['dns_servers'] = execute_command("awk '/^nameserver/ {print $2}' /etc/resolv.conf")
    
    info['os'] = platform.system()
    info['os_version'] = platform.version()
    info['kernel_version'] = platform.release()
    info['system_disk_size'] = execute_command("df -h --total | grep 'total' | awk '{print $2}'")
    info['system_disk_available'] = execute_command("df -h --total | grep 'total' | awk '{print $4}'")
    
    
    info['cpu_model'] = execute_command("grep 'model name' /proc/cpuinfo | uniq | awk -F ': ' '{print $2}'")
    info['cpu_count'] = execute_command("grep -c ^processor /proc/cpuinfo")
    info['cpu_cores'] = execute_command("grep 'cpu cores' /proc/cpuinfo | uniq | awk '{print $4}'")
    info['total_ram'] = execute_command("free -h | grep Mem | awk '{print $2}'")
    info['available_ram'] = execute_command("free -h | grep Mem | awk '{print $7}'")
    return info

def print_and_log_system_info(info):
    # filename = f"/home/student/{info['hostname']}_system_report.log"
    # with open(filename, 'w') as log_file:
        for key, value in info.items():
            line = f"{key.replace('_', ' ').title()}: {value}"
            print(line)
            # log_file.write(line + "\n")



def main():
    clear_terminal()
    system_info = get_system_info()
    print_and_log_system_info(system_info)
    while(True):
        alpha = input("stop and reset? y/n")
        if alpha.lower() == "y" or "yes" or "ye":
            clear_terminal()
            break

if __name__ == "__main__":
    main()
