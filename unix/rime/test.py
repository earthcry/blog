import os

reader=open("2008.txt")
lst=[]
n=0
for line in reader:
    lste=[]
    lste=line.split()
    if '~' in lste[1]:
        continue
#    print lste[1],lste[0]
#    if n > 99 :break
    n+=1
    lst.append((lste[1],lste[0]))
reader.close()
writer=open("cc.txt",'w')
for a,b in lst:
    strr=a+'	'+b+'\n'
    writer.write(strr)
writer.close()
'''
reader=open('cc.txt')
for line in reader:
    print line
reader.close()
'''

'''
from langconv import *

# 转换繁体到简体
line = Converter('zh-hans').convert(line.decode('utf-8'))
line = line.encode('utf-8')

# 转换简体到繁体
line = Converter('zh-hant').convert(line.decode('utf-8'))
line = line.encode('utf-8')
'''
