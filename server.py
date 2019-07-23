import socket
import hashlib


server_port = 2347
fname = "f_at_server.png"
hasher = hashlib.md5()


def fhash(data):
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def check_permission(reciever, data):
	reciever.send(fhash(data))
	while reciever.recv(1024) != b'OK':	
		reciever.send(fhash(data))


def recieve_data(reciever, filename):
	f = open(filename,'wb') #open in binary

	while True:
		data = reciever.recv(1024)
		print(data)
		if data:
			check_permission(reciever, data)
			f.write(data)
			print("Server sent data.")
		else:
			f.close()
			break

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