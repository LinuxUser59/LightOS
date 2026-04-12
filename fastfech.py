import os
import socket
import psutil

mem = psutil.virtual_memory()
total_ram = mem.total / (1024**3)
used_ram = mem.used / (1024**3)
free_ram = mem.free / (1024**3)

disk = psutil.disk_usage('/')
total_disk = disk.total / (1024**3)
used_disk = disk.used / (1024**3)

def fastfetch():
    print("""
  _      _       _     _      ____   _____ 
 | |    (_)     | |   | |    / __ \ / ____|
 | |     _  __ _| |__ | |_  | |  | | (___  
 | |    | |/ _` | '_ \| __| | |  | |\___ \ 
 | |____| | (_| | | | | |_  | |__| |____) |
 |______|_|\__, |_| |_|\__|  \____/|_____/ 
            __/ |                          
           |___/                           
""")
    print(f"Operating System:   LightOS")
    print(f"Release:            12.APR.26")
    print(f"User:               {os.getlogin()}")
    print(f"Host:               {socket.gethostname()}")
    print(f"Storage Used:       {round(used_disk, 2)}GB")
    print(f"Total Storage:      {round(total_disk, 2)}GB")
    print(f"Storage Used %:     {round(disk.percent, 2)}%")
    print(f"Memory Used:        {round(used_ram, 2)}MB")
    print(f"Memory Total:       {round(total_ram, 2)}MB")
    print(f"Memory Used %:      {round(mem.percent, 2)}%")

def Logo():
    print("""
  _      _       _     _      ____   _____ 
 | |    (_)     | |   | |    / __ \ / ____|
 | |     _  __ _| |__ | |_  | |  | | (___  
 | |    | |/ _` | '_ \| __| | |  | |\___ \ 
 | |____| | (_| | | | | |_  | |__| |____) |
 |______|_|\__, |_| |_|\__|  \____/|_____/ 
            __/ |                          
           |___/                           
""")