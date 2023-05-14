import os
import time

#Starter Bergen/Karmøy delen
os.system('start cmd /c "python Storage_Bergen-Karmøy/serverStart.py"')

time.sleep(1)

os.system('start cmd /k "python Weather_Station_Bergen/tcp_client.py"')
os.system('start cmd /k "python Weather_Station_Karmøy/tcp_client.py"')



# # Starter Oslo delen
os.system('start cmd /c "python Storage_Oslo/serverStart.py"')

time.sleep(1)

os.system('start cmd /k "python Weather_Station_Oslo/tcp_client.py"')