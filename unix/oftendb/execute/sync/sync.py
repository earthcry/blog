#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Filename:sync.py
# at once sync both dirs until to both same.

# question: sync dirs
#           .paths.txt and .files.txt in subdir & them in superdir 
#           in pathStr, in fileStr, b.txt in rmb.txt.

# logic: concept and logic is very clear.
# base thought: 
#    start at root dir layer, sync one layer finished, then next layer, every layer only sync dir util all finish, then sync files layer by layer.

# update
'''
  logicImage

safety
  log.txt
  shutil.move()


'''
import sys
import os
import shutil
import datetime


# file==path+'/'+filename
# dir==folder or dir==path
dirA='/home/nu/oftendb'        # will sync dirA
#dirA='/home/nu/seldomdb'     
dirB='/home/nu/android'        # will sync dirB

if len(sys.argv)>1:
  dirA=sys.argv[1]             # may accept cmdline param, that may sync diff dir

if len(sys.argv)>1:
  dirB=sys.argv[2]


pathtxtname='.paths.txt'       # for judge path is oldExists or newAdd, will put the file in dirA.
filetxtname='.files.txt'       # for judge file is oldExists or newAdd, will put the file in dirA.
rmed='/home/nu/rmed'           # deleted file will put down this dir.
both='/home/nu/bothmodify'     # the file in dirA and dirB, if both modified, them will been put down this dir.
android='android'              # if sync to android, for a jugde sign. because android os permisson denied, can not modify mtime&permisson, over sync , again copy back to linux for same mtime.through sshelper link android.

print '*'*76
pathtxt=dirA+'/'+pathtxtname   #.paths
filetxt=dirA+'/'+filetxtname   #.files

def mtime(aFile):
  mtimestamp=os.path.getmtime(aFile)
  mtime=datetime.datetime.fromtimestamp(mtimestamp).strftime('%Y%m%d%H%M%S')
  return mtime


def copytree(dirA,dirB):
  '''only use to copy dir from linux to android.
     A='/home/nu/tmp/a/aa'   true exists 
     B='/home/nu/tmp/b/aa'   not exists
     copy 'aa' from A to B.
     '''
  print 'make dir '+dirB
  os.makedirs(dirB)

  for i in os.listdir(dirA):
    srcItem=os.path.join(dirA,i)
    dstItem=os.path.join(dirB,i)
    if os.path.isdir(srcItem):          #/home/nu/tmp/a/aa/abc
      print srcItem+' is a dir'
      dstItem=srcItem.replace(dirA,dirB) #/home/nu/tmp/b/aa/abc
      copytree(srcItem,dstItem)
    elif os.path.isfile(srcItem):
      shutil.copyfile(srcItem,dstItem)
      print 'Copy '+srcItem+' to '+dstItem
    else:
      print 'not a file and not a dir'


def copystat(dirA,dirB):

  for i in os.listdir(dirA):
    srcItem=os.path.join(dirA,i)
    dstItem=os.path.join(dirB,i)
    if os.path.isdir(srcItem):           #/home/nu/tmp/a/aa/abc
      print srcItem+' is a dir'
      dstItem=srcItem.replace(dirA,dirB) #/home/nu/tmp/b/aa/abc
      copystat(srcItem,dstItem)
    elif os.path.isfile(srcItem):
      shutil.copystat(srcItem,dstItem)
      print 'Copy State '+srcItem+' to '+dstItem
    else:
      print 'not a file and not a dir'



# dir to list&dict
def dir2lst(aDir): 
  '''lst.sort by length, os.walk order by charactor and a dir recur to deep'''
  lst=[]
  for path,dirs,files in os.walk(aDir):
    length=len(path)
    lst.append((length,path,dirs,files))
  lst.sort()
  return lst
def dir2dct(aDir):
  dct={}
  for path,dirs,files in os.walk(aDir):
    dct[path]=(dirs,files)
  return dct

# read&write paths&files
def path2str(aDir):
  pathStr=''
  for path,dirs,files in os.walk(aDir):
    pathStr+=path+'\n'
  return pathStr
def file2str(aDir):
  fileStr=''
  for path,dirs,files in os.walk(aDir):
    files.sort()
    for afile in files:
      aafile=os.path.join(path,afile)
      fileStr+=str(mtime(aafile))+','+aafile+'\n'
  return fileStr
def str2txt(aStr,aFile):
  f1=open(aFile,'w')
  f1.write(aStr)
  f1.close()
def readtxt(aFile): 
  '''txt2str'''
  aStr=''
  f1=open(aFile,'rU')
  aStr=f1.read()
  f1.close()
  return aStr
def readfiles(aFile):
  '''txt2dct'''
  dct={}
  f1=open(aFile,'rU')
# print f1.read()
  if len(f1.read())<10:
    return dct
  f1.seek(0)
  for line in f1:
    mtime,path=line.strip().split(',',1)  # 按第一个逗号分割。
    dct[path]=mtime
  f1.close()
  return dct


def mvfile(aafile,aDir):
  '''move a file to a dir, deleted or bothmodify'''
  if aafile[0] == '.':
    mfile=str(mtime(aafile))+('o'+aafile[1:]).replace('/','_')
  elif aafile[0] == '/':
    mfile=str(mtime(aafile))+aafile.replace('/','_')
  else:
    print 'Path have a question.'
    return False
  maafile=os.path.join(aDir,mfile)
  print 'Move '+aafile+ ' to ' +maafile
  shutil.move(aafile,maafile)

def delTree(pathx):
  '''del a whole dir'''
  if os.listdir(pathx):
    count=0
    for path,dirs,files in os.walk(pathx):
      for aFile in files:
        aafile=os.path.join(path,aFile)
        print aafile
        if count < 3:
          if raw_input('Del the File Y or N: ').lower()=='n':
            return
        count+=1
        print 'Deled file '+aafile
        mvfile(aafile,rmed)
#       os.remove(aafile)
      for aDir in dirs:
        apath=os.path.join(path,aDir)
        delTree(apath)
    delTree(pathx)
  else:        
    print 'Deled dir '+pathx
    os.rmdir(pathx)
def substr(subLst,supStr):
  for substr in subLst:
    if substr in supStr:
      return substr
  else:
    return False

def doDirA(pathStr,didpath):
  '''process different dir than dirB in dirA, newAdd copy and deleted del'''
  lstA=dir2lst(dirA)
  dctB=dir2dct(dirB)
  print 'In dodirA'+'-'*20
  for item in lstA:
    pathA=item[1]

    # jump copied subdir
    subpath=substr(didpath,pathA)
    if subpath:
      print 'Jump subpath: '+ pathA+'-'*20
      continue

#   print pathA                         # pathA='/aaa/abc'
    pathB=pathA.replace(dirA,dirB)      # pathB='/bbb/abc'
    # del deleted path
    if pathB not in dctB and pathA in pathStr:
      delTree(pathA)
      didpath.append(pathA)
    elif pathB not in dctB and pathA not in pathStr:
    # copy new path
      print 'Copy '+pathA+' to '+pathB
#####
      if android in pathB:
        print 'Copy to android--------------------'
        copytree(pathA,pathB)
        print 'Copied to android.'
        print 'Copy State back to linux.'
        copystat(pathB,pathA)
      else:
        shutil.copytree(pathA,pathB)

      didpath.append(pathA)
      didpath.append(pathB)
  return didpath

def copymfile(aafile,bbfile):
  '''sync modified file'''
  print 'In copymfile'+'-'*20
  aamtime=mtime(aafile)
  bbmtime=mtime(bbfile)
  if aamtime < bbmtime:
    aafile,bbfile=bbfile,aafile
  print 'Copy modified '+aafile+ ' to ' +bbfile
  if os.path.getsize(aafile) < os.path.getsize(bbfile):
    if raw_input('The old file is bigger, Override the File Y or N: ').lower()=='n':
      print 'Uncopy'
      return False
  mvfile(bbfile,rmed)
  print 'old file moved.'+bbfile
  if android in bbfile:
    print 'Copy to android--------------------'
    shutil.copyfile(aafile,bbfile)
    print 'Copy State back to linux.'
    shutil.copystat(bbfile,aafile)
  else:
    shutil.copy2(aafile,bbfile)
  print 'Modifeid file copied.'

def delsameA(pathA,filesA,pathB,filesB,dct,bothM):
  '''sameNameFile: modified|unmodified'''
# print 'In delsameA'+'-'*20
  for fileA in filesA:
    if fileA == pathtxtname or fileA == filetxtname:
      continue
    if fileA in filesB:
      aafile=os.path.join(pathA,fileA)
      bbfile=os.path.join(pathB,fileA)
      aamtime=mtime(aafile)
      bbmtime=mtime(bbfile)
      if aamtime != bbmtime:
        filesB.remove(fileA)
        filesA.remove(fileA)
        # add in both dir new files and same name
        if aafile not in dct and bbfile not in dct and aamtime == bbmtime :
          continue
        elif aafile not in dct and bbfile not in dct and aamtime != bbmtime :
          bothM.append((aafile,bbfile))
          continue
        # modified in both dir
        if aamtime != dct[aafile] and bbmtime != dct[bbfile]:
          bothM.append((aafile,bbfile))
          continue
        # modified in any one
        copymfile(aafile,bbfile)
      else:
        filesB.remove(fileA)
        filesA.remove(fileA)
        delsameA(pathA,filesA,pathB,filesB,dct,bothM)
  return filesA,filesB,bothM

def dofileA(pathA,lst,pathB,fileStr):
  '''Del or copy diff files in all path'''
  for file1 in lst:
    if file1 == pathtxtname or file1 == filetxtname:
      continue
    aafile=os.path.join(pathA,file1)
    bbfile=os.path.join(pathB,file1)
    if file1 not in fileStr:
      print 'In dofileA'+'-'*20
      print 'Copy '+aafile+ ' to ' + pathB
      if android in pathB:
        print 'Copy to android--------------------'
        shutil.copyfile(aafile,bbfile)
        print 'Copy State back to linux.'
        shutil.copystat(bbfile,aafile)
      else:
        shutil.copy2(aafile,pathB)
    else:
      print 'In dofileA'+'-'*20
      print aafile
      if raw_input('Del the File Y or N: ').lower()!='n':
        print 'Deleted '+aafile
        mvfile(aafile,rmed)
#       os.remove(aafile)

def path2txt():
  strA=path2str(dirA)
  strB=path2str(dirB)
  pathstr=strA+strB
# print pathstr
  str2txt(pathstr,pathtxt)

def file2txt():
  strfileA=file2str(dirA)
  strfileB=file2str(dirB)
  fileStr=strfileA+strfileB
# print fileStr
  str2txt(fileStr,filetxt)


def syncFile(fileStr,didpath,dct):
  '''base: all dirs of dirA&dirB are same, ==first sync dirs.'''
  dctB=dir2dct(dirB)
  bothM=[] #bothModify
  print 'In syncFile'+'-'*20
  for path,dirs,files in os.walk(dirA):
    pathA=path

    # jump copied subdir
    subpath=substr(didpath,pathA)
    if subpath:
      print 'Jump subpath: '+ pathA+'-'*20
      continue

    pathB=pathA.replace(dirA,dirB)
    filesA=files
    filesB=dctB[pathB][1]
#   print pathA,filesA,dirs
#   print pathB,filesB,dctB[pathB][0]

    xfilesB,xfilesA,bothM=delsameA(pathA,filesA,pathB,filesB,dct,bothM)
    xxB,xxA,bothM=delsameA(pathA,xfilesA,pathB,xfilesB,dct,bothM)
    dofileA(pathA,xxA,pathB,fileStr)
    pathA,pathB=pathB,pathA
    dofileA(pathA,xxB,pathB,fileStr)
  return bothM

def mvBothM(bothM,both):    
  for item in bothM:
    aafile=item[0]
    bbfile=item[1]

    mvfile(aafile,both)
    mvfile(bbfile,both)



def main():
  global dirA
  global dirB

  # sure sync dir is exists.
  if not os.path.exists(dirA):
    print dirA+' is not exists.'
    return False
  elif not os.path.exists(dirB):
    print dirB+' is not exists.'
    return False

  # if not exists, create txt.
  if not os.path.exists(pathtxt):
    f1=open(pathtxt,'w')
    f1.close()
  if not os.path.exists(filetxt):
    f1=open(filetxt,'w')
    f1.close()

  # 1st sync only dirs to same in dirA&dirB
  pathStr=readtxt(pathtxt)
  didpath=[] # deleted or copied, use to not repeat process.
  #process different dir than dirB in dirA, newAdd sync and deleted del.
  didpath=doDirA(pathStr,didpath)
  dirA,dirB=dirB,dirA
  #process different dir than dirA in dirB, newAdd sync and deleted del.
  didpath=doDirA(pathStr,didpath)
  path2txt()

  # 2nd sync files in all same dirs.
  fileStr=readtxt(filetxt)
  dct=readfiles(filetxt)
  # in dirA&dirB, del same filename in bothside, and different: new copy, deleted del, modified in both dir turn to mvBothM().
  bothM=syncFile(fileStr,didpath,dct)
  # process modified files in both dir,
  mvBothM(bothM,both)
  file2txt()
  
  if bothM != []:
    for item in bothM:
      print item
    print 'upside files moved into '+both


if __name__=="__main__":
  main()




print '*'*76

'''> 
----LogicTree--------------
operate instance manually, then help by program.
from instance to abstract

??? sync dir: pcDir--usbDir == sync: dirA,dirB --> dirA==dirB
??? sync dir == copy diff(add,del,modify), copy file and copy dir(a group files)
  1:  sync nameLst 
      os.walk(dirA) -> namelst==pathLst,filesLst

      essence: copy diff(del,add,modify), let A == B.
      sync object split to part two: dirs & files == paths&files
      sync essence is file not dir, dir is a group files.
      sync dir == sync a group files

      11: sync: pathsA, pathsB 
        for path,dirs,files in os.walk(dirA):
          path



      12: sync: filesA, filesB


  2:sync physic dirs&files
     os.remove()
     os.rmdir()
     shutil.copy2()
     shutil.copytree()
     shutil.move() #move file or dir to des

sync
A:a,b,c  <-d,e
B:c,d,e  <-a,b

A==B
A:a,b,c,d,e
B:a,b,c,d,e

copy diff -->add


dirA,dirB == dctA,dctB == lstA,lstB
dct[path]=(dirs,files)
lst=[(length,path,dirs,files),(),()]
sycn dctA&dctB or lstA&lstB or lstA&dctB




----ConceptTree---------
print str(int)
os.listdir(adir)#not[]
lstExpress[i for...]
forin Lst,del item, recurFunc

editDir:
os.remove('./cc.txt')
os.rmdir('./cc')                    #dir must be empty.
shutil.copy2('./aa.txt','./bb.txt') # if bb.txt exists, override.cp file&state.
shutil.copytree('/a/aa','/b/aa')      # '/b/aa' dir must not already exist. 
shutil.move()


lst:
lst.remove(x)
lst.append(x)

path:
os.path.join(path,afile)
os.path.split(aafile)
path,afile=os.path.split(aafile) # '/home/nu','aa.txt'
aafile='/home/nu/aa.txt'

timestamp:

recursion:
  def func():
    if xxx:
      print a
    else:
      func()


<'''

'''
import sys
import getpass

# #复制文件
# shutil.copyfile("oldfile","newfile")       oldfile和newfile都只能是文件
# 创建多级目录：os.makedirs（"/Users/ximi/version"）
# 创建单个目录：os.mkdir（"project"）

# shutil.rmtree("dir")    空目录、有内容的目录都可以删
# 检验给出的路径是否真地存:os.path.exists()
os.path.isdir(x)

os.path.join(tar,filename)
os.listdir(src)
target = os.path.realpath(sys.argv[2])

username = getpass.getuser()
# 改变当前工作目录
os.chdir('/Users/' + username + '/Documents/client/myProj/')

# len(sys.argv)                # number of param
# sys.argv[0] --scriptname, sys.argv[1] --param1.
# >>>python sync.py aaa bbb



'''
