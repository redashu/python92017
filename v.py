#!/usr/bin/env python2

import socket
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
	msg=raw_input("type something to start chat :  ")
	s.sendto(msg,("192.168.10.65",8888))
	print "__________________________________"
	print "__________________________________"
	print "__________________________________"
	print  s.recvfrom(100)[0]
	print "__________________________________"
	print "__________________________________"
	print "__________________________________"
	print "__________________________________"
