
# Debian 12


### Python

install python3 python3-dev python3-pip






### Flatpak

 **mirror**

sudo flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo

经添加的话就用modify
From: https://mirror.sjtu.edu.cn/docs/flathub

Usage:
sudo flatpak remote-modify flathub --url=https://mirror.sjtu.edu.cn/flathub

reset:
sudo flatpak remote-modify flathub --url=https://flathub.org/repo

Error:

wget https://mirror.sjtu.edu.cn/flathub/flathub.gpg
sudo flatpak remote-modify --gpg-import=flathub.gpg flathub


flatpak search LibreOffice
flatpak install flatpak org.libreoffic.LibreOffice
flatpak list --app
flatpak run ID
flatpak update ID
flatpak uninstall ID

flatpak remove --unused

appflowy
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
it will writting to ~/.config/pip/pip.conf


### soft
- timeshift
- vim-gtk3/gnome
- audiorelay
- qtscrcpy
-

## Install debian

### disk
Btrfs文件系统


uefi setup
part
fdisk -l / lsblk
df -hT

df -i # inode 
lsof | grep deleted 


mount | grep sdb1

gdisk /dev/sdb or parted
sudo mkfs.ext4 /dev/sdb1 
chmod 755 /mnt/mydisk

mount -o loop image.iso /mnt/
df or mount -a

umount 
/etc/fstab #自动挂载
/dev/sdb1 /mnt/mydisk
sudo mount -a



### Linux  Terminal  Emulator

- Terminator
- Terminology
- Tabby
- WezTerm
- Kitty
- Alacritty
- 


### 修复文件系统错误
sudo  umount  /dev/sda8
sudo  fsck  -y  /dev/sda8 
sudo  fsck  -y  /dev/sda10 

sudo mount /dev/sda8 /mnt/
sudo mount /dev/sda7 /mnt/boot/efi 
sudo mount /dev/sda10 /mnt/home/


### grub install
sudo grub-install --target=x86_64-efi --efi-directory=/boot/efi --bootloader-id=Debian 


用live光盘重装GRUB引导，在Live系统中输入如下命令：/sbin/grub-install –root-directory=/mnt /dev/sda，重新安装GRUB引导。


### install deb
tar -zxvf 文件名.tar.gz -C /目标路径/
tar -ztvf 文件名.tar.gz

sudo dpkg -i xxx.deb
sudo apt -f -y install



听不懂就学一样孟德尔遗传定律！高中有学，再不行，让小辈教

听一亩耘心王澍老师的话，动手烧稻壳炭给水稻补充钾肥


我们这里遍地黄荆，听说驱蚊效果很好，所以看看有没有谁会做蚊香的教我一下，我用它来做蚊香.

### Highlight 高亮
tags: highlight; 

代码不高亮

**Terminal**
.bashrc lost.
sudo cp /etc/skel/.bashrc ~/

**Tabby**
/bin/bash not
/usr/local/bin/bash work
sudo cp /bin/bash /usr/local/bin/bash
tabby: 配置链接-管理配置-新建-新建配置







### 支持增量/差异备份
tags: backup;
- timeshift
- rsync, backintime, 
- 傲梅，diskgenius, 

diskgenius 系统迁移，或者硬盘克隆，很好用[调皮][调皮][调皮]
### shortcut key

setup: ctrl + alt + ,

windows:
alt + F3: gui menu to some shortcut key,
menu: open gui menu
menu + pageUp: max the windows, agin, back to origin.
menu + pageDown: min the windows, agin not back, alt + tab to back origin. 

tab windows:
ctrl + tab: swtich,
ctrl + t: new tab,
ctrl + w: close current tab


GUI dir:
alt + <-|->


### Qtscrcpy
tags: qtscrcpy;
功能 	快捷键(Windows) 	快捷键 (macOS)

切换全屏 	Ctrl+f 	Cmd+f
调整窗口大小为 1:1 	Ctrl+g 	Cmd+g
调整窗口大小去除黑边 	Ctrl+w | 左键双击 	Cmd+w | 左键双击
点击 主页 	Ctrl+h | 点击鼠标中键 	Ctrl+h | 点击鼠标中键
点击 BACK 	Ctrl+b | 右键双击 	Cmd+b | 右键双击
点击 APP_SWITCH 	Ctrl+s 	Cmd+s
点击 MENU 	Ctrl+m 	Ctrl+m
点击 VOLUME_UP 	Ctrl+↑ (上) 	Cmd+↑ (上)
点击 VOLUME_DOWN 	Ctrl+↓ (下) 	Cmd+↓ (下)
点击 POWER 	Ctrl+p 	Cmd+p
打开电源 	右键双击 	右键双击
关闭屏幕 (保持投屏) 	Ctrl+o 	Cmd+o
打开下拉菜单 	Ctrl+n 	Cmd+n
关闭下拉菜单 	Ctrl+Shift+n 	Cmd+Shift+n
复制到剪切板 	Ctrl+c 	Cmd+c
剪切到剪切板 	Ctrl+x 	Cmd+x
同步剪切板并粘贴 	Ctrl+v 	Cmd+v
注入电脑剪切板文本 	Ctrl+Shift+v 	Cmd+Shift+v


老硬件debian新硬件fedora，

### Fcitx5-rime
tags: rime; fcitx5;

apt-cache search fcitx5 
sudo apt install fcitx5-rime
ls -ashl .local/share/fcitx5/rime/
ls -ashl .local/share/fcitx5/rime/build/
setui add rime, restart
cd .local/share/fcitx5/rime/build/
cp default.yaml default.yaml.bak
cp ~/blog/unix/fcitx5-rime/build/* ./
setui select, restart


### sync
foldA -> foldB
SOURCE=""
DESTINATION=""
rsync -avz "$SOURCE" "$DESTINATION"

### Timeshift
tags: timeshift

只要不懂的目录都不排除,
只排除自己完全懂的.

- Exclude Dir : blog; data2025.------Source.list, upgrade, timeshift.  curl,vim, vim-doc, vim-scripts, universal-ctags,git config,first push-
- 
- highlight lost, cp bashrc
- add fcitx5-rime
- rsync: hard usb.
- 
- gparted,remove apache2,firefox
-
- remove vim,vim-gtk3/gnome, update python3-samba,nodejs,yarn,vundle,
-
- vim markdown-review, by vundle, but slowly.
- From: zhihu/gaoxiaozhuobiji:vim+markdown, bashrc: grep_edit()
- flatpak: audiorelay
- python3,python3-venv,python3-pip,python3-dev
- firefox about:addons: dark reader, github search, immersive_translate, oludict
- 
- off-edit
- grub
- quicknote








