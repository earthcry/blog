





### 
dpkg --list | grep apache2

### deb appimage

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
```





老硬件debian新硬件fedora，
