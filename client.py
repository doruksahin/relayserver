import socket
import sys
import time

relay_port = 1236
fname = "f_to_send.png"


def send_data(filename):
	sender = socket.socket()
	sender.connect(("localhost",relay_port))

	f = open (filename, "rb")
	data = f.read(1024)
	while (data):
		sender.send(data)
		data = f.read(1024)
		ack_check = sender.recv(1024)
		if ack_check == b'ACK':
			pass

	sender.close()



if __name__ == '__main__':
	send_data(fname)
