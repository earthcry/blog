tags_: _@string _@code of string
tree_: '''>

<'''
concept_: string code
core_: '''>
what's the string code in ramdisk?
Unicode  in RAM
but if zh-cn in xxx.py
add ...
# -*- coding: utf-8 -*-
<'''
detail_: '''>

<'''
time_: 20190926230431


tags_: _@format _@print
concept_: python format print, format output
tree_:'''>
<'''
core_:'''>
what's the law of format print?
'Hi, %s, you have $%d.' % ('Phil', 10000)
'growth rate: %d %%' % 7
'growth rate: 7 %'
print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)
<'''
detail_:'''>
<'''
time_: 20190926230230
tags_: _@number _@chufa _@equit
concept_: chufa
tree_:'''>
<'''
core_:'''>
17 / 3 == 5.6667
17 // 3 = 5   # 取整 除法运算
17 % 3  = 2   # 取余 除法运算
5**2 == 25
<'''
detail_:'''>
<'''
time_: 20190926230036
tags_: _@windows _@.pyw _@file.pyw
concept_: windows environment python file,
tree_:'''>
<'''
core_:'''>
.pyw ~ python.exe
<'''
detail_:'''>
<'''
time_: 20190926225841
tags_: _@env _@pyenv
concept_: python run environment, version manager
tree_:'''>
<'''
core_:'''>
pyenv
list versions in system:
$ ls /usr/local/lib
<'''
detail_:'''>
env look
1.env of python
A: 
list versions in system:
$ ls /usr/local/lib
B:
$ ls /usr/bin/python*
C: 
default version:
$ python --version
2. switch version
A: 
user level
$ vim ~/.bashrc
$ alias python='/usr/bin/python3.7'
$ . ~/.bashrc    # or relogin
B: 
system level
update-alternatives
https://www.cnblogs.com/yifugui/p/8649864.html
<'''
time_: 20190926225505
tags_: _@input
concept_: input function
tree_:'''>
<'''
core_:'''>
name = input('Please enter your name: ')
print('Hello, ', name)
<'''
detail_:'''>
<'''
time_: 20190926225326
tags_: _@range
concept_:
tree_:'''>
<'''
core_:'''>
print(range(5))       # range(0,5) [0,5)
print(list(range(5)))
for i in range(5):
  print(i)
lst = range(ord('a'),ord('z')+1)
for i in lst:
  print(chr(i))
<'''
detail_:'''>
<'''
time_: 20190926225118
tags_: _@for in _@loop
concept_: for loop
tree_:'''>
<'''
core_:'''>
# 按元素进行遍历
a = ['a','b','c']
for i in a:
  print(i)
# a
# b
# c
# 按序列号进行遍历
for i in range(len(a)):
  print(i,a[i])
# 0 a
# 1 b
# 2 c
<'''
detail_:'''>
<'''
time_: 20190926225043
tags_: _@data structure comparison 
concept_: 数据结构对比
tree_:'''>
<'''
core_:'''>
tuple(1,2,3)
list [1,2,2,3]
set  {3,1,2}       # no order, no same.无序无重合. 
dict {'z': 3, 'y': 1, 'x': 2}
<'''
detail_:'''>
<'''
time_: 20190926224407
tags_: _@script _@file.py
concept_: python script, file.py
tree_:'''>
<'''
core_:'''>
#!/usr/bin/env python3.7
$chmod +x myscript.py
<'''
detail_:'''>
<'''
time_: 20190926224019

