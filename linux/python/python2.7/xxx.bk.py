
#      python data struct 46-63

#               @list

#      序列.列表  索引数组list[] 
#      映射.字典  关联数组dict{}

# dictionary 字典
# list, string, dict

# 2.2序列通用操作：n[],[:],'---',in
# 2.2.1对序列索引存取操作  字面值、返回值
# 2.2.2对序列分片获取操作 [12:-4], 分片边界[ : ),[::3] 
# 2.2.5 成员资格，列表归属操作，布尔运算符 * in []
# 2.2.6 序列列表，len, min, max;

# 数据结构：按某种方式组织在一起的数据元素的集合；

# 容器container, 序列，映射, 集合set;

# 序列：索引数组；
# 序列：元组+列表, 字符串，unicode字符串，buffer对象，xrange对象；
# python 最基本的数据结构是序列sequence, 序号/元素位置/索引；
# 编号起始，从前右向0123，从后左向-1-2-3，无缝数轴；

# 2.2序列通用操作：n[],[:],'---',in
# 索引，分片、加乘、归属、迭代；
# 索引indexing, 分片sliceing, 加adding, 乘multiplying
# 归属、长度、最大、最小元素内建函数；
# 迭代iteration：依次，每个元素，重复，操作；遍历；

# 2.2.1对序列索引存取操作  字面值、返回值
index='hello'
index[0]    # 'h'
index[-1]   # 'o'
# 字符串 字面值 能直接使用索引，不需要变量引用；
'hello'[1]  # 'e'
# 对函数 返回值 直接进行索引操作；
fourth=raw_input('Year: ')[3]
Year: 2005
fourth      # '5'

# 2.2.2对序列分片获取操作 [12:-4], 分片边界[ : ),[::3] 
# 分片索引边界 [ : ) 
numbers=[0,1,2,3,4,5]
numbers[2:4]# [2,3]     数学表示：[2,4)
# 取最后3个
numbers[3:6]# [3,4,5]
numbers[-3:-1]  #[3,4]
numbers[-3:0]   #[]
numbers[-3:6]   #[3,4,5]
# 优雅的捷径: 到最后一个的话，就空着；
numbers[-3:]    # [3,4,5]
numbers[:3]     # [0,1,2]

numbers[:]      # [0,1,2,3,4,5]
numbers         # [0,1,2,3,4,5]

# project:输入Url，提取域名；
url=raw_input('Please enter the URL: ')
domain=url[12:-4]
print 'Domain name: ' + domain

# 步长，从零开始，step 3, 0,1,2,3,1,2,3；
numbers=[0,1,2,3,4,5]
numbers[::3]     # [0,3]
# 步长不能为0，负数为：从逆向提取；
numbers[5:1:-2]  # [5,3]
numbers[:1:-2]   # [5,3]

# 2.2.3 对序列相加操作
[1,2,3] + [4,5,6]       # [1,2,3,4,5,6]
'hello, ' + 'world!'    # 'hello, world!'
# 数字和字符串不能相加，同类相加；

# 2.2.4 对序列乘法操作 '-----'
'-'*5               # '-----'
[21]*3              # [21,21,21]
[None]*3            # [None, None, None]        length=3
# None,初始化,空列表;

# project:文本伸缩框
# 屏幕居中打印一框，中间为用户输入内容，且框随内容长度变化；

textlen=len(text)
kuanglen=textlen+6
bianlen=(screenlen-kuanglen)//2

                    +--------------------+
                    |                    |
                    |  aaaaaaaaaaaaaaa   |
                    |                    |
                    +--------------------+

sentence=raw_input('Sentenc: ')

screen_width=80
text_width=len(sentence)
box_width=text_width+6
left_margin=(screen_width-box_width)//2

print
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print ' '*left_margin + '|' + ' '*(box_width-2) + '|'
print ' '*left_margin + '| ' + ' ' + sentence + ' ' + ' |'
print ' '*left_margin + '|' + ' '*(box_width-2) + '|'
print ' '*left_margin + '+' + '-'*(box_width-2) + '+'
print

# 2.2.5 成员资格，列表归属操作，布尔运算符 * in []
# in 布尔运算符，非+*算术运算符；
permissions= 'rw'
'w' in permissions      # true
users=['aaa', 'bbb', 'ccc']
raw_input('Enter your name: ') in users          # true

# project: 检查用户名和PIN码；
database=[
        ['aaa', '1234'],
        ['bbb', '3456'],
        ['ccc', '5678']
        ]
username=raw_input('Username: ')
pin=raw_input('PIN code: ')

if [username, pin] in database: print 'Access granted.'

# 2.2.6 序列列表，len, min, max;
# len(), min(), max()
n=[2,3,5]
len(n)
max(n)
max(1,3,8)
# min(),max(),参数，即可是整个序列，也可直接是值；

# 2.3 列表
# 列表是可变的mutable
# 列表不同于元组和字符串；
# 2.3.1 list函数,转化为列表list('hello')
# 字符串转化为列表便于修改
list('Hello')               # ['H', 'e', 'l', 'l', 'o']         join()
# 2.3.2 列表基本操作，赋值、del、分片赋值n[1:1]=[2,3,4]
# 序列：索引、分片、加乘、归属
# 赋值可修改元素，不能增加超过长度元素，用None初始化长度；
# 1.赋值修改
x=[1,2,1]
x[2]=3
x           # [1,2,3]
# 2.直接删除
del x[0]
x           # [2,3]
# 3.分片赋值
# 分片赋值可以实现修改、插入、删除列表；
n=[1,5]
n[1:1]=[2,3,4]
n                               # [1,2,3,4,5]

name=list('Per1')
name[1:]=list('ython')          # 长度超越；
name                            # ['P','y','t','h','o','n']

n[1:4]=[]
n                               # [1,5]

# 2.3.3 列表方法 lst.append,pop;insert,extend,remove;sort
# 方法：与对象有紧密联系的函数；
# 方法的调用：对象.方法（参数）
# 列表方法：append, count, extend, index, insert, pop, remove, revers,sort
# 1.append
lst=[1,2,3]
lst.append(4)           # 直接修改原列表；

# 2.count
['a','b','c','a'].count('a')
x=[[1,2],1,1[2,1,[1,2]]]
x.count(1)              # 2
x.count([1,2])          # 1

# 3.extend
a=[1,2,3]
b=[4,5,6]
a.extend(b)
a                       # [1,2,3,4,5,6]
# a=a+b 要慢
# 也分片赋值
a[len(a):]=b            # 可读不如extend

# 4.index
strr=['a','b','c']
strr.index('c')         # 2

# 5.insert
n=[1,2,3,5]
n.insert(3,'four')
n                       # [1,2,3,'four',5]
n[3:3]=['four']

# 6.pop
# 移除最后一个，并返回其值；
x=[1,2,3]
x.pop()                 # 3
x.pop(0)                # 1
x                       # [2]
# 实现数据结构 栈
# push, pop
# append, pop in python. no push in python.
# append 压入，pop 弹出；后进先出；
# 先进先出insert(0,...),pop(0)

# 7.remove
# 移除第一个匹配项, 无返回值；
x=[1,2,3,2]
x.remove(2)

# 8.revers
x.reverse()         # no return
x                   # [2,3,2,1]

x=[1,2,3]
list(reversed(x))   # [3,2,1]

# 9.sort
x=[3,1,2]
x.sort()
x                   # [1,2,3]
# 副本
y=x[:]              # 得到副本y
y=x                 # x,y共同指向列表[3,1,2]

# 10.高级排序 ?
# compare(x,y) x>y 1,x<y -1, x=y 0;
n=[3,1,2]
n.sort(cmp)
n.sort(key=len)
n.sort(reverse=True)

# 2.4 元组：不可变序列
1,2,3               # (1,2,3)
()
42                  # 42
(42)                # 42
42,                 # (42,)

# 2.4.1 tuple()
# 功能类似list转化列表，但返回元组；
tuple([1,2,3])      # (1,2,3)
tuple('abc')        # ('a', 'b', 'c')

# 2.4.2 元组基本操作
x=1,2,3
x[1]                # 2
x[0:2]              # (1,2)

# 2.4.3 元组作用


# 2.5 小结




#           @string  64-75

# 3.1 string base operate 
#       str是不可变的, 操作同序列；

# 3.2 string 格式化输出：精简版 模板%f，%s
#       对数值进行格式化；格式化操作符% 匹配操作符
#       format % values
#       元组为值时，要对应替换
format='Pi with three decimals: %.3f'  # %f 浮点；
from math import pi
print format % pi               # ***:3.142

format='Hello, %s,%s enough for ya'
values=('world', 'hot')
print format % values           # hello,world.hot enough for ya?

# 3.3 string 格式化：完整版
# 3.3.1 简单转化
# 3.3.2 字段宽度和精度
# 3.3.3 符号、对齐和0填充

# 3.4 string method/function        operate self
#       str.method more than list, for extend from string module.
#       str.const
# 3.4.1 find    left,-1
# return index.left, no return -1;
'hello'.find('l')               # 2
a='hello world'
a.find('he')                    # 0
a.find('cc')                    # -1
a.find('w',5,9)                 # 提供起始点和结束点；
        operate self
# 3.4.2 join*        '/'.join(str)
# only join string, not numbers; split;
sep='+'
lst=['1','2','3']
sep.join(lst)                   # '1+2+3'

dirs='', 'usr', 'bin', 'env'
print '/'.join(dirs)            # '/usr/bin/env'
print 'c:' + '\\'.join(dirs)    # c:\usr\bin\env

# 3.4.3 lower
# title(), string.capwords()
'AbC'.lower()                   # 'abc'

name='Nudo'
names=['nudo','abc','def']
if name.lower() in names: print 'Find it.'

# 3.4.4 replace
'This is a test'.replace('is', 'eez')   # 'This eez a test'

# 3.4.5 split*      str 2 list
'1+2+3'.split('+')              # ['1','2','3'] 
'/usr/bin/env'.split('/')       # ['','usr','bin','env']
'a is title'.split()            # ['a','is','title']

# 3.4.6 strip脱去 只脱两头；php.trim修剪
' abc '.strip()                 # 'abc'
'*a*c**'.strip('#')             # 'a*c'

# 3.4.7 translate*？       single,multi
# only replace single a
from string import maketrans
table=maketrans('ab', '12')
'a b 3 4'.translate(table, ' ')         # '1234'


# 3.5 小结




#           @dict    75-85

# 4.1 字典的使用
#       mapping.dict

# 4.2 创建和使用字典{a:1, b:2, c:3}
phonebook={'aaa':'1234', 'bbb':'2345', 'ccc':'9876'}

# 4.2.1 dict函数, 用参数建字典
d=dict(name='nudo',age=36)          # 用 参数 建字典
d                               # {'name':'nudo','age':36}
items=[('name','aaa'),('age','36')] 
d=dict(items)                       # 用 序列 建字典
d                               # {'name':'aaa', 'age':36}

# 4.2.2 dict base operate
#       dict some same as list.
#       different:k in d, v in l,
x=[]                            # 无索引42；
x[42]='value'                   # error, 需[None]*43初始化索引；
x={}
x[42]='value'
x                               # {42:'value'}, key 可以为任何不变的类型

# project: search telbook
# search tel or addr by name
book={
        'aaa':{
            'phone':'9320',
            'addr':'aaaaaaaaaaaaaaaaaaaaaaaaaa'
            },
        'bbb':{
            'phone':'9879',
            'addr':'bbbbbbbbbbbbbbbbbbbbbbbbb'
            },
        'ccc':{
            'phone':'7657',
            'addr':'cccccccccccccccccccccccccccc'
            }
        }
name=raw_input('Name: ').lower()
if name in book:request=\
        raw_input('Phone number (p) or address (a)?').lower()
if request=='p': key='phone'
if request=='a': key='addr'
content={'phone':'phone number', 'addr':'address'}
print name+ "'s " + content[key] + ' is ' + book[name][key]
print "%s's %s is %s." % (name,content[key],book[name][key])

# 4.2.3 dict string format match
# 若元组，% 两边必须对应，
# 若字典，% 左边%s随便摆放；
telbook={'aaa':'2322', 'bbb':'9098', 'ccc':'7657'}
"aaa's phone number is %(aaa)s." % telbook

template='''
<html>
<head><title>%(title)s</title></head>
<body>
<h1>%(title)s</h1>
<p>%(text)s</p>
</body>
</html>
'''
data={'title':'My Home Page', 'text':'Welcom to my home page.'}
print template % data

# 4.2.4 dict.method 
#     1.clear
#       clear dict all items.
#       给别名赋空，不能清除原值;{...} x,y；
x={3:2,5:3}
y=x
x={}
x.clear()

#     2.copy / deepcopy


#     3.fromkeys
#       to built new dict
{}.fromkeys(['name','age'])         # {'name':None, 'age':None}
dict.fromkeys(['name','age'])       # {'name':None, 'age':None}

#     4.get
#      if not exist, no error, return None.

#     5.has_key

#     6.items & iteritems
#     7.keys & iterkeys
#     8.pop
#     9.popitem
#    10.setdefault
#    11.update
#    12.values & itervalues




#           @flow ctr 85-108 @if @forin

#   print语句，import语句，
#   赋值语句
#   条件语句，循环语句

# 5.1 print & import
# 5.1.1 print exp1,exp2,exp3    rsl1 rsl2 rsl3
# 5.1.2 把某件事作为另一件事导入,模块函数重名别名
# 5.2 赋值魔法
# 5.2.1 序列解包，元组赋值
# 5.2.2 链式赋值，
# 5.2.3 增量赋值
# 5.3 语句块：缩排的乐趣, :开始，然后都缩进，结束后缩回；
# 5.4 条件和条件语句
# 5.4.1 布尔变量作用，False, None, 0, '', (), [], {} 
# 5.4.2 条件执行和if语句
# 5.4.3 else子句
# 5.4.4 elif子句
# 5.4.5 嵌套代码块
# 5.4.6 更复杂的条件，对象相同与相等；或赋值；条件表达式
# 5.4.7 断言 assert
# 5.5 循环
# 5.5.1 while循环
# 5.5.2 for循环，for * in range()
# 5.5.3 循环遍历字典元素, for k in d:
# 5.5.4 迭代工具
#       1.并行迭代循环zip(); 任何序列，不等长；
#       2.编号迭代循环enumerate(),/i'nju:/列举、枚举、计算；索值对；
#       3.翻转和排序迭代reversed,sorted; return did 副本；list,join
# 5.5.5 跳出循环
#       1.break
#       2.continue  跳出本次循环
#       3.while True/if break  可以在循环内部任意地方终止循环;
# 5.5.6 循环中的else子句
# 5.6 列表推导式——轻量级循环103[x*x for x in range(10)]; []not()
# 5.7 三人行
# 5.7.1 pass    do nothing and continue. for test.
# 5.7.2 del & None
#       None to delete name but no value.
#       del to dleete name and value, 
#           but if two name one vlue, only del name.
# 5.7.3 use exec & eval 执行和求值字符串
# print code in string. disp str;
# exec code in string.  disp result of str;
#       1.exec
# scope /skoup/ 范围、眼界、作用域, 命名空间；
#       2.eval
#         exec 会执行python语句；  is 语句
#         eval 会计算python表达式；return result.





# 5.1 print & import
# 5.1.1 print exp1,exp2,exp3
#       print may output expresses表达式 by ','；result split by space;
print 1,2,3                 # 1 2 3     不是元组；
print (1,2,3)               # (1,2,3)
1,2,3                       # (1,2,3)   元组可以不写小括号；

# 5.1.2 把某件事作为另一件事导入,模块函数重名别名
# 磨,模型mo2 model毛豆
# 磨,模块mo2 module毛州
# 木,模板mu2 template
# 别名
from module1 import open as open1
from module2 import open as open2

# 5.2 赋值魔法
# 5.2.1 序列解包，元组赋值
x,y,z=1,2,3                 # 元组赋值, 序列解包；
x,y=y,x                     # 变量交换；

# 5.2.2 链式赋值，
x=y=z=func()

# 5.2.3 增量赋值
# 标准运算符放在=的左边；
x+=2
x*=6
x%=3

# 5.3 语句块：缩排的乐趣
#       :开始，然后都缩进，结束后缩回；

# 5.4 条件和条件语句
# 5.4.1 布尔变量作用，False, None, 0, '', (), [], {} 
False, None, 0, '', (), [], {}          # 皆为假false, 但都并不相等；
True+False+2                            # 3, 布尔值可看做是特殊的数字01；
#       bool()转换其他类型为布尔值, 一般Py会隐式转换；
bool('This is a test.')                 # 1
bool(23)                                # 1
bool('')                                # 0
bool(0)                                 # 0

# 5.4.2 条件执行和if语句
# 5.4.3 else子句
if ***:******
####
if ***:
    ******
else:
    ******
# 5.4.4 elif子句
if ***：
    ******
elif ***:
    ******
else:
    ******
# 5.4.5 嵌套代码块
# 5.4.6 更复杂的条件，对象相同与相等；或赋值；条件表达式
#     1.比较运算符; x!=y; 要同类型的比较；相同的值是不同的对象；
x is y                      # is判断是否是同一对象/值;=判断对象是否相等；
'abc' < 'ade'               # True;
[1,2] < [2,1]               # True;
[2,[1,4]] < [2,[1,5]]       # True;

#     2.布尔运算符 and or not 短路特性；
#       或赋值：
#           用户应输入名字或不输用默认：
name=raw_input('Please enter your name: ') or '<unknow>'
#       条件表达式：a if b else c       if b=true ,return a, else return c;
#       x?a:b (php)

# 5.4.7 断言 assert
#       断言，断然言之，十分肯定地说；坚持；
#       人为“要求”条件为真或假；关键字：assert
#       用于单元测试或检测；
age=10
assert 0<age<100        # 系统没报错；
age=-1
assert 0<age<100        # 系统报错；

# 5.5 循环
# 5.5.1 while循环
while ***:
    ******
x=1
while x < 100:
    print x,
    x+=1

name=''
while not name():
while not name.strip():
while not name.strip():
    name=raw_input('Please enter your name:　')
print 'Hello, %s!' % name

# 5.5.2 for循环，for * in range()
for *** in ***:
    ******

n=[0,1,2,3,4,5,6]
for nn in n:
    print nn

for n in range(1,101):
    print n,

# 5.5.3 循环遍历字典元素, for k in d:
d={'x':1, 'y':2, 'z':3}
for key in d:
    print key, 'corresponds to', d[key]      # 2,1,3? 字典没顺序 

# 5.5.4 迭代工具
#       1.并行迭代循环zip(); 任何序列，不等长；
names=['aaa', 'bbb', 'ccc']
ages= [23, 43, 65]
for i in range(len(names)):
    print names[i], 'is', ages[i], 'years old.'

for name,age in zip(names,ages):    # 解包元组,元组赋值；
    print name, 'is', age, 'years old.'

zip(names,ages) # [('aaa',23),('bbb',33),('ccc',65)]
# zip可以作用任意多的序列，特别是可以不等长；
zip(range(3),xrange(10000))         # [(0,0),(1,1),(2,2)]

#       2.编号迭代循环enumerate(),/i'nju:/列举、枚举、计算；索值对；
#           在提供索引的地方迭代索值对；
#           替换所有包含‘xxx’
for index,string in enumerate(strings):
    if 'xxx' in string:
        strings[index]='[censored]' # ?

#       3.翻转和排序迭代reversed,sorted; return did 副本；list,join
print sorted('abc')   # return ['a','b','c']
print reversed('abc') # None 必须和其它函数配合使用
print list(reversed('abc'))     # ['c','b','a']
print ''.join(reversed('abc'))  # cba

# 5.5.5 跳出循环
#       1.break
# project:寻找100内最大平方数；
from math import sqrt
for n in range(99,0,-1):            # 生成从大到小的元组
    root=sqrt(n)
    if root==int(root):
        print n
        break

#       2.continue  跳出本次循环
#       3.while True/if break  可以在循环内部任意地方终止循环;
while True:
    word=raw_input('Enter a word: ')
    if not word: break              # not word,--=+;
    print 'The word is '+word

# 5.5.6 循环中的else子句
#       如何没跳出前做些事情；？
from math import sqrt
for n in range(99,81,-1):
    root=sqrt(n)
    if root==int(root):
        print n
        break
    else:
        print "Didn't find it!"

# 5.6 列表推导式——轻量级循环103[x*x for x in range(10)]; []not()
#       利用其它列表创建新列表[],不能();
[x*x for x in range(10)]
[0,1,4,9,16,25,36,49,64,81]
[x*x for x in range(10) if x%3==0]
[0,9,36,81]

[(x,y) for x in range(3) for y in range(3)]
[(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
# 对比
result=[]
for x in range(3)
    for y in range(3)
        result.append((x,y))
# 找出名字首字母相同的男孩女孩：
girls=['a9', 'b9','c9']
boys=['b8','a8','c8']
[x+'+'+y for x in girls for y in boys if girls[0]==boys[0]]
['a9+a8', 'b9+b8', 'c9+c8']
?

# 5.7 三人行
# 5.7.1 pass    do nothing and continue. for test.
if name=='aaa'
    print 'welcome'
if name=='bbb'
    # 还没完。。。
    pass
if name=='kkk'
    print 'Access Denied'

# 5.7.2 del & None
#       None to delete name but no value.
#       del to dleete name and value, 
#           but if two name one vlue, only del name.

# 5.7.3 use exec & eval 执行和求值字符串
# print code in string. disp str;
# exec code in string.  disp result of str;
#       1.exec
exec "print 'Hello, world!'"        # Hello, world!
# scope /skoup/ 范围、眼界、作用域, 命名空间；
from math import sqrt
scope={}
exec 'sqrt=1' in scope              # 字典作为命名空间
sqrt(4)                             # 2
scope['sqrt']                       # 1

#       2.eval
#         exec 会执行python语句；  is 语句
#         eval 会计算python表达式；return result.
eval(raw_input('Enter an expression: '))
6+18*2                              # 42

scope={}
exec 'x=2' in scope
eval('x*x', scope)                  # 4; 在空间内算值；



#           abstraction:function 109-132  @func


# 本章，将语句组成函数；parameter, 作用域scope, 递归；
# 6.1 懒惰即美丽
# 6.2 抽象和结构
#       计算机善于精确和具体；
#       人更善于把握的总而概之的抽象；
#       把一段 相对独立功能的代码片段 封装为一个抽象概念函数；
#       就可以抽身于具体，站在更高的层面，操作代码；

# 6.3 创建函数
def hello(name):
    return 'Hello, '+name+'!'
print hello('nudo')

# 6.3.1 记录函数,注释文档；
def square(x):
    'Calculates the square of the number x.'    # 字符串注释法；
    return x*x
# 文档字符串的访问：
print square.__doc__

# 6.3.2 并非真正函数的函数, return;
#       when no value, func return None.
# 6.4 参数魔法
# 6.4.1 值从哪里来, 
#       形参:  接受外部值得内部变量;func(n),x=6,func(n=x);
#       实参： 给形参赋的值，传入内部的值；传参即赋值；
#       形参=实参；
# 6.4.2 我能改变参数吗
#       如果传入的是个变量func(x=a), 那形参就是这个变量的别名；
#       参值是不可变元素：
#       字符串、数字、元组，本不可变（局部修改），只能整体赋新，非别名了；
#       参值是可变元素：
#       列表，若别名修改，外部变量也会变；
#             若不变，引入副本，切片总是返回副本；
def func(n):
    n[0]='c'
    return n
x=['a','b']
print func(n=x)
print x
print func(n=x[:])
print x
#   1.为什么我要改变参数,局部作用域local scope
#       func change datastruct
#       抽象的要点就是隐藏细节；

#   2.如果我的参数不可变呢

# 6.4.3 关键字参数和默认值; 【位参pospar，键参keypar】
#       位置参数：顺序必须对应；
#       关键字参数；顺序灵活，还可提供默认值；
#       联合使用：位参在前，键参在后；
#       根据两参的特性，可以灵活调用
def hello(name, greeting='Hello', punctuation='!'):
    print '%s, %s%s'
hello('aaa')                    # Hello, aaa!
hello('aaa', 'Howdy')           # Howdy, aaa!
hello('aaa', 'Howdy' '...')     # Howdy, aaa...
hello('aaa', punctuation='.')   # Hello, aaa.
hello('aaa', greeting='Good morning')   # Good morning, aaa

# 6.4.4 收集参数【*pospar,**keypar】收位参，收键参；
#       就是没有对应形参的实参它都收；收集的结果形式为元组or字典；
#       将参数收集为元组和字典
def print_params(*params):          # 收位参
    print_params
print_params('a')                   # ('a', )
print_params(1,2,3)                 # (1,2,3)

def print_params(title, *params):   # 普参，收位参；
    print title
    print params
print_params(8, 1, 2, 3)            # 8 (1,2,3)
print_params(8)                     # 8 ()

def print_params(**params):         # 收键参
    print params
print_params(x=1, y=2, z=3)         # {'x':1, 'y':2, 'z':3}

def print_params(x,y,z=3,*pospar,**keypar):
    print x,y,z
    print pospar
    print keypar
print_params(1,2,3,5,6,7,foo=1,bar=2)
# 1 2 3
# (5,6,7)
# {'foo':1, 'bar':2}
print_parms(1,2)
# 1 2 3
# ()
# {}

# 6.4.5 翻转过程
# 6.4.6 联系使用参数
# 6.5 作用域
globals()[var]         # 访问全局变量
vars()[var]
locals()[var]          # 局部变量

x=1
def change_global():
    global x
    x=x+1
change_global()
x       # 2
# 嵌套作用域125
?
# 6.6 递归recursion/ri'ke:sen/
# print 3 2 1 0
def rcs(n):
    return n
    if n>0 :
        rcs(n-1)

print rcs(9)
# 6.6.1 两个经典：阶乘和幂
# 阶乘5*4*3*2*1
# 先实现一层，再调用 次本身 实现第二层；
def jc(n):
    if n==1:
        return 1
    else:
        return n*jc(n-1)
            #  n*((n-1)*jc(n-2))

print jc(5)
# 幂2*2*2=2^3
def mi(x,n):
    a=1
    for i in range(n):
        a*=x

def power(x,n):
    if n=0:
        return 1
    else:
        return x*power(x,(n-1))

mi(2,3)

# 6.6.2 另外一个经典：二元查找
lst=[3,89,5,7,10,88,6,99,12]


# 6.6.3 显示xx数；
def rcs(n):
    print n
    if n>0 :
        rcs(n-1)
    else:
        print '-------------'
    print n

rcs(9)





#           @object  132-147

# can program large project.

# 7.1 对象的魔力
# 7.1.1 多态
# unknow objectType, can call method.
# 不管对象类型，只要用对象的方法就行了；
#   1.多态的方法
'abc'.count('a')
[1,2,'a'].count('a')
#   2.多态的多种形式
# unknow object type, but must do something on object. then use ploym；
# not only method, operate and function also have ploym
def add(x,y):
    return x+y
add(1,2)
add('Fish','license')

def lengthMessage(x):
    print 'The length of', repr(x), 'is', len(x)
lengthMessage('Fnord')
# The length of 'Fnord' is 5
lengthMessage([1,2,3])
# The length of [1,2,3] is 5
# repr() is ploym. repr return express

# 7.1.2 封装encap
# not care inside, but can Use.

# 7.1.3 继承
# 7.2 类和类型
# 7.2.1 类到底是什么
# class, instance, subclass, superclass;
# 7.2.2 创建自己的类
__metaclass__=type # sure to use new class;
class Person:
    def setName(self, name):
        self.name=name
    def getName(self):
        return self.name
    def greet(self):
        print "Hello, world! I'm %s." % self.name
foo=Person()
bar=Person()
foo.setName('fff')
bar.setName('bbb')
foo.greet()         # Hello, world! I'm fff.
bar.greet()         # Hello, world! I'm bbb.
# bar.greet()=Person.greet(bar)

# 7.2.3 特性、函数和方法

# 7.2.4 类的命名空间

# 7.2.5 指定超类
# 7.2.6 调查继承
# 7.2.7 多个超类
# 7.2.8 接口和内省
# 7.3 面向对象设计的思考

















