import socket
import sys


server_port = 2347
fname = "f_at_server.png"


def recieve_data(reciever, filename):
	data = reciever.recv(1024)
	reciever.send(b'ACK')
	f = open(filename,'wb') #open in binary

	while True:          
		if data:
			f.write(data)
		else:
			f.close()
			break
		data = reciever.recv(1024)
		reciever.send(b'ACK')
	reciever.close()	



if __name__ == '__main__':
	reciever = socket.socket()
	reciever.bind(("localhost",server_port))
	reciever.listen(10) # Accepts up to 10 connections.

	while True:
		recv, address = reciever.accept() # Waits here until relay.py do 'sender.connect()'
		print("accepted")
		recieve_data(recv, fname)

	# s.close()	