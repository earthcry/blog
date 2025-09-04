
#       Beginning of Python from novice to professional
#       11-21 novice /naovis/


# 计算机程序是写给人看的，恰好能够运行。
# 软件设计其实就是对于抽象复杂度的控制。

# 习惯的组合是emacs+ipython+python-mode，用doctesting做TDD，效率很高。最近一段用sublime text比较多，也没觉得离开习惯的环境就做不下去。

《Python基础教程》
1.基础，2元组和列表，3字符串，4字典，5条件循环
6.抽象，7更加抽象，8异常，9魔法方法、属性和迭代器，10模块
11.文件和素材，12.图形用户界面13.数据库支持，14.网络编程，15.py和www
16.测试，17.extend py，18.程序打包，19.还玩的编程20.项目1
29.项目10。

另外android编程，并不难，你可以花10几天学习一下，并非一定要有JAVA基础，事实上你有python基础学习一个android编程也不难。java是小事儿。主要要熟悉android的应用开发框架。

python这个语言容易学，同样java语言本身也容易学。真正的大的学习工作量是开发模式，还有设计模式，更大的工作量是掌握特定业务。

比如GUI怎么设计，用户怎么登陆，数据怎么安全，系统怎么分析，效率如何优化等等。
python 能开发 Android 应用吗？SL4A, kivy,
试试QPython: QPython | Python for android
现在可以用 kIvy+PIL+python for android
作为一个3年PHP经验的程序员，我的建议就是：
如果你追求快速快速开发，招人简单，用PHP是非常不错的。但是，如果你预计你的项目以后会做得很大，需要代码更好，选择其他语言吧。不一定是python，因为你将一个项目的语言定死，那么这个项目的局限性就太多了。队列这一块用nodejs、业务逻辑可以用python，ruby也不错哦，前端通信用nodejs的有一个html5通信框架(名字我忘记了)，反正选择很多啦。数据库呢，redis做热点数据，mongodb做持久化存储，或者其他什么什么的。
说得太复杂了……总之就是，在开发进度和项目框架级别上做一个均衡。先用PHP做没问题的，PHP可以胜任很多事情，虽然某些时候他的表现会很糟糕。

    # 基本概念：

    # 运算符、表达式/值、语句、
    # 变量、数据类型/数据结构、函数/模块、算法/程序/步骤

    # 算法,程序,步骤 = 表达式 + 语句；

    # 表达式 某事
    # 语句 做某事 ，计算执行表达式 

    # 表达式 = 运算符 + 函数 + 变量 + dataType ; 
    # 变量是指代，是名字，是容器；表达式的结果是值；值=表达式；
    # 模块.函数 python 功能扩展； 
    import math
    math.floor, cmath.sqrt(-1), 3j

    # 整浮计算模式切换： 有浮即浮，2个指令，//为整算；长整数3L；
    # 数字计算常用函数：
    print,pow,round,

    # 字符串表示：
    #   单引号、双引号、转义线，引号相异套用；
    #   长字符串'''、原始字符串raw r''、unicode u''；
    # 字符串输出输入方式函数：显示，代码；
    str     repr(value)
    input() raw_input()


# 要素和指令；
# 1.3算法是程序procedure食谱recipe步骤；
# 1.4数字和表达式；
#    默认，你整它就整，你浮它就浮；浮点数=实数=整数+小数(分数+无理数)；
#       若都浮, 即普通除法:
        from _future_ import division
        Qnew #linux
#       要整的话用//
#   运算符：/ % *;
#   长整数：11111111111L
#   十六进制和八进制：0xAF;010;
# 1.5变量variable
#    赋值assignment
# 1.6语句
#   表达式是 某事；        2*2
#   语句  是 做某事；print 2*2
#   赋值语句；打印语句。。。
# 1.7获取用户输入
    x=input("x:")
    x:34
    y=input("y:")
    y:42
    print x*y
    1428
# 1.8 函数
    pow(2,3)
    标准函数，内建函数，调用函数；
    10+pow(2,2*5)/3.0
    round(1.0/2.0)
# 1.9 模块
    import math
    math.floor(32.9)
    int(math.floor(32.9))
    math.ceil(32.9)
    from math import ceil
    cmath和复数：(complex math)复数：实数和虚数之和；
    cmath.sqrt(-1)
    (1+3j)*(9+4j);xj为虚数；
#1.10
#    test.py IDLE交互解释器;  F5; 
#1.11
    # string;
    "Let's go"
    '"Hello, world!" she said'
    'Let\'s say "Hello, world!"'
    "Let's say "'"Hello, world"'
    "Hello, "+"world!"

    # 字符串的转换输出方式：
    # 显示输出，与代码输出；

    # 1.str & repr 把值转化成字符串；
    str  以易阅读为目标；
    repr 标准python表达式；
    temp=42
    print "The temperature is "+repr(temp)  # 数字转化成字符串；

    # 2.input & raw_input
    
    # 长字符串、原始字符串、Unicode

    # 为解决跨行，定义长字符串''' """；
    print '''This is a long string.
    It continues here.
    And it's not over yet.
    "Hello, world!"
    Still here.'''
    """This is a long"""
    # 普通字符串也可跨行；
    print "Hello, \
    world!"

    # 为解决普通斜线与转移字符等特殊字符，定义原始字符串r''；
    path='c:\\Program Files\\aaa\\bbb'
    print r'c:\nowhere'
    print r'c:\program files\aaa\bbb'
    print r'This is error\'                 '
    print r'This is right''\\'
    print r'c:\programe files\aaa\bbb''\\'
    # c:\programe files\aaa\bbb\

    # Unicode   u''
    # python string is 8 byte; Unicode is 16 byte;
    >>>u'Hello, world!'
a





7. Page130-145
    类，对象：  对全局变量和函数的封装；
                装函数的字典；

7.2.2 父亲的礼物,签名前,的名字,对每个儿子都合适的称乎-self,this,it,me...代称；
      公共方法
    __metaclass__=type

    Class Person:
        
        def setName(self, name):
            self.name = name

        def greet(self):
            print "Hello, my name is %s" % self.name

    foo = Person()
    foo.setName("aa")

7.2.3 self参数正是方法和函数的区别；
    function(a,b)
    x.method(self,a,b) 
    x.func(a,b)         # 隐藏绑定；self绑定到所属对象上；

class Child(object):
    def __init__(self):
        pass
    
    def __aa(self):
        print 'this is myself.'

    def hello(self):
        self.call.hello()
        self.__aa()

son = Child()
son.hello()
son.__aa()


9. page156-183

10. page 183-






12.1 Page237-248























