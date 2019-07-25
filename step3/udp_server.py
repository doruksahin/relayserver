import socket
import hashlib


server_addr = ("127.0.0.1", 2347)
fname = "f_at_server.png"


def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def check_permission(reciever, data, relay_addr):
	reciever.sendto(fhash(data), relay_addr)
	while True:
		chk_data, relay_addr = reciever.recvfrom(1024)
		if chk_data != b'OK':
			data = chk_data
			reciever.sendto(fhash(data), relay_addr)
		else:
			break
	return data


def recieve_data(reciever, filename):
	f = open(filename,'wb') #open in binary

	i = 0
	while True:
		data, relay_addr = reciever.recvfrom(1024)
		if data:
			data = check_permission(reciever, data, relay_addr)
			f.write(data)
			if i % 10 == 0:
				print(i)
			i += 1
		else:
			f.close()
			break

	reciever.close()	



if __name__ == '__main__':
	reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	reciever.bind(server_addr)

	while True:
		recieve_data(reciever, fname)
