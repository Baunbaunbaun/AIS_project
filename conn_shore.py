#!/usr/bin/env python3

import socket
import queue
import shore_db as sdb
import functions as fun
import time

menu_lst = []

# fill in test data
# slots_shore = sdb.test_data_in_db(6)

receive_queue = queue.Queue(100)
host = '127.0.0.1'
serverPort = 2001
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('', serverPort))
server_socket.listen(1)
print('The server is ready to receive')

def eval_sentence(sentence):
    lst = eval(sentence)

    # always query the menu with lowest slot
    # connectivity level (CL) 
    if (len(lst) != 2):
        print('EVAL1')
        global menu_lst
        if(len(lst)==3):
            menu_lst.append(lst)
        
        print('EVAL2')
        # there need to be at least 10 menus, so 
        # to compare CL and request from the 
        # most cost effecient vessel
        try: 
            if (len(menu_lst)<10 or len(lst[2]) == 0): 
                print('NUL')
                return []
        except: 
            pass
        print('EVAL3')
        # sort  
        menu_lst = sorted(menu_lst)

        # pop menu with lowest slot and CL
        slot1 = menu_lst.pop(0)
        
        # query
        out = sdb.get_mmsi_not_in_slot(slot1)                             # REQUEST

    else:
        print('EVAL4')
        out = sdb.insert_lst(lst)                                       # INSERT

    return out


while True:
    connectionSocket, addr = server_socket.accept()
    print('accepted!')
    out = ''

    while(True):
        try:
            sentence = connectionSocket.recv(2048).decode()             # RECEIVE
            print('\nSHORE receive with succes:\n', sentence)
        except:
            print('\nSHORE prob with receive!\n')
            pass
        if(len(sentence) == 0):
            print('ABORTING: sentence empty\n', time.time())
            break

        # send
        try:
            out = eval_sentence(sentence)
        except:
            print('\nNo evaluation of ', sentence, out)
            continue

        # PROBLEM
        fun.print_lst(menu_lst)

        # GET NEXT MESSAGE TO SEND

        try:
            print('\nSHORE send:\n', str(out))
            connectionSocket.send(str(out).encode())                    # SEND
        except:
            print('Closing connection')
            break

    connectionSocket.close()
    # TESTING WITH 1 CONNECTION
    break


sdb.print_db()
print('Size SDB', sdb.get_size())

