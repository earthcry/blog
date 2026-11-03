### 在手机上安装完整且带桌面的linux

- [ ] termux-setup-storage
https://wiki.termux.com/wiki/Internal_and_external_storage

- [ ] android root, linux deploy

- [ ] From:

CSDN/DCTANT/【合作原创】使用Termux搭建可以使用的生产力环境（四）


- [ ] termux, termux-x11
- battery,lock,
- termux-setup-storage, share storage
- 打开“授予管理所有文件的权限”这个开关，让Termux可以访问系统文件。
- 
- [ ] 切换源
- termux-change-repo
- Chinese Mainland”，然后必须按一下空格键确认选择才行！！否则是不生效的！！最后按回车完成该切换！！
- pkg i -y openssh vim git curl proot-distro pulseaudio 
- passwd
- sshd
- whoami
- ifconfig
- touch .bashrc  #sshd autorun
- nano .bashrc  # 在nano内write，sshd
- ctrl+O enter,ctrl+x
- 
- 
- [ ] termux-ubuntu
- proot-distro, 安装linux的发行版，
- proot-diatro list
- proot-distro install ubuntu
- proot-distro login ubuntu
- # super user, $ normal user
- app-arm64-v8a-debug.apk，+ down
- pkg i -y termux-x11-nightly
- termux-x11 :3 >/dev/null &
- 其中termux-x11就是程序名。:3为显示编号，为了防止与之前的教程中的显示编号冲突，这里采用3号显示。>/dev/null是重定向输出，将日志全部丢弃。&则告诉系统不要阻塞当前终端会话，让termux-x11这个程序在后台执行。
- 
- [ ] termux-debian
- proot-distro install debian
- https://github.com/termux/proot-distro/releases/download/v4.7.0/debian-bookworm-aarch64-pd-v4.7.0.tar.xz
- proot-distro login debian
- cp /etc/apt/sources.list /etc/apt/sources.list-bak
- nano /etc/apt/sources.list
- Ctrl+k，3次删除原有，
- deb [signed-by="/usr/share/keyrings/debian-archive-keyring.gpg"] https://mirrors.aliyun.com/debian bookworm main contrib
deb [signed-by="/usr/share/keyrings/debian-archive-keyring.gpg"] https://mirrors.aliyun.com/debian bookworm-updates main contrib
deb [signed-by="/usr/share/keyrings/debian-archive-keyring.gpg"] https://mirrors.aliyun.com/debian-security bookworm-security main contrib
- 按Ctrl+O保存，按回车键确认，最后按Ctrl+X退出nano编辑
- apt update
- 由于Termux不可能直接利用手机显示屏直接显示桌面环境，除非彻底刷机.因此需要特定的软件去显示xfce桌面的内容.
- VNC Server（后面简称vnc）和
- Termux-X11（后面简称t-x11
- 
- 组合c：Debian-xfce+Debian-vnc（在Debian内装一个自己的VNC Server）

组合d：Debian-xfce+Termux-vnc（Debian使用Termux的VNC Server）

组合e：Debian-xfce+Termux-t-x11（Debian使用Termux的Termux-X11）
- 
- 
- proot-distro login debian
- apt install -y dbus-x11
- ，桌面应用程序之间的消息总线
- apt install -y  tigervnc-standalone-server
- 设置显示序号:
- export DISPLAY=:1  
- 注意！这里:1对应的vnc端口就是5901，如果:2就是5902，依此类推。
- 
- 安装xfce桌面
- apt install -y xfce4
- 
- 
- [ ] 解决声音问题
- 目前Termux中是没有安装声音驱动的，这会导致进入xfce桌面后完全没有声音，xfce还会报找不到音频的错，
- 
- pkg i pulseaudio -y
- 
- 启动声音组件
- 
- pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1
- 
- 加入自启
- 
- nano .bashrc
pulseaudio --start --load="module-native-protocol-tcp auth-ip-acl=127.0.0.1 auth-anonymous=1" --exit-idle-time=-1
- 
- 安装附加组件
- 
- 补充安装一下xfce4-goodies和xfce4-terminal。xfce4-goodies是一组为 Xfce 桌面环境设计的增强工具和插件集合。xfce4-terminal是 Xfce 桌面环境的官方终端模拟器。
- 
- proot-distro login debian
- apt install -y xfce4-goodies xfce4-terminal
- apt remove xfce4-power-manager
- exit
- 
- 
- [ ] 备份proot-distro内的系统
- 
- proot-distro backup debian --output debian-backup-2024.12.7.bak
- 
- 其实这个命令就是把/data/data/com.termux/files/usr/var/lib/proot-distro/installed-rootfs/debian，这个目录和一个自动生成的Shell脚本打成一个tar包而已。
- 将包备份到电脑或
- 
- 还原系统
- 
- proot-distro restore debian-backup-2024.12.7.bak
- 
- [ ] 进入xfce桌面系统
- 
- proot-distro login debian
- export DISPLAY=:1
- vncserver -xstartup /usr/bin/startxfce4 -localhost no
- 
- 第一行指定显示编号，同时也间接指定了vnc服务器的端口号，如果:1就是5901端口，如果是:2就是5902端口，依此类推。
- 
- 第二行是启动vnc服务器，外加启动xfce4桌面，-localhost no指的是非本机模式，也就是整个局域网都能连接这个vnc服务器。
- 
- [ ] 关闭VNC服务器
- 
- vncserver -kill :1
- 
- 这个命令用于关闭VNC服务器，冒号后面的就是对应的显示序号。这种关闭属于符合流程的正常关闭VNC服务器，锁文件也会一并自动删除。
- 
- [ ] 解除VNC锁
- 
- 如果你的VNC服务器没有按照正常流程关闭，而是通过kill，或者划掉Termux APP或者出现了signal 9导致的意外关闭，则需要删除对应的VNC锁才行，不然5901就被占用了，会自动延续到5902等等。
- 
- rm -rf /tmp/.X1-lock
- rm -rf /tmp/.X11-unix/X1
- 
- X1-lock、X1对应的是5901
- 
- X2-lock、X2对应的是5902，依此类推，删除之后再启动VNC服务器就能通过5901启动了，而不是往后的端口号。
- 
- [ ] 启动xfce失败
- 
- 实测小米11无法启动xfce桌面系统，13，
- 
- 
- 
- [ ] Termux中安装并启动termux-x11
- 
- 
- pkg i -y termux-x11-nightly
- 与外部app适配适配
- 
- 启动termux-x11
- 
- termux-x11 :3 >/dev/null &
- 
- 其中termux-x11就是程序名。:3为显示编号，为了防止与之前的教程中的显示编号冲突，这里采用3号显示。>/dev/null是重定向输出，将日志全部丢弃。&则告诉系统不要阻塞当前终端会话，让termux-x11这个程序在后台执行。
- 
- 这时启动termux-x11是命令行
- 
- [ ] 启动xfce桌面
- 
- proot-distro login debian --shared-tmp -- /bin/bash -c 'export GTK_IM_MODULE=fcitx && export QT_IM_MODULE=fcitx && export XMODIFIERS=@im=fcitx && export PULSE_SERVER=127.0.0.1 && export XDG_RUNTIME_DIR=${TMPDIR} && export DISPLAY=:3 && startxfce4'
- 
- 
- 解释一下这个命令：

proot-distro login debian：用过很多次了，就是用于登录到Debian系统

--shared-tmp：将termux中的临时目录模拟出来给Debian使用，方便Debian和termux之间临时进行数据交互操作

-- /bin/bash -c：使用Debian环境去执行后续命令，后续命令通过单引号囊括

export GTK_IM_MODULE=fcitx && export QT_IM_MODULE=fcitx && export XMODIFIERS=@im=fcitx：用于指定输入法为fcitx，防止输入法出现问题

export PULSE_SERVER=127.0.0.1：使用本地音频服务，防止音频出现问题

export XDG_RUNTIME_DIR=${TMPDIR}：在基于 XDG（X Desktop Group）基本目录规范的 Linux 系统中使用。它主要用于指定用户运行时（runtime）文件和套接字（sockets）的基本目录，指定为TMPDIR，反正配置了不会错

export DISPLAY=:3：设置显示编号为3，需要和termux-x11指定的编号一致才行，不然会无法显示的

startxfce4：这个不用多说了，就是启动xfce桌面环境

注意！启动xfce4桌面过程中会有很多警告和报错，如果打开Termux-X11 APP桌面显示正常则不用管着报错信息，属于正常情况！


- [ ] 打开Termux-X11 APP
- 
- 修改Termux-X11 APP设置
- Preference
- Output:
- Reseed screen while soft keyboard is open，这个是点击右下角的键盘可以弹出手机的输入法，如果通过OTG外接键盘后建议取消勾选，如果没有的话，还是建议打开状态。
- 
- 修改Keyboard
- 这里修改的就是底部的黑色软键盘了.
- Show additional keyboard右边的齿轮。30%
- Prefer scancodes when possible：使用OTG连接物理键盘的时候建议打开，这样能保证键位映射不会出现问题.
- 
- 
- 
- [ ] 修改Linux时区和时间（debian）
1，date -R  查看时间和时区
2，sudo -i
3，cp /usr/share/zoneinfo/Asia/Shanghai /etc/localtime  修改为上海时区
4，date -s "2017-03-22 11:43:30"     手动设置系统时间，字符串形式
5，hwclock --systohc   将系统时间同步到硬件
- 
- 
- [ ] 安装软件
- 
- apt install -y firefox-esr  
- （Extended Support Release，简称
- 
- [ ] 安装中文字体
- 
- apt install -y fonts-noto-cjk fonts-wqy-microhei fonts-wqy-zenhei
- 







- [ ] 安装buzz？？？
- 
- PyPI推荐使用pip包管理器来下载第三方库。
- 安装python3-pip ffmpeg 
- 
- 
- [ ] 安装ffmpeg
- sudo apt-get install ffmpeg
#在最后PATH添加环境变量：
vi /etc/profile
#保存退出查看是否生效
export PATH=$PATH:/usr/local/ffmpeg
#设置生效
source /etc/profile

查看版本
 ffmpeg -version # 查询版本 
- 
- [ ] 安装 Poetry
- 
- curl -sSL https://install.python-poetry.org | python3 -
- 
- 将 Poetry 添加到 PATH（如果安装时未自动添加）：
- export PATH=$PATH:$HOME/.local/bin             
-   
- 验证安装
- 
- 安装完成后，运行以下命令验证：
- poetry --version    
- 
- [ ] 安装 Buzz
- 克隆项目仓库
- git clone https://github.com/chidiwilliams/buzz.git
- cd buzz
- 安装依赖
- poetry install
- 运行 Buzz
- python3 -m buzz
- 

