import socket
import hashlib


server_port = 2347
fname = "f_at_server.png"


def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def entropifier(data, katsayi):
	newdata = b""
	newdata += data
	
	chance = randrange(katsayi)
	if chance == (katsayi-1):
		newdata += b"x"
		newdata = newdata[1:]
	return newdata


def check_permission(reciever, data):
	reciever.send(fhash(data))
	while True:
		chk_data = reciever.recv(1024)
		if chk_data != b'OK':
			print("Failll")	
			data = chk_data
			reciever.send(fhash(data))
		else:
			break
	return data


def recieve_data(reciever, filename):
	f = open(filename,'wb') #open in binary

	i = 0
	while True:
		data = reciever.recv(1024)
		if data:
			data = check_permission(reciever, data)
			f.write(data)
			if i % 10 == 0:
				print(i)
		else:
			f.close()
			break
		i += 1

	reciever.close()	



if __name__ == '__main__':
	reciever = socket.socket()
	reciever.bind(("localhost",server_port))
	reciever.listen(10) # Accepts up to 10 connections.

	while True:
		recv, address = reciever.accept() # Waits here until relay.py do 'sender.connect()'
		# print("accepted")
		recieve_data(recv, fname)
