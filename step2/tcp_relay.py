import socket
import hashlib
from math import *
import random

relay_addr = ("127.0.0.1", 1236)
server_addr = ("127.0.0.1", 2347)

error_rate = 0.001

def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed

def change_byte(byte):
	if random.random() < error_rate:
		return not byte
	return byte

def recieve_and_send(reciever):
	sender = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sender.connect(server_addr)

	while True:
		data = reciever.recv(1024 + 16)       
		if data:
			data = bytes([change_byte(x) for x in data])
			sender.send(data)
		else:
			break
	reciever.close()
	sender.close()



if __name__ == '__main__':
	reciever = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	reciever.bind(relay_addr)
	reciever.listen(1) # Accepts up to 10 connections.

	while True:
		recv, address = reciever.accept() # Waits here until client.py do 'sender.connect()'
		recieve_and_send(recv)
