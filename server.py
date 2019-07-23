import socket
import sys


server_port = 2346
fname = "f_at_server.png"


def recieve_data(conn, filename):
	data = conn.recv(1024)
	f = open(filename,'wb') #open in binary

	while True:          
		if data:
			f.write(data)
		else:
			f.close()
			break
		data = conn.recv(1024)
	conn.close()	



if __name__ == '__main__':
	s = socket.socket()
	s.bind(("localhost",server_port))
	s.listen(10) # Accepts up to 10 connections.

	i = 1
	while True:
		conn, address = s.accept()
		recieve_data(conn, fname)

	s.close()	