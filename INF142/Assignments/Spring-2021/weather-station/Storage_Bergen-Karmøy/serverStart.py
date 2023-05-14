import os
os.chdir("Storage_Bergen-Karmøy")
os.system('start cmd /k "python tcp_server.py"')
os.system('start cmd /k "python udp_server.py"')