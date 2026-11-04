# linux phone

Linux Phone 
Linux手机，Android手机。

### 手机刷android 
- 资源地址
- 操作步骤
- 概念原理本质道理说明
- 
- [ ] android update to 11.1.22
- yun.daxiaamu.com baidudisk oos10.3.8,update620
- dev-oem-usbdebug
- debian, android-tools-adb, fastboot
- 


msm tool
线刷
卡logo, recovery, format


### 一加6刷Nura/PostMarketOS 

PostMarketOS/Nura/AlpineLinux
apk add vim

一加6t要比6在网络和usb上支持好

用途，mobile linux server


四个桌面，phosh, gnome-mobile
- 如果只是想把它当服务器用，纯命令行，选“console”，最省资源。\n
- 如果想体验图形桌面，选“xfce4”，这是轻量级桌面环境，2GB内存跑得动。\n
- 想尝鲜类似智能手机的触控界面，可以选“phosh”或“plasma-mobile”，但红米Note3跑起来会有些吃力，体验一般。


adb fastboot
install android-tools-adb
install android-tools-fastboot

install android-sdk-platform-tools

分区：

- boot_a
- boot_b
- system
- userdata
- dtbo
- 

进入fastboot模式，
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

二、自定义构建custom built
PMBootstrap会在电脑上先构建出nura再刷进手机
### pmbootstap install and build img

- [ ] 用pip 安装
"# 更新Ubuntu镜像源 
sudo apt-get update && upgrade

"# 安装刷机所需要的软件
sudo apt-get install -y git python-pip3 android-tools-adb android-tools-fastboot

"# 初始化pmbootstrap环境
pip3 install --user pmbootstrap

"# 生效当前环境变量，如果不生效环境变量 pmbootstrap命令使用不用了
source ~/.profile
"

- [ ] 用deb文件安装
Python 3.10 或更高版本、安装了 OpenSSL 和 Git 的 Linux 发行版上运行。
install python3 python3-dev python3-pip -venv

- [ ] wget https://mirrors.tuna.tsinghua.edu.cn/debian/pool/main/p/pmbootstrap/pmbootstrapx.deb
apt install pmbootstrapx.deb
pmbootstrap --version


- [ ] pmbootstrap init 
work path /home/user/.local/var/pmbootstrap
    - last release stable not edge 
    - 一般默认
    - qmenu oneplus
    - stable not nightly，
    - vim

- [ ] 设置换镜像源！！！
通过 pmbootstrap config 更新镜像配置。
测试镜像源速度，
pmbootstrap config mirrors.alpine https://mirrors.nju.edu.cn/alpine/
pmbootstrap config mirrors.pmaports https://mirrors.nju.edu.cn/postmarketOS/
pmbootstrap config mirrors.systemd https://mirrors.nju.edu.cn/postmarketOS/extra-repos/systemd/
mirrors.tuna.tsinghua.edu.cn
其中 mirrors.alpine 部分也可前往 Alpine 帮助 选择其他的镜像站。

init 6

移除镜像配置
pmbootstrap config -r mirrors.alpine
pmbootstrap config -r mirrors.pmaports
pmbootstrap config -r mirrors.systemd

pmbootstrap status
pmbootstrap update  --non-existing

- [ ] pmbootstrap install, build img

- [ ] full del pmbootstrap 
- pmbootstrap export
- pmbootstrap log
- 许多问题可以通过清除缓存或删除用于构建镜像/包的文件来解决。如果其他方法都无效，可以尝试运行 pmbootstrap zap （对所有问题回答“y”）
以通过添加 -a 标志来强制删除所有缓存数据：
$ pmbootstrap zap -a

日志文件位于 pmbootstrap 的工作目录下；默认情况下，其位置是 ~/.local/var/pmbootstrap/log.txt 。如果你不确定自己的工作目录在哪里，可以使用以下命令进行检查：

$ pmbootstrap config work
/home/user/.local/var/pmbootstrap


三、刷机
fastboot format system
sudo fastboot erase userdata
pmbootstrap fasher flash_rootfs --partition=userdata
pmbootstrap fasher flash_kernel
pmbootstrap chroot fastboot reboot 命令

四、备份userdata 
fastboot getvar all > android_device_backup.txt
adb pull /data/local/tmp/userdata_backup.img


2.2 定制Recovery与备份：最好别省这一步\npostmarketOS的官方镜像走的是Fastboot直刷路线，理论上不装TWRP也能刷机。但我还是强烈建议先刷一个TWRP恢复环境，用它把当前的Android系统完整备份一份，尤其是 boot 、 system 、 vendor 、 persist 这4个分区。\n\n为什么要备份这些分区：\n\nboot里是Android内核和dtb，刷机后想回Android系统时，可以直接用备份恢复。\nsystem里是完整Android系统，体积大但备份了等于有后悔药。\nvendor里存的是硬件固件和驱动，postmarketOS某些组件可能会依赖vendor分区里的固件，保持原样最稳妥。\npersist分区存放最终校准数据，包括传感器、Wi-Fi MAC等敏感参数，这个分区一般不用刷但一定要知道它是干什么的。\n刷TWRP的通用做法是把 twrp-xxx-fajita.img 放到电脑，手机关机进Fastboot，执行 fastboot boot twrp-xxx-fajita.img 。注意这里用的命令是 fastboot boot 而不是 fastboot flash ，它只会临时引导一次TWRP，不写死到分区，对新手更安全。进TWRP后就能在界面上操作“Backup”功能，把备份文件存到外接U盘或通过adb pull拉出来。


五、使用官方预构建的镜像，pre-built
mkdir plasma-mobile && cd plasma-mobile
 
wget https://images.postmarketos.org/bpo/v25.12/oneplus-fajita/plasma-mobile/20251222-1250/20251222-1250-postmarketOS-v25.12-plasma-mobile-6-oneplus-fajita-boot.img.xz
 
wget https://images.postmarketos.org/bpo/v25.12/oneplus-fajita/plasma-mobile/20251222-1250/20251222-1250-postmarketOS-v25.12-plasma-mobile-6-oneplus-fajita.img.xz
 sha256sum path-to-image-file.img.xz
$ sha512sum path-to-image-file.img.xz

$ xz --decompress path-to-image-file.img.xz

xz -tk 20251222-1250-postmarketOS-v25.12-plasma-mobile-6-oneplus-fajita-boot.img.xz ### boot.img 20251222-1250-postmarketOS-v25.12-plasma-mobile-6-oneplus-fajita.img.xz  ### system.img

sudo fastboot flash boot boot.img
sudo fastboot erase system ### 防出错
sudo fastboot flash userdata system.img
sudo fastboot reboot

刷写进去后使用fastboot reboot重启设备，主要不要长按电源开关机键重启，这样是确保数据正确写入。
system分区不够大，装不下这个镜像。
进入系统的默认密码是147147。

六、

在 postmarketOS 上，用户可以使用 GNOME Software 安装和更新软件，也可以从 Alpine 和 postmarketOS 仓库以及 Flatpaks（来自 Flathub）安装软件包。


### AlpineLinux
- alpinelinux.org/.cn
- small simple secure
- Docker镜像体积可控制在5MB以内，并因此成为容器化部署中广泛使用的基础镜像。
- 典型应用场景：容器化部署、网络安全设备、嵌入式系统,树莓派，路由，mobile,嵌入设备，netboot, vm, 
- 通过GitLab平台协作维护，
- 采用滚动更新模式。
- 软件包更新策略包含：
    - 每日构建测试的edge分支；
    - 半年周期的稳定版本维护；stable
    - 关键安全漏洞修复响应时间小于24小时
- 软件仓库包含三个层级：
    - main：经过完整兼容性测试的核心组件；
    - community：开发者提交的第三方应用；
    - testing：实验性功能预发布区。
- Shell 既是一种脚本编程语言，也是一个连接内核和用户的软件。
- sh, cat/etc /shells 
- Terminal 负责输入和显示的交互界面，
- TTY/PTY 负责连接终端程序与进程，
- SSH 负责把这种交互安全地延伸到远程计算机。
- Shell 是命令解释程序Shell 负责理解和执行命令，
-  https://wiki.alpinelinux.cn/wiki/Comparison_with_other_distros
- 

### PostMarketOS/Nura

- 项目背景‌：由 Oliver Smith 发起开发，
- nura.eco
- Nura赋予用户对设备的完全控制。
- pm是一个专为智能手机设计的开源 Linux 发行版‌，
- 基于 Alpine Linux 构建，
- 让用户能完全控制设备并延长旧手机使用寿命，
- 官网为 postmarketos.org。
- 核心定位‌：postmarketOS 不是"手机android或ios平台上的 一个Linux 应用"，而是把完整的 Linux 桌面环境直接运行在手机硬件上，让手机真正变成一台 Linux 电脑 。‌‌‌
- 采用上游优先策略，使用主线 Linux 内核而非厂商定制版本，可持续获得安全更新。
- 与 Android 区别‌：用户可备份完整主目录、安装任意 Linux 软件包 。‌‌
- that command should be run as a regular user ($), or as root (#).
- 



#### Fully uninstall pmbootstrap
$ pmbootstrap shutdown
$ pmbootstrap zap -p


### pmbootstrap usage 