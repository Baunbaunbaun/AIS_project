### CONNNECTION VESSEL ###

import socket
import queue
import random
import vessel_db as vdb
import functions as fun
import time

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

def send():
	while(True):
		if(send_queue.empty()):
			print('ABORTING: no more to send ', time.time())
			out = []
		else: 
			out = send_queue.get()
		print('\nVES: sending:\n', out)
		client_socket.send(str(out).encode())  						# SEND
		try:
			sentence = client_socket.recv(1024).decode()			# RECEIVE
			print('\nVES: receive:\n', sentence)
			sentence_eval = eval(sentence)
			try: 
				if(len(out)+len(sentence) == 2):
					print("Closing connection. Nothing is send.")
					break
			except:
				pass
			# receive slot number, delete this slot
			if(type(sentence_eval)==type(9)): 						# DELETE
				print('delete slot ', sentence_eval)
				vdb.delete(sentence_eval)
				continue
			# receive request, get messages, send back to shore
			msg = vdb.get_messages(sentence_eval)					# FETCH
			send_queue.put(msg)
		except:
			pass
	
	vdb.print_db()
	print('\nSize vessel DB: ', vdb.get_size())


