### install 

在 Linux 或 macOS 上用 lsblk 或 diskutil list 看当前挂载的磁盘，插上读卡器之后再执行一次，多出来的那个就是目标设备。

lsblk
diskutil list

#先卸载目标设备上已自动挂载的分区
sudo umount /dev/sdX* 2>/dev/null

#写入镜像，块大小 4M 是速度与稳定性的平衡点
sudo dd if=2024-xx-xx-raspios-bookworm-arm64-lite.img of=/dev/sdX bs=4M status=progress conv=fsync

bs=4M 这个参数值得说一下。块太小（比如默认的 512 字节）会导致大量系统调用，写入速度极慢；块太大在某些读卡器上会出问题。4M 是实测下来兼容性和速度都不错的取值。 status=progress 让你能看到进度，不然 dd 全程静默，很容易误以为卡死了。 conv=fsync 保证数据真正落到卡上再返回，避免拔卡时数据还在缓存里。

#dd if=alpine-standard-3.24.4-x86_64.iso of=/dev/sdX bs=4M status=progress; eject /dev/sdX

If your version of dd does not support the option "status=progress", remove it. The eject command removes the target device from the system and ensures the write cache is completely flushed.
如果您使用的 dd 版本不支持“status=progress”选项，请移除该选项。 eject 命令可以将目标设备从系统中移除，并确保写缓存完全清除。

root 
pwd blank






### alpinelinux

Alpine Linux 是一款基于 musl libc 和 BusyBox 构建的轻量级 Linux 发行版，Docker 镜像体积仅约 5MB，专为容器化部署和安全敏感场景设计‌。‌‌

采用 musl C 标准库替代传统 GNU glibc，显著降低内存占用和系统体积。
集成 BusyBox 工具集提供基础 Linux 命令，完整安装仅需约 130MB 磁盘空间。
Docker 官方镜像体积控制在 5MB 左右，相比 Ubuntu 镜像（约 200MB）大幅减少。‌‌


### gnu
与Linux的关系
GNU 项目本身没有完成可用内核，1991年林纳斯·托瓦兹开发出Linux内核后，将其与GNU的所有系统组件结合，才形成了完整可用的自由操作系统，这也是很多人将主流Linux发行版称为“GNU/Linux”的原因。
Alpine Linux，就是刻意绕开了GNU生态的典型发行版：它不用glibc，改用musl轻量C库；不用GNU coreutils，改用BusyBox精简工具集，完全跳出了传统GNU/Linux的技术栈，实现了极致轻量化。



### busybox

模块化结构的系统安装调试和应用等工具庫。


### musl

系统底层核心编译工具庫。
一个轻量、快速、简单且免费的开源C标准库实现，
musl是一个开源的C标准库实现，HarmonyOS采用musl作为C标准库。


