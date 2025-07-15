#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''test file'''
# DataStructure & OperateMethod
# ProblemModel & Algorithm
# frame & grow
# clear concept & logic, display result, graph process, conceptTree
# efficiency /i'fisfensi/
#print '*'*76

# question: sync dirs
# always display operate object, for xiaolv.
'''> 
----Logic--------------


<'''

import socket

skt = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print "Socket Created."

host = "www.oschina.net"
remote_ip = socket.gethostbyname(host)
print 'IP address of ' + host + ' is ' + remote_ip

port = 80
skt.connect((remote_ip,port))
print 'Socket Connected to ' + host + ' on ip ' + remote_ip


message = "GET / HTTP/1.1\r\n\r\n"
skt.sendall(message)
print 'Message send successfully.'

reply = skt.recv(4096)
print reply

skt.close()












'''

while True:
  send_data = input("Message: ")
  comms_socket.send(bytes(send_data, "UTF-8"))
  print(comms_socket.recv(4096).decode("UTF-8"))


'''




#print '*'*76


