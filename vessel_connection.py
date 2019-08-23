### VESSEL CONNECTION ###

### CODE FROM python-sockets-tutorial/multiconn-client.py

import sys
import socket
import selectors
import types
import random
import mock_signal as mock

# connection setup
host = '127.0.0.1'
port = 2001
server_addr = (host, port)
sel = selectors.DefaultSelector()
m = ''
messages = []

"""
# LAV OM TIL AT VENTE PÅ KØ IKKE TOM
while(not mock.NMEA_queue.empty()):
    m = mock.NMEA_queue.get()
    messages.append(m.encode())
"""





while(not mock.NMEA_queue.empty()):
    m = mock.NMEA_queue.get()
    messages.append(m.encode())



def start_connection():
    connid = 1
    print("starting connection", connid, "to", server_addr)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setblocking(False)
    sock.connect_ex(server_addr)
    events = selectors.EVENT_READ | selectors.EVENT_WRITE
    data = types.SimpleNamespace(
    connid=connid,

    msg_total=sum(len(m) for m in messages),
    recv_total=0,
    messages=list(messages),
    
    outb=b"",
    )
    sel.register(sock, events, data=data)

def service_connection(key, mask):
    sock = key.fileobj
    data = key.data
    if mask & selectors.EVENT_READ:
        recv_data = sock.recv(1024)  # Should be ready to read
        if recv_data:
            
            #print("received", repr(recv_data), "from connection", data.connid)
            data.recv_total += len(recv_data)

        if not recv_data or data.recv_total == data.msg_total:
            print("closing connection", data.connid)
            sel.unregister(sock)
            sock.close()
    if mask & selectors.EVENT_WRITE:
        if not data.outb and data.messages:
            data.outb = data.messages.pop(0)
        if data.outb:
            print("sending", repr(data.outb), "to connection", data.connid)
            sent = sock.send(data.outb)  # Should be ready to write
            data.outb = data.outb[sent:]

start_connection()

try:
    while True:
        events = sel.select(timeout=1)
        if events:
            for key, mask in events:
                service_connection(key, mask)
        # Check for a socket being monitored to continue.
        if not sel.get_map():
            break
except KeyboardInterrupt:
    print("caught keyboard interrupt, exiting")
finally:
    sel.close()