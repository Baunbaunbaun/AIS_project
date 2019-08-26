import socket
import queue
import vessel_db as vdb
import functions as fun

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

print('VCON!')

def send():

	while(True):
		if(send_queue.empty()):
			print('ABORTING: no more to send')
			break
		out = send_queue.get()
		print('\nVES: sending:\n', out)
		client_socket.send(str(out).encode())  						# SEND
		try:
			sentence = client_socket.recv(1024).decode()			# RECEIVE
			print('\nVES: receive:\n', sentence)
			sentence_eval = eval(sentence)
			# receive slot number, delete this slot
			if(type(sentence_eval)==type(9)): 
				print('delete slot ', sentence_eval)
				vdb.delete(sentence_eval)
				continue
			# receive request, get messages, send back to shore
			msg = vdb.get_messages(sentence_eval)
			send_queue.put(msg)
		except:
			print('VES prob with receive')
			pass
	
	vdb.print_db()


