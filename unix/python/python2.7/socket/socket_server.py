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

import socket   # twisted
import thread
import sys

HOST = "localhost" 
PORT = 8888
skt = socket.socket()
print 'Socket Created.'
skt.bind((HOST,PORT))
print 'Socket bind completed.'
skt.listen(10)
print 'Socket now listening.'

def clientThread(conn,addr):
  print 'Connection with ' + addr[0] + ':' + str(addr[1])
  conn.send('Welcome to the server.\n')
  while True:
    data = conn.recv(1024)
    if not data:break
    reply = addr[0] + ':' + str(addr[1]) + ': ' + data
    conn.sendall(reply)
  conn.close()


while True:
  conn, addr = skt.accept()
  thread.start_new_thread(clientThread,(conn,addr,))
    
skt.close()






#print '*'*76


