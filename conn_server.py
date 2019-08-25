import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 2001  # The port used by the server

serverName = 'servername'
serverPort = 12000

clientSocket = socket(AF_INET, SOCK_STREAM)

clientSocket.connect((serverName,serverPort))

sentence = B'Input lowercase sentence:'

clientSocket.send(sentence.encode())

modifiedSentence = clientSocket.recv(1024)

print('From Server: ', modifiedSentence.decode())

clientSocket.close()