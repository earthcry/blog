Question:
phone lined Linux and open file transfer 
adb shell ls /sdcard/
permission denied

Reason
Linux does not have permission to access USB device.

解决方案
adb + jmtpfs + udev.rules
adb, transfer
jmtpfs, mount
udev rules, linux recognize phone as mtp device 


CSDN/ 小圆圆伍
无需手机root权限，也不必安装BusyBox
 3动手前的准备：装好adb、建好udev规则、拿稳授权
3.1 安装platform-tools
发行版仓库里的旧版本。旧版本adb对新手机的支持明显不足，经常会遇到莫名其妙的unauthorized或offline。
wget https://dl.google.com/android/repository/platform-tools-latest-linux.zip
unzip platform-tools-latest-linux.zip -d ~/android-sdk
export PATH=$PATH:~/android-sdk/platform-tools
export 这行命令建议写进 .bashrc 


3.2开启USB调试并完成授权
第一次插上USB线执行adb命令时，手机上会弹出授权确认框，一定要勾选“一律允许”。如果手快点了拒绝，后面所有挂载操作都会卡在unauthorized。碰到这种情况不需要慌张，删除本地的调试密钥再重来一次就行：
rm ~/.android/adbkey ~/.android/adbkey.pub
adb kill-server
adb start-server

3.3 配置udev规则

不配置udev规则的情况下， adb devices 会提示未授权

sudo tee /etc/udev/rules.d/51-android.rules <<EOF
SUBSYSTEM=="usb", ATTR{idVendor}=="2a70", MODE="0666", GROUP="plugdev"
EOF
sudo udevadm control --reload-rules
sudo udevadm trigger
adb kill-server && adb start-server

3.4 验证基础文件访问
adb shell ls /sdcard

4.1 MTP路线：jmtpfs装好即用

fusermount -u ~/mnt/android


4.2 adb路线：adbfs把你的 /sdcard 变成本地目录
构建adbfs之前，先确认系统有libfuse和pkg-config：
sudo apt install libfuse3-dev pkg-config
git clone https://github.com/lunaryorn/adbfs.git
cd adbfs
make
sudo cp adbfs /usr/local/bin/

mkdir -p ~/mnt/adbfs
adbfs ~/mnt/adbfs
fusermount -u ~/mnt/adbfs 卸载

它更适合“需要在文件管理器里像浏览Linux目录一样逛手机”的低频场景，而不是高频大量搬数据的日常路径。

4.3 我日常更依赖的“半挂载”组合

# 备份手机整个目录到本地
adb shell tar -czf - /sdcard/DCIM | tar -xzf - -C ~/backup/

# 安装调试包
adb install -r app-debug.apk

# 持续采集日志落盘
adb logcat -v time > app.log

# 快速查看应用私有文件
adb shell ls -la /sdcard/Android/data/com.example.app/files

这套组合没有单独挂载进程，不担心断线，哪一步报错就重新执行哪一步，还能顺手把采集日志、拷贝文件这些操作全部写进自动化脚本。实测速度比挂载稳定得多，也是我至今仍然高频使用的工作方式。

下面要么空空如也，要么能看到目录但进不去。这不是命令写错了，而是Android 11开始强制启用分区存储后，应用私有目录对外部使用者做了隔离。shell用户和adb虽然对 /sdcard 这个大目录有读写权，但其他应用创建的私有数据目录不再直接开放，看不到内容很正常。
，因为自己应用写入的数据通常还是落在 /sdcard/Android/data/你的包名/ 这类可见路径，或者独立的内部存储路径。如果是后者，还有一条不需要挂载的命令可以应急：
adb exec-out run-as com.example.app cat files/log.txt
这条命令利用调试模式下的run-as机制，直接读取自己应用的内部文件，不需要root，也不会被分区存储限制。
顺便提一下网上流传很广的“旁门左道”：用root直接绕过分区存储去读取所有应用的数据。这在开发机上确实可行，但它已经离开了“无需root”的前提。你的目标是调试自己的产品，就按Android官方设计的数据边界来走；如果非要去读取别人应用的私有数据，那已经不是正常开发范畴了。

adb pull /sdcard/bigfile.mp4 ~/downloads/ || adb pull /sdcard/bigfile.mp4 ~/downloads/

6.2 我现在保留下来的工作习惯\n日常开发时，我始终开着adb，手机保持“仅充电”模式。文件搬运以 adb pull/push 和tar管道为主，只有需要在文件管理器里像逛Linux目录一样查看手机时，才会临时挂载一个adbfs，用完立刻卸载。MTP那套jmtpfs，我基本只在批量处理图片素材时偶尔用一下，绝不拿它应对大文件。\n\n最后分享一个让我省了根线的小技巧：Android 11以上开了无线调试后，可以用 adb pair 把手机和Linux主机配对到同一局域网，后续文件传输都走Wi-Fi，不需要一直挂着USB线。第一次配对还是需要USB线授权一次，之后在工位上来回换不同设备测试时就方便很多了。整个这套无root挂载方案到今天已经稳定跑了很长时间，我的建议始终是：别迷信“挂载”这个词，多试试原生adb命令，你很可能发现效率更高。

始终失败，最终排查发现是主板BIOS中USB Legacy Support设置为Enabled，干扰了xHCI控制器的MTP握手流程。



### Linux下无root挂载Android手机为本地存储：jmtpfs实战指南 CSDN WongKosheng


1. 不用 root 也能把 Android 手机当 Linux 外置存储用：adb mtp + fuse + jmtpfs 实战落地指南

# Ubuntu/Debian
sudo apt update && sudo apt install -y build-essential autoconf automake libtool pkg-config libusb-1.0-0-dev libgcrypt20-dev

# Fedora/RHEL
sudo dnf groupinstall "Development Tools" && sudo dnf install -y autoconf automake libtool pkgconfig libusb1-devel libgcrypt-devel

# Arch Linux
sudo pacman -S --needed base-devel autoconf automake libtool pkgconf libusb libgcrypt

# 下载并编译 libmtp（跳过此步将导致 Android 12+ 识别失败）
wget https://github.com/libmtp/libmtp/releases/download/libmtp-1.1.18/libmtp-1.1.18.tar.gz
tar -xzf libmtp-1.1.18.tar.gz && cd libmtp-1.1.18
./configure --prefix=/usr --enable-libusb_1_0 --disable-mtpz
make -j$(nproc) && sudo make install
sudo ldconfig

3.2 获取并安装 jmtpfs（推荐静态链接版）
# 下载预编译二进制（省去编译 libfuse 依赖的麻烦）
wget https://github.com/JasonFerrara/jmtpfs/releases/download/v0.5.3/jmtpfs-0.5.3-x86_64-linux-gnu.tar.gz
tar -xzf jmtpfs-0.5.3-x86_64-linux-gnu.tar.gz
sudo cp jmtpfs-0.5.3-x86_64-linux-gnu/jmtpfs /usr/local/bin/
sudo chmod +x /usr/local/bin/jmtpfs

# 验证安装
jmtpfs --version  # 应输出 jmtpfs version 0.5.3

3.3 配置 adb 设备授权与 USB 模式

# 启动 adb server（确保非 root 用户可访问 USB）
sudo systemctl stop ModemManager  # ModemManager 会劫持 adb 设备
sudo usermod -aG plugdev $USER    # 将当前用户加入 plugdev 组
newgrp plugdev                    # 立即生效组权限（或重新登录）

# 手机端操作（必须手动确认！）：
# 1. 开启开发者选项（连续点击「关于手机」→「版本号」7 次）
# 2. 进入「开发者选项」→ 开启「USB 调试」
# 3. 用 USB 线连接电脑 → 手机弹出「允许 USB 调试吗？」→ 勾选「始终允许」→ 点确定

# 终端验证 adb 连通性
adb devices  # 应显示 "0123456789abcdef    device"
adb shell echo "OK"  # 应返回 "OK"，证明 shell 可用

3.4 创建挂载点并设置权限

# 创建挂载目录（不要用 /media 或 /run/media，那些被 udisks2 管理）
sudo mkdir -p /mnt/android
sudo chown $USER:$USER /mnt/android
sudo chmod 755 /mnt/android

# 验证权限（非 root 用户必须能进入）
ls -ld /mnt/android  # 应显示 drwxr-xr-x 1 youruser yourgroup ...

3.5 执行挂载命令（含防崩参数）

# 单次挂载（调试用）
jmtpfs -o allow_other,uid=$(id -u),gid=$(id -g),umask=000 -d $(adb get-serialno) /mnt/android

# 生产环境推荐：后台守护 + 自动重连
nohup jmtpfs -o allow_other,uid=$(id -u),gid=$(id -g),umask=000,devgid=plugdev -d $(adb get-serialno) /mnt/android > /var/log/jmtpfs.log 2>&1 &
echo $! > /var/run/jmtpfs.pid


3.6 验证挂载效果与基础操作

# 检查是否成功挂载
mount | grep android  # 应输出 jmtpfs on /mnt/android type fuse.jmtpfs ...

# 查看手机存储结构（Android 10+ 的 scoped storage 下，/sdcard 指向 /data/media/0）
ls -l /mnt/android/  # 应列出 DCIM/ Download/ Pictures/ 等标准目录

# 测试写入（创建测试文件）
echo "test from linux $(date)" > /mnt/android/Download/test_linux.txt
adb shell ls -l /sdcard/Download/test_linux.txt  # 应返回文件信息

# 测试读取（同步手机里最近 10 张照片）
find /mnt/android/DCIM/Camera -name "*.jpg" -printf "%T@ %p\n" | sort -n | tail -10 | cut -d' ' -f2- | xargs -I{} cp {} ~/Desktop/from_android/






#!/bin/bash
# android-mount.sh - 支持热插拔的智能挂载脚本
MOUNT_POINT="/mnt/android"
LOG_FILE="/var/log/android-mount.log"
DEVICE_SERIAL=""

# 检测 adb 设备（支持多设备，取第一个可用的）
detect_device() {
    local devices=$(adb devices | grep "device$" | awk '{print $1}' | head -1)
    if [ -n "$devices" ]; then
        DEVICE_SERIAL="$devices"
        echo "$(date): Found device $DEVICE_SERIAL" >> "$LOG_FILE"
        return 0
    else
        echo "$(date): No device found" >> "$LOG_FILE"
        return 1
    fi
}

# 挂载函数（含重试和超时）
do_mount() {
    for i in {1..3}; do
        if jmtpfs -o allow_other,uid=$(id -u),gid=$(id -g),umask=000,devgid=plugdev \
                --chunk-size=1048576 -d "$DEVICE_SERIAL" "$MOUNT_POINT" 2>>"$LOG_FILE"; then
            echo "$(date): Mount success for $DEVICE_SERIAL" >> "$LOG_FILE"
            return 0
        else
            echo "$(date): Mount attempt $i failed" >> "$LOG_FILE"
            sleep 2
        fi
    done
    return 1
}

# 主逻辑
if [ ! -d "$MOUNT_POINT" ]; then
    sudo mkdir -p "$MOUNT_POINT"
    sudo chown $USER:$USER "$MOUNT_POINT"
fi

# 卸载旧挂载（忽略错误）
fusermount -u "$MOUNT_POINT" 2>/dev/null

if detect_device; then
    if do_mount; then
        # 启动守护进程监控设备状态
        nohup bash -c 'while adb get-state >/dev/null 2>&1; do sleep 5; done; fusermount -u '"$MOUNT_POINT" > /dev/null 2>&1 &
        exit 0
    else
        echo "$(date): Mount failed after 3 retries" >> "$LOG_FILE"
        exit 1
    fi
else
    echo "$(date): No device, exiting" >> "$LOG_FILE"
    exit 1
fi

