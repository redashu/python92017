#!/usr/bin/env python2

import  socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

s.bind(("192.168.10.65",8888))


#s.sendto("hiiiiiiii",("192.168.10.65",8888))

while True:
	data=s.recvfrom(100)
	print  "data from client  :   ",data[0]
        cliaddr=data[1]
	print  "________________________________"
	print  "________________________________"
	print  "________________________________"

	r=raw_input("type your reply:     ")
        s.sendto(r,cliaddr)
	print  "#######################################"
	print  "#######################################"
	print  "#######################################"

