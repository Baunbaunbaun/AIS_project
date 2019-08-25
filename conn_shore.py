#!/usr/bin/env python3

import socket
import queue

receive_queue = queue.Queue(100)

host = '127.0.0.1'
serverPort = 2001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# server_socket.setblocking(False)

server_socket.bind(('',serverPort))

server_socket.listen(1)
print('The server is ready to receive')

while True:
    connectionSocket, addr = server_socket.accept()
    print('accepted!')

    while(True):
        # receive
        try:
            sentence = connectionSocket.recv(1024).decode()
            receive_queue.put(sentence)
        except: 
            pass
        print('SHORE received: ', sentence)
        if(len(sentence)==0): break

        # send
        capitalizedSentence = sentence.upper()
        try: 
            connectionSocket.send(capitalizedSentence.encode())
        except:
            print('Closing connection')
            break

    connectionSocket.close() 
    # TESTING WITH 1 CONNECTION
    break

connectionSocket.close() 

"""
"""