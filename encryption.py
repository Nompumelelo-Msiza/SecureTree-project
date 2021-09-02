import json
def Decrypt(filename, key):
	file = open(filename, "rb")
	data = file.read()
	file.close()
	data = bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key
	file = open("user_management.json" , "wb")
	file.write(data)
	file.close()
def Encrypt(filename, key):
	file = open(filename, "rb")
	data = file.read()
	file.close()
	data = bytearray(data)
	for index, value in enumerate(data):
		data[index] = value ^ key
	file = open("user_management.json" , "wb")
	file.write(data)
	file.close()
	
key = 25
filename = "registered_users.json"
Encrypt(filename,25)