/run/user/1000/gvfs/mtp:host=OnePlus_SM8150-MTP__SN%3A0C912150_181e292b/
內部共用儲存空間/0data/test$ 


# Rime

rime.im/docs
fcitx-im.org/wiki

配方

配方 也記作 ℞，是由 東風破 /plum/ 配置管理工具所支持的 Rime 數據分發形式。

配方可以用來安裝輸入方案、修改配置、實現自定義功能。
庫藏配方一覽

    ℞ prelude 基礎配置
    ℞ essay 八股文詞彙表
    現代標準漢語
        ℞ luna-pinyin 朙月拼音
        ℞ terra-pinyin 地球拼音
        ℞ bopomofo 注音
    拼音的變體
        ℞ double-pinyin 雙拼
        ℞ stenotype 打字速記法
        ℞ combo-pinyin 宮保拼音〔專題介紹〕
    漢語方言
        ℞ jyutping 粵拼
        ℞ wugniu 吳語上海話
        ℞ soutzoe 蘇州話
    歷史音韻
        ℞ middle-chinese 中古漢語拼音
    字形輸入
        ℞ stroke 五筆畫
        ℞ cangjie 倉頡
        ℞ quick


© 2026 佛振@式恕堂   Powered by: Zola, Freewill & Bootswatch 






sudo apt update
apt-cache search fcitx5 #Debian/Ubuntu
sudo apt install -y fcitx5 fcitx5-chinese-addons fcitx5-config-qt fcitx5-frontend-gtk3 fcitx5-frontend-gtk4 fcitx5-frontend-qt5 fonts-noto-cjk fonts-wqy-microhei
    fcitx5: 输入法框架主体。
    fcitx5-gtk, fcitx5-qt, 针对最受欢迎的几种UI开发工具包的输入法模块。
    fcitx5-configtool, GUI配置程序。
    对于不同语言，有许多的输入法引擎
        参见 输入法引擎
        https://fcitx-im.org/wiki/Input_method_engines/zh-cn
中文
    fcitx5-chinese-addons。它包括简体中文最常用的输入法，包括拼音和码表（五笔等）引擎。 中文输入引擎（拼音、双拼、五笔等）。
    fcitx5-rime。一种可自定义的输入法，但默认情况下其默认配置为拼音。
    fcitx5-table-extra。附加中文表
    fcitx5-frontend-*: 确保 GTK 和 Qt 应用能正确调用输入法。
    fonts-*: 字体。防止候选框或界面中文显示为方块。
    fcitx5-chewing。基于libchewing的咀嚼引擎。
    fcitx5-zhuyin。基于lib注音的注音输入法引擎。

一些额外的插件和主题支持：
    fcitx5-lua, 提供lua脚本支持
    fcitx5-material-color, 一个Fcitx5漂亮主题的合集
多语言（如果上面没有列出，这可能是您需要的）

    fcitx5-m17n
    fcitx5-keyman
    fcitx5-table-other，它提供了许多其他表格，但如果适合您，建议您更喜欢 fcitx5-m17n。
    内置基于键盘布局的引擎。这允许使用传统的键盘布局。

从源码安装Fcitx5
    编译Fcitx5
### 配置
https://fcitx-im.org/wiki/Setup_Fcitx_5/zh-cn
$im-config, select fcitx5
$fcitx5-configtool。添加rime engine
查看记录用户目录
/home/nu/.local/share/fcitx5/rime

XDG Autostart
$mkdir -p ~/.config/autostart && cp /usr/share/applications/org.fcitx.Fcitx5.desktop ~/.config/autostart



        https://pkgs.org/search/?q=fcitx4-chinese-addons
        Debian Main amd63 Official
            fcitx4-chinese-addons_5.1.8-1_all.deb 	Chinese-related addon for fcitx5 (metapackage)
            fcitx4-chinese-addons-bin_5.1.8-1_amd64.deb 	Chinese-related addon for fcitx5 (binary tools)
            fcitx4-chinese-addons-data_5.1.8-1_all.deb 	Chinese-related addon for fcitx5 (shared data files)

 Debian 13 (Trixie)
Debian Main amd64 Official
fcitx5-rime_5.1.10-2_amd64.deb 	Rime input method support for fcitx5



2. 设置默认输入法框架

使用 im-config 工具将系统默认输入法切换为 fcitx5。

bash
im-config -n fcitx5

执行后检查 ~/.xinputrc 文件，确认内容包含 run_im fcitx5。

3. 配置环境变量
登录 shell 配置文件

如果您正在使用Bash作为您的登录shell，~/.bash_profile 是您可以信赖的最好的用户级东西。它受到不同 DM 的广泛支持，如果您从 TTY 启动图形，它也可以工作。
   - 支持主流显示管理器，包括GDM/SDDM/LightDM
   - TTY 登录
export XMODIFIERS=@im=fcitx
export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
有些人可能会认为 ~/.profile 是一个与 shell 无关的解决方案，这是错误的。虽然 GDM 始终获取此文件，但如果 ~/.bash_profile 存在，SDDM/Bash 将不会获取此文件。这使得 ~/.bash_profile 成为更好的解决方案，因为 bash 的使用相当广泛。但在继续之前请检查您的登录 shell，某些发行版可能不使用 bash 作为默认 shell。

此视频演示了如何在 Archlinux 上手动设置环境变量
/etc/profile

如果您不关心使用 root 修改文件，这是最好的选择。所有发行版通常都支持此文件。您需要附加到 /etc/profile 末尾的代码片段与 登录shell配置文件 相同。
~/.xprofile

如果您使用 X11 和显示管理器，这是一个古老的完美选择。但 Wayland 没有对应的环境变量，因此如果要为 Wayland 设置环境变量并不理想。您要添加的代码与登录shell配置文件 相同。 

DBus

在大多数附带 systemd 的发行版上，这应该不再是问题。但是如果您使用一些所谓的“systemd”free 的发行版，您可能需要自己启动DBus并设置相关的环境变量。通常，这可以通过在启动脚本中添加如下行来完成。例如，如果您使用的是 X11，则为 ~/.xprofile。此外，您还需要确保此语法适用于您的登录 shell。

eval `dbus-launch --sh-syntax --exit-with-session`

配置 Fcitx 5

参考 配置工具(Fcitx 5). 
fcitx5-configtool



为确保所有应用（包括终端、浏览器、IDE）都能识别输入法，需设置环境变量。推荐写入 ~/.xprofile（适用于大多数桌面环境如 GNOME, KDE, Xfce 的 X11/Wayland 会话）。

创建或编辑 ~/.xprofile：

export GTK_IM_MODULE=fcitx
export QT_IM_MODULE=fcitx
export XMODIFIERS=@im=fcitx
export SDL_IM_MODULE=fcitx

注意：GTK_IM_MODULE 和 QT_IM_MODULE 的值必须是 fcitx 而非 fcitx5，这是由模块接口规范决定的。

如果使用的是 Wayland 会话且遇到部分应用无法输入的问题，可尝试将环境变量写入 /etc/environment 以确保全局生效（需重启系统）：
GTK_IM_MODULE=fcitx
QT_IM_MODULE=fcitx
XMODIFIERS=@im=fcitx

4. 配置自启动

确保 fcitx5 随桌面会话自动启动。创建自启动桌面入口文件：
mkdir -p ~/.config/autostart
cat > ~/.config/autostart/fcitx5.desktop <<EOF
[Desktop Entry]
Type=Application
Name=Fcitx5
Comment=Start Fcitx5 input method
Exec=fcitx5
X-GNOME-Autostart-enabled=true
NoDisplay=true
EOF
5. 验证与配置

    ‌注销并重新登录‌系统，使环境变量和自启动配置生效。
    登录后，托盘区应出现键盘图标。右键点击图标选择“配置”或使用命令 fcitx5-configtool 打开配置界面。
    在“输入法”标签页中，点击左下角“+”号，取消勾选“仅显示当前语言”，搜索并添加“Pinyin”（拼音）或其他需要的输入方案。
    默认切换快捷键通常为 Ctrl + Space 或 Super + Space，可在配置界面的“全局配置”->“快捷键”中修改。

常见问题排查

    ‌候选框不显示/乱码‌：确认已安装 fonts-noto-cjk 或 fonts-wqy-microhei，并执行 fc-cache -fv 刷新字体缓存。
    ‌特定应用无法输入‌：检查该应用是否安装了正确的前端模块（如 Qt 应用需 fcitx5-frontend-qt5）。对于 Electron 应用（如 VS Code, Discord），确保环境变量已正确加载，必要时重启应用。
    ‌Wayland 兼容性‌：如果在 GNOME Wayland 下遇到问题，可尝试在登录界面选择“GNOME on Xorg”切换至 X11 会话，fcitx5 在 X11 下的兼容性更为成熟。




## Using Fcitx 5 on Wayland
fcitx-im.org/wiki/using_fcitx_5_on_wayland#gnome
GNOME

Best setup:

    Environment variables:
        Set XMODIFIERS=@im=fcitx for XWayland application
        Set QT_IM_MODULE=fcitx for Qt, since Qt5 would use XWayland by default.
        If you don't use Qt >=6.7,<6.8.2, set QT_IM_MODULES="wayland;fcitx" for Qt 6.8.2+
        Run chrome with XWayland and GTK_IM_MODULE=fcitx

Support information:

    Application/Compositor uses text-input-v3
    Compositor/Input Method uses ibus dbus protocol, so ibus frontend is required to be used.
    Adding Fcitx 5 to autostart, it will replace any existing ibus-daemon upon start up so it will work out of box.
    Popup candidate window is not able to be displayed over gnome-shell UI. Only solution is to use Kimpanel, link to extension.
    Qt < 6.8.2 need to use QT_IM_MODULE=fcitx since mutter doesn't support text-input-v2.


@frontend - 前端 是用户能直接看到和操作的界面部分，包括网页、APP 界面的展示和交互功能 ,HTML,CSS,JavaScript
Intro

Kimpanel is a DBus-based User Interface for Fcitx. It's oriented from KDE, and now it can also support gnome-shell.
Setup

Since 4.2.0, Fcitx will have ability to automatically switch to different UI based on current environment at runtime. If you are using Fcitx 4.1, you can use

fcitx -u fcitx-kimpanel-ui

to force fcitx to use kimpanel.
Kimpanel Frontend

You need a kimpanel frontend to actually use kimpanel to display UI, currently there are several implementations list below.

    Kimpanel in KDE Plasma Addons
    Kimtoy
    Kimpanel for GNOME-Shell
https://fcitx-im.org/wiki/Kimpanel
ifcitx -u fcitx-kimpanel-uii
Kimpanel for GNOME-Shell
Input Method Panel using KDE's kimpanel protocol for Gnome-Shell

Extension Homepage
    https://github.com/wengxt/gnome-shell-extension-kimpanel

Download shell version
$echo $0
$bash --version


@qt @gtk
Qt和GTK都是用于创建图形用户界面（GUI）的工具包‌，即开发桌面软件界面的框架。GTK（GIMP Toolkit）最初为图像处理软件GIMP开发，用C语言编写，是GNOME桌面的基础；Qt由挪威Trolltech公司开发，基于C++，是KDE桌面的基础。‌‌
查看版本的方法

‌查看GTK版本‌（Linux终端）：

bash
pkg-config --modversion gtk+-3.0    # 查看GTK3版本
pkg-config --modversion gtk+-2.0    # 查看GTK2版本
pkg-config --list-all | grep gtk    # 查看已安装的GTK相关包

‌查看Qt版本‌：

    ‌命令行‌：执行 qmake -v，输出中的 Using Qt version x.x.x 即版本号。
    ‌Qt Creator‌：菜单栏「帮助」→「关于Qt Creator」，可看到IDE和Qt版本。
    ‌代码中‌：用 qVersion() 获取运行时版本，QT_VERSION_STR 宏获取编译时版本。‌‌

    若 qmake 提示找不到命令，需将Qt安装目录下的 bin 文件夹路径加入系统环境变量PATH，或直接使用完整路径调用，如 C:\Qt\6.5.1\msvc2019_64\bin\qmake.exe -v。‌‌

@xwayland
XWayland 是‌运行在 Wayland 合成器上的 X11 兼容层‌，本质是一台完整的 X Server，用于在 Wayland 桌面会话中运行尚未适配 Wayland 的传统 X11 应用程序 。它把 X11 窗口请求翻译成 Wayland 协议，让老应用像普通窗口一样显示在 Wayland 桌面上，是 X11 到 Wayland 过渡期间的关键兼容组件 。‌‌‌


@Shell 和 @Bash
 是什么关系‌：Shell 是命令解释器这一类程序的统称，Bash 只是其中一种具体实现
怎么查看当前用的是哪种 Shell‌：可在终端执行echo $0
i脚本怎么指定用 Bash 解释‌：脚本首行写#!/bin/bash可强制用 Bash 解释器执行，

@wayland
Linux 桌面图形用户界面( GUI )采用分层架构设计,从底层到上层包括: 
显示服务器协议 (X11/ Wayland )→ 
显示服务器实现 (X Server /Wayland Compositor)→ 
桌面环境 (KDE/GNOME)→ 应用程序 。 
理解这些组件的关系对于深入掌握 Linux 桌面系统至关重要。 

@xdg
主要有三种含义：Linux 桌面环境的技术标准规范。
计算机技术领域的 XDG 标准

    ‌XDG 的全称与起源‌：XDG 是"X Desktop Group"（X 桌面工作组）的缩写，2000 年 3 月由红帽公司工程师创立，现由 freedesktop.org 维护，旨在为 Linux 桌面环境制定统一标准。
    ‌核心作用与应用场景‌：
        统一配置文件、数据文件和缓存文件的存储位置，解决不同桌面环境（如 GNOME、KDE、XFCE）的碎片化问题。
        定义了一系列环境变量，例如：
            $XDG_CONFIG_HOME：配置文件目录，默认~/.config
            $XDG_DATA_HOME：用户数据目录，默认~/.local/share
            $XDG_CACHE_HOME：缓存目录，默认~/.cache
        xdg-open 命令可根据文件类型自动调用系统默认应用打开文件或网址，是 Linux 桌面常用的工具。
    ‌实际应用价值‌：遵循 XDG 规范能让应用程序在不同桌面环境间更好地兼容，用户更换桌面环境时也能保留个人设置，方便数据管理和备份

