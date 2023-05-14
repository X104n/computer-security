from socket import socket, AF_INET, SOCK_DGRAM
import pickle,sqlite3 as sl
import structuring as st

def toInt(i:str) -> int:
    ###
    # for converting str to int
    # ###
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
sock.bind(("localhost",4444))

#connect to local database
slConn = sl.connect("weather-data.db")

print("[Bergen/Karmøy] launching FMI communication server")

while True:
    msg,address = sock.recvfrom(2048)
    #We want the command to start with a Capitalized location 
    comm_div = msg.decode().lower().capitalize().split(" ")

    if len(comm_div) > 1:
        if day:=toInt(comm_div[1]):
            if day < 32:
                data = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{comm_div[0]}' AND day = {day}")
                print(f"Sending data to {address}")
                send(data,address)
                continue
    
    #if the day was not specified, or the command was flawed, return the avg of each day of the month
    d = slConn.execute(f"SELECT * FROM WEATHER WHERE location = '{comm_div[0]}'")
    data = st.avg_temp(d)
    print(f"Sending data to {address}")
    send(data,address)
    
    


print("Server down")
slConn.close()
