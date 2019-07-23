import socket
import sys
import struct


relay_port = 1235
server_port = 2346

fname = "f_at_relay.png"


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


def send_data(sock, filename):
	f = open (filename, "rb")
	data = f.read(1024)
	while (data):
		sock.send(data)
		data = f.read(1024)



if __name__ == '__main__':
	recieve_socket = socket.socket()
	recieve_socket.bind(("localhost",relay_port))
	recieve_socket.listen(10) # Accepts up to 10 connections.

	sender_socket = socket.socket()
	sender_socket.connect(("localhost",server_port))

	i = 1
	while True:
		conn, address = recieve_socket.accept()
		print("accepted")
		recieve_data(conn, fname)
		send_data(sender_socket, fname)



	rs.close()