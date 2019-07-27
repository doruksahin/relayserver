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
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		data, client_addr = reciever.recvfrom(1024 + 16)

		if not data:
			break
		data = bytes([change_byte(x) for x in data])
		checksum = data[-16:]
		packet_data = data[:1024]

		if checksum == fhash(packet_data):
			sender.sendto(bytes([change_byte(x) for x in data]), server_addr)
			while sender.recv(1) != b'+':
				sender.sendto(bytes([change_byte(x) for x in data]), server_addr)
			reciever.sendto(b'+', client_addr)
		else:
			reciever.sendto(b'-', client_addr)

			
	reciever.close()
	sender.close()



if __name__ == '__main__':
	reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	reciever.bind(relay_addr)

	while True:
		recieve_and_send(reciever)
