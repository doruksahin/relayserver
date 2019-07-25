import socket
import hashlib



relay_addr = ("127.0.0.1", 1236)
server_addr = ("127.0.0.1", 2347)


def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def recieve_and_send(reciever):
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		data, cli_addr = reciever.recvfrom(1024)     
		if data:
			sender.sendto(data, server_addr)
			if data != b'OK':
				client_response, addr = sender.recvfrom(1024)
				reciever.sendto(client_response, cli_addr)
		else:
			break
	reciever.close()
	sender.close()



if __name__ == '__main__':
	reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	reciever.bind(relay_addr)
	# reciever.listen(1) # Accepts up to 10 connections.

	while True:
		# recv, address = reciever.accept() # Waits here until client.py do 'sender.connect()'
		recieve_and_send(reciever)
