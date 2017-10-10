#!/usr/bin/python

import socket
import  time
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM,0)
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

while True:
	s.sendto("Testinnnnnnnnnnnnnnnnnnngggg",("255.255.255.255",8888))
	time.sleep(5)



s.close()



