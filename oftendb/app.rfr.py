#!/usr/bin/env python
#coding: utf-8


###########################################################################
# _@csv
def dispCSV(filename):
  '''only display which you want '''
# Func to realize:
# 1.input filename


  import csv
  lstlst=[]
  rdfile=open(filename,'rU')
  csvReader=csv.reader(rdfile)
  for e in csvReader:
    lstlst.append(e)
    
  def overview():
    print 'csv file',filename,' over view:'
    print 'line max: ',len(lstlst)
    print 'fields:'
    for row in lstlst:
      if row == []:continue
      n=0
      for field in row:
        print n,field
        n+=1
      break
    print 
  overview()

  def disptable(rows=3,tpl=(0,1,3)):
    m=0
    for row in lstlst:
      if row == []:continue
      if m>int(rows): break
      for field in tpl:
        print row[int(field)],
      print 
      m+=1
  inpt=''
  inpt=raw_input('Do you want to display table? y or n :')
  while inpt.lower() == 'y':
    rows=raw_input('Enter rows numbers which to display:')
    cols=raw_input('Enter the columes numbers with space between them:')
    tpl=tuple(cols.split())
    print
    disptable(rows,tpl)
    print 
    inpt=raw_input('Do you want to display table? y or n :')
    overview()

  rdfile.close()

#dispCSV('workbook.csv')
#dispCSV('epaData2010.csv')


# _@wb
#############################################################################
# project: wb rootWord custom order
'''
x='a'
strName=''
while x!='z':
    strName=strName+rootName[x]
    x=chr(ord(x)+1)
print unicode(strName,'utf-8')
print '\n'

#_*_encoding:<>_*_    <>可以代笔：UTF8或cp936等编码。
# encoding=utf-8  unicode(strcn,'utf-8')

# more time : create object, display in cn.
# enjoy at upgradly realize. 愉悦在逐级实现。

rootName={'a':'工', 'b':'子', 'c':'又', 'd':'大', 'e':'月', 'f':'土', 'g':'王', \
        'h':'目', 'i':'水', 'j':'日', 'k':'口', 'l':'田', 'm':'山', 'n':'已', \
        'o':'火', 'p':'之', 'q':'金', 'r':'白', 's':'木', 't':'禾', \
        'u':'立', 'v':'女', 'w':'人', 'x':'幺', 'y':'言', \
        }
oneLtt={'a':'工', 'b':'了', 'c':'以', 'd':'在', 'e':'有', 'f':'地', 'g':'一', \
        'h':'上', 'i':'不', 'j':'是', 'k':'中', 'l':'国', 'm':'同', 'n':'民', \
        'o':'为', 'p':'这', 'q':'我', 'r':'是', 's':'要', 't':'和', \
        'u':'产', 'v':'发', 'w':'人', 'x':'经', 'y':'主', \
        }
rootWord={'a':('戈','七'), 'b':('耳','了','也'), 'c':('巴','巴'), 'd':('古','石','厂'), \
        'e':('力','臼'), 'f':('士','干','十','寸','雨'), 'g':('五','一'), \
        'h':('止','卜'), 'i':('小','小'), 'j':('曰','虫'), 'k':('川','口'), \
        'l':('四','车','甲'), 'm':('由','贝'), 'n':('巳','己','尸','心','羽'), \
        'o':('广','米'), 'q':('夕','儿'), 'r':('斤','手'), 's':('丁','西'), \
        'u':('门','门'), 'v':('刀','九'), 'w':('八','几'), \
        'x':('母','弓','匕'), 'y':('文','方') \
        }
'''
'''
sumlist=[]
sumlist.extend(rootName.values())
sumlist.extend(oneLtt.values())
sumlist.extend(rootWord.values())

def cltToStr(clt,shuffle):
    List=[]
    strClt=''
    if type(clt) is dict:               # if for more ...
        clt=clt.values()
    if isinstance(clt,list):
        for e in clt:
            if isinstance(e,tuple):     # list for more ...
                for ee in e:
                    List.append(ee)
            else:
                List.append(e)
    if shuffle=='y':
        import random
        random.shuffle(List)
    for e in List:
        strClt+=e
    return strClt

print cltToStr(rootName,'n')
print cltToStr(oneLtt,'n')
print cltToStr(rootWord,'n')
print cltToStr(sumlist,'n')
print '\n--------------------\n'
def strToFile(string,filename,t): # w a
    datafile=open(filename+'.txt',t)
    datafile.write(string+'\n')
    datafile.close()

    myFile=open(filename+'.txt','r')
    for line in myFile:
        print line
    myFile.close()

rootNameTitle='RootName: '
rootWordTitle='RootWord: '
oneLttTitle='OneLetter: '
shuffleTitle='Shuffle of RootName,RootWord,OneLetter: '
strToFile(rootNameTitle,'dict','w')

strToFile(cltToStr(rootName,'n'),'dict','w')
strToFile(cltToStr(oneLtt,'n'),'dict','a')
strToFile(cltToStr(rootWord,'n'),'dict','a')
strToFile(cltToStr(rootWord,'y'),'dict','a')
strToFile(cltToStr(sumlist,'y'),'dict','a')

'''

# _@random

#################################################################
# Question: Guess a random number.
'''
import random

rd=random.randrange(0,5)
    
def inputInt():
    inpt = raw_input('Number 0~100 : ')
    while not inpt.isdigit():
        inpt = raw_input('Error, only numbers please: ')
    inpt = int(inpt)
    return inpt

guess = inputInt()

print 

while 0 <= guess <= 100:
    if guess > rd:
        print 'Guess is too large.' 
    elif guess < rd:
        print 'Guess is too small.'
    else:
        print 'You get it .'
        break
    guess = int(raw_input('Please input a number 0~100: '))

else:
    print 'You outof number.bye.'

'''
# _@gui
###################################################
# Question:  GUI 
# simple GUI by Tkinter
# app    GUI by HTML5

'''
import Tkinter
top = Tkinter.Tk()

top.mainloop()

'''

###################################################
'''
from Tkinter import *
root = Tk()     # create backcolor of window object

lst = ['C', 'Python', 'PHP', 'HTML5', 'SQL', 'JAVA']
movie = ['CSS', 'jQuery', 'Bootstrap']

# create list zujian
lbx1 = Listbox(root)
lbx2 = Listbox(root)

# insert data into zujian
for i in lst:
  lbx1.insert(0, i)
for i in movie:
  lbx2.insert(0, i)

# zujian into window
lbx1.pack()
lbx2.pack()

# msg loop disp
root.mainloop()

'''
# _@pyside.py
#############################################
# pyside.py
'''
import sys
from PySide.QtCore import *
from PySide.QtGui import *

app=QApplication(sys.argv)
label=QLabel()

label.setText("Hello World!!!")
label.setWindowTitle("Hello")
label.setAlignment(Qt.AlignCenter)
label.setGeometry(300,300,500,175)

label.show()
app.exec_()
sys.exit()
'''
# _@
###############################################
'''
import os
def disp(path):
    reader=open(path)
    for line in reader:
        print line
    reader.close()

n=0
for dirname,subdirs,files in os.walk('.'):
    for efile in files:
        if efile=='ccc.txt':
            path=dirname+'/'+'ccc.txt'
            path=path.replace(r'\\','/')
            pring path
            break 
    print n,': ',
    print '-'*75
    n+=1
#    if n > 9:break
class FoundException(Exception): pass

try:
    for row,record in enumerate(table):
         for columu,field in enumerate(record):
               for index,item in enumerate(field):
                       if item == target:
                                 raise FoundException()
except FoundException:
      print ("found at ({0},{1},{2})".format(row,column,index))
else:
       print ('not found')

'''

# _@aeiou _@findWords searchWord
##################################################################################################
# Question:
# find the words which have order ('a', 'e', 'i', 'o', 'u') and include all.

# Analysis:
# take quest simply to a concept and resolve & transform to simple.
# 1.find words in file, article or dict.
# 2.words includding a,e,i,o,u.
# 3.order: a, e, i, o, u   ***
# file or article -->string
# string strip & replace --> list
# forin list --> word
# quest: if have a,e,i,o,u in order in the word. --> imaginal thinking,_@conceptionImage,iteration image
# quest: if a in the word. image/'imidg/ imaginal/i'madginel/
# Core:
# file -> string -> list -> a word.
# 1.right model: xaxxexxixoxxux   <--operate object, _@resultModel
# 2.judge 'a' if in xaxxexxixoxxux
# 3.judge 'e' if in   xxexxixoxxux.<--(e in xxx) & (e behand a)
# ...
# Thinking mode:
# question abstract a concept
# question resolve to parts
# question transform to ok
# question to simple
# core - imaginal thinking
# cube,virtual&actual
# resultModel,operateObject.

# Question:
# Analysis:
# Core:

def cleanwords(string):
  return string.strip().lower()

def haveaeiou(wword0):
  wword=wword0
  for ii in ('a','e','i','o','u'):
    if ii in wword:
      if ii == 'u':
         return wword0
         break
      idx=wword.index(ii)
      wword=wword[idx+1:]
    else:
      return False
      break
'''
lst=[]
filedata=open('dict.txt','r')
for line in filedata:
  wword0=cleanwords(line)
  haveaeiou(wword0)
  if haveaeiou(wword0) <> False:
    lst.append(haveaeiou(wword0))  
filedata.close()
print lst

'''
# _@wordsAnalysis _@fileAnalysis 
# Question:  fileAnalysis 
# 1.number of words, file length.
# 2.how many different words?

'''
def clean(e):
  for i in (',','.','-'):
    if i in e:
      e=e.replace(i,'')
#     e=e.lower() ?
  return e


lst=[]
filedata=open('address.txt')
for line in filedata:
  lst1=[]
  lst1=line.split()
  for e in lst1:
    e=clean(e)
    if e!='':
      e=e.lower()
      lst.append(e)
filedata.close()

print len(lst)

n=0
l=len(lst)
lst2=[]
while n<l:
  m=0
  for i in lst[n+1:]:
    if lst[n]!=i:
      m+=1
    if m==len(lst[n+1:]):
      lst2.append(lst[n])
  n+=1

print lst2
print len(lst2)



# _@mileage _@licheng _@table _@csv
'''
# example: 
# 行车里程 
# method1: index + oneDimension list
# method2: many Dimension list [(23,picar,car),(31,xxx,xxx),()]

# 1.0 Algo steps
# 0.0 Quest Analy, think process
# 0.1 root, real, split, trytest, core, frame, 
# 0.2 Analy quest condition, possible contrast judge
#       1.get operate object, display, analy struct.
#       2.question analy conditions,disp question object
#           1.maxMpg,minMpg,            MPG column
#           2.car-maxMpg,car-minMpg,    CAR column
#           3.disp question operate object
#       3.analy sulotion

'''
filedata=open('epaData2010.csv')
n=0
for line in filedata:
    print n,
    lstline=line.split(',')
    print '%-20s : %s' % (lstline[2],lstline[9])
    n+=1
    if n > 30 : break



filedata=open('epaData2010.csv')
n=0
mpg=[]
for line in filedata:
    lstline=line.split(',')
    print '%-20s : %s' % (lstline[2],lstline[9])
    if 'MPG' in lstline[9]:
        continue
    mpg.append(lstline[9])
    n+=1
    if n > 9 : break

print mpg
print max(mpg),min(mpg)
'''


# _@sheet _@table _@csv _@file
# question: mileage data
#       1.max mileage
#       2.min mileage
#       3.max model class
#       4.min model class

# object: epaData2010.data.csv
# structure:
'''
filedata=open('epaData2010.data.csv','rU')

n=0
for row in filedata:
  n+=1
  pass
print n
# 1248rows 

row1=filedata.readline()
row1lst=row1.split(',')
n=0
for i in row1lst:
  print n,i
  n+=1
# 30columns fields

n=0
for i in filedata:
  if 120<n<160:
    print n,i[:76]
  n+=1
# columns will use
# 0class,1MFR,2CAR LINE,9HWY MPG (GUIDE)

# mileagelist:
mileagelist=mlglst=[]
rowlst=[]
n=0
for row in filedata:
  if row[:5]=='CLASS' or 'VAN' in row or 'PICKUP' in row:continue
  rowlst=row.split(',')
  mlglst.append((int(rowlst[9]),rowlst[1],rowlst[2]))
  n+=1

# maxmileage,minmileage
print max(mlglst) # 45
print min(mlglst) # 12 
print '-'*70
# maxmileage and model,min...
maxmlglst=[]
minmlglst=[]

n=0
l=len(mlglst)
while n<l:
  if mlglst[n][0]==45:
    maxmlglst.append(mlglst[n])  
  if mlglst[n][0]==12:
    minmlglst.append(mlglst[n])  
  n+=1
print maxmlglst
for i in minmlglst:
  print i

filedata.close()

'''




# problemModel: _@grade _@sheet _@table _@csv
# question: lastGrade
# dataFile: grade.data.csv
# scene concept: weightAverage
#       lastGrade == weightedGrade == weightedAverageGrade
# algorithm:
#       cutMelon/breakParts thinkingMode.
'''
1.forin file
  1.1.input filename  
  1.2.forin file
2.name,lastgrade
  2.1.strr lst
  2.2.name,grade1,2,3;int 1,2,3
  2.3.compute grade
    2.3.1.gradelst,weightlst,
    2.3.2.g*w
3.display
  3.1.print name,weightgrade
'''


def weightedGrade(gradeLst,weights=(0.3,0.3,0.4)):
  '''weightedAverageGrade'''
  weightedGrade = gradeLst[0]*weights[0]+\
                  gradeLst[1]*weights[1]+\
                  gradeLst[2]*weights[2]
  return weightedGrade
'''
#filename=raw_input('Enter filename: ')
filename='grade.data.csv'
gradeLst=[]
filedata=open(filename,'rU')
for line in filedata:
  stulst=plst=line.split(',')
  stuname=plst[1]+' '+plst[0]
  stugrade=(int(plst[2]),int(plst[3]),int(plst[4]))
  gradeLst.append((stuname,weightedGrade(stugrade)))

filedata.close()

print '%-14s%10s' % ('Name','Grade')
print '-'*24
for e,f in gradeLst:
  print '%-14s %9.2f' % (e,f)

'''

# problemModel: _@wordsAnalisys _@fileAnalisys
# question: file analisys     P184 P241
# dataFile: address.data.txt

# subQuestions:
#       1.number of all words.       len()
#       2.words appear once.         notin or set()
#       3.number every word appear   find same as 1st, or dict[key]

# questionAnalisys:

'''
1.file->lst
  1.1.open,read line
  1.2.trip,split(' ',',','.')
2.len(lst)
3.set(lst),
4.wordTimes
'''

def art2lst(article):
  '''article to words list.\
       core: split->strip->lower'''
  import string
  f1=open(article,'rU')
  n=0
  wordsLst=[]
  for line in f1:
    strlst=line.split()
    for astr in strlst:
      astr=astr.strip(string.punctuation)
      if astr != '':
        word=astr.lower()
        wordsLst.append(word)
    n+=1
  f1.close()
  return wordsLst

def setedLst(lst):
  '''return unique element a list.\
       core: set method, or use 'not in' method. '''
  setedLst=[]
  set1=set(lst)
  for e in set1:
    setedLst.append(e)
  setedLst.sort()
  return setedLst

def uniqueLst(lst):
  '''return unique element list. core: not in.'''
  uniqueLst=[]
  for e in lst:
    if e not in uniqueLst:
      uniqueLst.append(e)
  return uniqueLst
'''
article='address.data.txt'
lst=['a','c','b','dd','e','b','a','a','b','c','b','a','b','e']
lst=art2lst(article)
'''
def itemTimes(lst):
  '''return a list which every item and times appeared in given list.
     _@core: find same as first element in given list, and recur.
  '''
  wordTimesLst=[]
  def findSame1st(lst):
    if lst!=[]:
      diffLst=[]
      sameLst=[]
      for e in lst[1:]:
        if lst[0] == e:
          sameLst.append(e)
        else:
          diffLst.append(e)
      wordTimesLst.append((len(sameLst)+1,lst[0]))
      lst=diffLst
      findSame1st(lst)

  findSame1st(lst)
  wordTimesLst.sort(reverse=True)
  return wordTimesLst

def wordsTimes(wordsLst):
  timesDct={}
  for word in wordsLst:
    if word not in timesDct:
      timesDct[word]=1
    else:
      timesDct[word]+=1
  return timesDct

def printDct(dct):
  '''print number value dict by turning to lstlst.'''
  valKeyLst=[]
  for key,val in dct.items():
    valKeyLst.append((val,key))
  valKeyLst.sort(reverse=True)
  m=0
  for val,key in valKeyLst:
    if m>=19:break
    print '%-19s %3d' % (key,val)
    m+=1

'''
itemTimesLst=itemTimes(lst)

n=0
for e,f in itemTimesLst:
  if n>=19:break
  print '%-12s %s' % (f,e)
  n+=1

'''
'''
print len(lst)
print len(setedLst(lst))
print len(uniqueLst(lst))
itemTimesDct=wordTimes(lst)
printDct(itemTimesDct)

'''

# _@searchFile
def searchFile(filename,keyword):

  '''search a File find keyword with detail'''

  f1=open(filename,'rU')
  bang='' # jielibang
  for line in f1:
    if keyword in line:
      bang=keyword
      print line,
    if bang==keyword and ('_@' not in line) and (keyword not in line):
      print line,
    if ('_@' in line) and (keyword not in line):
      bang=''
  f1.close()


# _@searchDirs
def searchDirs(searchdir,keyword,extname='.txt'):

  '''search treeDirs, return files with keyword in it.'''

  import os
  if '.' not in extname:
    extname='.'+extname

  for pathDir,layerDirs,files in os.walk(searchDir):
    findedFiles=[]
    for afile in files:
      if os.path.splitext(afile)[1]==extname:
        f1=open(afile)
        if keyword in f1.read():
          findedFiles.append(afile)
        f1.close()
  return findedFiles


# _@random _@randchar "随机字fu："
def randChar(n):
  '''n--length of random char.'''
  import random
  m=0
  sum=''
  if n%2==0:
    while m<n/2:
      sum+=chr(random.randint(65,90))+str(random.randint(0,9))
      m+=1
    return sum
  else:
    while m<(n-1)/2:
      sum+=chr(random.randint(65,90))+str(random.randint(0,9))
      m+=1
    return sum+str(random.randint(0,9))

