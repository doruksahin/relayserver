import socket
import hashlib
from random import randrange


relay_addr = ("127.0.0.1", 1236)
fname = "f_to_send.png"




def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed

def send_data(filename):
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	f = open (filename, "rb")

	while True:
		data = f.read(1024)
		if not data: 
			break
		hash = fhash(data)
		data += hash
		sender.sendto(data, relay_addr)
	sender.close()



if __name__ == '__main__':
	send_data(fname)
