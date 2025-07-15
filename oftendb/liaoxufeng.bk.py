


'''
www.liaoxuefeng.com

    Index

    Python教程
    	Python简介
    	安装Python
    		Python解释器
    	第一个Python程序
    		使用文本编辑器
    		Python代码运行助手
    		输入和输出
    Python基础
    	数据类型和变量
    	字符串和编码
    	使用list和tuple
    	条件判断
    	循环
    	使用dict和set
    函数
    	调用函数
    	定义函数
    	函数的参数
    	递归函数
    高级特性
    	切片
    	迭代
    	列表生成式
    	生成器
    	迭代器
    函数式编程
    	高阶函数
    		map/reduce
    		filter
    		sorted
    	返回函数
    	匿名函数
    	装饰器
    	偏函数
    模块
    	使用模块
    	安装第三方模块
    面向对象编程
    	类和实例
    	访问限制
    	继承和多态
    	获取对象信息
    	实例属性和类属性
    面向对象高级编程
    	使用__slots__
    	使用_@property
    	多重继承
    	定制类
    	使用枚举类
    	使用元类
    错误、调试和测试
    	错误处理
    	调试
    	单元测试
    	文档测试
    IO编程
    	文件读写
    	StringIO和BytesIO
    	操作文件和目录
    	序列化
    进程和线程
    	多进程
    	多线程
    	ThreadLocal
    	进程 vs. 线程
    	分布式进程
    正则表达式
    常用内建模块
    	datetime
    	collections
    	base64
    	struct
    	hashlib
    	itertools
    	contextlib
    	XML
    	HTMLParser
    	urllib
    常用第三方模块
    	PIL
    virtualenv
    图形界面
    网络编程
    	TCP/IP简介
    	TCP编程
    	UDP编程
    电子邮件
    	SMTP发送邮件
    	POP3收取邮件
    访问数据库
    	使用SQLite
    	使用MySQL
    	使用SQLAlchemy
    Web开发
    	HTTP协议简介
    	HTML简介
    	WSGI接口
    	使用Web框架
    	使用模板
    异步IO
    	协程
    	asyncio
    	async/await
    	aiohttp
    实战
    	Day 1 - 搭建开发环境
    	Day 2 - 编写Web App骨架
    	Day 3 - 编写ORM
    	Day 4 - 编写Model
    	Day 5 - 编写Web框架
    	Day 6 - 编写配置文件
    	Day 7 - 编写MVC
    	Day 8 - 构建前端
    	Day 9 - 编写API
    	Day 10 - 用户注册和登录
    	Day 11 - 编写日志创建页
    	Day 12 - 编写日志列表页
    	Day 13 - 提升开发效率
    	Day 14 - 完成Web App
    	Day 15 - 部署Web App
    	Day 16 - 编写移动App
    FAQ
    期末总结

'''

#    廖雪峰

# simple python
# Python is open, can not jiami.
# Python interpreters/compilers:
# speed->CPython,PyPy; javapalam->Jython; but net call.
# file model & interacive model ... out: ctr+enter | enter enter
# #!/usr/bin/env python3
chmod a+x hello.py
# coding run mode: cmd line, zhengti file.; jiaohu>>>, lingsan run.
# i/o:print('a','b','c')  # a b c
# var&bianlian:abstract data, zhidai,
# 机器码；
# 编程语言，唯一语义；
# 重构代码
# 数据类型：
#       数字、文本、图像、声音、影像；
#       number,string,bool,None,image,sound,video,
#       var,list,dict,object,changliang,
# int 8 -10 0x14 结果精确 16jinzhi:0x + 0-9 + a-f, 0xff00
# float 3.14 2.1x10^8 2.1e8 0.000001 1.0e-5 结果四舍五入；
# string '' "" 是表示方式，不是字符串的一部分；
# zhuanyizifu:\, use to display a spectical charictor, \',\'',\n,\t,
print 'I\'m xxx.'# I'm xxx.
print '\\'       # \
print r'\\a\'b'      # \\a'b  zhuanyi little use \,many use r；
print '''
abc
def
ghi
'''              #       用于多行，或复杂的串；
# bool 3 > 2; True or False; 
# None not 0 not ''.
# 变量
a = 'abc'
# Python 解释器干了两件事：
# 1.在内存中创建了一个字符串'abc'
# 2...............名为a的变量，并指向'abc'
a = 'abc'
b = a 
a = 'def'
print b         # abc
# var class: 
int a=3
str b='ab'
# if var class is gudingde, then it is a staic language, not dymic language.

# 常量 是约定不要改变的变量，daxie,up,PI；
# 除法 / result is float. 
#      // % 取商，取余, result is int.；//dibianchu.
9/3    # 3.0
9//3   # 3
10%3   # 1
10/3.0 # 3.3333333333333335 精确
# Python支持多种数据类型，可以any data look object, var refer to dataobject.
# 对变量赋值，就是把数据和变量关联起来；

# 字符编码 
# ASCII:  America, english                1 byte.
# Unicode:Many country, many language.    2 byte.  storage and pass.
# UTF-8:  update of Unicode.              en 1byte, cn 3byte
# cpu only handle number, if do char, encode,
# America ASCII one byte, China GB2312 3byte ... unicode 2byte;
# if main english, 2byte will fill double space for save.
# can change long or short encode: utf-8; 1-6byte, en 1b, cn 3b, some 4-6b;
# ram(unicode) disk(utf-8) net(utf-8)
#      str         byte      byte      . str == n*byte. 
# 'ABC'.encode('ascii')=b'ABC'
# Python default encode: ASCII utf-8 unicode;
u'abc'             # unicode encode;
len('abc')         # 3  ascii or utf-8
len(u'abc')        # 3  unicode
len('中文')        # 6  utf-8
len(u'中文')       # 2  unicode
# utf-8 --> unicode
'abc'.decode('utf-8')       # u'abc'
# file.py use UTF-8, vim,notepad++, use 'Encode in UTF-8 without BOM'

# string 格式化 'xxx您好，您xx月的话费是xx,余额是xx'
'%d-%0d' % (12,3)       # '12-03'
'growth rate: %d %%' % 7# 'growth rate: 7 %'

# _@list/tuple
# list is varable/editable order set.
# tuple not .............. order set.
# list: append()/pop(), insert(i,str)/pop(i), i=index. pop():del from end
# replace: x[i] = a
# tuple:
(2)   # 2
(2,)  # (2,) 定义一个元素的元组+‘,’ ,以区别小括号成运算；

# varable tuple:
t = ('a', 'b', ['A','B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print t         # ('a', 'b', ['X', 'Y'])
# tuple 指向不变.

# 变量var 和  本例的图表 表示；====drawing

# 选择_@if
if xxx:
[[elif xxx:]
else:
]
# if is run from up to down, and if up is True,then not run down, so first False then True.

# 重复_@for in
# 计算1-100 之和；
sum = 0
for x in range(101):
    sum = sum + x
print sum

# 计算100以内奇数之和；
sum = 0
n = 99
while n > 0:
    sum = sum + n
    n = n - 2
print sum

# _@dict & set:
# dict good at find speed, bad at use ram big.
# key only have 1 value;
# key 不可变,no repeat.

dd = ['aa': 'Jack', 'bb': 'Rose']
dd['aa'] = 'Jack'
dd['bb'] = 'Rose'

# if key not exit:
# 'aa' in dd
# dd.get('aa') return None
# del key, pop(key)

# _@set : no same no order;
# set is key collect, not value.
# no order no repeat.
set(list), set([1,2,3]) # {1,2,3}
#       add(key)
#       remove(key)
# set and dict 区别是 no value;
# jiaoji bingji:
s1=set([1,2,3])
s2=set([2,3,4])
s1 & s2         # {2,3}
s1 | s2         # {1,2,3,4}

# 不可变对象：
a = ['c', 'b', 'a']
a.sort()
a               ['a', 'b', 'c']

a = 'abc'
a.replace('a', 'A')          # 'Abc' 对象方法会自动创建副本，并生成新对象；
b=a.replace('a', 'A')        # 'Abc' 
a                            # 'abc'


# 函数_@func
# s = PI*r*r
r1
r2
r3
# 抽象_@abstract
100cgma1(n) = 1 + 2 + 3 ... + 100
100cgma1(n*n + 1) = (1x1+1)+(2x2+2) ...
# 借助抽象，不用关心底层具体计算过程，而直接在更高层次上思维问题；
# 函数是最基本的一种代码抽象方式；
# python built in many usefull function, can be called directly.
# coding run in jiaochu: if is many lines, disp ..., two entry reback.
def aa():
    pass
if age > 18:
    pass

def Nonee():
  pass
# func return many vales is tuple
# question:new zuobio in game:
import math
def move(x,y,step,angle=0):
  nx=x+step*math.cos(angle)
  ny=y+step*math.sin(angle)
  return nx,ny
x,y=move(100,100,60,math.pi/6)
print x,y
r=move(100,100,60,math.pi/6)
print r  # (151.79475, 70.0)

# interface of func,_@argument_@canshu._@funcArgument _@args
# 函数参数：
# func(*lst,**dct) _@args

# 1/5_@positionArgument_@pa_@weizhi:
# x*x
def power(x):
  return x*x
# x*x*x*x...n
def power(x,n):
  s=1
  while n>0:
    n=n-1
    s=s*x
  return s

# 2/5默认参数defaultArgument_@da:
def power(x,n=2):
# default argument must be unvarable object.
def add_end(L=[]):
  L.append('END')
  return L
add_end([1,3,4]) # [1,3,4,'END']
add_end()        # ['END']
add_end()        # ['END','END']
add_end()        # ['END','END','END']
# L is a var, direct to [],every call func, value is var.
# now use unvarable var: None.
def add_end(L=None):
  if L is None:
    L=[]
  L.append('END')
  return L


# 3/5_@varableArgument_@va_@kebian _@lstarg_@la _@args
# number of argument is var.
# q:1^2+2^2+3^2...
def calc(numbers):
  sum=0
  for n in numbers:
    sum = sum + n*n
  return sum

calc(2)
calc(1,2,3)
cals(*[1,2,3])
cals(*lst)

def calc(*numbers):
# if list or tuple,
def cals(*list):

# 4/5_@keywordArgument_@kwa_@dctArg
def person(name,age,**kw):
def person(name,age,**dct):

# 5/5_@nameKeywordArgu

def person(name,age,*,city,job):  # * fengefu

def person(name,age,*args,city,job):  # if before have a varable arg,not need

# 6/5 args mix hunhe

# order: must,default,varable,namedKwArg,kwArg
def f1(a,b,c=0,*args,**kw):
def f1(a,b,c=0,*,e,**kw):

f1(1,2)                # a=1,b=2,c=0,args=(),kw={}
f1(1,2,3,'a','b',x=99) # a=1,b=2,c=3,args=('a','b'),kw={'x':99}

# func(*args,**kw)
# func(*lst,**dct) _@args

### _@iteration _@diedai
# use forin traverse a list --> iteration
# iterable object: lst, dct, str
for i in 'abc':
for i in [1,2,3]:
for key in {'a'=1,'b'=2}:
for key in dct:             # dct default traverse key
for v in dct.values:
for k,v in dct.items:
# q: how judge a object if is a iterable?

from collections import Iterable
isinstance('abc',Iterable)   # True
isinstance([1,3,4],Iterable) # True
isinstance(123,Iterable)     # False

# Q: how traverse a list by index?
for i,value in enumerate(['a','b','c']): # /i'njumerat/lieju
  print i,value

### _@ListComprehensions _@lstcmprhs _@liebiaoshengchengshi_@lbscq
[x*x for x in range(1,11)]
[x*x for x in range(1,11) if x%2==0]
[m+n for m in 'ABC' for n in 'XYZ']
import os
[dr for dr in os.listdir('.')]
[i.lower() for i in ['A','B','C']]
lst=['x':'A','y':'B','z':'C']
[k+'='+v for k,v in lst.items()]

l=['Hello','World',18,'Apple',None]
lst=[s.lower() for s in l if isinstance(s,str)]
print lst

### _@generator _@gnrt  _@shengchengqi_@scq
# come from: if create a big list, list will use big ram.
# generator save suanfa not list in ram, now using, now create/compute.next()
# generator: while traverse, compute next listItem.
# generator&list: gnrt next value come from pre value. Fibonacci list, yanghuisanjiao.
# create generator: 
# 1.lstcmp
(x*x for x in range(10))       # is (),not []
# 2.def func:
#   Fibonacci list
def fib(max):
  n,a,b=0,0,1
  while n<max:
    yield b                    # print b.
    a,b=b,a+b
    n=n+1
  return done

# Different:
# lstcmp&generator: 
#       1.[],()
#       2.printi,next(g) or for in g: (one by one create.)
# func&generator:
#       1.print, yield
#       2.every once: start->return x, start->yield x, yield x->yield x+1.

def odd():
  print 'step 1'
  yield(1)
  print 'step 2'
  yield(3)
  print 'step 3'
  yield(5)

o=odd()
next(o)
next(o)
next(o)
next(o)
for n in fib((6):
    print(n)

# _@triangles _@yanghuisanjiao_@yhsj
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
   1 5 10105 1

# _@iterator _@diedaiqi

# iterable > iterator > generator((listcmp),func(yield))
# lst/str(forin)

isinstance(iter([]),Iterator) # True

























### _@module
# file: mdl.py
#!/usr/bin/env python
#coding: utf-8
'a test module'
_author_='xxx'

def test():
  return 'module test'

import mdl
print mdl.test()


# sys.argv, argv[0]=filename.py

# _@installModule _@im
# install third module by pip install xxx
# pypi.python.org reged all 3rd lib.
# use to image: Pillow
# use to MySQL: mysql-connector-python
# use to cmpt:  numpy
# use to text:  Jinja2
from PIL import Image
im=Image.open('test.png')
print(im.format,im.size,im.mode)
im.thumbnail(200,100)              #/s^m/muzhijia
im.save('thumb.jpg','JPEG')
# module search path: import module, python will first search path.
# _@modulePath:sys.path
# add Person Path:
# 1.append:running work,after reback.
# 2.PYTHONPATH: the value will add self to python search path.

### _@object
# Python type and class have great same. int type, str type, list type,
# object = attribute + method = var + func = data + operate; dir()
# advanced abstract, obj is set of some var/data and funces/method.
# class/instance, class is a template of instance, is a abstract of same attribute, is virtual
# class work like type, int is template, 356,2,25 is instance,
# class def attribute and structure and operaters of instance.
# operaters work at instance not class,is 1+2,not int+int; mould/matrix
# def + Name + comefrom (parent object):
class Student(object):
  pass
# create instance: use the same function to create instance.
myInstance=Student()
# Instance can be added attribute freedly.
myInstance.name='ada'
# add attribute of class:
class Student(obj):
# def __init__(self,*argus,**dct):  self <-is instance, not subclass, not subclass
  def __init__(self,name,score):
    self.name=name
    self.score=score
#   ...++

  def print_score(self):
    print('%s:%s' % (self.name, self.score))

# ...++

### data of obj access/visit:  _@dataaccess
print myInstance.name
print_score(myInstance)

# limit access/edit of attribute/var:
# self.__name=name
# self.__score=score
# add __attribute, to private var.
# __var__ is python var.
# _var: is private var which can be accessed outside,but carefully
def get_name(self):
  return self.__name
def get_score(self):
  return self.__score
def set_score(self):
  self.score=score
# different access direct: can control access.
# different attribute of class and instance:
class Student(object):
  anotherName='xuexizhe'
  def __init__(self,name):
    newName=name

instc=Student('abb')
print Student.anotherName
print Student().newName
print Student().anotherName
print instc.newName
# if newName is anotherName? instc.name will recove class.name.
# creat,access,edit attributes and methods of class and instance

### Get info of object: _@getinfo
# type() instance() dir() getattr() setattr() hasattr()
# judge obj type:
# use type(obj)        
type('123')==int # True
type('abc')==str # True
# if judgeObj is func? 
# use constant of typesModule:
import types
def func():
  pass
type(func)==types.FunctionType
type(abs)==types.BuiltinFunctionType
type(lambda x:x)==types.LambdaType
type(x for x in range(10))==types.GeneratorType

# use isinstance():
# judge inheritRelation of class type
# object->Animal->Dog->Husky
a=Animal()
dd=Dog()
h=Husky()

isinstance(h,Husky) # True
isinstance(h,Dog)   # True
isinstance(dd,Husky)# False

isinstance(123,int)
isinstance('abc',str)
isinstance(b'a',bytes)

isinstance([1,2,3],(list,tuple)) # True
isinstance((1,2,3),(list,tuple)) # True

# use dir():
# Get all attributes and methodes of a object.
dir('abc')
'abc'.__len__()
# len() == __len__()
# getattr(),setattr(),hasattr()
hasattr(instc,'name')
setattr(instc,'age',19)
getattr(instc,'age')      # 19
getattr(instc,'z',404)    # 404  default argu

def readImage(fp):
  if hasattr(fp,'read'):
    return readData(fp)
  return None

### Inherit and Polymorphic  _@inherit _@jicheng 
# Subclass Super class / base class

class Animal(object):

  def run(self):
    print 'Animal is running.'

class Dog(Animal):
  pass

class Cat(Animal):
  pass

dog=Dog()
dog.run()

class Dog(Animal):
  def run(self):
    print 'Dog is running.'

# subclass method will reover superclass,
# poly: same method, different object to run, get diffrt result.
# no diffrt:
a=list()  # a type is list
b=Animal()# b type is Animal
c=Dog()   # c type is Dog

def run_twice(animal): 
  animal.run()
  animal.run()

run_twice(Animal())  # Animal is running
run_twice(Dog())     # Dog is running

class Tortoise(Animal):
  def run(self):
    print 'Tortoise is running slowly'

run_twice(Tortoise())# Tortoise is running slowly
# abstractMethod apply at diffrt obj, get diffrt result.

class Timer(object):
  def run(self):
    print('start...')

run_twice(Timer())   # start...     
# only have run method, not request same class.
# dynamic language, file-like object.






# rhythm



















# from filename import func
# _@err
# def func, check argument.
def my_abs(x):
  if not isinstance(x,(int,float)):
    raise TypeError('bad operand type')
  if x >= 0:
    return x
  else:
    return -x






