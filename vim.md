# 追加内容到文件

## vim界面三模式

- 命令模式 ESC
- 编辑模式 i or a
- 可视选择模式  
  - 字符模式 v
  - 行模式 V
  - 区域模式 ctrl v

‌使用可视模式‌：按下v进入字符模式，选择你想要复制的内容。如果你想要选择多行，可以使用Shift + v进入行模式，或者使用Ctrl + v进入列模式。

## 临时显示行号
‌绝对行号‌：在命令模式（按Esc键）下输入:set number（或简写:set nu），左侧即显示行号；关闭用:set nonumber。‌‌‌‌1
‌相对行号‌：输入:set relativenumber（或:set rnu），当前行标记为0，其他行显示相对距离，适合快速跳转。‌‌2‌‌3
‌混合行号‌：同时输入:set number relativenumber，当前行显示绝对行号，其余显示相对行号。‌‌2‌‌4


## 移动光标

← ↓ ↑ →
h j k l

gg 文件开头行首，
G  文件尾行行首，

## 追加内容

echo 'word' >> file.md

:31,34 w! >>./vhost/res.help.com.conf

a. 使用 :r 命令（read 的缩写）来将一个文件的内容读取并插入到当前文件的结尾。

vim filename.txt
G
:r /path/to/otherfile.txt

b. 将多个文件的内容接连追加到当前文件的尾部。

vim filename.txt
:r !find . -type f -name "*.txt" -print0 | xargs -0 cat

这条命令做了以下几件事情： find . -type f -name \"*.txt\" -print0：在当前目录（.）及其子目录中查找所有类型为文件（-type f）且文件名匹配 *.txt 的文件，并使用 -print0 选项来以 null 字符分隔文件名，这有助于正确处理文件名中包含空格、换行符或其他特殊字符的情况。xargs -0 cat：xargs 命令从标准输入读取由 null 字符分隔的项目，并将它们作为参数传递给 cat 命令。cat 命令会将这些文件的内容串联起来并输出到标准输出。
 
