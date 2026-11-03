#!/bin/bash
# boot by systemrescuecd
# mkdir /media/sda4
# mount -v /dev/sda4 /media/sda4
# mkfs -t /ext4 /dev/sda4
# cd /media/sda4
# tar xpvf backup_..._.tar.gz
# sudo mkdir -pv home sys proc dev usr/portage/distfiles
# chroot
# /usr/grub-install --recheck /dev/sda

# mount -v /dev/sda4 /media/sda4
# cd /media/sda4
# rm -rf *

echo '------'
echo "Start to restore"
tar -zxvpf /media/nudata/bkp/ubuntu-2015-03-08.tar.gz --directory /media/sda4
echo 'Restore success.'
echo 'make dir...'
#sudo mkdir -pv dev proc sys usr/portage/distfiles
echo '------'

#mkfs -t /ext4 /dev/sda4
#edit three files after restore.
#/boot/grub/grub.cfg
#/etc/fstab
#/etc/X11/xorg.conf
#blkid /dev/sda4 >> /etc/fstab  blkid /dev/sda4 >> /boot/grub/grub.cfg

