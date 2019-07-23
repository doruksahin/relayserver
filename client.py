import socket
import sys


relay_port = 1235
fname = "f_to_send.png"


def send_data(sock, filename):
	f = open (filename, "rb")
	data = f.read(1024)
	while (data):
		sock.send(data)
		data = f.read(1024)



if __name__ == '__main__':
	s = socket.socket()
	s.connect(("localhost",relay_port))

	send_data(s, fname)
	s.close()