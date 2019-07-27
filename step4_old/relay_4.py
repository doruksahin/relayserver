import socket
import hashlib


relay_port = 1236
server_port = 2347

fname = "f_at_relay.png"

'''
def recieve_data(reciever, filename):
	data = reciever.recv(1024)
	reciever.send(b'ACK')
	f = open(filename,'wb') #open in binary

	while True:          
		if data:
			f.write(data)
			reciever.send(b'ACK')
		else:
			f.close()
			break
		data = reciever.recv(1024)
	reciever.close()


def send_data(filename):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	f = open (filename, "rb")
	data = f.read(1024)
	while data:
		sender.send(data)
		ack_check = sender.recv(1024)
		data = f.read(1024)
		if ack_check == b'ACK':
			pass

	sender.close()
'''

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


# design 1: relay client'a aldigi dosyanin hashini yollar.
# 			hash ayniysa client relay'e OK yollar.
#			relay'in cevabi OK degilse bozuk gelen data tekrar yollanmistir.
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


# design 2: client hem data alir hem de hashlenmis halini alir.
#			relay hashlediginde ayni cikiyorsa client'a OK yollar. 
#			client OK'u aldiginda yeni data yollar, degilse farkli data yollar.
#			BUNU DAHA IYI OLUR DIYE YAZDIM AMA DAHA IYI OLMADI KIIIII
def check_permission2(reciever, data):
	while True:
		data = reciever.recv(1024)
		datahash = reciever.recv(1024)
		if fhash(data) == datahash:


def chk_checksum(sender, data):
	while sender.recv(1024) != fhash(data):
		sender.send(data)
		print("Fail")
	else:
		sender.send(b'OK')


def recieve_and_send(reciever):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	while True:
		data = reciever.recv(1024)       
		if data:
			data = check_permission(reciever, data) # Client'dan OK mesajini bekle.
			sender.send(data)
			# print("Relay sent data to Server.")
			chk_checksum(sender, data)
		else:
			break
	reciever.close()
	sender.close()


# Step1'de sadece e2e chksum isteniyordu. Bu yuzden check_permission gereksiz.
def recieve_and_send_step1(reciever):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	while True:
		data = reciever.recv(1024)       
		if data:
			#data = check_permission(reciever, data) # Client'dan aldigin datayi hashleyip client'dan OK mesajini bekle.
			sender.send(data)
			chk_checksum(sender, data)
		else:
			break
	reciever.close()
	sender.close()



if __name__ == '__main__':
	reciever = socket.socket()
	reciever.bind(("localhost",relay_port))
	reciever.listen(10) # Accepts up to 10 connections.

	while True:
		recv, address = reciever.accept() # Waits here until client.py do 'sender.connect()'
		# print("accepted")
		recieve_and_send(recv)
