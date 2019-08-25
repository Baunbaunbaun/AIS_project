#!/usr/bin/env python3

import socket
import queue
import shore_db as sdb
import time

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
    out = ''

    while(True):
        # receive
        try:
            sentence = connectionSocket.recv(1024).decode()
            receive_queue.put(sentence)
        except: 
            pass
        print('\nSHORE received: ', sentence)
        if(len(sentence)==0): 
            print('sentence == 0')
            break
        
        # send
        try:

            out = eval(sentence)
        except:
            print('\nEVAL broke with', sentence)
            break

        answer = sdb.get_mmsi_not_in_slot(out)
        print('MMSI not in slot ', out[0], '\n', answer)
        # capitalizedSentence = sentence.upper()
        try: 
            print('TRY encode and send')
            connectionSocket.send(str(answer).encode())
            print('succes')
        except:
            print('Closing connection')
            break

    connectionSocket.close() 
    # TESTING WITH 1 CONNECTION
    break

connectionSocket.close() 

"""
"""