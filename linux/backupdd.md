
# Linux如何备份系统镜像？
使用DD命令备份还原详细步骤【详解】
雨墨同学_9660
雨墨同学_9660

2026-04-17


如果您需要将Linux系统完整保存为可恢复的原始字节级镜像文件，则必须使用dd命令直接读取块设备。该操作生成的镜像包含MBR/GPT分区表、全部分区结构、文件系统元数据及未分配空间，适用于裸机灾难恢复。以下是具体实施步骤：

### 一、确认源设备与目标存储路径
准确识别待备份的物理磁盘或根分区设备节点，并确保目标存储介质具备足够空间且已正确挂载。dd操作按整块设备容量复制，不区分已用/未用空间。

1、运行lsblk命令列出所有块设备，定位系统所在主磁盘（如/dev/sda）及其各分区挂载点。

2、使用df -h /确认根文件系统挂载的设备（例如/dev/sda2），但注意dd将复制整个磁盘而非仅该分区。

3、创建挂载目录并挂载*外部存储设备*：
```
mkdir -p /mnt/backup && mount /dev/sdb1 /mnt/backup
```
随后执行ls -ld /mnt/backup验证写入权限。


### 二、执行全盘镜像备份
dd以原始扇区为单位读取输入设备全部内容，写入指定路径生成不可分割的img文件。该镜像可直接用于dd回写恢复，无需解包或格式转换。

1、切换至root用户或在命令前添加sudo提升权限。
2、执行核心备份命令：
```
dd if=/dev/sda of=/mnt/backup/system_full.img bs=4M status=progress conv=noerror,sync
```
3、其中if指定源磁盘设备，of指定输出镜像路径，bs=4M设定每次读写4MB以提升效率，status=progress显示实时进度，conv=noerror,sync确保遇到坏道时继续复制并强制同步写入缓存。

4、等待终端输出xxx bytes copied完成提示，此时/mnt/backup/system_full.img即为完整镜像文件。

### 三、执行分区级镜像备份


当仅需备份特定分区（如/boot或根分区）时，可缩小备份范围，减少镜像体积并加快操作速度。此方式适用于多系统共存或仅关键分区需保护的场景。

1、通过lsblk -f确认目标分区设备名（如/dev/sda2）及其文件系统类型。

2、执行分区备份命令：
```
sudo dd if=/dev/sda2 of=~/root_partition.img bs=4M status=progress
```

3、镜像文件root_partition.img将保存在当前用户主目录下，其大小等于该分区总容量而非已用空间。

4、若需备份多个独立分区，需分别为每个分区执行单独dd命令并指定不同输出文件名。

### 四、实时压缩镜像以节省空间
由于dd生成的是未压缩原始镜像，其体积恒等于源设备容量。通过管道结合压缩工具可在写入过程中即时压缩，避免产生中间大文件。

1、卸载目标挂载点：umount /mnt/backup，再重新挂载为可写状态（如仍需使用该路径）。

2、执行压缩备份：
```
sudo dd if=/dev/sda bs=4M status=progress conv=noerror,sync | gzip > /mnt/backup/system_full.img.gz
```

3、若系统已安装pigz（多核gzip），可替换为：
```
lsblk #find if dev
df -h  #had mounted part
sudo  fsck  -y  /dev/sda2
sudo  umount  /dev/sda2
apt install pigz
gparted #small rootfs part
su
dd if=/dev/sda bs=4M status=progress conv=noerror,sync | pigz > /mnt/backup/system_full.img.gz
```
4、*压缩后的.gz文件不可直接dd回写；恢复前必须先解压为原始img文件。*


### 五、从镜像文件恢复系统
恢复操作将完全覆盖目标设备所有现有数据，包括分区表与全部扇区内容。必须严格核对of参数指向的设备是否为目标磁盘，误操作将导致不可逆数据丢失。

1、确认镜像文件路径有效且未被损坏，检查目标磁盘（如/dev/sda）当前无任何挂载点：lsblk与mount | grep sda。

2、执行全盘恢复命令：
```
sudo dd if=/mnt/backup/system_full.img of=/dev/sda bs=4M status=progress
```
3、若恢复的是分区镜像（如root_partition.img），则目标应为对应分区设备：
gparted back part
```
gunzip ...
gparted
su
sudo dd if=~/root_partition.img of=/dev/sda2 bs=4M status=progress
gparted #fix
```
4、*恢复完成后切勿立即断电或重启；建议先执行sync命令确保所有缓存数据写入磁盘。*






# Linux 环境快速备份方案

小易撩挨踢
2026-09-03 09:27江苏
分整机系统备份、配置文件备份、已装软件列表备份、容器环境备份，根据场景选择，追求速度优先，不备份大日志 / 数据。

⚠️注意：不要备份 /proc /sys /dev /tmp /mnt 这些虚拟文件系统。

一、只备份配置文件（最快，日常环境备份推荐）
只备份系统配置、用户配置，不备份系统二进制，体积小速度快。

1. tar 打包关键配置
1
# 备份系统配置 + 用户家目录配置，排除缓存、日志
2
tar -czf config_backup_$(date +%Y%m%d).tar.gz \
3
--exclude=/var/log/* \
4
--exclude=/var/cache/* \
5
--exclude=/tmp/* \
6
--exclude=/dev/* \
7
--exclude=/proc/* \
8
--exclude=/sys/* \
9
/etc \
10
/root \
11
/home
恢复示例：

1
tar -xzf config_backup_20260902.tar.gz -C /
2. 导出已安装软件清单（重装系统必备）
Debian/Ubuntu
1
dpkg --get-selections &gt; packages.list
2
# 恢复
3
dpkg --set-selections &lt; packages.list
4
apt-get dselect-upgrade -y
RHEL/CentOS/openEuler
1
rpm -qa &gt; packages.list
2
# 恢复
3
yum install -y $(cat packages.list)
Alpine
1
apk info -q &gt; packages.list
2
#恢复
3
apk add $(cat packages.list)

二、整机系统备份（完整系统快照，迁移机器）
方式 1：tar 整机备份（通用，所有 Linux 发行版）
1
tar -czf full_backup_$(date +%Y%m%d).tar.gz \
2
--exclude=/full_backup*.tar.gz \
3
--exclude=/proc/* \
4
--exclude=/sys/* \
5
--exclude=/dev/* \
6
--exclude=/tmp/* \
7
--exclude=/mnt/* \
8
--exclude=/media/* \
9
/
不要在系统根目录下生成备份包，建议放到外接磁盘 / NFS 挂载目录。

方式 2：rsync 增量备份（适合频繁备份，速度更快，推荐生产）
rsync 只同步变更文件，第二次备份速度极快。

1
#备份整个系统到/mnt/backup磁盘
2
rsync -av --delete \
3
--exclude={"/proc/*","/sys/*","/dev/*","/tmp/*","/mnt/*","/media/*"} \
4
/ /mnt/backup/system_backup/
恢复：把目标盘挂载，反向 rsync 拷贝回去。

三、容器环境备份（Docker/iSulad）
如果你环境大量使用容器，不要 tar 整个系统，优先备份容器配置、镜像、卷。

1
#导出所有容器名称
2
docker ps -a --format '{{.Names}}' &gt; container_list.txt
3
4
#备份容器卷数据（卷路径 /var/lib/docker/volumes）
5
tar -czf docker_volume_backup_$(date +%Y%m%d).tar.gz /var/lib/docker/volumes
6
7
#导出镜像列表
8
docker images --format '{{.Repository}}:{{.Tag}}' &gt; docker_images.txt
iSulad 命令和 docker 基本兼容，替换docker为isula。

四、工具方案：一键备份工具
timeshift：桌面版 Linux 常用，快照式备份，只备份系统，不备份用户数据，适合 Debian/Ubuntu。
1
apt install timeshift
clonezilla 再生龙：整机磁盘镜像备份，适合服务器磁盘克隆，适合离线迁移。

五、最佳实践（快速备份工作流）
日常快速备份，不需要整机：

打包 /etc /root /home 配置文件 tar 包
导出软件包列表
Docker 环境额外备份 volume 卷
将备份文件拷贝到外部存储 / NFS / 对象存储，不要留在本机磁盘
六、避坑要点
备份时尽量停止业务服务，避免文件处于写入状态，备份文件损坏；
虚拟目录 /proc /sys /dev 一定不要打包；
大文件目录（数据库数据、日志）用--exclude排除，提升备份速度；
恢复前先测试 tar 包完整性：tar -tzf xxx.tar.gz
本文原创作者：易君召，详见：https://www.yijunzhao.cn/authors/yijunzhao，转载请注明出处。
原文链接https://www.yijunzhao.cn/archives/linux-quick-backup-solutions-guide
欢迎访问小易撩挨踢
https://www.yijunzhao.cn/