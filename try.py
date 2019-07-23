from random import randrange


def entropifier(data, katsayi):
	newdata = b""
	newdata += data
	
	chance = randrange(katsayi)
	if chance == (katsayi-1):
		newdata += b"x"
		newdata = newdata[1:]
	return newdata


fname = "f_to_send.png"
f = open(fname, "rb")
data = f.read(1024)
print(len(data))
print(type(data))
print(" ")
entropifier(data, 2)
