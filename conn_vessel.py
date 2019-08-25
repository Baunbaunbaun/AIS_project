import socket
import sys, errno
import queue
import time
import vessel_db as vdb

# variable declarations
sentence = ''
serverName = "127.0.0.1"
serverPort = 2001
send_queue = queue.Queue(maxsize=100)
messages = []


# fill up list with test values
#lst = []
#for i in range(20):
#    lst.append(str(i)+' test sentence!\n')

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connet to server
client_socket.connect((serverName,serverPort))
#client_socket.setblocking(False)

print('VCONN!')

def send():

	while(True):
		out = send_queue.get()
		if(send_queue.empty()): 
			break
		print('\nSending: ', out)
		client_socket.send(str(out).encode())
		
		try:
			print('\nTRY receive on vessel')
			sentence = client_socket.recv(1024).decode()
			print('VESSEL received: ', sentence)
			msg = vdb.get_messages(eval(sentence))
			send_queue.put(msg)

		except:
			pass


	# client_socket.close()


