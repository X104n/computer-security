# Imports
from socket import socket, AF_INET, SOCK_DGRAM

socket = socket(AF_INET, SOCK_DGRAM)

while ((text := input('> ').lower()) != 'shut down'): 
    socket.sendto(text.encode() , ('localhost', 55554))
    msg, addr = socket.recvfrom(2048)
    print(msg.decode())