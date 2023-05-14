from socket import socket,timeout,AF_INET,SOCK_DGRAM
import pickle

#set up client with timeout
sock = socket(AF_INET,SOCK_DGRAM)
sock.settimeout(1)

print("Welcome to FMI!")

while (text:=input("> ").lower()) != "quit":
    #seperate between different commands

    #the command can consist of multiple words, but at this point we only care about
    #the first
    comm = text.split(" ")
    if(comm[0] in ("bergen","karmøy")):     
        sock.sendto(text.encode(),("localhost",4444))

    
    elif(comm[0] == "oslo"):
        sock.sendto(text.encode(),("localhost",2222))

    
    elif text == "help":
        print("Enter location name!")
        continue
    else:
        print("unknown command! (help)")
        continue

    print("Location\tday\tmonth\ttemperature\train")
    #The data is transferd in small chunks, so we have to
    #keep reciving and printing until the transfer is done
    while True:
        try:
            data = sock.recv(2048)
            d = pickle.loads(data)
            print(f"{d[1]}\t\t{d[2]}\t{d[3]}\t{d[4]}\t\t{d[5]}")
        except timeout:
            break
        except:
            print("this local server is down!")
            break



print("Thank you for using FMI!\nWelcome back")
    