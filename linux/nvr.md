
NVR in docker: 探索使用Shinobi搭建家用场景视频监控录像系统，支持云端准实时查看录像


或两个手机实现监控，

什么值得买
2023-12-30 10:58:07

作者：wakeforest

本文纯属自娱自乐，如果你认为使用品牌监控一步到位就可以了，那就不用继续往下看了。

本文仅用于记录自己折腾家用监控系统的过程，也推荐给和我一样爱折腾docker/linux服务器的站内值友。

以下正文

需求动机和方案

家用监控越来越普及，包括室内/入户/庭院等场景。我的需求是在入户门厅布控，当有人来时进行抓拍或者录像，平时不用录像。一般的家用监控摄像头或者智能门铃设备可以完全满足我的需求，但是爱折腾的我怎么会满足于买一个品牌摄像头+云存储（还要收费）的简单方案。

当然要利用已有的设备--Linux小主机，最好可以用Docker部署视频监控软件，再外接硬盘(已有)，IP摄像头通过局域网接入监控软件，在后端(监控软件)进行目标检测，然后在检测到目标或者运动后触发录像->保存到硬盘。后端小主机+监控软件+硬盘有点类似一套NVR (network video recorder)。

视频监控软件可以用NAS上自带的产品，比如威联通的QVR Pro，但是考虑到不给NAS增加额外负载所以放弃。

经过非常不完全调查🔎，可以用Docker部署的视频监控软件知名的有以下几款：

Frigate - NVR With Realtime Object Detection for IP Cameras, 12.4k stars

Shinobi - the Open Source CCTV Solution written in Node.JS. Designed with multiple account system, Streams by WebSocket, and Direct saving to MP4. Shinobi can record IP Cameras and Local Cameras. 1.3k + 600 stars

moonfire-nvr - a security camera network video recorder, 1k stars

OS-NVR is a lightweight extensible CCTV system, 100+ stars

实际尝试了Frigate和Shinobi，前者由于CPU占用过高放弃（可能是没配置好）。相比Frigate，Shinobi的web页面看起来更加专业，资源占用也少的多。后两款没有尝试，不做评论。


最终方案为：IP摄像头(废旧pad或者手机)+Linux小主机(部署Shinobi)+外接硬盘+(阿里云同步)，括号内可选，可实现检测到目标或者运动触发录制，（准实时在云端查看监控录像）。

最终硬件: 废弃多年的小米平板(安装IP摄像头软件)+Linux小主机+USB外接硬盘(绿联硬盘盒+海康OEM)，这些设备都是复用的，并不是为了监控专门购置。


题外:如果对上面这个服务器监控小屏幕感兴趣可以移步🔽

Shinobi介绍

Shinobi是一款开源视频管理软件，它可以接入网络摄像头/USB摄像头，具有实时录制/回放、运动检测、目标检测等完整功能，免费版完全够用。详细功能请前往官方特性页查看。


原项目1.3k stars说明确实是一个非常成功的开源项目。目前项目在gitlab上还在不断更新。🔽


Shinobi支持通过Docker部署，大大减少了对环境的依赖程度和部署难度。在Linux小主机上部署Shinobi并接入网络摄像机，小主机再外挂一块硬盘，可以简单搭建一套家用网络录像系统（NVR）。

准备工作

在宿主机上新建shinobi对应的几个目录（以下路径根据实际情况调整）：

1. 新建文件夹 shinobi 和 子目录

mkdir -p /mnt/hdd_hikvision/shinobi

mkdir -p /mnt/hdd_hikvision/shinobi/{config,customAutoLoad,database,plugins,videos}

说明：

config目录保存配置文件

database保存数据库，shinobi自带mysql数据库，该目录将容器内部的数据库文件映射到宿主机目录

videos目录存放记录的视频片段

上面的目录在初次容器启动前保持为空即可。

2. 新建临时文件存储文件系统

mkdir -p /dev/shm/Shinobi/streams

说明：

/dev/shm 是linux下一个利用内存虚拟出来的一个目录，这个目录中的文件都是保存在内存中，而不是磁盘上。/dev/shm/Shinobi/streams用户存放一些临时的视频片段，当持久化到videos目录后，streams中的数据会被删除。


3.镜像

拉取镜像registry.gitlab.com/shinobi-systems/shinobi:dev。这个镜像比较大，1.55G。也可以在部署时拉取。🔽


Docker部署

按照官方说明 Install Shinobi with Docker 来实现部署。

sudo docker run -d --name='Shinobi'

-p '28080:8080/tcp'

-v "/dev/shm/Shinobi/streams":'/dev/shm/streams':'rw'

-v "/mnt/hdd_hikvision/shinobi/config":'/config':'rw'

-v "/mnt/hdd_hikvision/shinobi/customAutoLoad":'/home/Shinobi/libs/customAutoLoad':'rw'

-v "/mnt/hdd_hikvision/shinobi/database":'/var/lib/mysql':'rw'

-v "/mnt/hdd_hikvision/shinobi/videos":'/home/Shinobi/videos':'rw'

-v "/mnt/hdd_hikvision/shinobi/plugins":'/home/Shinobi/plugins':'rw'

-v '/etc/localtime':'/etc/localtime':'ro'

registry.gitlab.com/shinobi-systems/shinobi:dev

部署完成，可以从浏览器进入管理页面

Web地址（管理端）：http://HOST-IP:PORT/super

默认超级用户 : admin@shinobi.video； 密码：admin

Web地址（客户端）：http://HOST-IP:PORT，用户和密码通过管理端设置。

PORT为容器映射到宿主机的端口，上面脚本中 -p '28080:8080/tcp' 说明宿主机的端口为28080，可以自行修改。

Shinobi使用

Shinobi的功能比较完整，界面也比较丰富。但是，要很好的使用这个系统还是需要一些学习成本，个人感觉整个系统的设计对监控新手并不算友好。下面从纯新手的角度介绍下使用方法。

1. 新建用户

通过默认超级用户{admin@shinobi.video}登录管理端(http://HOST-IP:PORT/super)，然后新建用户用以日常管理。

填写用户名，可以是email，也可以其他。[Group Key] 为用户组，与视频存放的目录结构有关，个人使用可以不关心。其他属性先按照默认。🔽


🔼上述用户新建完成后，可以登录http://HOST-IP:PORT。

2. 增加摄像头

用上述新建的用户登录，找到左边[Monitor Settings]，然后在页面中填写摄像头信息，最后记得在右下角点击[SAVE]保存。


这里以网络摄像头（IP Camera）为例，有几个关键信息需要解释下：

Identity区域的[Mode]选项：Watch-Only，可以查看摄像头，默认不录视频，可以配置事件触发录像；Record，全程记录模式，默认每隔15分钟保存一次录像。🔽


视频压缩不建议开启，特别是在record模式下。如果视频录制速度快于压缩速度，那么可能产生问题。而且，如果CPU性能一般，视频压缩会长时间让CPU负载在较高值，还需要探索下是否有硬件加速功能。🔽


Connecttion区域，在[Full URL Path]中填写rtsp码流的地址，这个可以从摄像头中查看，一般格式类似 rtsp://{username}:{password}@CAMERA_IP:PORT/****。填写完成后，可以下方绿色的【Probe】进行测试，是否能正确获取到码流信息。🔽


对填写的rtsp地址进行检验🔽


如果不清楚rtsp的完整地址，也可以使用ONVIF扫描器（ONVIF Scanner）。在扫描器页面上填写IP（支持IP段）、Port、Username(如有)、Password(如有)，然后【search】。如果信息填写正确，右边【Found Devices】中会出现摄像头信息。复制其中的rtsp协议完整地址，或者直接【Add All】可以将信息自动填写到新增摄像头页面。🔽


Input区域，官网建议在网络状况良好的环境中，分别将Duration和Probe Size修改为0和32。不修改也可以。🔽


3. 设置运动检测

前面[Monitor Settings]--[Identity]--[Mode]设置为“Watch-Only”，然后[Monitor Settings]--[Detector Settings]开启检测，可以在检测到运动或者目标时触发录像。具体设置如下：


🔼上图中[How to Record]选择“Event-Based Recording(For Watch-Only Mode)”，[Trigger Record]选择“Yes”。

运动检测 (Motion Detection)：这里直接使用Build-in检测器（猜测就是简单的帧差或者背景建模），当画面中有运动目标可以触发录像，一般够用了。🔽


目标检测 (Object Detection)：需要安装插件（TensorFlow目标检测），而且最好搭配GPU，由于硬件问题没有开启。

4. 设置通知（非必要）

设置事件通知，当检测到运动或者目标时，Shinobi可以通过邮件等方式发送通知。

先到[Account Settings]-[Email]中设置邮件服务器信息/发送的邮箱/接收的邮箱。邮件服务器和发送的邮箱以新浪邮箱为例:

Host: smtp.sina.com

Port: 25

Email: 发送的邮箱

Password: 上面Email的密码或者授权码。

Send to: 接收的邮箱


然后到[Monitor Settings]--[Notifications]开启通知，将Email设置为Yes.🔽


备注: 以新浪邮箱为例，Password需要输入的是邮箱的授权码，因为Shinobi发送邮件是使用内置的nodemailer，对新浪来说是第三方客户端。🔽


当检测到运动以后，除了记录视频，也会收到邮件通知。🔽


监控效果

Web端[Live Grid]可以查看实时画面（有10s左右延迟）。


检测到运动时整个摄像头框会变红色🔽


查看录像[Videos]，因为我设置的是Watch-Only模式+运动检测事件触发，所以这些录像是运动检测触发录制下来的，说明上面设置的运动检测生效了。🔽


这些监控录像也可以在宿主机本地找到，因为docker启动脚本中将容器内部的录像目录映射到了宿主机目录:

-v "/mnt/hdd_hikvision/shinobi/videos":'/home/Shinobi/videos'

videos目录下按照Group key/Monitor ID/的组织形式按照摄像头对录像进行存放。


云端准实时查看录像(非必须)

在外想要看到家里的实时监控画面，可以通过一些内网穿透的办法。但是我在用的zerotier带宽不够无法实现视频回看。

这里介绍一种准实时查看监控视频的思路，需要用到阿里云盘(或者其他网盘)，clouddrive2网盘工具，rsync文件夹同步工具。

原理是通过clouddrive2将网盘文件夹W挂载到本地文件夹H，然后使用rsync工具定时将视频录像文件同步到本地文件夹H，实现录像准实时存储到云端。

shinobi录像文件夹--(rsync)-->本地文件夹H--(clouddrive2)-->网盘文件夹W

Docker部署clouddrive2

sudo docker run -d --name clouddrive2 --env CLOUDDRIVE_HOME=/Config -v /mnt/hdd_hikvision/work/clouddrive2/data:/data_container:shared -v /mnt/hdd_hikvision/work/clouddrive2/Config:/Config -v /mnt/hdd_hikvision/work/clouddrive2/media:/media:shared -p:19798:19798 --privileged --device /dev/fuse:/dev/fuse cloudnas/clouddrive2:latest

然后进入clouddrive2页面: http://IP:19798，注册🔽


注册完成，这里选择阿里云盘，然后扫码绑定阿里云盘账号🔽


将阿里云的文件夹shinobi挂载到clouddrive2中的文件夹data_container (这个是容器内部路径，详见上面脚本)🔽



完成上面操作后，本地文件夹data/shinobi（映射容器内部/data_container）与阿里云的文件夹shinobi进行了挂载。

文件夹同步

可以使用以下脚本将录像目录与clouddrive2目录建立同步:

sudo rsync -rt --delete /mnt/hdd_hikvision/shinobi/videos/12345/* /mnt/hdd_hikvision/work/clouddrive2/data/shinobi/

将上述脚本放到crontab定时任务工具中:

crontab -e 编辑定时任务，每5分钟同步一次（可以算准实时了）


同步到阿里云的录像🔽


系统运行情况

小主机的配置不高，NVR类软件需要长期运行，所以要求内存/CPU占用在合理的范围内。

通过netdata查看Shinobi容器，可以看到使用CPU和内存资源比较少。🔽


运行一整天后大概占用了500MB内存，可以接受。CPU占用可以忽略不计。🔽


总结

整个监控方案使用了一段时间，在门厅场景中能准确记录到访的情况，因为是事件触发所以存储下来的录像不会占用太大空间。

Shinobi作为整个系统的核心运行稳定，占用资源较少，体验下来是一款比较成熟的视频监控管理软件，用来作为家用NVR是合适的。如果想在外查看家中监控，文中也给出了一种免费的准实时的方法，仅供参考。



远程视频监控搭建教程：低成本、支持任意网络，各地摄像头实时观看
飞象网02-14 13:59

OPPO Watch X2 Mini 智能手表支持实时定位分享、一键报警等功能
IT之家04-07 20:36

谷歌搜索测试上线 AI 模式：整合多模态和实时信息，一键解答复杂问题
IT之家03-06 09:17

真我游戏功能接入DeepSeek：实时攻略支持深度思考
PChome02-20 10:24
许继电气新注册《一种E8000实时监控平台实时库浏览工具系统V1.00》等2个项目的软件著作权
证券之星官方微博04-29 02:46
查看更多相关新闻
发表你的精彩评论

