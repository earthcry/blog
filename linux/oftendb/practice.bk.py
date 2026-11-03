# 4.0 字符串 _@string

#  str - num, str <-> num; duiying yu zhuanhuan;
print "编码转换，数字与字母:"
print "ord('a'): %s" % ord('a')
print "chr(97): %s" % chr(97)
print " A: %s\n Z: %s\n a: %s\n z: %s" % (ord('A'),ord('Z'),ord('a'),ord('z'))

# traverse alphabet list:
print "26英文大写字母:"
for e in range(ord('A'),ord('Z')+1):
  print chr(e),
print '\n'
print "26英文小写字母:"
for e in range(97,123): # range(65,91)
  print chr(e),
print '\n'

print "26随机大写字母："
import random
n=0
while n<26:
  print chr(random.randint(65,90)), # [65,90] v;
  n+=1
print '\n'


# 产生a-z的序列
# another
print ord('a')
print ord('z')

lst=range(97,123)

chrLst=[]
for e in lst:
    chrLst.append(chr(e))

print chrLst
# 
lstchr=[]
for e in range(97,123):
    lstchr.append(chr(e))


# 编码转换，数字与字母之间的，函数ord()chr()
char='a'
lst=[]
while char!='z':
    lst.append(char)
    char=chr(ord(char)+1)
else:
    char=='z'
    lst.append(char)
print lst



# 4.1 字符串类型
#       string=Index + Char  索引
#       list  =index + item
#       dict  =key   + value

#       字符串<序列<数据集 len() for in
#       字符串对象的构建，'',"",str();
#       字符串是一种序列，序列中的对象按一定顺序排列；
# 4.1.1 三重引号字符串，保留所有格式信息；
# 4.2 字符串基本操作_@strOperate_@so,+,*,[:],in,replace;
# 4.2.1 连接+和重复* 画图
print 'ab-'*8
print 'ab-'+'-cd'
x='a'
x=x+'b'
x=x+'c'
print x
# 4.2.2 '+'连接运算与加法运算，看对象，不同方法的符号 相同;
# 4.2.3 比较运算符
#       1.单字符 字符串的比较，AC码
#       2.多字符 字符串的比较，
# 4.2.4 in运算符 e in hello
# 4.2.5 字符串集合是 不可变的，副本[:]，创建新字符串；
#       一旦创建对象，其值不可改；要改变，创建新值，赋于原名；
strr='hello'
strr[0]='k' # err

# get 'jello'
strr='j'+ strr[1:]
print strr

a='hel,lo.'
a='hello'
b=a.replace('h','j')
print a     # hello
print b     # jello

# 数据处理.字符串除杂.集合遍历置换;
strr='hel,lo. w-or,ld.' 
for e in (',', '.', '-'):
   strr=strr.replace(e,'') # str not change
print strr  # hel lo

# 4.3 函数和方法预览
# 4.3.1 第一步：什么是函数，打包封装的程序；函数>方法；对一段代码的命名；
#       1.字符串函数
#       2.字符串方法，区别，调用方式；
#       3.方法链，'A string'.upper().find('S');
#       4.可选参数
#       5.方法的嵌套 aStr.find('t',aStr.find('t')+1)
# 4.3.2 选择方法的名字和参数
# 4.3.3 _@strMethod_@sm字符串方法 strip脱去，剥去；清洗除杂；
#       Python/dir(str)/help(..)
#        strr.split() <==> ' '.join(lst)
# +,*,in,[:];   len(),for in,
# bStr=aStr.lower().upper()
# bstr.find(),
# bStr=aStr.replace('.', '') all '.' replace in str.
# bStr=aStr.strip(',. ') work at head and tail, not middle.

# s.strip():  _@strip
# default remove noDispChar at head&tail,or s.strip(',.!?')(string.punctuation)
# 4.4 字符串的格式化输出_@strPrint_@print_@geshi
print "format string" % (data1, data2,...)
print "%s is %d years old." % ("Bill", 25)
# Bill is 25 years old.

# 4.4.1 Number描述符 码
# %s, %d, %f, %e浮点指数；
print '%f' % 3      # 3.000000
print '%0.2f' % 3   # 3.00

num=0.0
while num < 3:
    print '%0.2f' % (num)
    num+=0.1

#   print "a"+str(int(num))+":%5.2f" % (num)

# 4.4.2 宽度描述符   '%-3s' % a, '%5d' % b.  (a,str(b))
#       用于表格整齐显示
print "%-6s%5.2f" % ("Bill", 2.5)
# Bill__|_2.50                 -左对齐,+右对齐；
# var+blankspace=6

# 4.4.3 浮点数精度描述符
# 小数点后的位数，精度；%.3f
print math.pi
# 3.14159265359
print "Pi is %.4f" % (math.pi)
# Pi is 3.1416
print "Pi is %3.4f" % (math.pi)
# Pi is ___3.1416

# 4.5 字符串与控制语句 147
# **** list iter index, dict iter key.

# use find() get 'p' in 'Mississippi'
river="Mississippi"
river.find('p')
# 字符串都有个隐式索引
# example：
# Replace find() by use normal operate of string.
# 算法思想：迭代+对比
# 迭代对象：数据集，列表，
# 字符串列表？索引列表？如何产生索引列表？range(0,len(river))
# 对比对象：索引？字符？对应的字符；
# 不用额外计数器，e
# 迭代迭代

#       代码                逻辑
river="Mississippi"      # 待操作的字符串对象；
lst=range(0,len(river))  # 建立索引列表
for e in lst:            # 迭代索引列表
    if river[e]=='p':    # 对应的字符串元素，对
        print e,river[e] # 打印索引及对应的字符；
        break
# another
def myfind(string,letter):
    n,index=0,0
    for e in string:
        if e==letter:
            index=n  
            break         # disp first index
        print e,n,index
        n+=1
    return index

print myfind(river,'p')
# 用概念和关系，进行算法描述；
# 双层思维，代码和逻辑；
# 一定要先将问题形象化；

# 形象，逻辑，代码；


# 4.6 处理字符串

# 4.6.1 示例：记录人名

# 4.6.2 回文
#       1.改变大小写
#       2.只有字母和数字
#       3.综合应用
# ********************************

# 分类 字符集 字符串；
import string

print string.punctuation,\
      string.digits,\
      string.lowercase,\
      string.whitespace

a=string.punctuation #标点符号/pankchu'eishen/ punc
b=string.digits
c=string.lowercase
d=string.whitespace
print a, '\n', b, '\n', c, '\n', d
# 4.7 示例：计算扑克牌
#       1.对文件中所有牌进行计数
#       2.计算包含1对牌的总手数
#       3.编程计算出现一对牌的概率
#       4.程序其余部分
#       5.观察输出
# 4.8 总结


#!/usr/bin/env python
#coding:utf-8



#          Python Concept Tree



# python.ebook.txt
# linux.ebook.txt
# vim.ebook.txt
# internet.ebook.txt
# ai.ebook.txt
# cognition.ebook.txt

# note mode: search remember
#       knowledge point,concept system,
# note rule: interaction dialog for understand, concept for remember.



# 	book: The Practice of Computing Using Python




'''

以思想逻辑层面阅读预测

_@computer计算机
        gongneng: moni xianshi.计算机是加工信息的机床.
        class: 机床，算盘，逻辑电路。万能工具，智能工具.
	yuanli: 开关真假，电路晶体管，逻辑电路
	structure: 体系结构，各个部分及作用。模型。
	计算流程:
		取指令
		解码指令，取数据
		执行指令
		存储结果
		重复
		sum=num1+num2
	最小通用程序:
		load a
		++
		store a
		back x
		clear
	二进制，计算与存储
_@计算，加工，规则编辑，
	材料，树木钢铁，社群，语言图像。
	质子中子电波，细菌基因。时空星河。
	节奏节拍，时钟鼓手传送带
_@算法
	编辑加工的规则方法. gongshi
	化整为零是一个算法的主要原则。分解
	问题模型，算法公式。周长面积椅子 _@problemModel,algorithm
	数据结构，操作方法               _@dataStructure,method
		数字及其操作
		字符串及其操作
		木材结构金属结构塑料结构
	食谱
_@编程，流程工序,buzhou
	_@语言，_@指令
	语言，描述对象及其关联和相互作用。
		描述现象，用于对象间的沟通。
		人与人，人与机器。
		编程语言是人机对话语言
		程序=指令+算法
		文章=语言+思想
	层级交互界面
	算法，
	数据，代表模拟测量
		二进制十进制
			进制基数，单位木桶瓷缸池塘立方
			用数字来代表一个池塘水的数量
			753(10)=7*10^2 + 3*10^1 + 5*10^0
			101(2)=1*2^2 + 0*2^1 + 1*2^0
			1052(10) = 2^10 + 2^4 + 2^3 + 2^2
			一个基数进一位，两个基数
			64位存储器
		字符集
		数据类型，对应用途
		数据量
			KBGBTBPBEBZBYB2^10203080
	数据，程序，结果
_@control控制语句：分支选择，重复循环，tiaozhuan函数，对象
	_@控制语句，控制 指令执行顺序路线
	控制指针路线
	逻辑流程图
		可选，三角形
		二选，菱形
		多选，菱体
		条件循环，半圆
	可择一 选择语句 if
	二择一 选择语句if else
	多择一 选择语句 if elif else
	条件循环语句 while，重复次数
		用while重复做事，次数，用一个变量计数器来控制。
			定义 重复次数 初始点，终止点。
		当计数器为某一值时重复运行
		while else先分支后重复
		break 找到答案
		continue 跳过某次循环 如一个错误输入
		while 也可计数循环，代替for in
	集合循环语句 for in
		要借助迭代器
		for in else
		range(a,b,c) [a,b) a2-a1=c
		random.randrange(a,b,c)
		int(raw_input())，一切输入皆为字符
		数字计算_真假判断_真假计算
			数字关系真假判断 5-3 < 7 == True
			判断的判断 True or False ==True
				真假的计算: 并或非and or not
			对数字求整计算
			对大小求真计算
			对真假求真计算、、、
		控制结构的嵌套与函数封装
			可读性
_@绘图，数字计算_真假判断_真假计算
	turtle, time.sleep()
	pylab,
	matplotlib
_@字符串 str，序列
	构造字符对象的方式：str(),  ' ',  " ",  ''' ''',  \n \t
	ASCII, ord('a'), chr(97)
	序列索引运算符[ ], word[0], 子序列 word[1:3]，digits[ : : -1]
	连接，重复 +  * , type() .in
	比较的是ASCII
	字符串集合是不可变的
	集合长度 len(),  set.find() 未找到，返-1非0
	raw_input() 都转化为字符串
	字符串函数与方法len()，str.upper().find('S', 1, 6)
	字符串方法集
	格式化输出：print 'xxx%dxxx%sxxx' % (8, 'ok'),    %8.2d
	字符串模块
_@函数，化整为零
	函数是一种把问题化整为零的实现方式
	函数调用函数，函数调用自己。
	代码模块化：封装抽象，简化，功能
	功能代码的封装
	方法是操作对象的函数 str1.upper()
        代码复用：重复调用，
	def fun(x, y):
         return value
        fun(5, 9)
	return
	函数内部，有独立命名空间。
_@列表，元组，list，tuple
【】
'''

#           操作信息，操作数据


# &智能工具'，电脑网络，用来 操作加工 信息数据，效果非常高效；&机床；

# layeres of use computer: 
#  headware > os > app > operateres
# 原始电脑网络 属于 高科技 范畴，常人难以使用；
# 业内人士，
# 在 原始电脑网络 和 常人 之间，
# 创建了 不同层次 的 分门别类 的 交互界面，让应用变的简单。
# 业内人士，程序员，专家：通过算法和编程，
# 创建多层各类，应用界面，应用程序，应用软件。 

# 电脑是计算加工，互联网是连接；
# *程序员提供软件和服务，用户提供数据和需求。

# *操作 信息数据，简称 计算；data+cmd=programe
# 计算是人类或机器对数据进行操作。*因果计算；
# 计算机按人类输入的 指令和数据 进行计算；数据指令；
# 计算 是 计算机最在行的事情，但只能用 二进制 进行 计算；
# 二进制 是 电脑语言，是电脑能直接接受人类的指令。
# 为了简易和高效，专家在电脑语言和人类语言之间，创建了各种编程语言；
# 即在数字和特定单词与字符之间建立映射关系；
# 这些特定单词与字符，即是编程语言；

# 现在，人类不用输入长串长串的数字，
# 只要按某种算法输入特定单词和字符，即编程，就可以让计算机对某种问题计算；

# 编程语言，与二进制有 "映射关系" 的，描述 "数据及其操作" 的单词和字符，指令集；Python.
# 算法，解决问题的方法, 加工规则；

# 编程，算法+语言
# 计算机做任何事情，都可以分解为一系列简单操作。
# 编程，对任何复杂问题的解决，都分解为... 

# _@程序，指令集，溶入算法的。程序=指令+算法
# _@编程，构建算法，指令表达。问题，算法，表达。

# 知识点的融会贯通，因果关联，模型结构概括关联，融会贯通的结果：整体化；

# 算法方法要适合环境；
# 核心，最简分块，迭代，实现；
# relax
# 函数模块，已解决基本问题的程序的封装；

# _@数据结构，操作方法；num,str,bool, lst[],dct{},obj,
# _@问题模型，算法；
# _@data object
'''
q: 数字及其操作；
q: 字符串及其基本操作与方法；

q: 圆的周长，面积：问题模型，公式，算法；
q: 降雨量，体积，单位换算：...
q: 五角开形：调用模块，输入参数；
q: 篮球安全领先：
q: 完全数：定义=公式
q: 布尔：google search
q: 数字猜迷：
q: 蛋糕：食谱=量料+步骤 
q: 巴比伦平方根：
q: 词频：
'''
#   Python入门经典 / 用Python解决问题的练习
#   The Practice of Computing using Python
#   (美)William F.Punch Richard Enbody 著


# 0.0计算机科学的重要性：
# 很难找到计算机不起作用的领域。计算机---*万能工具；
# 计算机解决问题的范围。

# *翻译法语诗歌；语言，问题；
# 先策略后编程, 先算法后编程；
# 可读和编程一样重要；可读，算法；

# 神经网络
# 遗传算法

# 开关，晶体管，集cheng电路，微处理器，
# CPU运行速度，时钟，鼓手，协调，节奏；

# 计算机基本功能：
# sum=num1+num2
# 获取指令；sum=num1+num2
# 指令解码；，提取num1,num2
# 执行指令；加法
# 存储结果；


# 数据表示，二进制数据，计数，以2为基数，以10为基数；
# 二进制，表示，数字，字符；page31, ？


# ******用代码实例，到位，理解概念；
# 36
# 1.0 开始编程
#       程序，指令集，溶入算法的。特点，快速虚拟实现。    程序=指令+算法
#       文章，语言，溶入思想的。特点，传播认知，同步观念。文章=语言+思想
#       编程，构建算法，选择指令表达。思想方法与语言。
#       问题，对象，分类，学科；难易，变数；
#       输入，算法，输出；
#    ***计算机做任何事情，都可以分解为一系列简单操作。
# 计算是人类或机器对数据进行操作。
# 程序组成：模块+语句表达式+标记+空白+注释（标记语句，运算符）
# 程序组成：模块+关键字+数值+运算符

# 通过算法和编程，叫电脑操作数据。 


# ******用代码实例，到位，理解概念；
#       概念，字符，结构，功能；

#       生活由琐碎组成，单独的琐碎无意义，
#       由“卓越思想”统一的琐碎，就很不一样了。
#           算法－－－思想


# 1.1 练习，练习，再练习； 
# _@jieshiqi
# _@interpreter of python:                 # /in'teprite/, pass side
#  1.statement interactive model.       
#       IDLE/python&exit()...ctr+enter/enter*2
#       cmdLineArgv: ./test.py argv1 argv2; import sys,sys.argv;
#  2.file      execute     model.  
#    chmod a+x xxx.py, 
#    python ./xxx.py
#    #!/usr/bin/env python
#    #coding: utf-8
#    ./xxx.py
#  3.setdefaultencoding of python
#  Lib\site-packages\sitecustomize.py(new)

_@argv


#encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# display
print sys.getdefaultencoding()   # ascii

#  _@decode and _@encode
#  utf-8,gbk,ascii < unicode, string unicoded in python. u'abc'
#  gbk->unicode->utf-8
str1.decode('gbk')
str1.encode('utf-8')  # or 
str1=str1.decode('gbk').encode('utf-8')
#  judge what encode:
# method1: 
isinstance(str1,unicode)  # (/ (str1,str)python3)
# method2: 
chardet.detect(strr)      # {,'encoding':'utf-8'} 
chardet.get('encoding')   # utf-8

# out gb2312
s='图形'
if (isinstance(s,unicode)):
  s.encode('gb2312')
else:
  s.decode('utf8').encode('gb2312')

# another method: codecs
import codecs

# fangshi:form, fangan:scheme
# 1.2 快速入门——计算圆周长的程序
#       图形量化问题，量化公式，
# lenccl=math.pi*2*r
# sqrccl=math.pi*r*r
# sqrccl=math.pi*r**2

import math
r=raw_input('Circle R: ')
r=int(r)
lenc=math.pi*2*r
area=math.pi*r*r
print 'Circle lenth:', lenc, 'area:', area
# 1.3 交互式会话
# 1.4 程序的组成部分
# 1.4.1 _@模块，文件，object,导入模块，导入代码； 
# import _@module     math,os,int,str,list,tuitle,pylab,
# module.py:
def func1():
  '''func1'''
  pass
def func2():
  '''func2'''
  pass
# ______________________
print module.func1()
dir(module)
['__doc__','__name__','__package__','func1','func2']
help(module.func1)
math.pow.__doc__
# import & form module import *: later not need object.
pow.__doc__
########
# 1.4.2 表达式和语句 _@statement and _@expression
#	语言=指令=代码=表达式+语句
#	语言=关键字+数值+运算符

#       表达式=数值+运算符，将产生新值（有返回值,有值）；x+5,
#       语句，执行一些任务，无返回值,无值。赋值语句x=5,
#	值=对象，数据；
#      *语句=关键字+表达式；?
#       指令，语句，标记；
x=5
print x+8   //right   python 允许 print an expression.
print y=x+8 //err     python not print  a statement.

# 1.4.3 空白blank, blankLine
#       1.缩进 4*whitespace ,vim set.?
#      *2.续行 \
# 1.4.4 注释 #，''', function''',__doc__;
# 1.4.5 Python特殊元素：标记(特殊关键字、运算符), 指令；
#       1.关键字
#       2.运算符
#       3.标点符号和分隔符
#      *4.字面量，代表一个固定值，123，
# 1.4.6 对象命名，区分大小写；
# 1.5  *变量与赋值，对象引用；复制关联；_@var

var=var+1       # 表示 从变量var中 取出值后+1 再放回变量var中；
# loop up, 累加赋值；递减赋值；累乘赋值；

id(var)
type(var)

# 1.6 对象和类型
#       多个命名空间，可以关联同一对象不同名子；
#       对象的类型，告诉Python两个事情：
#           对象基本属性，整数对象中没有小数点；
#           能进行的对象操作和返回的结果，字符串不能除法操作；
#       变量名与它相关联的对象类型无关；

#       数据类型，对象类型: 及其操作：
#       基本类型，数字，字符串，布尔；
#	组合类型，列表，字典，对象，集合，队列，矩阵；
# 1.6.1 数字_@number
#       1.整数，int,长整型，L；12，012，8八进制, 0x；
#       2.浮点数,float 代表实数，但只是近似值，不是精确值。0.66666666666666
#       3.复数，2+3j，实部和虚部；
# 1.6.2 其他内置类型；
#       1.布尔类型，bool表示为整数；True,False.
#       2.字符串，string是集合序列类型；
#       3.列表，[] list. () tuple
#       4.字典，{} dict
#       5.阵列，array([])；numpy.array,主要do float data,优点可用算术符
#       6.集合，set([])不重复元素，数据集；
#       7.队列，
#       8.矩阵，
#
#           数据结构：
#           变量，数据容器；
#           序列，映射，集合；
#           堆栈，队列，矩阵；           

#           数据结构，及其操作与方法；
#           语句，执行顺序：选择，重复，函数；

# 1.6.3 对象类型：非变量类型
#       对象类型决定了对象的存储方式，运算类型；
#       构造函数，生产新对象，int(),float(),str(),bool();

# 1.6.4 创建新值
# 1.7 运算符_@operator
#     重载，change object of operator.3+2,'a'+'b'; "+"的重载；
# 1.7.1 整数运算符，+ - * / % **;
#       除法不一定为整数，分为，取商/，取余%；结果为整数，**幂；

5/3  # 1
5%3  # 2. n%3==0,
3**2 # 9
2**3 # 8 

# 1.7.2 浮点运算符，得到一个近似值。+-*/**;
# 1.7.3 混合运算符
#           整数和浮点都有各自独立的运算硬件。分类运算；
int(2/3)        # 0
float(2/3)      # 0.666...

# 1.7.4 运算符顺序和圆括号
# 1.7.5 增强的赋值运算符：快捷方式 a+=1
# 1.8 第一个模块：math模块 
# _@help _@manual _@doc _@pydoc _@help() _@dir()

pydoc math          # outside python

import math
dir(math)           # find object attribute/property
help(math.pow) 
math.pow.__doc__    # **
def xx():
  '''test a test
  test test a try'''
  pass

# _@algo
# 1.9 开发算法
#       算法，一种方法，描述如何解决一个问题或一类问题；
#                       英语，图表，流程图；gongshi
# example: PG58
# 降雨量：1亩地上有1英寸的降雨，请问累积多少加仑的水？？？
# 第一反应，困难——默生单位
#         1平方米上有1米的降雨，请问累积多少立方米的水？
# 困难的是什么？
###########################333
'''
question model:
加仑 ~~~ K 亩 * 英寸

v=s*h, 立方米=平方米*米
aj=bm*cy a加仑=b亩*c英寸,
j=q*m*y, q=b*c/a

264.1720524加仑=0.0015亩*39.3700787英寸
q=(0.0015*39.3700787)/264.1720524
j=q*1*1
'''
# 1.10 总结
# 1.11 视觉场景：海龟绘图
# import _@turtle # /t3:tl/ ********
# example:
# 绘制五角星？？？？？？？？？？？
import turtle
import time
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
turtle.forward(100)
turtle.right(144)
time.sleep(3)

# 2.0 _@control控制语句  PG65
#     控制语句，改变代码 执行方向；
#	        选择和重复
# 判定，选择和重复，函数；

# 2.1 选择语句：_@if

# 判定方向

'''
if boolexp:
    suite

if boolexp:

[[elif boolexp:]]
[[elif boolexp:]]

[else:]


'''
# 2.1.1 利用布尔值做决定
# 2.1.2 if语句
#       1.基本的if语句
#       2.缩进与Python代码块
#       3.if-else语句
# 2.1.3 示例：在篮球运动中，领先多少分才安全？
#
# example:
# 在篮球运动中，领先多少分才安全？
# *算法：
# *找出算法是编程中最难的部分。
# *将原始算法包含在注释中。
# 1.获取领先一队A的分数score。
# 2.减三分；
# 3.A控球+0.5，否则-0.5（score<0,=0）；
# 4.result=score.sqr
# 5.result>time is safe.
pointsStr=raw_input('Enter the lead in points: ')
points=int(pointsStr)
has_ball=raw_input('Does the lead team have the ball (Yes or No): ')
if has_ball==Yes:
    points+=0.5
else:
    points-=0.5
if points < 0:
    points=0
points=points**2
seconds=int(raw_input('Enter the number of seconds remaining: '))
if points > seconds:
    print 'Lead is safe.'
else:
    print 'Lead is not safe.'

# 2.1.4 重复循环，计数循环count _@loop _@while _@for _@recursion
#       1.基本while语句
#       2.迭代：基本for语句
#       3.break,continue
while boolexpression:
    suite

# example: print 0-9
x=0
while x < 10:
    print x,
    x=x+1

# break: out hole loop
# continue: out back code of the word continue, then contiue next loop.
# loop       1 2 3 4 5
# break      1 2 3
# continue   1 2   4 5
i = 0
while i < 5:
    if i == 3: 
        i += 1          # ! 
        continue
    print i,
    i += 1


tags_:_@recursion

concept_: recursion, func call self.

core_:'''>
recur is a type loop, need a stop thing.
  condition call
  times loop call
<'''

detail_:'''>

<'''
time_: 20170907195019

----------------------------------------------------------------------------    



tags_: _@recurCall _@callback _@layerPositioin

concept_: recurcall callback

core_:'''>

def main(times,dirA):
  print '\n----called times '+str(times)+'--------------------------------'

  layer=process(times,dirA)

  times+=1
  if times>=layer:return
  main(times,dirA)

if __name__=="__main__":
  dirA='./c1'
  times=1
  main(times,dirA)

<'''

detail_:'''>

def dispLayer(layer,path):
  astr='In Path ' + str(layer) + ' Layer: '+ path
  strLst=[astr]
  print 'Layer '+str(layer)+': '+str([i for i in strLst if times==layer])

def process(times,dirA):
  layer=1
  for path,dirs,files in os.walk(dirA):
    dispLayer(layer,path)
    


    layer+=1
  return layer


<'''
time_:20170908205611

----------------------------------------------------------------------------

# 迭代：for in _@forin_@iteration
# obj: str, list, set,
# ??? 迭代对象是 序列 or 集合？，按什么顺序来迭代？
# 迭, lvci lianzhe, 交替,gangzichuanbo,
# 迭代，更替；迭，更，更递，交替，轮流；高潮迭起,diedangqifu；
# _@iterate  /'it3reit/迭代
# _@traverse /tr3'v3:s/ 穿过，横贯; 遍历；
# 在Python中 迭代器 是与所有 集合类型 相关联的对象。
# 检验集合中的每一个元素，每次一个，
# 任何Python集合都可以用迭代器检验其中每个元素，每次一个。
# item,    task item list.
# element  systme elements
for anElement in object:  
    suite
# example
for theChar in 'hel lo':
    print theChar
# cmd print will + enter, and 'print x,' + space in forin
str1='hello'
for e in str1:
  print i

# another _@forin | iterate
n=0
l=len(lst)
while n<l:
  print lst[n]
  n+=1

# 2.1.5 例子：寻找完全数
# example:
# 寻找完全数。
'''
概念解析：
因数的和是数字本身即完全数，大的是丰沛数，小的是不足数；
因数n，对数N来说，因数是能整除N的数字。28=1+2+4+7+14
实例化：
lst = rang(100)
wqs = []
for e in lst:
    wqs.append(i)
# 寻找因数：
ys = []
for j in range(i):
    if i%j == 0:
        ys.append(j)

# 合成

for e in lst:
    I = range(i)
    ys = 0
    for j in I:
        if I%j == 0:
            ys += j
    if ys == i:
        wqs.append(i)

print  wqs

'''
lst = range(100)
wqs = []

for e in lst:
    elst = range(e)
    sum = 0
    for ee in elst:
        if ee != 0 and e%ee == 0:
            sum += ee
    if sum == e:
        wqs.append(e)

print wqs


# *策略一次只针对一部问题，逐步建立方案；
# *将问题分解为更简单的部分；
# *整合代码时注意细节，如一些特殊情况；
# 1.获取判定数theNum
# 2.求出theNum的所有整数因数
# 3.将每个因数都与sum相加，sum=0；
# 4.比较sumys与theNum
N=int(raw_input('Enter: '))
n=1
while n < N:
    if N%n==0:
        print n,
    n=n+1

##########
theNum=raw_input('Please enter a number to check: ')
theNum=int(theNum)

divisor=1
sumdvs=0
while divisor < theNum:
    if theNum%divisor==0:
        sumdvs=sumdvs+divisor
        print sumdvs
    divisor=divisor+1

if theNum==sumdvs:
    print theNum,'is perfect.'
else:
    print theNum,'is not perfect.'


# 2.1.6 例子：对数字分类
# example:
# 对数字分类
# 76
# 2.1.6 程序的修改扩展
# 程序是对象，要能阅读和理解，并执行一些功能。还可以扩展功能。
# 程序，能被阅读理解，能实现基础功能、核心功能，能扩展功能。
while theNum <= topNum:
    # sum
    # class
    theNum+=1

# 2.2 深入控制语句 condition
# 2.2.1 真与假：布尔值
# 2.2.2 布尔变量，True, False
# 2.2.3 关系运算符,比较；
# 2.2.4 布尔运算符,and,or,not
# 2.2.5 优先级
# 2.2.6 布尔运算符示例，搜索引擎，  用算法指令解决问题；
# w1 w2 or w3 -w4 
'w1' and ('w2' or 'w3') and not 'w4'
a & (b || c) not e 
# 2.2.7 另一种赋值方式
#       1.多重赋值 a,b,c=1,3,2
#       2.交换赋值 a,b = b,a
# 布尔运算符, 优先级最低；and 先于 or
# 字符串永远大于任何数字；

# 有两种不同的相等: 对象相等，引用相等；
# 值相同；a == b;关联的值相同;a=1, b=-,another one;
# 值共享；a is b;之间的关联相同；联系；引用,别名；

# == 检查，两个对象是否，具有相同的值；相同；a == b;
# is 检查，两个名字是否，引用同一对象；共享；a is b;
float1 = 2.5
float2 = 2.5
float3 = float2

f1 ---> 2.5
               ==
f2 ------|
         v     is
f3 ---> 2.5


#  【对于浮点数，检测是否全等测试：】
# 浮点数是实数的近似值；
# 因为有计算机有限位数存储无限大实数的问题；
u=11111113
v=-11111111
w=7.51111111
x=(u+v)+w=9.5111111109999999
y=u+(v+w)=9.5111111104488373
(u+v)+w==u+(v+w)  # False

# 讨论问题要有现象，
# 结论要有现象对象；
x-y < 0.0 000 001

delta=0.0 000 001
if math.fabs(x-y) < delta:

# 优先级_@first：
# 算术 > 比较 > 逻辑； **************************
() > ** > +x-x > */% > +,- >  !=  > not x > and > or

# 布尔表达式在搜索引擎中的应用：
# a b or c -d
'a' and ('b'or'c') and not 'd'

# 多重赋值：
a, b, c = 2, 8, 9
# 交换赋值：
a=2
b=3
temp=a
a=b
b=temp
#
a, b = b, a     # ***

# 2.2.8 用于判定的选择语句
#       1.用于判定的布尔值
#       2.复合语句和语句块
#           按顺序分组的语句，标题+语句块；4个空格的缩进；
#       3.在语句中使用语句块
# 2.2.9 Python判定语句进阶 89 _@if
#       1.if-elif-else并列分支、递进分支、嵌套分支；***********
#           简单的if-elif语句不需要else结束
#           虽然并列分支，但有判定顺序；
if exp:     # 共 1 种可能；
    aa
##########
if exp:     # 共 2 种可能；
    aa
else:
    bb
##########  # 选 2 种可能，在多种可能中；
if exp:
    #
elif exp:
    #
#########

if exp:     # 全选 多种可能；
    aa
elif exp:
    bb
elif exp:
    cc
else:
    dd
############

#       2.更新寻找完全数的例子
if theNum == sumDvs:
    print theNum, 'is perfect'
elif theNum < sumDvs:
    print theNum, 'is abundant'
else:
    print theNum, 'is deficient'
# 2.2.10 循环：_@while语句 91
#       1.基本的循环和while循环
#       2.循环控制和初始化
#           修改循环控制变量，加乘初始值0,1
#           加法恒等式：0+x=x，1*x=x；
#       3.else 和 break
while boolexp:
    # suite1
else:               # True and False also exec, ????
    # suite2

#       4.break语句与提前退出；
#           break用于中途退出循环，降低可读性，两害相权取其轻；
#         **break 找到序列中的某个元素，停止所有重复；
# example:

# Guest number:
'''
1.random 0~100,num,
2.a=input,
3.num <> a; litter,bigger
5.right, out range.exit

'''
import random   
num = random.randint(0,100)
print num
print '\n'
a = raw_input('Please input a number in 0 ~ 100:\n> ')
a = int(a)
while True:
    if a > num and a < 100:
        print 'It is too big, please input agin.'
        a = int(raw_input('>'))
        continue
    elif a < num and a > 0:
        print 'It is too small, please input agin.' 
        a = int(raw_input('>'))
        continue
    elif a == num:
        print 'Right, you are good.'
        break
    else:
        print 'Sorry, you are out of game rule.'
        break



# 猜数字：
# 1.隐式产生0~100的一个随机数；
# 2.提示用户范围；
# 3.用户输入猜测数；
# 4.1猜中退出
# 4.2不中，提示，不中，提示；
# 4.3放弃，提示；
# range范围，_@random随机数
import random
number=random.randint(0,100)
# random.randrange()
print number

print 'Hi-Lo Number Guessing Game: between 0 and 100 inclusive.'
guessString=raw_input('Guess a number: ')
guess=int(guessString)

while 0<=guess<=100: # guess!=number
    if guess > number:
        print 'Guessed too hight.'
    elif guess < number:
        print 'Guessed too low.'
    else:
        print 'You guessed it.The number was', number
        break
    guessString=raw_input('Guess a number: ')
    guess=int(guessString)

else:
    print 'You quit early, the number was: ', number



#       5.while循环内控制语句96
#        (1)continue跳出本次循环, 跳过序列中某个元素，不处理；
#       raw_input 返回值为字符串；isdigit,  
# example:
# 计算整数之和；
# . 用户输入一系列整数，
#       . 如输入非整数，指出错误，忽略输入，继续输入；
#       . 如输入特殊字符，显示最终的和，结束程序；
# . 计算整数和；

print 'Allow the user to enter a series of integers. Sum the integers.'
print "Ignore non-numeric input. End input with a '.'"
theNumStr=raw_input('Number: ')
theSum=0

while theNumStr!= '.':
    if not theNumStr.isdigit():
        print 'Error, only numbers please.'
        theNumStr=raw_input('Number: ')
        continue
    theSum+=int(theNumStr)
    theNumStr=raw_input('Number: ')
print 'The sum is: ', theSum

#        (2)检查用户输入是否出错
# 2.2.11 信号量循环,标记循环
value=someValue
while value != sentinelValue:
    #
while theNum != '.'
# 2.2.12 循环总结
# 2.2.13 _@for语句进阶
#           else, break, continue; else no use.
for target in object:
    # suite1
    if boolexp1:
        break
    if boolexp2:
        continue
else:
    # suite2


tags_:_@range

concept_: range

tree_:'''>

<'''

core_:'''>
#       1.用range产生数字序列 /reind3/范围；random
range(3)        # [0,1,2]
range(1,9,3)    # [1,4,7]  通过加步长 +step 来推进；
# example:
# find sum of 1~100
theSum=0
for number in range(1,101):
    theSum+=number
print "Sum is: ", theSum


<'''

detail_:'''>

<'''
time_: 20180405161345



#       2.while 与 for 进阶 100
# 2.2.14 嵌套
# 2.2.15 冰雹序列示例

# 冰雹序列
'''
公式：
    nmb == int
 * if nmb is double nmb/2; 
 * if nmb is single nmb*3+1;
 * if nmb is 1 exit.
for a list.
'''

a = raw_input("Please input a int number:\n> ")
a = int(a)
lst = []
lst.append(a)
# ??? lst[0]=a

while a != 1:
    if a == 0:
        print lst
        break
    elif a%2 == 0:
        a = a/2
        lst.append(a)
    else:
        a = a*3+1
        lst.append(a)

print lst




# 'num%2==1' 简写'num%2'
num=raw_input('number: ')
num=int(num)
while num!=1:
    if num%2==0:
        num=num/2
    else: 
        num=num*3+1
    print num,
  

# _@pylab _@numpy _@plot _@huitu

# Graph by 3 suit:
# numpy
# scipy
# matplotlib

# 2.3 视觉场景：用pylab对数据绘图
# pylab.plot(x,y,'ro')，
# pylab.show()

# plot /plot/绘制，情节，

# 用X序列，表示X轴；x=[]
# 用Y序列，表示Y轴。y=[]
# 用字符， 表示‘点’，‘KO’

# 2.3.1 使用列表和第一次绘制 102

# example
# 绘制斜线；
import pylab

# use pylab.plot() display a list.用图显示一个序列；
# two lists must same length, both to a point. 对应的俩值，组成一个点。
y=[]
y=range(10)
print y,len(y)
pylab.plot(y)   #(y,y,'ko')/(y,'ko')
pylab.show()


# ***问题举一反三，一个模式，不同参数；一个核心，渐进增长；展开思维；系列

# 2.3.2 更有趣的绘图：正弦波 ko
#       1.绘制元素和他们的颜色
#           color: r,red; b,blue; g,green; k,black;
#           target:o,circl; . dot; x,x; +,+;
#                   ro 红色的圆圈，bx 蓝色的叉号；
#       2.进一步调用绘图
#           pylab.plot(x, y, string) formatString;

# 绘制正弦波
# 0~4π按0.1递增的 正弦波；
import math
import pylab

y=[]
x=[]
# 赋值产生序列，
# 方法产生序列，
num=0
while num < 5:
    print num
    num+=1

# start
num=0.0
xList=[]
yList=[]
while num < 4*math.pi:
    xList.append(num)
    yList.append(math.sin(num))
    num+=0.1                        # 步长为0.1
pylab.plot(xList,yList,'ko')
pylab.show()

# 2.4 计算机科学观点：最小的通用计算，5条基本指令。

#       选择 & 重复 是编程的两个核心；
################################################################################
#       最小指令集： for all programes
#       LOAD  A：RAM.A-addr.Content --> 累加器；
#       STORE A：累加器.Content --> RAM.A-addr;
#       CLR    ：clear 累加器;
#       INC    ：累加器 + 1;
#       BRZ   X：if累加器==0, --> RAM.X-addr; 分支指令；
#       有了选择和重复，就可以编写任何程序。之后的内容是
#       如何使程序更易于阅读和书写。
# 2.5 总结

# 3.0 算法和程序开发 112 

#       ***算法是方式；定性实现的；策略，布局，
#       ***程序是方法；具体实现的；
#       ***算法是条件对象和操作方法. 细化到所有可能性.
#       ***a algo have two parts: object + operate

# 3.1 什么是算法 _@algorithm /3elg3ri73m/算法；   食谱
#       foodlist is a algo;
#       算法，遵循的过程与规则；
#       食谱，对象与操作；还有数量的计算。
#       一个数的平方根，

# 3.2 算法特征，细节，有效，规范，通用；
# 3.2.1 算法和程序realize
#       program is realize. detail.
# 3.2.2 细化，算法需要足够细节，细到所有的可能性；
# 3.2.3 有效性，to stop at good time;
#       bestAngser,nearAngser;
# 3.2.4 指定行为，指定输入和输出；
# 3.2.5 通用算法，好的算法，
# 3.2.6 真的可以实现一切吗

# 3.3 程序是什么
# 3.3.1 可读性
#       1.最简单的事：好名字
#       2.注释
#       3.代码缩进
# 3.3.2 鲁棒性，意料之外的输入与操作；对错误与特例的处理。
# 3.3.3 正确性

# 3.4 程序设计策略，解决问题的意见，《how to solve it》
# 3.4.1 参与并提交，专注；
# 3.4.2 了解然后想象
#       1.问题的实质是什么；
#           ‘无马的马车’新问题？有类似解决过的问题吗？己知解法，模式；
#           每一个输入，预期输出是什么？
#           改变描述，重新，简化描述；
#       2.让问题真实化
#           什么是必须的？
#           纸牌游戏，拿一副牌，尝试；
# 3.4.3 编程之前先思考
#        透彻理解问题。
# 3.4.4 实验，尝试；
#           从简单开始，一部分一部分实验。不要企图一次写出整个程序。
#           化整为零，各个击破，分治策略；
#           尝试，在有想法之前。
#           如果解决不了问题，就先找到问题所在；
# 3.4.5 简化，分解，框架，行走：转向，左腿，右腿；填充子问题
# 3.4.6 停下来思考，反思是否好。
# 3.4.7 放松：让自己休息一下，如果长时间未解，

# 3.5 简单示例122

# 巴比伦平方根算法
'''
问题描述：
1.
    number=input
    guest=input
    tolfloat=input
    if value2 - value1 < tolfloat, exit
2.
    01.guest
    02.shang=number/guest
    03.guest=(shang+guest)/2
    04.if preguest != guest, return 02, or exit.

3. echo a,b,c, value,count

问题描述2：
1.
    number=input
    oguest=input
    tolfloat=input
2.
    01.guest
    02.shang=number/guest
    03.guest=(shang+guest)/2
    04.if (preguest-guest) > tolfloat,loop 02, or exit

3. echo a,b,c, value,count
*** Frame or Core or simple or expect:
core:
preguest = 0
guest=oguest
while abs(preguest-guest) > tolfloat :
    shang = number/guest
    guest = (shang+guest)/2

Simple:
'''
number = int(raw_input('Input a int.\n>'))
oguest = int(raw_input('Guest the int PingFangGen.\n>'))
tol = float(raw_input('Tolerance.\n>'))

preguest=0
guest=oguest
while abs(preguest - guest) > tol :
    preguest=guest
    sng=number/guest
    guest=(sng+guest)/2

print number,guest




# 简化描述；       

root ?

num=raw_input()
guest0=raw_input()
tol=raw_input()
if root2-root1 < tol: over

1.guest0
2.root0=num/guest0
3.(root0+guest0)/2
4.guest1
5.if guest1 != guest0: goto 2.
  else: stop

print num,guest0,tol,root,n

# 形象流程模型，
# 找出结构
guest=raw_input()
while guest1 != guest0:
    root0=num/guest0
    print ()/2
    guest=raw_input()
else:
    print num,,,


# 3.5.1 搭建框架



# 3.5.2 输出
# 3.5.3 输入
#       1.浮点数输入
#       2.测试输入例程
# 3.6 总结

# 三、组织：数据结构和函数PG129

# 4.1.2 非显示字符_@noDispChar，回车符，制表符；\n,\t,'',[],whitespace...;
# 4.1.3 字符串表示形式
# 4.1.4 字符串序列
#       字符在字符串中的位置称为索引；0，1，2，。。。-2，-1；hello[2]
#       索引运算符[]，定位功能；
# 4.1.5 字符串中，某个字符或某段字符的访问；
# 	索引和分片hello[1]==e;hello[2:4]=='ll'; hello[2:-1],hello[2:]
#       通过 索引   来确定字符；
#       通过 索引段 来确定分片,半开段[2:4)；分片，分段，分割；
#       1.扩展分片，步长：间隔的个数；hello[::2]
#       2.复制分片，str2=str1[:]，副本；
# s.split():  _@split
# default remove noDispChar every word both sides,or s.split(','),only one char
s=' a b c '
print '1234567890'
print s.split()       # ['a','b','c']

s=',ab,cde,fg'
print s.split(',',2)  # ['','ab','cde,fg']

# _@blankLine, whitespace, '\n','\t'
# not line.split(), not line[:-1].strip()
# line.strip()[0] != '#'
# _@print '' or var behind with enter or ',' whitespace

# 4.3.4 字符串函数

# 5.0 函数快速入门 PG166 _@function
# 	优势是分治和复用；复合表达式，控制语句；
#       对一个代码段，通过封装、抽象、标准化，形成一个整体对象；
#       很多代码段，简化成，多个对象；
#       函数的优势：
#           分块解决—框架部署，——分工合作，简化问题；
#           相同复用—直接调用，——重用易用通用；
#       函数使编程更容易，相同功能不用重复编码；
#       函数的主要优势是它支持使用分治策略来解决问题；分治复用；
#       部署deploy /di'ploi/
#       
# 5.1 函数是什么
#       函数＝定义+调用
#       参数，形参；
# 5.2 Python函数 _@function
def func(x):
    return x+x
print func('func')


#  两种调用的区别：
def fxun():
    print 'ok'
    return 'ko'

xfun()            #  ok
print xfun()   #  ok ko

# 5.3 函数控制语句
#       函数是另一种控制语句；
# 5.3.1 函数控制语句详解
#       像一个复合表达式, 调用函数=调用其计算结果，return；
# function is new program, so it have new namespace.
a=func(x) 
a='function'

# 5.3.2 另一个函数示例 171
# 实现len的功能。
# 遍历，计数
def length(strr):

    count=1
    for e in strr:
        print count,e # #this sentence?
        count+=1

    return count

print length('hello')
print length('hel lo')

# extend letter count
if e.lower() in string.lowercase:

# 5.3.3 函数示例：猜词 172 _@findWord._@guessWord
# 分治，分步，每步用函数表示；
# example
# 猜词
# 找到按'a', 'e', 'i', 'o', 'u'的顺序，包含5个元音的单词。





# Method1: ****************************

# t simply to big and the to small.

# 1.find words in file, article.
# 2.words includding a,e,i,o,u.
# 3.order: a, e, i, o, u
# file or article -->string
# string strip & replace --> list
# forin list --> word
# quest: if have a,e,i,o,u in order in the word.
# quest: if a in the word

lst=['k','aaekiou','abc','abstemious','klmu']

def haveaeiou(wword0):
    wword=wword0
    for ei in ('a','e','i','o','u'):
      if ii in wword:
        if ii == 'u':
          return wword0
          break
        idx=wword.index(ii)
        wword=wword[idx+1:]
      else:
        return False
        break
            
lst1=[]
for e in lst:
  if haveaeiou(i) <> False:
    lst1.append(haveaeiou(i))
  
print lst1


# Method2: ****************************************************
# 0.0 Quest Analy, think process
# 0.1 root, real, split, trytest, core, frame, 
# 0.2 Analy quest condition
#    1.get a word list----dictionary.txt 
#       get dictionary.txt
#       display ahead lines, analy struct, clean for got operate object.
#    2. more than 5 aeiou, get vowels(str or lst) and continue len<=6
#    3. order a,e,i,o,u; 
#         vowels=[...], more possible. solution.
#           display vowels
#           analy possible
#         find 'aeiou' in vowels;

'''
root:
1.include 5 'aeiou', 
  more than 5 : aaeiouuu
2.order 'a,e,i,o,u',
  xaxexixoxux
  aa
  da
  aadeeikouuuu
  aeiouuu   >>> root
  aaeeiouuu >>> root 

    abstemious
'''
#
# 1.0 Algo steps
# 1.1 get operate object
# 1.2 cleanstr(),word
# 1.3 getVowels(),vowels
# 1.4 contrast judge 'aeiou' in vowels
filedata=open('dictionary.txt','r')

def cleanword(string):
    return string.strip().lower()
def getVowels(word):
    vowels=''
    for char in word:
        if char in 'aeiou':
            vowels+=char
    return vowels

n=0
for line in filedata:
    word=cleanword(line)
    if len(word) <= 6:continue
    print word,
    vowels=getVowels(word)
    print vowels
    if 'aeiou' in vowels: 
        print word
        break
    n+=1
#    if n>9:break
filedata.close()

# aString.strip(',. ') work at head and tail, not middle.
def myStrip(string,lst,s):
    for e in lst:
        string=string.replace(e,s)
    return string
strr=' a a, bb. cc,. '
print myStrip(strr,[',','.',' '], '')


lstWords=['b', 'aeiou', 'aeou', 'aeiouuu', 'eioua', 'abeiou', 'ddaeiou']
lstWords=['b', 'aeiou', 'aeou', 'aeiouuu', 'eioua', 'abeiou', 'ddaeiou','Aeiou']


# 5.3.4 函数调用函数    176
# 5.3.5 什么时候使用函数

#       重构：修改，改进；
#       需要修改改进的代码，重构为函数；

# 5.3.6 如果没有return语句如何
#       过程，None
# 5.3.7 如果有多个return语句会如何
#       first reutrn == break
#       can have many values, return a,b,c
# 5.4 视觉场景：用海龟绘图方法绘制美国国旗 p165
# 5.5 总结


# 6.0 列表和元组 183 _@lst_@list
# 6.1 什么是列表
#       1.创建列表对象
aList=[1, 2, 'a', 3.14159]
# list(cllct)
listStr=list('hello')           # ['h', 'e', 'l', 'l', 'o']
[]==''
#       2.二维列表 _@lstlst
lstlst=[[1,2,3], ['a', 'b', 'c']] == [[row1], [row2], [row3]]
lstlst=[1][-1]   # 'c'        row1 = ['col1', 'col2', 'col3', 'col4']

# 6.2 操作列表 _@lstoperate_@lo _@lstOperate
# 6.2.1 索引和分片, 同字符串；
# 6.2.2 运算符，
#       +, *, []+[], n*[];
#       <>!=
#       in
# ***** num < [] < char
lsta=[1,2,3]
lstb=['a','b','c']
lstc=[1,2,3]+['a','b','c']
lstd=[1,2,3]*3
[1,2,3] > [1,2,2]

# 6.2.3 函数
len([1,['a','b'],3])  # 3
min(lsta)      # 1
max(lstb)      # c
sum(lsta/lstb) # 6 / err

c=[1, [2, 1, 4], 3000000]
print min(c), max(c), len(c)  # 1 [2,1,4] 3

c=[1, 'a', 8, 300000]
print min(c), max(c)          # 1 a

c=[1, ['c', 1, 4], 'b']       # 1 b
print min(c), max(c)

c=[3000000, [2, 1, 4], 'b']   # 300000 b
print min(c), max(c)

# **** num < [] < char ???

c=[1,2,3]
print sum(c)                  # 6
c=[1,[2,4],3]                 # only number for sum(num), not char, not lst
print sum(c)                  # err

# 6.2.4 列表循环 187
# 列表遍历 _@lstIterate
lst=[1,2,3,4,5,6,7]
for e in lst:
    print e

lst=[(3,'b'),(2,'a'),(2,'c')]
for e,f in lst:
    print f,e

# 6.3 列表新内容
# 6.3.1 列表可变性， 
#       ***字符串不可变值，列表不可变性；
myList=[1,2,'a', 'z']
myList[:2]=[27]         # [27, 'a', 'z'],lst assign and lst element assign.
myList[:2]=15           # err. must be collection type.
                        # sublist change must use list
lst=[1,2,3]
print type(lst[1])  # int   var
print type(lst[:1]) # list  sure operate object concept essence/'esns/本质.
lst[1]=8
print lst       # [1,8,3]
lst[:2]=['a']
print lst       # ['a',3]
lst[:1]=8       # err, only same type to set. 
print lst  

# 6.3.2 列表方法 _@lstMethod_@lm_@lstedit_@le     p176
#       Python/dir(list)/help(..)
#       return value,pop have, other no./string all have.
#       1.not change list method: lst.index(x),err, count(x),0;
#       2.    change list method: lstedit:add/del/sort；no return;
#           +: append(x) insert(i,x) extend(c)
#           -: pop()'last x' | pop(i) remove(x)
#           s: .sort(L) func:sorted(C)return副本,return list。
#              sort([['d','a'],['c','b']]) ,firstelement
#               只有同类元素，才有顺序可言；
#               顺序：sort,reverse,min,<,>, to use same type e.
#           S: [].reverse() == [][::-1] 
#           [].sort(reverse=True)

aList=[1,12,5,8]

print aList.index(12)      # 1
print aList[1]             # 12

aList.append([40,50,60])   # [1,12,5,8,[40,50,60]]            +1  element.
aList.extend([40,50,60])   # [1,12,5,8,40,50,60]              +n  elements. 

# 6.4 range、split及其他函数和方法
# 6.4.1 range, (split、join)和多重赋值
#      strr.split() <==> ' '.join(lst)
a,b,c=1,2,3
a,b,c=(1,2,3)
a,b,c=[4,5,6]       # 多重赋值
print a,b,c
result='this is a test'.split()
print result                    # ['this', 'is', 'a', 'test']
new=' '.join(result)            # ' '.join(lst)==strr.split()
print new
rangeList=range(-2,2)
print rangeList                 # [-2,-1,0,1]
a,b,c,d='this is a test'.split()

# 6.4.2 使用join在列表和字符串中转换
#       ' '.join(lst)==strr.split()
# 6.4.3 _@sorted函数
#       sort   method only for list.    change lst, return None.
#       sorted function for collection. return lst   
s=['chr1-10.txt','chr1-1','chr1-2.txt']
sorted(s,key=lambda var:int(var.split('-')[-1].split('.')[0]))
# key=lanbda x:len(x), key=lambda x:(x[1],x[0])

result=sorted([2,1,3])      # [1,2,3]
result=sorted('Hi mom')     # [' ', 'H', 'i', 'm', 'm', 'o'] 打散，排序；

a=[2,1,3]
b=a.sort()  # None 
print a     # [1,2,3]
print b     

# 6.5 示例   193
# 6.5.1 字谜
# Question: if same two words.

# 1.0 Algo 
# 1.1 get two words.
# 1.2 aw,bw;
# 1.3 sort;---sort();sorted()
# 1.4 =?

# use sort()
#simple object
lst=['abc','cba']
lst2=[]
for e in lst:
    sublst=[]               # concept 明晰，不要糊涂。
    for ee in e:
        sublst.append(ee)
    lst2.append(sublst)
for e in lst2:
    e.sort()
# compare/kem'pae/
if lst2[0]==lst2[1]:
    print lst[0],lst[1],'is same'
else:
    print lst[0],lst[1],'is difference'

# use sorted()
# 1.0 Algo steps
#       1.get two words
#         _@raw_input() return a string. int(raw_input())
words=raw_input('Enter two words with space between them:')
worda,wordb=words.split()
#       2.sort
lsta=sorted(worda)
lstb=sorted(wordb)
#       3.contrast judge
if lsta == lstb:
    print worda,wordb,'is zimi'
else:
    print worda,wordb,'is difference'


# 6.5.2 示例：文件分析 196 file analisys
# dataFile: address.data.txt
# problem model: _@fileAnalysis _@wordsAnalisys

# question analisys:
# 1.length of file by words.== n*word
# 2.find words for appear once.
# 3.every word appear number.

# Question Analysis with Function Concept.
# 1.file --- string
# 2.string --- list
# 3.len(list)

# len()
a='abc'
b=[1,2,3,4]
c={'a':1, 'b':2}
print len(a)
print len(b)
print len(c)
# strfile
string=''
filedata=open('address.txt','r')
for line in filedata:
    string+=line
filedata.close()

# strip str
for e in (',','.','-'):
    string=string.replace(e,' ')
string=string.lower()

# lststr len
lst=string.split()
length=len(lst)
print length

# find words appeared once
lst.sort()  # for same words to together
#lst=['a','b','b','b','c'] simple and image
lstonce=['a']
prev='a'
for e in lst:
    if prev!=e:
        lstonce.append(e)
        prev=e
print lstonce
# how to fine the algo. think process is how?
# another once
unique=[]
for e in lst:
    if e not in unique:
        unique.append(e)

#################################33
# function thought

# file analy,1 count words,2 find words appear once.

# 1.0 Algo steps
# 0.0 Quest Analy, think process
# 0.1 root, real, split, trytest, core, frame, 
# 0.2 Analy quest condition, possible contrast judge
#       1.get operate object, display, analy struct.
#       1.get address.txt
#       2.file --- lstwords
#       3. len(words)
#       4. words once
#           1.display and analy struct.
#           2.sort()
#           3.contrast once,more difference
def clean(word):
    cdword=''
    cdword=word.strip(',.- ').lower()
    return cdword

def filetowords(filename):
    words=[]
    filedata=open(filename)
    for strline in filedata:
        lnwords=strline.split()
        for word in lnwords:
            e=clean(word)
            if e=='':continue
            words.append(e)
    filedata.close()
    return words

def once(lst):              # [item for in]
    once=[lst[0]]
    prev=lst[0]
    same=''
    for e in lst:
        if prev!=e:
            once.append(e)
            prev=e
        elif prev==e and same!=e and e!=lst[0]:
            once.pop()
            same=e
    return once

def unique(lst): # appeared
    unique=[]
    for e in lst:
        if e not in unique:
            unique.append(e)
    return unique

words=filetowords('address.txt')
print len(words)
words.sort()
once=once(words)   # 92 
print len(once)
once=unique(words) # 138 'a'
print len(once)

for e in once:
    print e


# *尝试用不同的知识来解决；

# 6.6 可变对象及其引用 200 
#       变量名 引用 对象/值 object==value
#       联系==引用==关联
#       可变对象，不可变对象，varObject,conObject, varValue,conValue
#       python 引用 by 命名空间
#       reference 引用；
#       assign    赋值；
lst2=lst1
lst2=lst1[:]
lst2 is lst1 # False
lst.append(lst) # 自引用，无穷递归

# 6.6.1 深拷贝与浅拷贝？？？
#       在Python中，拷贝是为对象添加新名字。
#       深拷贝，复制对象，_@deepcopy；
#       浅拷贝，复制引用；

# 6.6.2 可变与不可变
#       operate var of conValue, will create new object.
#       operate var of varValue, will create new object or not.
#       不可变对象：int,string,tuple,key

# 6.7 元组_@tuple/tju:pl/ _@tpl
#       逗号创建元组
# 6.7.1 从列表到元组sorted() not sort()change object
lst=[1,2]
tpl=tuple(lst)    # (1,2)
sorted(aTuple)    # [1,2]

# 6.7.2 为什么需要元组
#       提供一种有 完整性和持久性 的数据结构。

# 6.8 列表：数据结构, 结构与操作
#       数据结构，数据类型＝object+operate(method)
#                 数据的组织和操作；     *
#       效率＝算法+时间+空间
# 6.8.1 数据结构示例
#           一种结构，高效操作，低效操作；*****************************
# 6.8.2 数据结构的另一个示例
#       队列、字典、集合、数字矩阵
#       定义自己的数据结构，以解决特定问题；*****************


# 6.9 算法示例：美国环境保护署 通车里程 数据 209  _@mile_@tongchelicheng
#       csv以文本形式存储表格数据的文件格式。"字段，字段，字段\n";
#       HWY:high way; MPG:miles per gallon每加仑行驶的英里数；
#       原始数据下载
#       http://www.fueleconomy.gov/feg/download.shtml
#       csv,lstStr to disp xcolumn;prevElem
# 1. operate object analydisplay
filedata=open('epaData2010.csv')
n=0
for line in filedata:
    print n,len(line)
    print '---%s---' % (line)
    lstline=line.split(',')
    print len(lstline)
    m=0
    for column in lstline:
        print m,column
        m+=1
    n+=1
    if n >= 1 : break
# 2. question analy 
#           1.maxMpg,minMpg             MPG column
#           2.car-maxMpg,car-minMpg     CAR column
#           3,disp question operate object

filedata=open('epaData2010.csv')
n=0
for line in filedata:
    print n,
    lstline=line.split(',')
    print '%-20s : %s' % (lstline[2],lstline[9])
    n+=1
    if n > 30 : break


epafile=open('epaData2010.csv','rU') # rU, 通用换行；
mpglst=[]
carmax=[]
carmin=[]
n=0
for line in epafile:
    if line[:5]=='CLASS' or ('VAN' in line) or ('PICKUP' in line):
        continue 
    e=int(line.split(',')[9])
    mpglst.append(e)
    if e==45:
        carmax.append(line.split(',')[2])
    if e==12:
        carmin.append(line.split(',')[2])
    n+=1
#    if n==10:break
epafile.close()
print n,len(mpglst)
print max(mpglst),min(mpglst)
print carmax
print carmin

# _@listComprehension _@lstCompr _@lstJiexi _@lstShencheng _@lstExpresion
# 6.10 列表解析， 用于列表转换；
#       [item for in]
#       列表内，放了一个表达式，遍历语句的变形；
#       执行速度较快；
#       return lst 的 forin, 都可用[item for in]
#       vowel /'vauel/元音
#     [expression for-clause condition]
print [i for i in range(20) if i%2==0]  # range(20) 为operate object 

word='solidarity'
vowels='aeiou'
print [v for v in word if v in vowels]  # word 为操作对象

print [(x,y) for x in range(3) for y in range(4) if x>y and x%2==0]

string='John Doe, 874 Main st.,'
print [int(c) for c in string if c.isdigit()]

# _@numpy _@pylab _@arange _@array _@floatList _@numpy.arange()

# 6.11 视觉场景：更多绘制任务 P205
# 6.11.1 numpy阵列  浮点列表，实数列表；numpy.arange(0, 1, 0.1)
#        numpy.array floatList < lst, arange == array range.
#       1.阵列(array)和arange     array/e'rei/  range/arrange
#           阵列是种序列，可索引和分片，可赋值改变，
#           与列表区别，only same data type, default float.
#           阵列，处理浮点数的列表？可用算术运算符；
import numpy
print numpy.array([1.,2.1,3.])
arr=numpy.arange(0,1,0.2)               # return array
# array([0., 0.2, 0.4, 0.6, 0.8])
myarr=array([1,2,3])
numpy.append(myarr, 50.0)   # array([1., 2., 3., 50.])

#       2.广播    broadcast: math operate of array.
#           阵列优势，在两个阵列之间，可以用标准的算术运算符来操作；
#           重载override覆盖，让同名方法因不同datatype,return diff data.
import numpy
arr=numpy.arange(0, 1, 0.2)  # array([0., 0.2, 0.4, 0.6, 0.8])
narr=arr*2                   # array([0., 0.4, 0.8, 1.2, 1.6])
narr=numpy.sin(arr)
print narr

# 6.11.2 绘制三角函数

import numpy
import pylab

x=numpy.arange(0, 4*numpy.pi, 0.1)
y1=numpy.sin(x)
y2=numpy.cos(x)

pylab.title('Sine and Cosine Plot')
pylab.plot(x,y1,'b')
pylab.plot(x,y2,'r')
pylab.show()




# 7.0 深入了解函数229  _@function
# noname function _@nonamefunc _@lambda
a=lambda x,y:x*y
a(2,3)
# 7.1 函数调用函数
# 7.2 作用域 _@scope/skop/
#       包含某个变量的程序语句集合；set of statements which the var in them.

# 实参_@arg 形参_@param  _@parameter/pe'ramite/
# 7.2.1 实参、形参和命名空间 
#       传参是种复制，here is 复制了what? 值？对象？is 关联，引用关系；
#       即传参是 实参arg、形参param共同引用同一对象；
#       func(*lst,**dct) args
arg=25
def myfunc(param):
    print arg,param   # 25,25
    param=32

print arg,param       # 25,32

# _@varValue,  _@varObject
# 7.2.2 传递可变对象 list,set,dict, have ability of learn.
#       chuancan,ji yingpin ruzhi.
#       作用，调用函数来改变 主程序中的变量；
# arg -> lst -> param: arg == param, to change value of main.
# arg -> int -> param: arg != param
# 不可变对象：int,string,tuple,key
arg=[1,2,3]
def myfunc(param):
    print arg,param   # [1,2,3],[1,2,3]
    param[0]=32

print arg,param       # [32,2,3],[32,2,3]

# _@returns
# return lst,tpl,lstCompr,funcExpr
# 7.2.3 返回复杂对象
def evens(n):                # even/'iven/oushu; event/i'vent/shijian.
    evensLst=[]
    for item in range(1,n+1):
        evensLst.append(2*item)
    return evensLst
#   return pair[1],pair[0]   #(3,2), pair:double

# 7.2.4 重构evens
return [2*i for i in range(1,n+1)]

# 7.3 默认值以及形参为关键字
def func(a,b=3):   # 顺序传参，默认在后；
func(b=3, a=8)     # 有关键字，可不按顺序；
func(a=9)          # 有关键字，可不按顺序；

# _@paramDefault
# 7.3.1 示例：默认值和参数关键字
# 7.3.2 默认值问题
#       不要使用可变的默认值，用不可变对象；
def vardefault(e, lstparam=[]):
    lstparam.append(e)
    return lstparam
vardefault(1)             # [1]
vardefault(2)             # [1,2]     仍带着上次调用的值。
vardefault(4,[7,8,9])     # [7,8,9,4]
vardefault(5)             # [1,2,5]   仍带着上次调用的值。

# 7.4 函数和对象
#       文档字符串
# in shell
import math
dir(math)
math.ceil.__doc__   # return 'help string'

# _@weightAverage _@jiaquanAverage _@finalGrade _@quanzhong
# 7.5 示例：确定最终成绩 
# question moxing: table csv
# app scene concept: weightAverage
# example:
# in bus, number of age15 people is 4, 20 6, 30 10, for average age.
# quan:4,6,10, numbers of the same element,
# weight:4/(4+6+10),6/(),10/(), xishu,bili,quanzhong
# weightedAverage:sum/(4+6+10),weightedAge, jiaquan average
# average:(15+20+30)/(4+6+10)
# 15*4+20*6+30*10,sum,weighting
# 15*4/(4+6+10),20*6/(),

# exam1,exam2,finalExam = 60,80,100
# weight1,weight2,weight9 = 0.3, 0,3, 0,4
# weightedAverage = 60*0.3 + 80*0.3 + 100*0.4
#         average = (60 + 80 + 100)/3

# lastGrade==weightedGrade==weightedAverageGrade

# 7.5.1 数据
# 7.5.2 设计
# 7.5.3 函数：weightedGrade
# 7.5.4 函数：grade
# 7.5.5 函数：main
# 7.5.5 使用示例
# 7.6 "传值" or "传引用"
#       都不是，Python传递的是对象引用，看对象而定。

# _@dict _@dct
# 8.0 字典236和集合248 
# 字典，映射，关联数组，担不是序列，键值对。
# key是不可改变的对象, 可以是整数，字符串，元组；
contacts={'aaa':'1238008', 'bbb':'7898008', 'ccc':'4568008'}
print contacts['bbb']

{} == dict()
dct={} 
# dct[key]==value
dct['a']=1
dct['b']=2
dct['c']=3
print dct   # {'a':1, 'b':2, 'c':3}
dct['c']=dct['c']+1
# key is not var.
dct={2:[], (2,4):27, 'x':{1:2.5,'a':3}}
2 in dct  # True
27 in dct # False.  'in' only looks at key.

# 8.1.4 运算符 _@dctMethod
#       1.集合操作，操作的是key, key like index of list.
#       2.字典方法 
#           items(): [()]
#           keys():  []       default iterater
#           values():[]
#           copy():  {} 浅拷贝，值为列表时，改变副本，也改变原值。
#           pop(k):     del a key:val; dct.pop(k)

dct={'a':1, 'b':2}              # iterate key
for key in dct:
    print key,':',dct[key]

dct={'a':3, 'b':2, 'c':9}
print dct.items                 # [('a',3), ('b',2), ('c',9)]
for key,val in dct.items():     # iterate items字典元素
    print key, val

for val in dct.values():        # iterate values 
  print...

lst=[('a',1),('b',2)]           # lst -- dct
for e,f in lst:
    print e,f

# enumerate/i'numereit/ lst, iterate every element and its index(xiabiao)
seq=['a','b','c']
for i,e in enumerate(seq):
  print i,e

# _@cipin _@dancipinlv
# 8.2 单词计数示例 241
# 8.2.1 统计字符串中的单词数
# 8.2.2 《葛底斯堡演说》中的单词出现频率
#       1.函数：addword
#       2.函数：processline
#       3.函数：prettyPrint
#       4.函数：main

# 1.0 Algo steps
# 0.0 Quest Analy, think process
# 0.1 root, real, split, trytest, core, frame, 
# 0.2 Analy quest condition, possible contrast judge
#       1.get operate object, display, analy struct.

def clean(word):
    cdword=''
    cdword=word.strip(',.- ').lower()
    return cdword

def filetowords(filename):
    words=[]
    filedata=open(filename)
    for strline in filedata:
        lnwords=strline.split()
        for word in lnwords:
            e=clean(word)
            if e=='':continue
            words.append(e)
    filedata.close()
    return words

def once(lst):              # [item for in]
    once=[lst[0]]
    prev=lst[0]
    same=''
    for e in lst:
        if prev!=e:
            once.append(e)
            prev=e
        elif prev==e and same!=e and e!=lst[0]:
            once.pop()
            same=e
    return once

def unique(lst): # appeared
    unique=[]
    for e in lst:
        if e not in unique:
            unique.append(e)
    return unique

def dctwordcount(lst):
    dct={}
    for e in lst:
        if e in dct:
            dct[e]+=1
        else:
            dct[e]=1
    return dct

# dict turn to tupleList
def dcttolst(dct):
    lst=[]
    for key,val in dct.items():
        lst.append((val,key))
    return lst

def dctdisp(dct,order=-1):
    lst=dcttolst(dct)
    lst.sort()
    lst=lst[::order]
    print 'Length of the file: %d' % (len(lst))
    print '\n%15s : %s' % ('Word','Count')
    print '-'*30
    for e,f in lst:
        print '%15s : %s' % (str(f),e)

words=filetowords('address.txt')
print len(words)
words.sort()
dct=dctwordcount(words)
dctdisp(dct)


# _@periodicTable
# 8.3 示例：周期表
# 8.3.1 使用CSV文件
# 8.3.2 算法概述
# 8.3.3 实现分治的函数
#       1.函数：readTable
#       2.函数：parseElement

--------------------------------------------------------------
tags_: __@Set __@set __@set  __@jihe

concept_:set

core_:'''>

set([1,2])
set(123)                    # err; int is not iterable
cset=set([1,2,2,1,2])       # set([1,2])

aset=set('abc')             # set(['a','c','b']) 元素不重复；
aset=set('abbc')            # set(['a','c','b']) 元素不重复；

bset=set(['a', 1, 2.5, (3,6)])

nullSet=set()               # set([])  empty set.
print nullSet

set(c) c must be iterable可迭代
元素不重复
Python集合是可变的

<'''

detail_:'''>
# 8.4 集合 262 set
# 8.4.2 集合的组成
# 8.4.3 python集合

<'''
time_:20170822221014

-------------------------------------------------------------



tags_: __@setMethod

concept_: set method

core_:'''>

# len(), in, for;

myset=set('abc123')
for e in myset:
    print e
print myset

aSet.intersection(bSet) 
aSet.union(bSet)
aSet.difference(bSet)
aSet.symmetric_difference(bSet)

smallSet.issubset(bigSet)           # True
bigSet.issuperset(smallSet)         # True
#       6.其他集合方法
# add(), clear()all, remove()return err,discard()no, copy()simple.
a=set('abc')
a.add('d')
print a

<'''


detail_:'''>
# 8.4.4 python集合的方法、运算和函数

# 8.4.5 集合方法
aSet=(['a', 'b', 'c', 'd'])
bSet=(['c', 'd', 'e', 'f'])
#       1.交集
aSet.intersection(bSet)     # set(['c','d'])
bSet.intersection(aSet)     # same
#       2.并集
aSet.union(bSet)            # set(['a','b','c','d','e','f'])
bSet.union(aSet)            # set(['a','b','c','d','e','f'])
#       3.差集
aSet.difference(bSet)       # set('a','b')
bSet.difference(aSet)       # set('e','f')
#       4.对称差 symmetric/si'metric/
aSet.symmetric_difference(bSet)     # set(['a','b','e','f'])
bSet.symmetric_difference(aSet)     # set(['a','b','e','f'])
#       5.子集和超集
smallSet=set(['a','b'])
bigSet=set(['a','b','c'])
smallSet.issubset(bigSet)           # True
bigSet.issuperset(smallSet)         # True
#       6.其他集合方法
# add(), clear()all, remove()return err,discard()no, copy()simple.
a=set('abc')
a.add('d')
print a


<'''
time_: 20170823224635
----------------------------------------------------------------------------



# _@setApp
# 8.5 集合应用
# 8.5.1 不同文件中单词之间的关系
#       1.函数：addWord
#       2.函数：processLine
#       3.函数：main
#       4.函数：prettyPrint
# 8.5.2 输出和注释

# _@nameSpace _@scope
# 8.6 作用域：完整的故事 
# 8.6.1 命名空间namespace和作用域scope.
#       nameSpace: set of relation of name and value.

#       nameSpace: dict, name:object.
#       scope:     statements including the var.

#       name: var,func,lst,dct,tpl,set

# 8.6.2 作用域搜寻规则
#       在不同命名空间中，按 规定顺序 搜索；
#       LEGB,legb, legbm ***查找命名空间的顺序；

#   Local     局部的names inside func1                   locals().items()
#   Enclosing 封闭的func2 inside func1 /in'klozing/
#   Global    全局的 all new object in it.      __main__ globals()   
#   Built-in  内置的                        __builtins__.__dict__ 
#   module    外载的                                math.__dict__    

# Python interpreter, boot with modules of __main__ and __builtins__.

print type(globals())
print type(__dict__)

import math
for e,f in math.__dict__.items():
    print '%-20s %s' % (e,f)

# app:
if __name__=="__main__":      # diff:run directly or called as module.
  main()
# __name__ is names set of modules.
# __main__ is name of main module.
################
# _@locals _@globals
# locals()
# globals()

import math
globalx=27
print 'math.pi: ',math.pi

def myfunc(param1=123,param2='abc'):
    localx=521.11
    print '\n===this is myfunc() print==='
    print 'localx: ',localx
    print 'globalx: ',globalx
    print '\n***local namespace***'
    for key,val in locals().items():
        print '%-15s : %s' % (key,str(val))

myfunc()

print '\n---global namespace---'
for key,val in globals().items():
    print '%-15s: %s' % (key,str(val))

# local  var: localx, param1, parm2;
# global var: math, globalx, myfunc,
# notice var: pi, key, val,
# locals() total name on space of it in. if outside of myfunc(),\
# locals() as same as globals().
# globals() and locals() can not total name on code of it in.key,val.

# _@localNameSpace _@globalNameSpace _@nameSpaceSkip
# 8.6.3 局部命名空间 local, inside of func.
# 8.6.4 全局命名空间
#       1.局部赋值规则 
#       外部变量，在函数内部，可以显示和运算，\
#               一赋值就变成内部变量，并先被Python找到, namespaceskip:global
out=88
def myfunc1():
    print out       # 88
    local=22+out
    print local     # 110

out=88
def myfunc2():
    print out       # err, local var 'out' referenced before assignment
    out=33
    out=out+1

#       2.global语句
out=88
def myfunc2():
    global out
    print out     # 88       
    out=33
    print out     # 33

myfunc2()
print out         # 33

# 8.6.5 内置模块 _@builtins
builtinDct=__builtins__.__dict__
print 'Builtin dictionary has %d entries.\n' % (len(builtinDct))
n=0
for key,val in builtinDct.items():
    print '%-20s : %s' % (key,str(val))
    n+=1
    if n>22:break

# 8.6.6 封闭式变量 _@enclosing 函数创建函数时
def func1():
  var1='abc'
  def func2():
    var2='def'   # enclosing var

# 8.7 Python指针：使用zip创建字典 _@zip
#     zip(),dict(),together, easy to get a dict from two lists or dicts.
zip(lst1, lst2) # [(),()]  lsts to fields of tableLst.

lst1=[1,2,3]
lst2=['a','b','c']
print zip(lst1,lst2)  # [(1,'a'),(2,'b'),(3,'c')]

# ###
lst1=['a', 'b', 'c']
lst2=[1,2,3]
d=dict(zip(lst1, lst2))   #dict()??
d2=dict(zip(d.values(), d.keys()))

# _@tick _@bar _@pylab
# 8.8 视觉场景：词频条形图 matplotlib
# 0.1 root, real, split, trytest, core, frame, 

# 8.8.1 正确获取数据
# 8.8.2 标签和xticks命令 tick/tik/kedu,zuobiao; label
xVals=numpy.arange(len(keyLst))
pylab.xticks(arange(12),calendar.month_name[1:13],rotation=18)
pylab.xticks(xVals+barWidth/2.0,keyLst,rotation=18)         # ticks+label;
pylab.bar(left,height,width,color='r')                      # bar
pylab.bar(numpy.arange(len(keyLst)),valLst,width,color='r') # bar
pylab.show()


# 8.8.3 绘图



# 9.0 文件284 _@fileReadWrite_@frw
# 9.1 什么是文件
#       文本文件，二进制文件；

# file is a collection type, and lines in it.'\n'
# file= n * line
# access file mode:
#   fileData=open('file.txt')   ('file.txt','a+') filedata is set can be iterate
#   fileData.readline()   'aaa\n'
#   fileData.read()       'aaa\nbbb\nccc' == filedata
#   fileData.write(line), afte open, flow write, but reopen, rewrite.

# 9.2 存取文件：读取文本文件
#       shell.program<===连接管道fileObject===>disk.file
#       opencmd create link,pipe  return fileObject
#       文件对象，连接，管道，文件流，文件描述符；
#       flow: program<===[throughCache]===>disk
#       fileobject cache area.Listcache.
#       open() copy to Listcache, close() Listcache write to disk.

# 通过 文件对象 遍历文件的每一行；  
fileObject=open('dict.txt','r')
for line in fileObject:
    print line
fileObject.close()

# read(), all at once, return a char once;
wholeFile=fileObject.read():
# readline(), before forin, use to del title line.

    aLine=fileObject.readline()  #'first line\n'

    for line in fileObject:
        print line               # second line
                                 # third  line
# 9.2.1 其他文件存取方法
# 9.2.2 数据流
# 9.3 存取文件：写文本文件
#       加入'\n'，文本间交互时，其它类型to string;
# 9.4 在程序中存取文本文件
#     rU is know '\n' or '\r' in diffrent os.
rdFile=open('datafile.txt', 'rU')   # file of readed. 
wrtFile=open('spacefile.txt', 'w')  # file of writed

oneline=readfile.readline()

for line in rdFile:
    wrtFile.write(line)

rdFile.close()
wrtFile.close()



tags_: _@fileExists _@exists @except

concept_: fileExists

core_:'''>

while True:
  try:
    searchdir=raw_input("Search Dir: ")
    for path,dirs,files in os.walk(searchdir):
      pass
      break
  except IOError:
    print ""
------------------------------------------
def file_exists(filename):
  try:
    with open(filename) as f:
      return True
  except IOError:
    return False


<'''

detail_:'''>

<'''
time_: 20170914215122

----------------------------------------------------------------------------



# 9.5 创建文件和重写文件 _@rwa
#           'r,w,a'only,'r+w+a+' read and write;
#           'w':fugaixie; 'a':zhuijiaxia
# edit: r+, whitespace.

#   'rU',  第二次写会出错

# _@newLine
# 9.5.1 通用新行格式
# unix & mac  '\n'
# mac         '\t'
# windows     '\n','\t'

# _@filemove _@fm _@seek
# 9.5.2 文件内移动 指针，位置；
#       beginningfile, beginningline,zero,cursor . fo.seek(0)
#       fo.tell(),[beginningfile, cursor] 
#       tell(), return n*char between begin and current, incude '\n'
#       fo.seek(-24,2), 0,1,2. 0,beginning; 1,current, 2,end;
#       seek('byte', 'begin') seek(8,0),seek(8); seek(-30,2)
#       fo.readline() [zero,\n]
#       disk---cache---datalist
#       read(),seek(),think '\n' 1 byte, tell() 2 byte.
#       enter to new line, or one blank to new line.
# _@seek _@tell _@fileMove
'''
# aaa.txt
10123456789
20123456789
30123456789
'''
# beginning of file, zero, pointer/cursor
# fo.readline()  [zero,\n] [beginning of line,\n]
# fo.tell()      [beginning of file, cursor]
f1=open('aaa.txt')        
print f1.readline()       # 10123456789. 
print f1.tell()           # 12. 11 +'\n' = 12.tell. 
print f1.readline()       # 20123456789. [beginningline,\n]
print f1.tell()           # 24. [beginningfile,cursor]
f1.seek(4)                # reset zero
print f1.tell()           # 4. 个字符, if more disp xL长整型；
print f1.readline()       # 3456789. line [zero,\n], 
print f1.tell()           # 12. [beginningfile,cursor] 

f1.seek(4,1)              # from curent posit move.
print f1.tell()           #  个字符
print f1.readline()       # 

f1.seek(-4,1)             # move reback from curent position
print f1.tell()           #  个字符
print f1.readline()       # 

f1.seek(0)
print f1.tell()           # 0
print f1.readline()       # 12 这两个字符，第一行的字符；

f1.seek(1,2)              # move to end. 1 char new file.
print f1.tell()           # total bytes
f1.seek(-1,2)             # f1.readline()=='\n'. err new file.

for line in f1:
    pass                  # to end, 'pass' read but do nothing. 
print f1.tell()           # 36 个字符.

f1.seek(0)                # back to head
whole=f1.read()
print len(whole)          # 16

lastLine=''               # firstline: use readline()
for line in f1:              # lastline: use last iterateAssign
  lastLine=line
print lastLine

f1.close()

# _@lastLine
# question: read last line in file.
# reverse iterate assign
# reverse one by one byte iterate until find second '\n' assign
import os
fdata=open('bb.txt')
n=3
fdata.seek(-2,2)
lastline=fdata.read()
begin=lastline[0]
fdata.seek(0)
while begin != '\n':
  fdata.seek(-n,2)
  lastline=fdata.read()
  begin=lastline[0]
  fdata.seek(0)
  n+=1
fdata.close()
print lastline



tags_: _@exists _@isfile _@isdir

concept_: exists isfile isdir

core_:'''>

os.path.exists('/home/xxx/mp3')
os.path.isfile('/home/xxx/a.txt')
os.makedirs('/home/xxx/video')

<'''

detail_:'''>

<'''
time_: 20170824173512

----------------------------------------------------------------------------




# 9.6 关闭文件
#      close(),是取消连接，cache to disk.
#      forget to close, when it's writting, maybe can loss info

# 9.7 CSV文件 _@csvfile_@cf
#       CSV not a file type, it is a 格式；it's a text file yet.
#       CSV use to save table data.存储表格数据；

# 9.7.1 CSV模块
#       Python的优势 在于有提供应用的社区；csv.reader, csv.writer
# 9.7.2 CSV Reader
#       csv.reader(fObj)return not string is a lstLine. e is field.
import csv
fObj=open('workbook.csv','rU')  # 加U，再写的话，err in windows.

csvReader=csv.reader(fObj)

for row in csvReader:
    print row

fObj.close()

# 9.7.3 CSV Writer_@csvWrite_@cw
#       window 下创建文件，在VIM里，回车符为^w   ????????????
#       csv.writer(fObj).writerow(row)
import csv

rdfile=open('file.csv','rU')
csvReader=csv.reader(rdfile)

wrtfile=open('new.csv','w')
csvWriter=csv.writer(wrtfile)

for row in csvReader:
 csvWriter.writerow(row)
# wrtfile.write(line)

rdfile.close()
wrtfile.close()

# 9.7.4 示例：更新某些成绩 292     _@chengji_@exam
#       exam /ig'zam/ 考试，测验
#       grade 年级、等级、阶段
#       average/'averizh/平均

# 格式赋值：
a=3
b='%.2f'%a
print b

# 二维表格 列表，某行某列的遍历_@sheet_@biaoge

# sheet[row][col]； lstlst[row][col]

# disp sheet rows and cols
n=0
for e in sheet:    
    print n,len(e)    #sheet(7,5)
    n+=1

# first line:
sheet[0], sheet[0][:]
# first field of second line.
sheet[1][0]
# all line except first and last line.
sheet[1:-1]
# all fieldes except first and last field in third line.
sheet[3][1:-1]
# 在表格特定行中，遍历某分片分段的字段：
for strField in sheet[rown][x:y]:

# 遍历表格,显示每行的 某些列：
for row in sheet:
  if row==[]:  
    continue
  print row[cola],row[colb]


# example
# sheet[3][1:-1] 分片半开范围
def filedisp(name):
    fObj=open(name,'r')
    for row in fObj:
        print '--L--%s--R--' % (row)
    fObj.close()
    
import csv
readFileObj=open('workbook.csv','r')    # 创建文件读对象；
csvReader=csv.reader(readFileObj)       # 文件读对象，转化为，CSV读对象

sheet=[]                                # 表格列表，二维列表
for row in csvReader:                   # 通过CSV对象，遍历文件每一行；
    sheet.append(row)                   # 压入这行列表，非相加；
readFileObj.close()

def sheetdisp():            
    for field in sheet[0][:]:           # 显示第0行，字段行；   
        print ('%-10s'%field),
    print '\n'
    for row in sheet[1:-2]:             # 显示表格每一行，除首末行； 
        print ('%-6s'%row[0]),          # 显示这行的 第0列；
        for col in row[1:]:             # 显示这行的每一列，除0列；
            print ('%10s'%col),
        print '\n'
    for field in sheet[6][:]:           # 显示第6行末行的每一列；
        print ('%-10s'%field),
    print '\n'

sheet[3][3]='%0.2f'%100                 # 格式赋值

sum=0
for col in sheet[3][1:-1]:              # 累计第3行，除首末列；
    sum+=float(col)
sheet[3][4]='%0.2f'%(sum/3)

sum=0
for row in sheet[1:-2]:                 # 累计表格每行的第四列，除首末次末
    sum+=float(row[4])

sheet[-1][-1]='%0.2f'%(sum/4)           # 对表格最后一格，格式赋值；

writeFileObj=open('wWorkbook.csv','w')
csvWriter=csv.writer(writeFileObj)      # CSV写对象     
for row in sheet:
    csvWriter.writerow(row)             # CSV写对象的写行方法；
#   writefObj.write(row)          # 对比文件对象的写方法；
writeFileObj.close()

filedisp('wWorkbook.csv')


# 9.8 示例：反复提示，要求输入正确的文件名 294
# try except 出错误，也能继续；
# 获取正确文件名，避免错误，写入同名变换的文件；

opened=False
while (not opened):
    readName=raw_input('Open what file: ')
    try:
        reader=open(readName,'r')
        opened=True
    except IOError:
        print 'File opening failed, try again.'

lstReadName=readName.split('.')
writeName=lstReadName[0]+'Revs.'+lstReadName[1]

writer=open(writeName,'w')
for line in reader:
    lstWords=line.split()
    lstWords.reverse()
    for e in lstWords:
        writer.write(e)
        writer.write(' ')
    writer.write('\n')
writer.close()
reader.close()

reader=open(writeName,'r')
for line in reader:
    print line
reader.close()

# 9.9 模块：OS  _@os _@dir _@walk
#       math, OS,    dir path file      os.listdir(), os.walk() os.path.split()
# 9.9.1 目录/文件夹的结构
#       目录树 结构 dirtree
#       路径，      strPath

#       目录，完成三件事情：
#           fileList
#           dirList
#           upperdir

#       '/'根目录， '.'当前目录, '..'上级目录
#       window,linux 的目录分隔符，统一用'/', 'e:/python/aaa'

# 9.9.2 OS模块函数, 目录操作 os.listdir(), 'e:/python'
#       os.getcwd(),'current work dir', is dir of program start to run.
#       os.chdir(),'change directory',
#       os.listdir(),return lst of dirs and files, 可以显示window下的任何目录；
#       os.walk(dir) /wo:k/ 
#           only iterate, not direct to run.
#           digui iterate disp dirname,dirs,files of every a ceng.
#           return: current dirname,subdirs,files;
#           current dirname start at dir.
        for pathDir,layerDirs,files in os.walk(searchDir): #rootDir,treeDirs
          for afile in files:
            afile=os.path.join(pathDir,afile)
            print afile
#       path=dirname + basename ; '/home/myhome/python','test.py';
#       os.path.split(path), (dirname,basename) 
#       os.path.join(dirname,basename), path;
#       os.path.split(dirname)  "/home/myhome/python" ("/home/myhome","python")
#       os.path.splitext(path),  (string,ext) '.py','.txt', get extension name.

#       os.isfile(), os.isdir(), os.exists(), 

#       os.rename(oldpath,newpath)
#       os.stat().st_ctime

#       skill: search module,submodule,function.

import os
#os.chdir('c:/')
print os.getcwd()
lstdir=os.listdir(os.getcwd())
lstdir=os.listdir('.')
lstdir=os.listdir('..')
lstdir=os.listdir('/')  # 'c:/', 'e:/python'
for file in lstdir:
  print file

for file in os.listdir('.'):
  print file

path='c:/python27/py/test.py'
print os.path.isdir('c:/python27/py/')          # True
print os.path.isfile('c:/python27/py/test.py')  # True
print os.path.exists('c:/')                     # True
print os.path.basename('c:/python27/py/test.py')# 'test.py'
print os.path.dirname(path)                     # 'c:/python27/py'
print os.path.split(path)                       # (dirname, basename)
print os.path.splitext(path) # ('c:/python27/py/test', '.py')
print os.path.join('c:/python27/py', 'test.py') # value of varpath
print '========================='

n=0
for dirname,subdirs,files in os.walk('.'):
    print n,': ',dirname,subdirs,files
    print '-'*76
    n+=1
    if n > 9:break
# strCurrentDirName, lstCurrentSubDir, lstCurrentDirFiles
# 下一层的，相对dirname, subdir, files;
# .aaa\bbb, ['ccc1', 'ccc2'], ['ccc1.txt', 'ccc2.txt']
-----------------------------------------------------------------
_@fileOperate _@dirOperate
python文件和目录操作方法大全（含实例）

转载自：http://www.jb51.net/article/48001.htm

一、python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法。
1.得到当前工作目录，即当前Python脚本工作的目录路径: os.getcwd()
2.返回指定目录下的所有文件和目录名:os.listdir()
3.函数用来删除一个文件:os.remove()
4.删除多个目录：os.removedirs（r“c：\python”）
5.检验给出的路径是否是一个文件：os.path.isfile()
6.检验给出的路径是否是一个目录：os.path.isdir()
7.判断是否是绝对路径：os.path.isabs()
8.检验给出的路径是否真地存:os.path.exists()
9.返回一个路径的目录名和文件名:os.path.split() eg os.path.split('/home/swaroop/byte/code/poem.txt') 结果：('/home/swaroop/byte/code', 'poem.txt')
10.分离扩展名：os.path.splitext()
11.获取路径名：os.path.dirname()
12.获取文件名：os.path.basename()
13.运行shell命令: os.system()
14.读取和设置环境变量:os.getenv() 与os.putenv()
15.给出当前平台使用的行终止符:os.linesep Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
16.指示你正在使用的平台：os.name 对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
17.重命名：os.rename（old， new）
18.创建多级目录：os.makedirs（r“c：\python\test”）
19.创建单个目录：os.mkdir（“test”）
20.获取文件属性：os.stat（file）
21.修改文件权限与时间戳：os.chmod（file）
22.终止当前进程：os.exit（）
23.获取文件大小：os.path.getsize（filename）
二、文件操作方法大全：
1.os.mknod("test.txt") #创建空文件
2.fp = open("test.txt",w) #直接打开一个文件，如果文件不存在则创建文件
3.关于open 模式：
复制代码 代码如下:
w：以写方式打开，
a：以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+：以读写模式打开
w+：以读写模式打开 (参见 w )
a+：以读写模式打开 (参见 a )
rb：以二进制读模式打开
wb：以二进制写模式打开 (参见 w )
ab：以二进制追加模式打开 (参见 a )
rb+：以二进制读写模式打开 (参见 r+ )
wb+：以二进制读写模式打开 (参见 w+ )
ab+：以二进制读写模式打开 (参见 a+ )

 

fp.read([size]) #size为读取的长度，以byte为单位
fp.readline([size]) #读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size]) #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str) #把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq) #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
fp.close() #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。 如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush() #把缓冲区的内容写入硬盘
fp.fileno() #返回一个长整型的”文件标签“
fp.isatty() #文件是否是一个终端设备文件（unix系统中的）
fp.tell() #返回文件操作标记的当前位置，以文件的开头为原点
fp.next() #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence]) #将文件打操作标记移到offset的位置。这个offset一般是相对于文件的开头来计算的，一般为正数。但如果提供了whence参数就不一定了，whence可以为0表示从头开始计算，1表示以当前位置为原点计算。2表示以文件末尾为原点进行计算。需要注意，如果文件以a或a+的模式打开，每次进行写操作时，文件操作标记会自动返回到文件末尾。
fp.truncate([size]) #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。
三、目录操作方法大全
1.创建目录
os.mkdir("file")
2.复制文件：
shutil.copyfile("oldfile","newfile") #oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile") #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
3.复制文件夹：
4.shutil.copytree("olddir","newdir") #olddir和newdir都只能是目录，且newdir必须不存在
5.重命名文件（目录）
os.rename("oldname","newname") #文件或目录都是使用这条命令
6.移动文件（目录）
shutil.move("oldpos","newpos")
7.删除文件
os.remove("file")
8.删除目录
os.rmdir("dir") #只能删除空目录
shutil.rmtree("dir") #空目录、有内容的目录都可以删
9.转换目录
-------------------------------------------------------------------

# 9.9.3 OS模块示例 298
# question:
# search the string in dirtree.

#_@qiegua
# 10.0 程序开发进阶303



### 11.0 Object _@object _@class

# lst[0],lst[2]          func(lst)
# obj.name, obj.age      func(obj)

# design: custom data structure and algorithm
# OOP: program is set of objects and interaction each others.
# OOP, 3character/kArIkt/: 
#   encapsulation/in,capse'lefen/fengzhuang: data and method
#   inheritance/in'heritens/jicheng: attribute
#   polymorphism/pBli'mB:fizm/duotai: operator and method. '+'
# type and class of python have great same. int&123 str&'abc'.lower()
# class&instance: class is template,is rule,is virtual, int&123, 
# operate and method on instance not class, is 1+3, not int+int
# all python buitin dataStructure defined to class.

# buildin class make instance with constructor or fastMode
astr=str(123), "abc"
lst=list("abc"), [1,2,3]
stu1=Student('Terry','Jones',12345)
# data to a type structure, to create a object.
# object(data & data.method)
# object have its values and functiones.
# interaction between objectes.

class Student(object):
  """Simple Sludent class"""
  def __init__(self,first='',last='',age=18,idn=0): # init instance
    self.firstNameStr=first
    self.lastNameStr=last
    self.idInt=idn
    self.__age=age   # "__" is pravite attribute.
  def __str__(self): # string, e.g. for printing, __xxx__ python specital var
    return "%s %s, ID:%s" % \
           (self.firstNameStr,self.lastNameStr,self.idInt)
  def __attribute2(self,score=0):   # private attribute, not called outside
    self.score=score
    return self.score

stu1=Student('Terry','Jones',12345)
print stu1

# _@objAttribute
dir(myClass)      # display all attributes and methodes of myClass
dir(myInstance)
type(myInstance)

# edit attribute/add,del,update
Student.classAttribute='hello'
print Student.classAttribute
dir(Student)
stu1.instanceAttribute='world'
print stu1.instanceAttribute
dir(stu1)

# type: (buildin: type(), custom: instance.__class__), instance-of

# _@objScope: first instance then class.  same as: var-> LEGB
# any attributeofinstance of sameName can cover class's.whenever change.
# same var name of instance and class, instance first.

class Test1(object):
  pass
inst1=Test1()
inst2=Test1()
inst3=Test1()

Test1.age=27
inst1.age=72

prnt inst2.age

Test1.age=999

print inst1.age
print inst2.age


# _@self
# self is interface of instance/object call method.
# self refer instance of call this method. def myMethod(self):

# method
# method of instance is user interface. object ~ method ~ user.

# _@Point class
# e.g.
# distance=math.sqrt((x1-x2)**2+(y1-y2)**2)

import math
class Point(object):
  def __init__(self,xParam=0.0,yParam=0.0): # constructor:__init__
    self.x=xParam
    self.y=yParam

  def __str__(self):
    return "(%.2f,%.2f)" % (self.x,self.y)

  def distance(self,pt2):
    xDiff=self.x-pt.x
    yDiff=self.y-pt.y
    return math.sqrt(xDiff**2 + yDiff**2)

p1=Point(2.0,3.0)
p2=Point()
p2.distance(p1)         # ?

# _@pravite attribute
self.__age=age   # "_ _" is pravite attribute. double '_'. designer, programer.




# _@advClass
# 12 advanced class  P344
# how in a familiar way. construct, display, mathOperate, __xxx__,
# same as rules, buildin, standmethod.
# 如何使 行为方式 一致，新建类 与 内置类对象。构造,显示,算术,比较.

# _@rational _@fenshu _@Fraction _@fraction
# fraction /frAkFEn/fenshu, rational /rAFEnEl/youlishu. == equel/ikwEl/dengtong
# fraction:          1/3, 3/8, 7/9,TrueFraction<1, 1/n, ba 1 pingjun fencheng n
#   fenmu:           1/n, biaoshi ba wuti pingjun fencheng n dengfen.
#   fenzi:           m/n, biaoshi qu le qizhongde m fen.
# rational number:   3, 2/5, 8/3, youlishu, Rat == TrueFra + FalseFra
# Irrational number: gen2,pi,e, wulishu,wuxian no loop, no x/y model.
# xiaoshu:           fraction another expression, float == fractions.

# int, float, fractions.

# _@standardMethod
'''
__init__          构造，生成instanc，
__str__           响应 >>>print  name 
__repr__          响应名称，>>>name

'''
# Question: create _@Rational number Class.
#   construct,display,mathoperate(+,-,*,/,<,>,==,),
r1=RatClass(1,2)  # 1/2
r2=RatClass(3,2)  # 3/2
r3=RatClass(3)    # 3/1
rSum=r1+r2
print rSum
rSum
r1==r1
# ?byWhat "+" called which method, (numMethod,strMethod,otherMethod)
# python 使对象 由其类型 来确实 operater and method.
# by type to confirm/ensure operate

# 类型检测 _@type
type()
isinstance()
# 自检, 运行时查看其类型
# >>> float # <type 'float'>
# >>> list # <type 'list'>
# reload, operator and method. specialnames.__add__()
# python support permits operaters set.
# None  == empty

# _@operatorMethod _@objAdd 
# ?how "+" how ~ map method.
var1+var2 == var1.__add__(var2)
# ?how to define operatorMethod?

# e.g.: x+y
class Add(object):
  def __init__(self,x):
    print 'In constructor'
    self.val1=x

  def __str__(self):
    print 'In str'
    return 'Val is: %s' % str(self.value)

  def __add__(self,y):
    print 'In add'
    sum=self.val1+y.val1 # must be a same type.  type == data+structure
                         # y.val1, not y.other, same type, same atribute.
    return Add(sum)      # also return a same type result


inst1=Add(3)
inst2=Add(5)

print type(inst1)  # <class '__main__.Add'>
print type(Add)    # <type 'type'>
print inst1        # 3
sum2=inst1+inst2
print sum2         # 8
print type(sum2)   # <class '__main__.Add'>

# _@rationalAdd _@fractionAdd _@+
# 分数加法

1/2 + 3/5

# 公分母，1/2, 3/2, 2
# 最小公倍数，lcm, 1/2, 3/5,---5/10, 6/10, 10
# 最大公约数，gcd, 12/24, 24/36---1/2, 2/3, 12

a*b=gcd(a,b)*lcm(a,b)


#_@gcd(max gongyueshu): 6,15->3
# lcm(min gongbeishu): 6,15->30
# lcm(a,b)=a*b/gcd(a,b)

# gcd
def gcd(a,b):

  if not a>b:
    a,b=b,a

  while b!=0:
    yu=a%b
    print a,b,yu
    a,b=b,yu

  return a

def lcm(a,b):
  return (a*b)/gcd(a,b)


# _@fractionEqual _@rationalEqual _@==

# 1/2==1/2?

# a/b==c/d?  <==> (a==c and b==d) ?

# 2/4==5/10?

# reduce/ri'djus/化简   rdc
	gcd

# a/b.rdc()


# _@Rational
# question: create class Rational.

# denominator/di'nBmI'netE/ 
# numerator/'njumE'ret/ 
# representation/'rZprIzZn'teFEn/daibiao
# func and var all have its owner

# question: create class Rational.

class Rational(object):

  def __init__(self,numer,denom=1):
    self.numer=numer
    self.denom=denom

  def __str__(self):
    return str(self.numer)+'/'+str(self.denom)

  def __repr__(self):
    return self.__str__()

  def gcd(self,a,b):
    if not a>b:
      a,b=b,a
    while b!=0:
      yu=a%b
      a,b=b,yu
    return a

  def lcm(self,a,b):
    return (a*b)/self.gcd(a,b)

  def __add__(self,f):

    if type(f)==int:
      f=Rational(f)
    if type(f)==Rational:
      lcm1=self.lcm(self.denom,f.denom)
      sum1=(lcm1/self.denom * self.numer) + \
           (lcm1/f.denom * f.numer)
      return Rational(sum1,lcm1)   
    else:
      print 'Type Error'
      raise(TypeError)
  
  def __radd__(self,f):
    return self.__add__(f)

  def __sub__(self,f):
    lcm2=self.lcm(self.denom,f.denom)
    diff2=(lcm2/self.denom * self.numer) - \
         (lcm2/f.denom * f.numer)
    return Rational(diff2,lcm2)   

  def reduceRational(self):
    theGcd=self.gcd(self.numer,self.denom)
    return Rational(self.numer/theGcd,self.denom/theGcd)

  def __eq__(self,f):
    f1=self.reduceRational()
    f2=f.reduceRational()
    return f1.numer==f2.numer and f1.denom==f2.denom


rat1=Rational(6,12)
rat2=Rational(18,24)
print type(rat1)        # <class '__main__.Rational'>
print rat1              # 6/12
rat2
sum=rat1+rat2
print type(sum)         # <class '__main__.Rational'>
print sum               # 30/24
diff=rat1-rat2
print diff              # -6/24
print rat1==rat2        # False
print rat1+1            # 18/12
print 1+rat1            # 18/12




# 14 _@exception  _@try

# exceptionType: input,error,event

try 
  True
  # code to watch here
except
  False
  # some code to bandle the named error, if it occurs.

else:

finally: # whatever to do

# e.g.

while True:
  try:
    filename=raw_input("Open file: ")
    datafile=open(filename,'r')
    break # success...
  except IOError:
    print "Bad file name."

# e.g.
# int(str)
if not isinstance(s.str) or not s.isdigit:
  return None
elif len(s) > 10: #too manay digits for int conversion
  return None
else:
  return int(str)
#------------------------------------------------
try:
  return int(str)
except (TypeError,ValueError,OverflowError):  #


tags_: _@withas

concept_: with as

core_:'''>

with open("x.txt") as f:
    data = f.read()
    do something with data

with open("x.txt") as f1, open('xxx.txt') as f2:
    do something with f1,f2

<'''

detail_:'''>

try:
    f = open('xxx')
except:
    print 'fail to open'
    exit(-1)
try:
    do something
except:
    do something
finally:
    f.close()

<'''
time_: 20170824172157

----------------------------------------------------------------------------
#_@over
