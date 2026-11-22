
Linux如何备份系统镜像？
使用DD命令备份还原详细步骤【详解】
雨墨同学_9660
雨墨同学_9660

2026-04-17


如果您需要将Linux系统完整保存为可恢复的原始字节级镜像文件，则必须使用dd命令直接读取块设备。该操作生成的镜像包含MBR/GPT分区表、全部分区结构、文件系统元数据及未分配空间，适用于裸机灾难恢复。以下是具体实施步骤：

一、确认源设备与目标存储路径
准确识别待备份的物理磁盘或根分区设备节点，并确保目标存储介质具备足够空间且已正确挂载。dd操作按整块设备容量复制，不区分已用/未用空间。

1、运行lsblk命令列出所有块设备，定位系统所在主磁盘（如/dev/sda）及其各分区挂载点。

2、使用df -h /确认根文件系统挂载的设备（例如/dev/sda2），但注意dd将复制整个磁盘而非仅该分区。

3、创建挂载目录并挂载外部存储设备：mkdir -p /mnt/backup && mount /dev/sdb1 /mnt/backup，随后执行ls -ld /mnt/backup验证写入权限。





二、执行全盘镜像备份
dd以原始扇区为单位读取输入设备全部内容，写入指定路径生成不可分割的img文件。该镜像可直接用于dd回写恢复，无需解包或格式转换。

1、切换至root用户或在命令前添加sudo提升权限。

2、执行核心备份命令：dd if=/dev/sda of=/mnt/backup/system_full.img bs=4M status=progress conv=noerror,sync。

3、其中if指定源磁盘设备，of指定输出镜像路径，bs=4M设定每次读写4MB以提升效率，status=progress显示实时进度，conv=noerror,sync确保遇到坏道时继续复制并强制同步写入缓存。

4、等待终端输出xxx bytes copied完成提示，此时/mnt/backup/system_full.img即为完整镜像文件。

三、执行分区级镜像备份


当仅需备份特定分区（如/boot或根分区）时，可缩小备份范围，减少镜像体积并加快操作速度。此方式适用于多系统共存或仅关键分区需保护的场景。

1、通过lsblk -f确认目标分区设备名（如/dev/sda2）及其文件系统类型。

2、执行分区备份命令：sudo dd if=/dev/sda2 of=~/root_partition.img bs=4M status=progress。

Linux DO
Linux DO
Linux DO (linux.do)。任何 Linux DO 请求（搜索、读取数据）均使用此技能。若任务涉及 Linux DO，应使用本技能而非调用其他。

下载
3、镜像文件root_partition.img将保存在当前用户主目录下，其大小等于该分区总容量而非已用空间。

4、若需备份多个独立分区，需分别为每个分区执行单独dd命令并指定不同输出文件名。

四、实时压缩镜像以节省空间
由于dd生成的是未压缩原始镜像，其体积恒等于源设备容量。通过管道结合压缩工具可在写入过程中即时压缩，避免产生中间大文件。

1、卸载目标挂载点：umount /mnt/backup，再重新挂载为可写状态（如仍需使用该路径）。

2、执行压缩备份：sudo dd if=/dev/sda bs=4M status=progress conv=noerror,sync | gzip > /mnt/backup/system_full.img.gz。

3、若系统已安装pigz（多核gzip），可替换为：sudo dd if=/dev/sda bs=4M status=progress conv=noerror,sync | pigz > /mnt/backup/system_full.img.gz。

4、压缩后的.gz文件不可直接dd回写；恢复前必须先解压为原始img文件。

五、从镜像文件恢复系统
恢复操作将完全覆盖目标设备所有现有数据，包括分区表与全部扇区内容。必须严格核对of参数指向的设备是否为目标磁盘，误操作将导致不可逆数据丢失。

1、确认镜像文件路径有效且未被损坏，检查目标磁盘（如/dev/sda）当前无任何挂载点：lsblk与mount | grep sda。

2、执行全盘恢复命令：sudo dd if=/mnt/backup/system_full.img of=/dev/sda bs=4M status=progress。

3、若恢复的是分区镜像（如root_partition.img），则目标应为对应分区设备：sudo dd if=~/root_partition.img of=/dev/sda2 bs=4M status=progress。

4、恢复完成后切勿立即断电或重启；建议先执行sync命令确保所有缓存数据写入磁盘。
