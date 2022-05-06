#!/usr/bin/python
#Simple Python program to receive data from another RPi over WiFi. Both devices must in same network and ports must be configured correctly.

import socket

TCP_IP = '<insert IP here>' #Server Address
TCP_PORT = 5005
BUFFER_SIZE = 1024
# MESSAGE = "Hello from "+ TCP_IP

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('Connected to: ', addr)

while 1:
  data = conn.recv(BUFFER_SIZE)
  print "received data:", data
