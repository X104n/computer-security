from selectors import DefaultSelector, EVENT_READ
from socket import create_server
import pickle, sqlite3 as sl

def accept(sock):
    #accept incoming connection
    conn, address = sock.accept() 
    print(f"{conn} accepted from address {address}")
    conn.setblocking(False)
    #register the connection to the selector
    sel.register(conn,EVENT_READ)

def read(conn):
    ###
    # recive data from accepted connection
    # ###
    eData = conn.recv(2048)
    if eData:
        data = pickle.loads(eData)
        print(data[0])
        slConn.execute(sql,data)
        slConn.commit()
    else:
        print(f"Closing bad connection: {conn}")
        sel.unregister(conn)
        
#create socket and selector
sel = DefaultSelector()         #for keeping track of connections
sock = create_server(("localhost", 3333))
sock.listen()
sock.setblocking(False)
sel.register(sock,EVENT_READ,True)

print("[Oslo] Launching the storage server")

#connect to local database
# Loc,Day,Month,Temp,Rain
slConn = sl.connect("weather-data.db")
sql = "INSERT INTO WEATHER (location,day,month,temperature,rain) values(?,?,?,?,?)"

#clear out the database (see README)
slConn.execute("DELETE FROM WEATHER")
slConn.execute("DELETE FROM sqlite_sequence")
slConn.commit()
slConn.execute("VACUUM")

while True:
    events = sel.select()
    for key,_ in events:
        if key.data:
            accept(key.fileobj)
        else:
            read(key.fileobj)