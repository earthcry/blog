
一加6 刷TWRP root（处理Qualcomm Crashdump Mode） 原创

2023-04-19 22:23:20
目录

前言

刷入官方OxygenOS固件：

强制禁用驱动程序签名（win10）

安装OnePlus 6驱动

使用MsmDownloadTool V4.0

手机root

解锁BL（会清除所有数据）

刷入第三方Recovery和Magisk：

下载twrp：

下载Magisk：

刷入：

结尾：

前言
        有需求需要个已经root的手机进行操作，找到了之前的一加6手机，但是之前折腾刷机版本兼容问题，当我想刷TWRP然后root的时候发现了下图这个问题，报如下错误：

Qualcomm Crashdump Mode

"Attemped to kill init! exitcode=0x0000000b, complete_and_exit"



刷入官方OxygenOS固件：
强制禁用驱动程序签名（win10）
win10以后需要禁用驱动程序签名，所以首先需要禁用程序签名

开始---运行，输入gpedit.msc（win10 家庭版本没有，可以去网上找开启的方法）





 开始菜单->更新和安全->恢复->高级启动（立即重启）



 重启成功后点击疑难解答---高级选项---启动设置---最后点击“重启”

重启后在启动设置界面，选择“禁用驱动程序强制签名” 



这就禁用了驱动程序强制签名 。

安装OnePlus 6驱动
首先安装Qualcomm HS-USB QDLoader 9008 Driver

安装成功后在右键电脑->管理

这个时候 只按住手机的音量＋键，等待5秒左右会出现下面，就可以了。



使用MsmDownloadTool V4.0
下载Decrypted OxygenOS 10.3.5，地址如下（需要梯子）：

运行MsmDownloadTool V4.0.exe ​​，链接成功后点击start，等待写入完成即可。

 手机重启完成后，就成功的刷入了官方的OxygenOS 10.3.5。

手机root
解锁BL（会清除所有数据）
首先需要我们解锁手机的BL锁，方法如下：

1. 手机打开开发者模式（设置→关于手机→快速连按5次版本号开启），设置oem锁允许（设置→系统→开发者选项→OEM解锁）。

2. 启动到bootloader模式（设置→开发者选项→打开高级重启），

按电源键选择“引导加载器”重启。

3. 手机连电脑，在cmd窗口内输入adb命令：

fastboot oem unlock

然后回车，手机即出现解锁确认界面，按音量键调到最下面一个选项，UNLOCK开头，按电源键确认，手机重启开始解锁，耐心等待即可，解锁成功显示新机的的欢迎界面。

刷入第三方Recovery和Magisk：
下载twrp：
首先下载twrp，去下载对应版本的twrp，下载地址如下：

https://dl.twrp.me/enchilada/

找到对应的版本，这里我使用的是twrp-3.4.0-0-enchilada-Q-mauronofrio

下载twrp-3.4.0-0-enchilada-Q-mauronofrio.img和twrp-3.4.0-0-enchilada-installer-mauronofrio.zip

下载Magisk：
下载地址如下：

Releases · topjohnwu/Magisk · GitHub



 下载zip，非APK。

刷入：
手机开机链接USB，并打开USB调试模式，并将twrp-3.4.0-0-enchilada-installer-mauronofrio.zip和Magisk-v21.4.zip放入手机

输入命令：adb reboot bootloader

进入引导模式后输入命令：fastboot boot twrp-3.4.0-0-enchilada-Q-mauronofrio.img

进入twrp界面后，安装twrp-3.4.0-0-enchilada-installer-mauronofrio.zip

选择install->选择twrp-3.4.0-0-enchilada-installer-mauronofrio.zip->然后滑动安装



安装完成后点击Reboot->Recovery开始重启

重启成功后安装点击install->选择Magisk-v21.4.zip->然后滑动安装



安装成功后选择Reboot->poweroff关机再开机即可，等待一会可以看到安装成功了Magisk



 这个时候点击右上角的设置按钮，可以根据自己的需求进行选择哪些获取root权限

 

使用adb链接手机，输入

可以看到已经获得了root权限。



设置里可以看到哪些程序取得了root权限



结尾：
        因为电脑端的android模拟器有很多限制，很多应用会检测手机所处环境，虽然通过hook可以解决大部分的校验，但是太麻烦了，最好的办法就是使用真机，这样可以节省很多时间。

关于一加手机出现 qualcomm crashdump mode 解决办法
一加手机只要是 出现 qualcomm crashdump mode那么恭喜你百分百是CPU虚焊 要拆机的, 处理器那部分拆出来再装回去, 原理很简单 CPU虚焊的解决教程 本人聊QQ突然黑屏重启直接 qualcomm crashdump mode 好家伙9008刷还是开不了机 #include"stdio.h"voidfun(char*t,char*s){while(*t!=0)t++;while((*t++=*s++...
继续访问
crashdump(crashdumps文件夹可以删除吗)
crashdump(crashdumps文件夹可以删除吗) 本文介绍了电脑蓝屏和手机出现qualcommcrashdumpmode的情况及其处理方法。对于手机,建议尝试重启或前往售后检测;对于电脑蓝屏,可能原因包括病毒感染、硬件故障、驱动问题等,解决办法包括重启、安装补丁、查杀病毒、检查硬件、更新驱动等。此外,还提供了系统恢复和硬件检查的建议。
继续访问
MsmDownloadTool
MsmDownloadTool是一款用于刷写、升级和修复Qualcomm芯片手机的官方工具。它通常由Qualcomm官方发布，用于处理基于Qualcomm芯片的设备的固件刷写和修复。用户可以使用MsmDownloadTool将固件文件刷写到支持Qualcomm芯片的手机上，以解决软件问题或升级系统版本。这个工具通常用于恢复手机到出厂设置、修复软件故障或升级系统等操作。需要注意的是，使用MsmDownloadTool需要谨慎操作，因为错误的操作可能导致设备损坏。
热门推荐 关于一加手机出现 qualcomm crashdump mode 解决办法
一加手机只要是 出现 qualcomm crashdump mode那么恭喜你百分百是CPU虚焊 要拆机的, 处理器那部分拆出来再装回去, 原理很简单 CPU虚焊的解决教程 本人聊QQ突然黑屏重启直接 qualcomm crashdump mode 好家伙9008刷还是开不了机 诶FUCK一加，FUCK刘作虎，怪我有眼无珠 我朋友的 一加8 我的一加6都出现这个，这个不是巧合，这是通病 ...
继续访问
高通u-boot关闭crash dump_高通 crash dump mode
2.打开宏,但是makefile中屏蔽掉crashdump的编译,然后其他依赖的地方注释掉,在dump文件的地方,将broad_restar提前,直接重启板即可。 这个crash dump对于debug是一个很好的帮助,大概看了一下就是u-boot启动时会去固定地址读取固定的标记,这个标记不正常即意味着非正常重启,就把固定区域的内容通过tftp上传到到读服务器端...
继续访问
针对oneplus6 怎么选择lineage源码的什么分支_一加6 lineageos
fastboot boot /app4/twrp-3.7.0_11-0-enchilada.img#正常启动到twrp#twrp界面: wipe --> 格式化 data分区adb sideload lineage-17.1-20210119-nightly-enchilada-signed.zip 1 2 3 sideload走完 在twrp界面选择重启手机, 启动后崩溃进入Qualcomm Crashdump mode...
继续访问
最新发布 [手机Linux] onepluse6T 系统重新分区
安卓1+手机重新扩容分配系统分区大小
继续访问
小白刷机自救----逃出qualcomm crashdump mode
由于一直在折腾，也没想着记录下来，所以就没有特意拍照截图，但实在是太诡异了，而且折腾了我好久，让我这个i人都忍不住发声了！好在最后的结果还是好的。本文非专业教程，就是一个小白的日记，语言散漫啰嗦，望海涵！
继续访问
 
QPST捕获crashdumps时,无法进入Saharamode_qualcommcrashdumpmode...
资源浏览查阅169次。手机crash后,连接QPST无法进入saharamode。参考文件是高通文件,无法下载可以联系qualcommcrashdumpmode更多下载资源、学习资料请访问CSDN文库频道.
继续访问
lingeaOS 一加8T qualcomm creashdump mode高通崩溃
一加8T ，软件层面的qualcomm creashdump mode修复
继续访问
一加6T第三方TWRP-3.3.2B-fastboot模式刷写
标题“一加6T第三方TWRP-3.3.2B-fastboot模式刷写”涉及到的是为一加6T手机安装第三方恢复系统TWRP的过程，具体版本为3.3.2B，并且该过程是在fastboot模式下进行的。TWRP（Team Win Recovery Project）是一个开源的...
一加11刷写第三方twrp资源 多个版本+刷写步骤
在一加11手机上刷写第三方的TWRP（Team Win Recovery Project）是许多高级用户进行自定义系统修改的第一步。TWRP是一款开源的恢复环境，它提供了更丰富的功能，比如安装第三方ROM、备份系统、擦除数据等。本教程将...
一加8第三方TWRP-3.4.2B-fastboot模式刷写
标题“一加8第三方TWRP-3.4.2B-fastboot模式刷写”涉及到的是为一加8手机安装第三方恢复系统TWRP的过程，其中TWRP是Team Win Recovery Project的缩写，它是一个自定义的Android设备恢复程序，提供更高级的功能，如...
一加7第三方TWRP-3.3.1-fastboot模式刷写
【一加7第三方TWRP-3.3.1-fastboot模式刷写】是指在一加7手机上安装非官方的TWRP恢复程序的过程。TWRP（Team Win Recovery Project）是一个开源的自定义恢复系统，它提供了比原厂恢复更丰富的功能，如刷机、备份、...
一加8pro第三方TWRP-3.4.2B-fastboot模式刷写
一加8pro第三方TWRP-3.4.2B-fastboot模式刷写 请解锁bl后fast模式刷写 完美测试 兼容多版本 需要其他第三方twrp的友友请私信
【小白向教程】从零开始为你的手机安装Win11系统
【小白向教程】从零开始为你的手机安装Win11系统 本教程基于项目Renegade Project，为本人原创但是有大量借鉴和引用，已于文中注明。本人能力有限，从小白到写出这篇文章不过一周的时间，如有谬误请各位指正。 注意： 1.本教学使用一加6（8G+128G）手机在Hydrogen OS 10.0.10基础上进行操作，如系统版本低于安卓10请先跳至本文的第三部分的(3)4。如果在过程中因误操作或者其他原因，引起包括但不限于变砖死机等在内的问题，导致无法恢复至上一步，请直接跳至本文的第三部分。 2.一加6
继续访问
 
一加6 避免 crashdump mode win11
1.关闭电源选项快速启动 2.从不休眠硬盘 崩溃触发点集中在2个方向 一，win系统一些重要参数设置和上次启动发生改变 二，除了关机硬盘不能断电，比如进入休眠 所以避免以上两点就没有发生过崩溃 ...
继续访问
安卓测试环境搭建
本文聊聊安卓测试环境搭建。这里推荐两个测试环境，分别是lineageOS和Kali Nethunter。lineageOS支持开启adb root权限进行frida调试，通过这个特性能绕过大部分root检测。Kali Nethunter通过magisk获取root权限，满足日常的APP测试学习之外，还能进行近源渗透测试攻击。
继续访问
 
Oneplus9Pro变砖后修复解锁刷回lineage18
开启USB调试，开启OEM模式(需要翻墙后使用谷歌账号登录1加账号)通过apply update就可刷新的zip包进去。按下音量下 + 音量上 ，连接表格出现一个条目。5.刷回lineage18(linux环境下)出现这个界面（下面显示是uocked）user type 选择others。然后选择进入recovery模式。
继续访问
 
小米Note4、小米8、一加6刷机（三方rec+rom+root）
小米Note4、小米8、一加6刷机（三方rec+rom+root）
继续访问
一加7 pro第三方TWRP-3.3.2B-fastboot模式刷写
本文将详细讲解如何在一加7 Pro上使用第三方TWRP恢复系统3.3.2B，并通过fastboot模式进行刷写操作。首先，我们来了解相关知识点。 1. **一加7 Pro**：一加7 Pro是一款由一加科技推出的高端智能手机，以其出色的性能...
一加9R 刷写第三方twrp教程+工具
一加9R 刷写第三方twrp教程+工具 资源说明： 1----刷写第三方twrp的前提是手机要解锁bl先。请自行解锁bl先。 2----资源可以支持当前机型刷写第三方rec 3-----内含刷写资源和详细刷写教程步骤 4-----带刷写图示...
360N5机型解锁刷入第三方TWRP root工具
360N5解锁刷入第三方TWRP root工具 中文版软件 可以解锁并且刷入第三方rec 进入rec后按提示步骤root即可 兼容性强。有第三方rec可以刷入第三方rom 框架等等 高版本平台有可能刷写不成功。如高版本不成功请降级后按...
qualcomm crashdump mode
安全
写评论

25

18

踩

分享
APP 内打开

小程序内打开
