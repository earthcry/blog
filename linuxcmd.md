











scp —r -P 8022 yuan u0-a275@192,168.41.217:wenjianjia

### Flatpak
sudo apt install flatpak

    添加Flathub软件仓库‌：
        运行命令：flatpak remote-add --if-not-exists flathub https://dl.flathub.org/repo/flathub.flatpakrepo‌‌1‌‌5
        （可选）国内镜像加速（如中科大源）：
        flatpak remote-modify flathub --url=https://mirrors.ustc.edu.cn/flathub‌‌3

‌安装Flatpak应用程序‌

根据获取方式选择以下任一方法：

    ‌通过应用ID安装‌（推荐）：
        搜索应用ID：flatpak search <应用名>（例如 flatpak search thunder）。‌‌3‌‌6
        执行安装：flatpak install flathub <应用ID>（例如 flatpak install flathub com.xunlei.Thunder）。‌‌7‌‌8

    ‌直接安装.flatpakref文件‌：
        双击下载的.flatpakref文件，系统将自动调用安装程序。‌‌9
        或使用命令：flatpak install <文件名>.flatpakref‌‌9

flatpak install flathub id
flatpak run org.gimp.GIMP
flatpak update
flatpak uninstall id
flatpak remove --unused


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
