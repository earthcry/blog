
    core of python

1.3.12 字节统编译
1.5 run python mode:
        shell:   python >>>cmd
        script:  python xxx.py; ./xxx.py
        GUI
    run shell:
        $>python 
        $>ctrl+d
    run script:
    add python into system-search-path:
    #!/usr/bin/python; 
    #!/usr/local/bin/python; 
  * #!/usr/bin/env python; 
    #!/bin/env python; 
    whereis env; whereis python
    chmod +w xxx.py
    ./xxx.py
    
2.2 
  % 字符串格式运算符；%d, %s, %f, fload;
  >> 重定向输出；
  raw_input() return string,
    num=raw_input()
    print int(num)*2
  >>>help(raw_input)
  ???函数外做用户交互；

2.3 注释---文档字符串，'''xxx''';access at running, and auto doc;
  def myfunc():
    '''this is myfunc'''
    print 'myfunction'

2.4 + - * / // % ** ;传统除法int，浮点除法，取余，乘方；pow()

2.5 动态语言，不需预先声明变量； 
    增量赋值：先自乘10, 再赋值给自己；
    n=n*10
    n*=10, n+=1, n-=1;

2.6 number
    int, long, bool; float, complex(复数)

2.13 for range（），可迭代对象，序列，迭代器；
    print # 换行；  
    foo='abc'
    Loop index or loop item;
    for i in range(len(foo)):
      print foo[i], '(%d)' % i,

    for i, ch in enumerate(foo):
      print ch, '(%d)' % i,

    a(0) ,b(1), c(2)

2.14 列表解析
    squared = [x**2 for x in range(4)]
    for i in squared:
      print i,
    0, 1, 4, 9
    sqdEvens = [x**2 for x in range(8) if not x % 2]
    0, 4, 16, 36

2.15 handle = open(filename,'r')
    handle, 文件对象句柄；

2.16 错误检测，异常处理；try-except

2.18 类，是相关数据及逻辑的容器；

    class ClassName(base_class):
      "optional documentation string"
      static member_declarations
      method_declarations

    self 自身的引用  other language this.

2.19 模块是一种组织形式，将彼此有关系的代码，组织到一个个独立文件中；

3.2 变量赋值，python是将对象的引用赋值给变量；
    链式赋值：
    y=x=x+1
    增量赋值：x+=1; x=x+1;
    多元赋值multupl：
    x,y,z = 1,2,'abc'
    x,y = y,x

3.3 标识符：
    _xxx        不用导入；
    __xxx__     系统定义名字；
    __xxx       类中的私有变量名；

3.4 obj.__doc__

3.4.1 模块结构和布局
#!/usr/bin/env python           #UNIX起始

"this is a test module"         #模块文档
"module.__doc__"

import sys                      #导入模块(all)
import os

debug = True                    #声明变量(global)

class FooClass (object):        #定义类
    "Foo class"
    "class.__doc__"
    pass

def test():                     #定义函数
    "test function"
    "module.function()"
    "function.__doc__"
    foo = FooClass()

    if debug:
      print 'run test()'

if __name__ == '__main__':      #主程序
    test()

    __name__
    if module is import: __name__ == module.name
    if module is exec:   __name-- == __main__

3.6 ? First program

3.7 tools
    PEP8
    Python快速参考
    Python常见问答
    Debugger: pdb
    Logger: logging
    Profiles: cProfile

4.1 Python对象三特性：
        Id(),Type(),Value;

4.2 标准数据类型：
        Num,    int,bool,long; float,complex;
        Str
        List    tuple
        Dict

4.3 other type:
        Type    type(42) type(type(42))
        Null obj (value=None)
        Collection
        Function/Method
        Class
        Module
        File

4.3.2 Bool
      False
        None
        Num=0
        0
        0L
        Float
        0.0+0.0j
        ""
        []
        ()
        {}
      True other
 
4.4 ? 内部类型

4.5 3<4<7 # same as (3<4) and (4<7)
    a == b : value == value
    a is b : id(a) == id(b)
    
    赋值 == 创建对象；
    a = 1
    id(a)       # 8402824
    b = 1
    id(b)       # 8402824 不重复创建对象
    o
    c = 1.0
    id(c)       # 8651220
    d = 1.0     
    id(d)       # 8651204
    整形对象和字符串对象是不可变对象，Python会高效缓存；

4.6 cmp(4, 8)   # -1
    cmp(8, 4)   # 1
    cmp(8, 8)   # 0

    Python2.2统一了类型和类；

4.6.4 ? type() isinstance()

4.7 工厂函数，类型，类，内建函数；
    int(), long(), float(), complex()
    str(), unicode(), basestring()
    list(), tuple()
    type()
    调用它们就产生一个实例；

    dict()
    bool()
    set(), frozenset()
    object()
    classmethod()
    staticmethod()
    super()
    property()
    file()
    
5.4 complex = real + imagj

5.5 重载+
    4.0**-1.0   # 0.25

5.5.4 ? *位运算符

6.1 s = 'abcdefgh'
    s[::-1]  # 翻转
    s[::2]   # 隔一个取一个；

6.1.2 ??? prgrm: 字符串的末尾递减显示；

6.1.3 浅拷贝，only copy 索引，没重建对象；

6.2 del char and string
    astr='Hello World!'
    astr=astr[:3] + astr[4:]
    astr        # 'Helo World!'
    astr=''
    astr        # ''

6.3.2 ??? prgrm idcheck.py
    性能：不重复计算
    'aa' 'bb' == 'aabb'
    'http://' 'xxx' 

    Unicode string:
    'aa' + u'bb' == u'aabb'

    '*'*40      # *************************************

6.4 ??? 格式化操作符
6.4.2 string.template ${}

6.4.3 原始字符串r
    print r'\n'         # \n
    f = open(r'c:\windows\temp\readme.txt', 'r')
    f.close()

    ur'Hello\nWorld'

6.5 enumerate()
    s = 'foobar'
    for i,t in enumerate(s):
        print i,t
    0 f
    1 o
    2 o
    3 b

    zip()
    s, t = 'foa', 'obr'
    zip(s,t)
    [('f','o'),('o','b'),('a','r')]

















