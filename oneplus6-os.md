## 手机刷机知识





### 一加6刷Nura/PostMarketOS 
Linux Phone 
Linux 手机，Android的手机。

PostMarketOS/Nura/AlpineLinux
apk add vim

一加6t要比6在网络和usb上支持好

用途，mobile linux server


四个桌面，phosh, gnome-mobile

adb 
install android-tools
fastboot

分区：

- boot_a
- boot_b
- system
- userdata
- dtbo
- 

- 一加6只按音量加键
- 同时按住一加6T 的音量加和音量减键，然后单击右侧的开关机键，就能直接进入BootLoader fastboot模式（前提是已经将手机解锁）。


一、前置条件
1. 更新氧系统到最新，线刷氧os10.3.8后可直接更新至11.1.22
2. sudo fastboot devices 
3. unclock，开发者usb调试，
    - sudo fastboot oem unlock
    - fastboot reboot
4. del dtbo
5. fastboot reboot

二、构建
apt install pmbootstrap
github download newer 
pmbootstrap init
    - 一般默认
    - qmenu oneplus
    - vim
pmbootstrap pull
pmbootstrap install
三、刷机
sudo fastboot erase userdata
pmbootstrap fasher flash_rootfs --partition=userdata
pmbootstrap fasher flash_kernel
sudo fastboot reboot
