from socket import socket, AF_INET, SOCK_DGRAM
import pickle,sqlite3 as sl
import structuring as st

def toInt(i:str) -> int:
    try: 
        n = int(i)
        return n
    except:
        return None

def send(data,address):
    #send in small chunks
    for row in data:
        sock.sendto(pickle.dumps(row),address)

#set up server
sock = socket(AF_INET,SOCK_DGRAM)
sock.bind(("localhost",2222))

#connect to local database
slConn = sl.connect("weather-data.db")

print("[Oslo] launching FMI communication server")

while True:
    msg,address = sock.recvfrom(2048)
    comm_div = msg.decode().lower().capitalize().split(" ")

    if len(comm_div) > 1:
        if day:=toInt(comm_div[1]):
            if day < 32:
                data = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{comm_div[0]}' AND day = {day}")
                print(f"Sending data to {address}")
                send(data,address)
                continue
    

    d = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{comm_div[0]}'")
    data = st.avg_temp(d)
    print(f"Sending data to {address}")
    send(data,address)
    
    


print("Server down")
slConn.close()
