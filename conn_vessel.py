import socket
import sys, errno
import queue

# variable declarations
modifiedSentence = b''
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
client_socket.setblocking(False)

print('VCONN!')

def send():

	while(True):
		out = send_queue.get()
		if(send_queue.empty()): 
			break
		print(out)
		client_socket.send(str(out).encode())

	try:
		modifiedSentence = client_socket.recv(1024)
		print('VESSEL received: ', modifiedSentence.decode())
	except:
		pass


	# client_socket.close()


"""




modifiedSentence = client_socket.recv(1024)
print('From Server: ', modifiedSentence.decode())
client_socket.close()






while(not send_queue.empty()):
    m = send_queue.get()
    print("SEND Q")
    messages.append(m.encode())

# send loop
# for i in range(len(messages)):
while (True):
	if(send_queue.empty()): break
	try:
		print('testing')
		# client_s
		#ocket.send(messages.pop(0).encode())
		client_s
	ocket.send(t)
	except: 
		break

try:
	modifiedSentence = client_socket.recv(1024)
except:
	# print("Receive error – bytes: ", modifiedSentence.__sizeof__())
	pass

print('From Server: ', modifiedSentence.decode())
client_socket.close()
"""
