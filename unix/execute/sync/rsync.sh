#!/bin/bash
#?auto link not password by hand.


# android, dirC -> dirB

dirC='192.168.43.1:/storage/emulated/0/0openOften' #this path is sdcard sometime
#dirC='192.168.43.1:/storage/emulated/0/1openSeldom'
#dirC='192.168.43.1:/storage/emulated/0'
#dirC='192.168.43.1:/sdcard/0jkd'

# linux, sync A B
#dirA='/home/nu/seldomdb'
dirA='/home/nu/oftendb'
dirB='/home/nu/android'



#cp -avfu /home/nu/execute /home/nu/oftendb/
#./execute/mkrecent.py
sshfs -p 2222 $dirC $dirB  #connection reset by peer sometime  
ls ~/android
./execute/sync/sync.py  $dirA $dirB
sudo umount -l ~/android
ls ~/android




#scp -P 2222 -r -v -C root@ip:/usr/local/src/*.log /root/
#ls ./android ./oftendb

#sshfs -p 2222 192.168.43.1:/storage/emulated/0/0openOften ~/android

# often
#rsync -e 'ssh -p 2222' -rauv 192.168.43.1:/storage/emulated/0/0openOften/ /home/nu/oftendb
#rsync -e 'ssh -p 2222' -ruv  /home/nu/oftendb/ 192.168.43.1:/storage/emulated/0/0openOften
#rsync -e 'ssh -p 2222' -rauv 192.168.43.1:/storage/emulated/0/0openOften/ /home/nu/oftendb

# seldom
#rsync -e 'ssh -p 2222' -rauv 192.168.43.1:/storage/emulated/0/1openSeldom/ /home/nu/seldomdb
#rsync -e 'ssh -p 2222' -ruv  /home/nu/seldomdb/ 192.168.43.1:/storage/emulated/0/1openSeldom
#rsync -e 'ssh -p 2222' -rauv 192.168.43.1:/storage/emulated/0/1openSeldom/ /home/nu/seldomdb

















