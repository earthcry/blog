#!/bin/bash
# @file         utf-8.sh
# @author       ymm
# @brief        修改当前目录下的.cpp .c .h文件的编码格式为utf-8
# @date         2014-07-23
# @History
# 1、2014-07-23  author ymm    初步完成
# 在目录下执行该脚本，就可以把该目录下的所有“.cpp .c .h”文件的编码格式转换成utf-8并且是UNIX格式了。
# 唯一的遗憾，就是每次使用vim之后标准输出都会出现大部分的空白，如果vim中有一个参数，像gdb中的-q（不会输出介绍和版权信息，也就是类似于静默模式），那就更不错了。

for i in $(ls *.txt *.cpp *.c *.h)
do
echo "begin to modify the fileencoding of $i to utf-8"
vi +":set fileencoding=utf-8" +":set fileformat=unix" +":wq" $i
done
