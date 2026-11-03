#!/usr/bin/env python
# -*- coding:utf-8 -*-

# question: mkRecent


'''
DataStructure:
the date structure will been process.
a data file is saved many concept blocks. its format look like this.
"#" is not exists in format.
'''
#---a concept block--------------------------
#tags_: _@dog _@gou

#concept_: dog

#tree_:'''#>
#animal
#  wolf
#  dog
#<'''

#core_:'''>
#dog is ...
#<'''

#detail_:'''>

#<'''
#time_: 20180405143719
#----------------------------------
#or like this:
#----a nother concept block-----------------------------
#_@computer _@mobile
#computer is ...

#----------------------------------
'''
Algorithm:

dir -> files -> afile -> blockStrLst -> aBlkStr -> blkLstLst -> sort() -> number items -> str -> strs -> file


'''

import os,datetime,time,sys

readdir='/home/nu/Nutstore/oftendb/'
inFile='/home/nu/Nutstore/oftendb/recent.txt'
ext=('rmb','bk','rfr')
inDays=30
number=36  # concept block numbers

if len(sys.argv)>1:
  number=sys.argv[1]

def inDaysFiles(readdir,ext,inDays):
  '''Get fileLst of inDays & in ext'''
  fileLst=[]
  inDaysAgoStamp=time.time()-60*60*24*inDays #timestamp of a time ago
  for pathdir,layerdir,files in os.walk(readdir):
    for aFile in files:
      lst=aFile.split('.')
      if len(lst)>1:
        ext2nd=lst[-2]
        if ext2nd in ext:
          aFile=os.path.join(pathdir,aFile)
          filemtimestamp=int(os.path.getmtime(aFile))
          if filemtimestamp > inDaysAgoStamp:
            fileLst.append(aFile)
  return fileLst




def afile2blkStrLst(aFile):  
  '''Function: a file -> string list,
     Algorithm: a sting is start at '_@', end at '_@' of next line.
     '''
  blockStrLst=[]
  blockStr=''
  f1=open(aFile,'rU')
  bang=''                     # 接力棒
  for line in f1:
    if '_@' in line and bang=='':
      bang='_@'
      blockStr=blockStr+line
    elif bang=='_@' and '_@' not in line:
      blockStr=blockStr+line
    elif bang=='_@' and '_@' in line:
      blockStrLst.append(blockStr)
      blockStr=line
  f1.close()
  return blockStrLst

def aBlkStr2dct(aBlockStr):
  '''Function: oneConceptBlockStr -> Dct, return a str or a dct.
     dctKeys, tags,concept,tree,core,detail,time.
     '''
  
  astr=aBlockStr
  if 'tags_:' not in astr:
    return astr

  lst=astr.split('\n')
  dct={}
  bang=''
  for line in lst:
    #   _:
    if "_:" in line and "'''>" not in line:
      a,b=line.strip().split('_:') # ()() ->
      dct[a.strip()]=b.strip()     # ?time int

    #   _:'''>
    elif "_:" in line and "'''>" in line:
      bang="'''"
      a,b=line.strip().split('_:')
      b=''
    #  
    elif "_:" not in line and "'''>" not in line and "<'''" not in line  and bang=="'''":
      b=b+line+'\n'  # ?
    # <'''
    elif "_:" not in line and "<'''" in line and bang=="'''":
      dct[a]=b.strip()
      bang=''

  if 'tree' in astr:
    dct['tree']=dct['tree'].split('\n')

  dct['core']=dct['core'].split('\n')
  dct['detail']=dct['detail'].split('\n')

  aBlkDct = dct
     
  return aBlkDct


def aFile2DctLst(aFile,inDays):
  '''Function:
     Algorithm: collect the blocks withinDays.
     '''
  print aFile 
# if raw_input('Continue Y or N: ').lower()=='n':
#   return ''
 
  inDaysDctLst=[]
  inDaysAgoStamp=time.time()-60*60*24*inDays
  inDaysAgodate=datetime.datetime.fromtimestamp(inDaysAgoStamp).\
              strftime('%Y%m%d%H%M%S')

  blockStrLst=afile2blkStrLst(aFile)

# print 'length of strLst: ',len(blockStrLst)

  for aBlockStr in blockStrLst:
    aobj=aBlkStr2dct(aBlockStr)  # return str or dct
    if type(aobj)==str:
      astr=aobj
    else:
      dct=aobj
      if dct['time'] > inDaysAgodate:
        inDaysDctLst.append(dct)
  return inDaysDctLst
'''
  print 'length of dctLst: ',len(inDaysDctLst),
  if len(inDaysDctLst)!=0:
    print inDaysDctLst[0]['tags']
  else:
    print
'''





def lst2str(lst):
  lst=lst
  astr=''
  for i in lst:
    astr=astr+i+'\n'
  return astr.strip()

def dct2str(dct):
  aDct=dct
  aDctStr=''

  if 'tree' not in aDct:
    tree='empty' 
  else:
    tree=lst2str(aDct['tree'])

  core=lst2str(aDct['core'])
  detail=lst2str(aDct['detail'])
  aDctStr='-'*70+'\n'+\
          'tags_: '+aDct['tags']+'\n'*2+\
          'concept_: '+aDct['concept']+'\n'*2+\
          'tree_: '+"'''>"+'\n'+tree+'\n'+"<'''"+'\n'*2+\
          'core_: '+"'''>"+'\n'+core+'\n'+"<'''"+'\n'*2+\
          'detail_: '+"'''>"+'\n'+detail+'\n'+"<'''"+'\n'\
          'time_: '+aDct['time']+'\n'
  return aDctStr

    
def main():

  fileLst=inDaysFiles(readdir,ext,inDays)

    
  allInDaysDctLst=[]
  for aFile in fileLst:
    alst=aFile2DctLst(aFile,inDays)
    allInDaysDctLst.extend(alst)
  allDct=allInDaysDctLst


  tplDctLst=[]
  for dct in allDct:
    tplDctLst.append((dct['time'],dct))
  tplDctLst.sort(reverse=True)


  allDctStr=''
  n=0
  for tpl in tplDctLst:
    if n==number:break # not work when sys.argv?
    aDct=tpl[1]
    aDctStr=dct2str(aDct)
    allDctStr=allDctStr+str(n)+'/'+str(number)+aDctStr+'\n'
    n=n+1
  print n,

  f1=open(inFile,'w')
  f1.write(allDctStr)
  f1.close()

  print 'recent.txt writed success.'


if __name__=="__main__":
  main()


'''

#bak
def mtime(aFile):
  mtimestamp=os.path.getmtime(aFile)
  mtime=datetime.datetime.fromtimestamp(mtimestamp).strftime('%Y%m%d%H%M%S')
  return mtimestamp,mtime

#size=os.path.getsize(afile)
#mtimestamp=os.stat(afile).st_mtime
'''

