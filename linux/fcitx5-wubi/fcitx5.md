# Install Linux五笔输入法，新世纪五笔

#fcitx5 #rime

fcitx5-table-wubi06  Fcitx5TableWubi06
fcitx5-rime-wubi06   Fcitx5RimeWubi06


fcitx-im.org
rime.im
CSDN/

### Custom Table CSDN\风扇爱好者
ibus,fcitx4

- fcitx5.inside.wubi86，仅有
- fcitx5.custom.wubi06，两张表扔进去 简单重复麻烦
- fcitx5.rime.wubi06 复杂灵活简便，
- 
- 资源地址，
- 操作步骤，
- 义理说明，
- 
现实问题。码表庞杂，不标准，不丰富。
找码表、洗数据、转格式到最终正常上屏的完整过程梳理一遍.

- 一、环境准备：检查 fcitx5 与依赖
- 自定义组件包含在这个扩展里码表引擎fcitx5-chinese-addons，
- 不同发行版的安装组件：
~# Debian / Ubuntu / Linux Mint\nsudo apt install fcitx5 fcitx5-chinese-addons fcitx5-config-qt\n\n
~# Arch / Manjaro\nsudo pacman -S fcitx5 fcitx5-chinese-addons fcitx5-configtool\n
- 装完之后，先运行一次 fcitx5-configtool，确认“附加组件”列表里能看到“码表”这个组件。
- 准备一个临时工作目录，我习惯在 ~/wubi-build 下操作，把原始码表和脚本放一起，方便反复调试。
- 
- 二、处理码表
- 检查编码规范，编码 词条 权重，
- 一般用 head -n 20 先看前 20 行，再用 wc -l 统计总行数。
- 查编码是否有全角字符。有些 Windows 下导出的码表会把全角空格或者全角字母混进去，
- # 看看有没有包含非 ASCII 可打印字符的行
grep -P '[^\x00-\x7F\t ]' 原始码表.txt | head -n 20
- 如果有大量包含中文或其他非 ASCII 字符的行，那说明这个文件本身可能是 GBK 编码，需要先转码，而不是急着清洗。
- 
- 格式转换脚本与批量处理：脚本保存成 clean_wubi.py
- python3 clean_wubi.py 原始码表.txt 新世五笔_fcitx5.txt
- 
- 如果原始文件是 GBK 编码，脚本里直接以 UTF-8 读取会报错。这种时候先转码一步：
- iconv -f GBK -t UTF-8 原始码表.txt > 原始码表_utf8.txt
- 转完再看一眼内容，确认没有乱码，再跑清洗脚本。
- 
- 三、导入码表
- 
-  fcitx5-configtool，在“附加组件”选项卡里找到“码表”。注意，这里不是直接勾选启用，而是要点击右侧的齿轮图标，进入码表管理界面。
- 确认之后，fcitx5 会开始编译生成 .mb 文件，这个编译过程通常几秒钟就完成。
- 编译完成后，回到“输入法”选项卡，点左下角的“+”号添加输入法。
- 
- 重启一下 fcitx5 让配置完全生效。
- fcitx5-remote -e
- fcitx5-remote -r
- 第一条命令是退出输入法进程（强制结束），第二条是重启。我实际操作中经常用这两条命令来快速重置输入法状态，不需要重新登录系统。
- 按下 Ctrl + Space ，切换到新世纪五笔输入，试试打“工”字，输入 a 
- 
- 候选词与词频的个性化调教：
- 然后是唯一候选直接上屏
- “即时编码提示”打开
- 

### Install fcitx5-rime CSDN/用户甲

apt-cache search fcitx5 # Debian/Ubuntu

sudo apt update
sudo apt install \
fcitx5 fcitx5-chinese-addons \
fcitx5-rime fcitx5-table-extra libime-bin \
fcitx5-material-color 
7.1 桌面环境兼容性\n不同DE需要额外配置：\n\n
GNOME：安装gnome-shell-extension-kimpanel

https://fcitx-im.org/wiki/fcitx5
- [ ] 一个基本的fcitx5安装包括：
- fcitx5, 主程序
- fcitx5-gtk, fcitx5-qt, 针对最受欢迎的几种UI开发工具包的输入法模块。
- fcitx5-configtool, GUI配置程序。
- 
- [ ] 对于不同语言，有许多的输入法引擎。中文
- fcitx5-chinese-addons。它包括简体中文最常用的输入法，包括拼音和码表（五笔等）引擎。
- fcitx5-table-extra。附加中文表
- fcitx5-rime。一种可自定义的输入法，但默认情况下其默认配置为拼音。
- fcitx5-chewing。基于libchewing的咀嚼引擎。
- fcitx5-zhuyin。基于lib注音的注音输入法引擎。
- 
- [ ] 一些额外的插件和主题支持：
- fcitx5-lua, 提供lua脚本支持
- fcitx5-material-color, 一个Fcitx5漂亮主题的合集
- libime-bin, 编译工具和运行库，把纯文本码表编译成fcitx5 能读的二进制 dict


- [ ] 设置环境变量，让 fcitx5 真正接管输入
在 ~/.profile 或 ~/.bashrc（或 ~/.zshrc）中加入：\n\n
echo $0
if bash then
 ~/.bash_profile
export XMODIFIERS=@im=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx

这个配置确保GTK/QT程序都能正确调用fcitx5输入法框架。设置环境变量，把 GTK/Qt 程序的输入模块指到 fcitx5。
然后重新加载配置：\n\n
source ~/.bash_profile
验证：
fcitx5-diagnose

- [ ] 设置自启动，相关
- im-config
- fcitx5-configtool



- [ ] rime的配置
- 插件/usr/share/fcitx5/addon
- 主要存放在~/.local/share/fcitx5/rime/目录下：\n\n
default.custom.yaml：全局配置
ls ~/.local/share/fcitx5/rime/ | head



fcitx5 -rd


# Fcitx5 dict genurate
fcitx5dict fcitx5table

1. source table from CNMan/rime-data/wubi06-tygfhzb.dict.yaml
2. rime table -> fcitx5 table
   convert-rime2fcitx5.py
3. table -> dict
   libime-tabledict xxx.txt xxx.main.dict

Rime 的 dict 通常是 词按 Tab 编码 。
 Windows 环境下压出来的，文件名和内容编码很可能是 GBK/GB18030。在 Linux 下用默认方式解压，文件名直接变成乱码
 
sudo apt install unar
lsar 新世纪五笔.zip
unar 新世纪五笔.zip

file -i newcentury.txt
iconv -f gbk -t utf-8 -o newcentury_utf8.txt newcentury.txt

-# 去掉空行和以 # 开头的注释
grep -v '^[[:space:]]*$' newcentury_utf8.txt | grep -v '^#' > newcentury_clean.txt

-# 按编码排序，方便肉眼检查
sort newcentury_clean.txt -o newcentury_sorted.txt

-# 统计重复情况
sort newcentury_sorted.txt | uniq -d | head -50

Frome:
https://bbs.deepin.org/zh/post/233979


发表于 2022-04-02 03:50
楼主

本人使用新世纪五笔，但是更新系统后新世纪输入法经常消失不见，根据这位老哥的贴子把fcitx升级到了fcitx5：https://bbs.deepin.org/zh/post/233230?offset=1&postId=1314838

但是fcitx和fcitx5的码表文件并不通用，码表需要重新制作，下面是制作方法：

1、准备码表文件，格式如下：

KeyCode=abcdefghijklmnopqrstuvwxy
Length=4
Pinyin=@
[Rule]
e2=p11+p12+p21+p22
e3=p11+p21+p31+p32
a4=p11+p21+p31+n11
[Data]
a 工
aa 式
aaa 工
aaaa 工
aaaa 恭恭敬敬
aaad 工期

[Data]之前的配置必须要加上，不然转换码表的时候会报错。也可以在/usr/share/libime/中找到.main.dict文件，使用libime_tabledict -d命令把码表转换到文本文件查看格式，如：libime_tabledict -d wbx.main.dict 1.txt

2、从码表文本转换到码表dict：

libime_tabledict 1.txt nwb.main.dict

３、从/usr/share/fcitx5/inputmethod/目录下找个.conf文件做模板，修改Name[*]和File，conf文件还放在此目录

4、把转换的码表文件*.main.dict放到/usr/share/libime/，网上有些说把两个文件放到～/.local...下，但我这样配置无法使用。

5、注销一下输入法就能添加了。

附加自用的新世纪五笔码表：新世纪.zip
-----------------------------------------------------------------
reply:

beavailable
deepin
发表于 2022-04-02 03:57
沙发

放在家目录下也是可以的。

这是我的一个码表项目，里面有个安装脚本（支持 fcitx和 fcitx5），你可以看看：https://github.com/beavailable/better-wubi
-----------------------------------------------------------------------
https://github.com/CNMan/rime-data


--------------------------------------------------------------------

https://github.com/rime/home/wiki/UserGuide

https://github.com/rime/home/wiki/CustomizationGuide

https://github.com/rime/home/wiki/RimeWithSchemata

https://github.com/rime/plum 東風破, 安裝和配置碼表 






 王码五笔字型大一统2018高级版本

WM18  字符集
可输入GB18030字符27,533个简体繁体汉字

① 除WM07以外，其他所有产品均适用于win7/8/8.1/10 32/64位操作系统（不支持平板电脑）。

② WM18、WM01、WM04，每一个序列号均可安装三台电脑。

货款汇出后，须尽快用“个人手机”发“短信息”给180 3728 0259，告知我们购买人的姓名、单位、汇款金额、要买的产品名称！否则，客户太多，汇款与购买方“对不上号”，会耽误时间。 
简繁同台，插打拼音，
 支持操作系统：

Microsoft Windows XP(sp3)/vista/7/ 8/8.1/10 32/64位操作系统


可输入汉字集：

国标（GB-18030）大字符集27,533个汉字，包括有：简体、繁体、日、韩、香港地区汉字。


集成王码五笔字型(86版＋98版＋新世纪版)三个版本输入法。


 【2018版大一统软件含五项重大创新】

A、简繁同台

在字母键“五笔”输入状态下，同一编码，用大写字母输入，显示繁体字（以及没有简体的字）；用小写字母输入，显示简体字(以及字符集内的字）：
如：XAG～ 紅，   YGKG～語，
   　xag～红；   ygkg～语。

B、插打拼音

在五笔字型输入过程中，可以直接用“ \` ”（在键盘上排数字键1 的左边那个键上）引导，用全拼输入汉字，同时，显示出五笔字型编码，帮助学习五笔。插打之后，自动返回五笔输入状态。

C、三代同堂

2018版软件包含五笔字型第一代、第二代、第三代(86 、98 、新世纪版)共“三代版本”；在同一台电脑上，三个版本随意切换，各个版本功能相同。

D、快捷符号

王码首创58组“王码符号双轨输入法”，可轻松输入900个符号。如按词汇码：
输入（王码五星）GDGJ，即可显示“ ★ ☆ ”；
输入（王码三角）GDDQ，即可显示“ ▲ △ ”；
输入（王码日期）GDJA，即可显示“ 当天日期”。

 E、提示编码

可提示五笔编码／字根分解／汉语拼音；

【关于“产品序列号”的重要说明】
Ａ、“产品序列号”是用户购买的［王码正版软件］的唯一凭证，2018软件的序列号与2016版（共4组）有所不同，是由5组数字构成（每组5个数字），第一组都是“20180”，作为“版本特别标识”，以便与2016版区别。如20180-22222……。
B、每个序列号，无论2016版或者2018版，仍然是最多可在3台电脑上反复安装使用！请妥善保密保存你的“产品序列号”！如果丢失或被他人获得，不能补发。
C、务请注意：2016版软件与2018版软件，只能分别装用，不能安装在同一台电脑上并行使用。
 
【安装操作步骤】

1、首先清空电脑中原先安装的同类软件和360软件；
2、点开王码网首页上排的【购买／安装】，下拉找到价格表中2018大一统的产品代号“WM18”，点开，再点开右下角【下载安装包】按钮，开始自动下载软件；
3、运行步骤2中的安装程序时，按照提示，需要正确输入所购买的“产品序列号”。

序列號

wmdyt18--20180-35739-63179-03824-29537

## Debian & Ubuntu

### fcitx

fcitx5默认系统级安装路径
/usr/share/fcitx5  #conf
/usr/share/libime  #table, 是生成的二进制文件，

```shell
# requires
# fcitx: sudo apt install fcitx fcitx-table-wubi fcitx-tools
# fcitx5: sudo apt install fcitx5 fcitx5-chinese-addons libime-bin
git clone --depth=1 https://github.com/beavailable/better-wubi.git
cd better-wubi
./install-for-fcitx.sh
```
文件安装到了目录~/.config/fcitx/table/    or
                ~/.local/share/fcitx5/inputmethod/
然后在`fcitx`设置面板添加`better-wubi`输入法即可。

## Android
在内部共享存储空间下面这两个目录分别添加两个文件，xxx.conf, xxx.main.dict。
xxx.main.dict 是xxx.txt通过libime-tabledict命令生成的二进制文件。

/storage/emulated/0/Android/data/org.fcitx.fcitx5.android/files/data/inputmethod/
/storage/emulated/0/Android/data/org.fcitx.fcitx5.android/files/data/table/

再在设置里添加新输入法。

注意：dict&table, 詞庫與碼表，


# 脚本
`convert.py`可以将码表转换为你需要的格式。

`regenerate.py`可以重新生成（根据单字编码）并排序码表。

`statistics.py`可以查看相关的统计信息。

# 鸣谢
- 王码五笔发明者王永民先生
- [CNMan](https://github.com/CNMan) 提供原始码表
- [字甲达宾](https://bbs.deepin.org/user/53398) 制作图标

# 版权
版权归王码公司所有，禁止商用。



