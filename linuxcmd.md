







### make install 编译安装

1. download

cd /usr/local/src && \
wget http://nginx.org/download/nginx-1.15.4.tar.gz

2. install depend

apt install -y gcc openssl-devel pcre-devel zlib-devel

3. unzip

tar -zxvf nginx-1.15.4.tar.gz -C /usr/local
cd /usr/local/nginx-1.15.4

4. build makefile and refer install path

./configure --prefix=/usr/local/nginx

5. make && make install


### list process
top
ps -ef
pgrep sshd
lsof -i:port
kill id

### 
dpkg --list | grep apache2

### Install .deb appimage

**AppImage** 一个程序一个文件。
```
chmod +x xxx.appimage
./xxx.appimage
```

**deb**
```
sudo apt install xxx.deb
```
 由于文件'/root/下载/xxxt.deb'无法被用户'_apt'访问，已脱离沙盒并提权为根用户来进行下载。 - pkgAcquire::Run (13: 权限不够)

不让通过apt的方式安装解决的办法是，直接双击，通过系统自带市场进行安装或者
```
sudo dpkg -i xxx.deb
sudo apt-get install -f
```
or
sudo apt install gdeb-core
sudo gdeb install xxx.deb

### switch root

su root
or 
su -
sudo passwd root


老硬件debian新硬件fedora，

ip addr show
du -sh ./ # display size, du=disk usage
