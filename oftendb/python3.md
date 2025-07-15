

python3





@可变参数 

#变量个数可变的参数

def abc(list):   #列表参数
  pass

def abc(*var):   #可变参数，*var == var1,var2, ... ,varn  表示多个参数。
  pass

abc(*listaa)     # *listaa == listaa[1] + listaa[2] + ... 把列表变成多个参数。
                 #  listaa = [ listaa[1]+listaa[2]+... ]


@function

def func():
  pass
  return 1,2

func(*var, **kw)

@typeswitch @类型转换
int()
float()
str()
bool()

@除法
10 /  3 = 3.33333  #浮点除
10 // 3 = 3        #地板除
10 %  3 = 1        #取余除


@关键字参数
def xxx(**kw):   # n个赋值
  pass

xxx(name='aaa',gender='m')
xxx(name='aaa',gender='m',age=32)

@命名关键字参数 @键值对参数
def aaa(name,*,gender,age,city='shanhai'):
  print(name,gender,age,city)

aaa('aaa',gender='m',age=33)

