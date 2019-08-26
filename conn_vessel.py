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
			print('ABORTING: no more to send')
			break
		print('\nVES: sending:\n', out)
		client_socket.send(str(out).encode())
		print('succes')
		try:
			sentence = client_socket.recv(1024).decode()
			print('\nVES: receive:\n', sentence)
			sentence_eval = eval(sentence)
			# receive slot number, delete this slot
			if(type(sentence_eval)==type(9)): 
				print('delete slot ', sentence_eval)
				vdb.delete(sentence_eval)
			else: 
				# receive request, get messages, send back to shore
				msg = vdb.get_messages(eval(sentence))
				send_queue.put(msg)
			print('succes')

		except:
			print('VES prob with receive')
			pass
	
	vdb.print_db()

	# client_socket.close()


