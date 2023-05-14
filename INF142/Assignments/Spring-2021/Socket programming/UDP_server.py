# Imports
from socket import socket, AF_INET, SOCK_DGRAM

sock = socket(AF_INET, SOCK_DGRAM)
socket.bind(('localhost', 55554))

while True:
    msg, addr = socket.recvfrom(2048)
    print(f'{addr[0]} says {msg.decode()}')
    socket.sendto(('ACK: '.encode() + msg), addr)
