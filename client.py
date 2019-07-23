import socket
import hashlib


relay_port = 1236
fname = "f_to_send.png"
hasher = hashlib.md5()


def fhash(data):
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def chk_checksum(sender, data):
	while sender.recv(1024) != fhash(data):
		sender.send(data)
	else:
		sender.send(b'OK')


def send_data(filename):
	sender = socket.socket()
	sender.connect(("localhost",relay_port))
	f = open (filename, "rb")

	while True:
		data = f.read(1024)
		if not data: 
			break
		sender.send(data)
		print("Client sent data")
		chk_checksum(sender, data)

	sender.close()



if __name__ == '__main__':
	send_data(fname)
