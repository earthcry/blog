#!/bin/bash
# ubuntu backup
# du -h /var/cache/apt/archives 
# sudo apt-get autoclean
# sudo apt-get autoremove
# sudo apt-get clean

# systemrescuecd boot
# fdisk -l
# df -hl
# mkdir /media/sda4
# mkdir /media/nudb
# mount /dev/sda4 /media/sda4
# (mount /dev/sda1 /media/sda4/boot)
# mount /dev/sda8 /media/nudb

echo '------'
echo "Start to backup..."
tar -zcvp -f /media/nudata/bkp/ubuntu-`date '+%Y-%m-%d'`.tar.gz \
--directory /media/sda4 . \
--exclude=/media/sda4/lost+found \
--exclude=/media/sda4/proc/* \
--exclude=/media/sda4/dev/* \
--exclude=/media/sda4/sys/* \
2> /media/error.txt
echo 'Backup success.'
echo '------'

# name_$(date +"%Y-%m-%d")_img.tar.gz
# name_`date '+%Y-%m-%d'`_img.tar.gz
# name_2015-03-06_img.tar.gz
