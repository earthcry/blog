
termux



pkg search
pkg install
pkg upgrade
pkg install vim-python
       curl wget unzip unrar 
       openssh git
       
ssh
cd .ssh // Test if have
pwd      // current dir
ssh-keygen -t rsa -C "email reg in github"
vim .ssh/id_rsa.pub
cp key to github/setting/ssh
head-bottom-desktopversion
ssh -T git@github.com  //test

git config --global user.email "mlinks@163.com"
git config --global user.name "earthcry"

-------------------------------- Old Version-------------------------------
设置默认编辑器
export EDITOR=vi

切换更新源
百度  termux 镜像

sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux stable main@' $PREFIX/etc/apt/sources.list
pkg up


直接编辑源文件:
vi  $PREFIX/etc/apt/sources.list
更换Termux清华大学源,加快软件包下载速度.
deb [arch=all,i686] http://mirrors.tuna.tsinghua.edu.cn/termux stable main

@shell @storage

cat /etc/shells

sudo chsh -s /bin/zsh  # switch shell, exit and restart.

zsh for outside storage

sh -c "$(curl -fsSL https://github.com/Cabbagec/termux-ohmyzsh/raw/master/install.sh)"

@挂载设备存储
termux 默认情况下无法直接访问 Android 设备的存储。你可以通过运行以下命令来请求存储权限：
termux-setup-storage
运行该命令后，你可以通过~/storage 目录访问存储。
ls ~/storage


@root
pkg install proot

termux-chroot


@Domain

DNS记录管理
哪怕是namecheap和http://name.com，他们的管理界面以2014年的眼光来看都不太好使，DNS刷新速度也不是很理想。我的做法一般是国外域名就直接把name server(域名服务器)转到Home | CloudFlare，国内的转到DNSPod-免费智能DNS解析服务商。速度快，界面好，免费。

https://www.sqlsec.com/2018/05/termux.html#Jupyter-Notebook


@ssh login termux

ssh-keygen -t rsa

ssh-copy-id -p 8022 u0_a108@192.168.43.1

ssh -p 8022 u0_a108@192.168.43.1

scp -P 8022 u0_a270@192.168.49.1:/data/data/com.termux/files/home/test.md ~/
scp -r -P 8022 u0_a270@192.168.49.1:/data/data/com.termux/files/home/apks ~/
speed is slowly

git origin url
origin  ssh://u0_a108@192.168.43.1:8022/data/data/com.termux/files/home/art.git (fetch)

