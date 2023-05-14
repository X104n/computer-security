import os
os.chdir("Storage_Oslo")
os.system('start cmd /k "python tcp_server.py"')
os.system('start cmd /k "python udp_server.py"')