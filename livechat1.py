#!/usr/bin/python2

import  socket
import  thread
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)

s.bind(("",9999))

c_ip="192.168.10.169"
c_port=8888
def  recv():
	while  True:
		data=s.recvfrom(100)
		print  data[0]


def  send():
	while True:
		msg=raw_input(" ")
		s.sendto(msg,(c_ip,c_port))

thread.start_new_thread(recv,())
thread.start_new_thread(send,())

while True:
	pass




