#!/usr/bin/env python3

import socket
import queue
import shore_db as sdb
import time

receive_queue = queue.Queue(100)
host = '127.0.0.1'
serverPort = 2001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('',serverPort))
server_socket.listen(1)
print('The server is ready to receive')

def eval_sentence(sentence):
    lst = eval(sentence)
    if (len(lst)==2):
        print('Getting mmsi not in slot!')
        out = sdb.get_mmsi_not_in_slot(lst)
    else: 
        print('Inserting list!')
        out = sdb.insert_lst(lst)
    return out

while True:
    connectionSocket, addr = server_socket.accept()
    print('accepted!')
    out = ''

    while(True):
        # receive
        try:
            sentence = connectionSocket.recv(2048).decode()
            # receive_queue.put(sentence)
        except: 
            pass
        print('\nSHORE received: ', sentence)
        if(len(sentence)==0): 
            print('sentence == 0')
            break
        
        # send
        try:
            out = eval_sentence(sentence)
        except:
            print('\nEVAL broke with', sentence)
            break

        # if out not 1 then request messages
        if (out != 1):
            try: 
                print('TRY encode and send')
                connectionSocket.send(str(out).encode())
                print('succes')
            except:
                print('Closing connection')
                break

    connectionSocket.close() 
    # TESTING WITH 1 CONNECTION
    break



connectionSocket.close() 
