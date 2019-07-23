import socket
import hashlib
from random import randrange


relay_port = 1236
fname = "f_to_send.png"


def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def entropifier(data, katsayi):
	newdata = b""
	for i in range(len(data)):
		chance = randrange(katsayi)
		if chance == (katsayi-1):
			newdata += bytes(data[i]+1)
		else:
			newdata += bytes(data[i])
	return newdata




def chk_checksum(sender, data):
	while sender.recv(1024) != fhash(data):
		sender.send(data)
		print("Fail")
	else:
		sender.send(b'OK')


def send_data(filename):
	sender = socket.socket()
	sender.connect(("localhost",relay_port))
	f = open (filename, "rb")

	i = 0
	while True:
		data = f.read(1024)
		if not data: 
			break
		sender.send(data)
		# print("Client sent data to Relay")
		chk_checksum(sender, data)
		i += 1
	sender.close()



if __name__ == '__main__':
	send_data(fname)
