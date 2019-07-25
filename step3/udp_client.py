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


def chk_checksum(sender, data):
	while sender.recvfrom(1024)[0] != fhash(data):
		sender.sendto(data, relay_addr)
		print("Fail")
	else:	
		print("OK")
		sender.sendto(b'OK', relay_addr)


# Client datanin ardindan hashli halini yollar. Relay hicbir kontrol yapmadan aldiklarini gonderir.
# Server'a geldigimizde hashler kiyaslanir. Hashler ayni ise server OK mesaji yollar. 
# Client'a gelen mesaj kontrol edilir. OK ise yeni dosya ve yeni hash, OK degilse eski dosya ve eski hash bir daha yollanir.

# Client datayi yollar, hashli halini saklar. Relay aldigi datayi hashleyip client'a geri yollar. OK mesaji alirsa mesaji Server'a yollar.
# Relay, OK mesaji almadiysa data almistir. Datayi hashleyip bir daha client'a yollar. Yani veri dogru oluncaya kadar adim 1'i uygular. 
# Server aldigi datayi hashler ve dogru mu diye hash'i Relay'e yollar.
# Relay, hashler ayni ise 'OK' yollar. Ayni degilse data'yi yollar. 
def send_data(filename):
	sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	f = open (filename, "rb")

	while True:
		data = f.read(1024)
		if not data: 
			break
		sender.sendto(data, relay_addr)
		chk_checksum(sender, data)
	sender.close()



if __name__ == '__main__':
	send_data(fname)
