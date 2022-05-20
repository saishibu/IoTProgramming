#!/usr/bin/python
#http://www.steves-internet-guide.com/install-mosquitto-linux/

#Simple Python program to send data to another RPi over WiFi. Both devices must in same network and ports must be configured correctly.

import socket

TCP_IP = '<insert IP here>' #Server Address
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello from "+ TCP_IP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(MESSAGE)
# data = s.recv(BUFFER_SIZE)
s.close()

print "received data:", data
