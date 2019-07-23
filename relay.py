import socket
import sys


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


def recieve_and_send(reciever):
	sender = socket.socket()
	sender.connect(("localhost",server_port))

	while True:
		data = reciever.recv(1024)       
		if data:
			reciever.send(b'ACK')
			sender.send(data)
			ack_check = sender.recv(1024)
			if ack_check == b'ACK':
				pass
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
		print("accepted")
		recieve_and_send(recv)


	rs.close()