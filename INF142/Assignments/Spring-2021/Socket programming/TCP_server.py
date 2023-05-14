# Imports
from socket import socket, AF_INET, SOCK_STREAM

socket = socket(AF_INET, SOCK_STREAM)
socket.bind(('localhost', 55555))
socket.listen(1)

while True:
    connectionSocket, addr = socket.accept()
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()