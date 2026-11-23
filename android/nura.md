

adb
fastboot 

xz -dk boot.img.xz
fastboot mode:
fastboot devices
fastboot oem unlock
fastboot flashing unlock //oneplus6t
fastboot erase dtbo
fastboot flash boot_a boot.img
fastboot flash boot_b boot.img
fastboot getvar current-slot
fastboot erase system
fastboot erase userdata
fastboot flash userdata userdata.img
fastboot reboot
user 147147





