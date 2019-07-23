import socket
import hashlib


relay_port = 1236
server_port = 2347
hasher = hashlib.md5()

fname = "f_at_relay.png"

'''
def recieve_data(reciever, filename):
	data = reciever.recv(1024)
	reciever.send(b'ACK')
	f = open(filename,'wb') #open in binary

	while True:          
		if data:
			f.write(data)
			reciever.send(b'ACK')
		else:
			f.close()
			break
		data = reciever.recv(1024)
	reciever.close()


def send_data(filename):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	f = open (filename, "rb")
	data = f.read(1024)
	while data:
		sender.send(data)
		ack_check = sender.recv(1024)
		data = f.read(1024)
		if ack_check == b'ACK':
			pass

	sender.close()
'''

def fhash(data):
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def check_permission(reciever, data):
	reciever.send(fhash(data))
	while reciever.recv(1024) != b'OK':	
		reciever.send(fhash(data))


def chk_checksum(sender, data):
	while sender.recv(1024) != fhash(data):
		sender.send(data)
	else:
		sender.send(b'OK')


def recieve_and_send(reciever):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	while True:
		data = reciever.recv(1024)       
		if data:
			check_permission(reciever, data)
			sender.send(data)
			print("Relay sent data")
			chk_checksum(sender, data)
		else:
			break
	
	reciever.close()
	sender.close()



if __name__ == '__main__':
	reciever = socket.socket()
	reciever.bind(("localhost",relay_port))
	reciever.listen(10) # Accepts up to 10 connections.

	while True:
		recv, address = reciever.accept() # Waits here until client.py do 'sender.connect()'
		print("accepted")
		recieve_and_send(recv)


	rs.close()