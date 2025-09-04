#!/bin/python3
import os,sys
from datetime import datetime

# Display dir sorted by x:
# by name, mtime, ctime, size, digits,




# Order List

file_path="./."
file_path='./test'
file_path="../moves/d7"
#file_path=input("Please input the File Path: ")

def ordlist(file_path):
    """
    Order List
    os.listdir(),return random order, so...
    custorm sorted by attribution: mtime, ctime, name, size
    """
    dir_list=os.listdir(file_path)
    if not dir_list:
        return
    else:
        # getmtime()
        # getctime()
        # getsize() 
        # dir_list=sorted(dir_list,key=lambda x: os.path.getmtime(os.path.join(file_path,x)))
        # ord(x[-5]), unicode order
        # int(x[9:-4]), order by part of digit.按name的数字部分排序。
        # 屏幕截图13.png, int(x[4:-4]) need change by actuality,  
        # ****3E18****, 
#       dir_list=sorted(dir_list, key=lambda x:(int(x[34]),int(x[36:-22])))
        dir_list=sorted(dir_list, key=lambda x:(int(x[40:-22])))
        return dir_list

'''
# 寻找文件名中需要截取字段的号码
for file in ordlist(file_path):
#   print(file,file[36:-22] ) 
    print(file[38],file[36:-22], "***"+file[36:-22]+".中英字幕.WEB-HR.AC3.1.mkv")
sys.exit()
'''


for file in ordlist(file_path):
    print(file)

print(60*"-")
print('''The Order is right?
      Y to rename,
      N to break and fix it.''')
user_input=input()
if user_input=='n':
    sys.exit(0)

print('Now to rename...')


# Rename


for file in ordlist(file_path):
    print('将要命名为：')
#   print(file[36:-22],'-->', "***"+file[36:-22]+".2020.中英字幕.WEB-HR.AC3.1.mkv")
    print(file[36:-22],'-->', "***"+file[36:-22]+".2020.中英字幕."+ file[48:])
#   break
#sys.exit()



print(60*"-")
print('''The Name is right?
      Y to rename,
      N to break and fix it.''')
user_input=input()
if user_input=='n':
    sys.exit(0)

print('Now to rename...')

'''
# 创建实验文件
#file=file.replace('.txt', '.md')
#字符串常量
file_path='../moves/1'


for file in os.listdir(file_path):
    print(file)
    f=open('./test/'+file, 'w')
    f.close()
#   sys.exit()
'''


#sys.exit()

for file in ordlist(file_path):
#   new_name="***"+file[36:-22]+".2020.中英字幕.WEB-HR.AC3.1.mkv"
    new_name="***"+file[36:-22]+".2020.中英字幕."+file[48:]
    print(file[36:-22],'-->', new_name)
    old_path=os.path.join(file_path, file)
    new_path=os.path.join(file_path, new_name)
    dest_path=os.path.join(file_path, new_name)
    if not os.path.exists(dest_path):
        os.rename(old_path, new_path)
    else:
        print(f"Pass: {new_name} is already exist.")

print("Rename was done.")
 


'''
# rename
folder="./"
for index,filename in enumerate(os.listdir(folder), start=1):
    print(index,filename)
    if filename.endswith('.txt'):
        mtime=os.path.getmtime(filename)
        hmtime=datetime.fromtimestamp(mtime).strftime("%Y%m%d")
        new_name=f"note_{hmtime}_{index:03d}.txt"
        print(new_name)
        old_path=os.path.join(folder, filename)
        new_path=os.path.join(folder, new_name)
        dest_path=os.path.join(folder, new_name)
        if not os.path.exists(dest_path):
            os.rename(old_path, new_path)
        else:
            print(f"Pass: {new_name} is already exist.")

'''

'''
x=[0,1,2,3,4,5,6,7,8,9]

x=list(range(10))
print(x[-4]) # 6              第4个数，
print(x[:-4]) # [0,1,2,3,4,5] 第5个数，
print(x[3:-4]) # [3,4,5]

y=['截图屏幕10','截图屏幕2','截图屏幕12','截图屏幕1','截图屏幕9','截图屏幕3',]
y.sort(key=lambda x:int(x[4:])) # sort by cuted digit part.
print(y)

'''
'''
# lambda x 表示一个匿名函数，x是列表中的原素.
c=[('b',4,2), ('a',6,1), ('c',5,3)]
print(sorted(c, key=lambda x: x[2]))

'''

'''
Unicode Order:  ['*', '.', '2', 'A', 'a', '。', '你']
characters=['你','a','A','2','*','.','。']

sorted_characters=sorted(characters, key=lambda c: ord(c))
print("Unicode Order: ", sorted_characters)

'''








