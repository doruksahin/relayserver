import socket
import hashlib


server_addr = ("127.0.0.1", 2347)
fname = "f_at_server.png"


def fhash(data):
	hasher = hashlib.md5()
	hasher.update(data)
	hashed = hasher.digest()
	return hashed

def recieve_data(reciever, filename):
	f = open(filename,'wb') #open in binary

	i = 0
	valid_packets = 0
	resend = 0
	while True:
		data, relay_addr = reciever.recvfrom(1024 + 16)
		if data:
			checksum = data[-16:]
			data = data[:1024]
			if checksum == fhash(data):
				reciever.sendto(b'+', relay_addr)
				valid_packets += 1
			else:
				resend += 1
				reciever.sendto(b'-', relay_addr)
			f.write(data)
			if i % 10 == 0:
				print("Total packet:", i+1, "- valid packet:", valid_packets, "- error rate:", (i+1-valid_packets)/(i+1), "- resend:", resend)
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
