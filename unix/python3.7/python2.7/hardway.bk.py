
# 0: Python setup, powershell;
[Environment]::SetEnvironmentVariable("Path","$env:Path;c:Python27","User")
# restart powershell,  ctrl-z, quit shell;

# 1: @print a string
# coding: utf-8
print "I'm nudo."
print 'I "said" do not touch this.'
print "您好。"

# 4: variable = name
#   var only is a name which referece a thing.
#   var can help programmer remember some code.
#   "="equal get a name for a thing. get name operator.

# 5: %s display variable in format string. 
#   变量在格式化的字符串中的显示；%s

#   %r debug专用,显示字符和数字；
#   %s 字符，显示给用户;
#   %d 数字

print 'My name is %r' % 'Jack'
print 'My age is %r' % 23

print int(1.7333)    # 1					整数取整；
print int(2.1123)    # 2
print math.floor(1.9999)  # 1.0  /flo/地板  浮点取整；
print math.floor(2.1111)  # 2.0
print round(1.733)   # 2.0 四舍五入函数； ***************************
print round(2.133)   # 2.0

print float(1.999)   # 1.999
print float(2.111)   # 2.111

# 6
# %r 显示raw data原始数据
x="%d" % 10
y="%s" % "don't"

print "I said: %r." % x  # I said: '10'.        嵌套格式打印；
print "I said:'%s'" % y  # I said: 'don't'.     %r,%s区别
print "I said: %s" % y   # I said: don't.     %r,%s区别

# 9 print 有换行的str,
#   原码print多行str；
# 逆向阅读，加注释；
# 倒着朗读，找错误；
print 'a\nb\nc' 
# 原码打印 多行str； 
print """
aaa
bbb
ccc
"""
# 一行未完待续；
print 'abbbbbbbbbbbbbbbbbbbbbb\
c'

# 10
# 制表符t，转义符\，可显难显字符；
print "I'm \\ a \\ cat."
fatCat="""
I'll do a list:
\t* cat food
\t* fishies
\t* catnip
\t* grass
"""
print fatCat

# 每行不多于80个字符；
# ~$ pydoc

# 11:
# 接收 用户原始输入 赋值
x=int(raw_input('>'))
print x*x

# 13：传参给脚本；argv

#     参数、解包、变量
#     参数变量包argv会接收所有变量，并会传给脚本；
#     argv, argument variable;you pass to python args.
#     modules, libraries, 模组，库，

# ex13.py:
from sys import argv

script, a, b, c = argv      # unpack
print a,b,c

#~$ python ex13.py aaa bbb ccc ## python 后都是参数；
#~$ ./ex13.py aaa bbb ccc      ## #!/usr/bin/env python

#   argv,raw_input()共同点是脚本用来接收信息的；
#   argv        执行命令时的接收输入； 
#   raw_input() 脚本执行过程中的接收输入；

#   命令行参数是字符串；3, int(3)

# 14:提示和传递 
b=raw_input(">")


# 15: 读取文件
#	查看文件读写命令 ~$ pydoc file

filename=raw_input('Please input file name that you will read.\n>')
txt=open(filename)
print "The file content is: "
print txt.read()
txt.close()


# 16:
#   写入文件；
filename=raw_input('Input file name for write something.\n>')
print 'Openning the file %s ...'%filename
txt=open(filename,'a')
content=raw_input('The file was opened, input your content now.\n>')
txt.write(content)
txt.close()
txt=open(filename,'r')
print 'File content:'
print txt.read()
txt.close()

# erase file and write file
filename=raw_input("Input a filename you want to erase all and write new.\n>")
print "Openning the file %s..." % filename
txt=open(filename,'w')
print "Truncating the file."
txt.truncate()
print "Now the file is empty."
newtxt=raw_input("Please input your new content.\n>")
txt.write(newtxt)
print "Now the content saved.bye."

# 17: 更多文件操作

from_file=raw_input("Input filename you'll copy.\n>")
inFile=open(from_file)
inData=inFile.read()
print inData
inFile.close()
toFile=raw_input("Input filename you'll write.\n>")
outFile=open(toFile,'w')
outFile.write(inData)
outFile.close()

# 18: 命名，变量，代码，函数

# 变量是给字符串数字命名；  
# 函数是给代码段命名；
# 函数名即命令,又是小脚本；

# function
def myfun():
    print 'My first function.'

def myfun2(a,b):
    print 'myfunction %s, %s.'%(a,b)

def another(*argv):
    a,b,c=argv
    print a,b,c

myfun()
another('aaa', 'bbb', 'ccc')

# 21: func return
def rtn(a,b):
    return a+b

print rtn(3,4)              # 7
print rtn('aaa','bbb')      # aaabbb


# 30: if else elif

a=3
b=8
c=13

if a < b :
    print "a is small."

if c<b :
    print 'IIIIIIIII'
else:
    print 'c is large'

if a>b:
    print 'aaaa'
elif a>c:
    print 'bbbb'
else:
    print 'b is middle'


# 32: for-loop; list
# condition loop

mycount = [1,2,3,4,5]
mychar=['a', 'b', 'c']

for e in mycount:
    print e,

print '\n'

for e in mychar:
    print e,

print '\n'

for e in range(1,6):
    print e,

# 33: while-loop
#   count loop
x = 1
while x < 9:
    print x,
    x = x + 1  # 累加 赋值 1 -> 9；

x = 9
while x > 0 :
    print x,
    x = x - 1  # 递减 赋值 9 -> 0；

x = 2
i = 1
while i < 4 :
    print x,
    x = x * 2  # 累乘 赋值 2 -> 100；
    i = i + 1

####################### Loop n ####################
# loop n, 1 ---> n
i=1
while i <= n:
    print i,
    i += 1


#? int x 的n次方：

'''
x^n 
cmpt can do:
    a*a
    val = a
    loop statment

    not x^n

turn:      .---n----.
    x^n == x*x*x...*x
    
    charcater: loop * self          
         1.x*x  -> val   v = x * x, v=x, v = v * x
         2.val*x -> val  v = v * x
         3.val*x -> val  v = v * x
         ...
         loop v = v * x
         loop n

'''
def power(x=2,n=5):
    if n == 0:
        return 1
    i = 1
    v = 1
    while i <= n:
        v = v * x
        i += 1
    return v
# 4 8 16

print power(2,0)
print power(2,1)
print power(2,2)
print power(2,3)



# 34: access e of list

char=['a', 'b', 'c']
print char[1]

# 39: dictionary

mydict = {'name':'nudo', 'age':38, 'sex':'man'}
print mydict['name']    # nudo


# 40: 模块，类，对象

# 类，装函数的字典，把函数放到字典里，即是类；

# first class
class MyFruit(object):
    def __int__(self):      # add attribute for object pass from self.
        self.number=8       # num, name, age...

    def apple(self):        # bind method for object pass from self.
        return 'I am a apple.'

MyFruit()       # call class by add () like func, return empty object ---self
fruit = MyFruit()           # call class, name refer self object;
print fruit.apple()
print fruit.number

# module
myfruit.py:
def apple():
    return 'I am a apple.'
number=3

import myfruit
print myfruit.apple()
print myfruit.number


# Get B from A:
# dict style
myfruit = {'apple':'I am a apple', 'number':8}
print myfruit[apple]
# module style
import myfruit
print myfruit.apple()
print myfruit.number
# class style
thing=MyFruit()
print thing.apple()
print thing.number


# 41: class

# instance and self
class My(object):
    def hello(self):    # pubulic method
        print 'hello, this is myself.'

My().hello()   # add () to instance.
my = My()
my.hello()     # after self = my, public hello() become method of my

# add initial attribute to object
class My(object):

    def __init__(self, name):
        self.name = name

    def hello(self):
        return 'My name is %s.'%self.name
    
my = My('Jack')
print my.name
print my.hello()



    class Person(object):

        def __init__(self, name):
            self.name=name

        def say(self):
            print 'My name is %s' % self.name

    # 实例化 的方法就是 像调用函数一样 调用一个类；
    p = Person()    # python create a space object for self,and find __init__
    p.say()
    p.name

    class Song(object):

        def __init__(self, lyrics):
            self.lyrics = lyrics

        def sing(self):
            for line in self.lyrics:
                print line

    aa = Song(['dear,', 'I love you.'])  # create space obj self, and init self.
    bb = Song(['dear,', 'I love you too.'])

    aa.sing()                            # run obj'method.
      dear,
      I love you.

    bb.sing()
      dear,
      I love you too.


# 42:

# 一个类的变量 传到 另一个类；
class Mult(object):
    def __init__(self, base):
        self.base = base
        
    def doit(self, m):
        return m * self.base

x = Mult(a.num)                 # inter attribute between objects.
print x.doit(b.num)


# 43:
# 44: 继承inheritance，合成composition
    # pass 是在Python中 创建空的代码区块；

'''
# Implicit Inheritance
class Parent(object):

    def hello(self):                    # public method; xxx.hello()
        print 'Hello, parent should program using c.'

class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.hello()
son.hello()

# Explicit Override
class Parent(object):

    def hello(self):
        print 'Hello, parent should program using c.'

class Child(Parent):

    def hello(self):
        print 'Hello, child should program using python.'

dad = Parent()
son = Child()

dad.hello()
son.hello()

'''
# Inheritance and Override
# 多重继承Student(Person,Teacher) 与 super()
class Parent(object):

    def hello(self):
        print 'Hello, parent should program using c.\n'

class Child(Parent):
    
    def hello(self):
        print 'Hello, child should program using c also.'
        super(Child,self).hello()  # 这句你可以读作“调用 super 并且加上 Child 和 self 这两个参数,在此返回的基础上然后调用 altered ” 。
        Parent().hello()
        print 'Hello, child should program using python too.'

dad = Parent()
son = Child()

dad.hello()
son.hello()
# super(), Python 帮你选择父类，在多重继承中； 
# super()和__init__()搭配使用主要；

class Child(Parent):
    def __init__(self,data):
        self.data = data
        Parent().__init__()
        super(Child,self).__init__()


# 合成---调用；     尽量用合成调用，不用继承；
# 不用继承，可以直接调用；

class Child(Parent):
    pass

class Child(object):
    def __init__(self):
        self.call = Parent()
    def hello(self):
        self.call.hello()
######################################33
class Person(object):
    def __init__(self, data):
        self.name = data
    def say(self):
        return 'I is %s' % self.name

class Student(Person):
    pass

class Teacher(object):
    def __init__(self,data):
        self.person = Person(data)      # let a class come to a attribute
    def say(self):
        return self.person.say()


t = Teacher('teacher')
print t.say()

# ? 重用
    '''
    1.不惜一切代价 避免多重继承；
    2.code will used in many position or scene, call.
    3.clearly relation, inheriate.
    '''

# 45: game




# 46: project skeleton /skelitn/骨架
#     项目骨架<软件包<package installer

path:
ls -R
projects/
         skeleton/setup.py
                  docs/
		  bin/
	          tests/__init__.py, NAME_tests.py
		  NAME/__init__.py


# python package manager tool:
# old tool: setuptools easy_install
# new tool: pip distribute(disutils,dist-util-s)
# pip,distribute,nose
apt-get install pip
pip install pip --upgrade
apt-get install virtualenv
...
pip install distribute
pip install nose

skeleton>nosetests
# 使用这个骨架:
# 以后每次你要新建一个项目时,只要做下面的事情就可以了:
# 1.拷贝这份骨架目录,把名字改成你新项目的名字。
# 2.再将 NAME 模组更名为你需要的名字,它可以是你项目的名字,当然别的名字也行。
# 3.编辑 setup.py 让它包含你新项目的相关信息。
# 4.重命名 tests/NAME_tests.py ,让它的名字匹配到你模组的名字。
# 5.使用 nosetests 检查有无错误。
# 6.开始写代码吧。


# 47: 自动化测试

# 你需要为自己写的所有代码写自动化测试,
# 单元测试




















