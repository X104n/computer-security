# Imports
from socket import socket, AF_INET, SOCK_STREAM

socket = socket(AF_INET, SOCK_STREAM)

socket.connect(('localhost', 55555))

while ((text := input('> ').lower) != 'shut down'):
    socket.send(text.encode())
    modifiedSentence = socket.recv(1024)
    print('From Server: ', modifiedSentence.decode())
    socket.close()