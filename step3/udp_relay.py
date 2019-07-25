import socket
import hashlib
from math import *
from random import *


relay_addr = ("127.0.0.1", 1236)
server_addr = ("127.0.0.1", 2347)
i = 0

def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed


def entropifier(data, error_rate):
	global i
	success_rate = int(pow(1-error_rate, len(data))*10000)
	newdata = b""
	newdata += data
	
	chance = randrange(10000)
	if chance >= success_rate:
		i += 1
		print(i)
		newdata += b"x"
		newdata = newdata[1:]
	return newdata


# Relay, server'a data yollar.
# Server, karsilik olarak datanin hashlenmis halini yollar.
# Relay, eger bu hashler farkliysa dogru oluncaya kadar data yollar.
# Eger hashler ayniysa Relay, OK yollar.
def chk_checksum(sender, data):
	while sender.recvfrom(1024)[0] != fhash(data):
		sender.sendto(data, server_addr)
		print("Fail")
	else:	
		print("OK")
		sender.sendto(b'OK', server_addr)


# Relay, Client'dan aldigi mesaji hashleyip client'a yollar.
# OK cevabini alirsa looptan cikar ve dogru oldugunu dusundugu datayi server'a iletir.
def check_permission(reciever, data, cli_addr):
	reciever.sendto(fhash(data), cli_addr)
	while True:
		chk_data, cli_addr = reciever.recvfrom(1024)
		if chk_data != b'OK':
			data = chk_data
			reciever.sendto(fhash(data), cli_addr)
		else:
			break
	return data


def recieve_and_send(reciever, error_rate):
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

	while True:
		data, cli_addr = reciever.recvfrom(1024)     
		if data:
			data = entropifier(data, error_rate)
			data = check_permission(reciever, data, cli_addr) # Relay, aldigi dosyanin hashini client'a yollar. OK alirsa server'a yollar.
			sender.sendto(data, server_addr)
			chk_checksum(sender, data)
		else:
			break
	reciever.close()
	sender.close()



if __name__ == '__main__':
	error_rate = 0.001
	print("Success rate for len = 100: {}".format(int(pow(1-error_rate, 100)*10000)))
	print("Success rate for len = 100: {}".format(pow(1-error_rate, 250)*10000))
	print("Success rate for len = 1024: {}".format(int(pow(1-error_rate, 1024)*10000)))
	reciever = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	reciever.bind(relay_addr)

	while True:
		recieve_and_send(reciever, error_rate)
