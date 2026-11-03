#!/usr/bin/env python
# -*- coding:utf-8 -*-


### question: search @@keyDetail.

'''
 question1: logic frame for test or update or error or share
 question3: when find filename, display file dirtree/keys/concepts
 question2: more one blocks update, piliang ru ku.
 question4: have like keyes in same file, e.g. ssh sshelper
 update:20180322074614


first:
graph draw;

second:
logic math

thrd:
python code.

'''

### DataStructure:
'''
mang file saved blockes which have extent rmb,bk,rfr.

---
title: blank
indexing: false
toc: true
comments: true
date: 2022-03-01 09:11:56
updated: 2022-03-01 09:11:56
pic:
categories:
- [fruit, apple]
- [fruit, orange]
- [vegetable]
tags:
- markdown
- syntax
- md
---
#- 有[]平级, 无层级

tags_: @@xxx @@xxx
tree_: ''> 
categories:
- [fruit, apple]
- [fruit, orange]
- [vegetable]
<''                                                            
concept_:
core_:
detail_:
date_:
update_: YYMMDDHHMMSS


Edit_vim:
x_date
x_cbf

'''

### Algorithm:

'''
  fileLst of ext&key --> a file -> 3str --> a str -> dct -->  

0.key dir
1.fileLst:    find fileLst key in it in the dir
2.middleStr:  aFile -> 3str: frontStr, middleStr, backStr, keyInMiddleStr
3.cbDct:      mid -> dct,
4.display:    dct->astr
5.update:     mdl -> file, edit, new3str -> file.

'''

### Programe

print '*'*76

import sys


searchDir='/home/nu/Nutstore/oftendb'
#searchDir='/home/nu/tmp'
ext=('rmb','bk','rfr')

# searchDirs
def searchDirs(searchDir,keyword,ext):

  '''search treeDirs, return fileLst about ext&key'''

  import os
  keyword='@@'+keyword
  findedFiles=[]
  for pathDir,layerDirs,files in os.walk(searchDir):
    for afile in files:
      lst=afile.split('.')
      if len(lst)>1:
        ext2nd=lst[-2]
        if ext2nd in ext:
          afile=os.path.join(pathDir,afile)
          f1=open(afile)
          if keyword in f1.read():
            findedFiles.append(afile)
          f1.close()
  return findedFiles


def file23str(searchfile,keyword):
  ''' a file --> 3strings
      frontStr is at keyblock front str,
      middleStr is keyblock,
      backStr is keyblock back str.
      '''
  if '@@' not in keyword:
    key='@@'+keyword
  else:
    key=keyword
  searchfile=searchfile
  frontStr=middleStr=backStr=''
  middleLst=[]
  bang='front'   # jielibang

  f1=open(searchfile,'rU')
  if key not in f1.read():
    print 'Not in '+searchfile
    return frontStr,middleStr,backStr
  f1.seek(0)
  for line in f1:
    if len(line) < 2:
      continue
    elif bang=='front' and key not in line:  #only exe one in elif block
      frontStr=frontStr+line
    elif key in line:
      middleStr=middleStr+line
      bang=key
    elif bang==key and "@@" not in line and 'time_:' not in line:
      middleStr=middleStr+line

    elif bang==key and 'time_:' in line:
      middleStr=middleStr+line
      middleLst.append(middleStr)
      middleStr=''
      bang='back'
    elif bang=='back' and "@@" in line and key not in line:
      backStr=backStr+line
    elif bang=='back' and key not in line:
      backStr=backStr+line

  f1.close()
  length=len(middleLst)
  if length>1:
    print 'Concept Block number: '+str(length)

  return frontStr,middleLst,backStr


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


def lst2str(lst):
  lst=lst
  astr=''
  for i in lst:
    astr=astr+i+'\n'
  return astr.strip()

def dct2str(aDct):
  aDctStr=''
  if 'tree' not in aDct:
    tree='empty' 
  else:
    tree=lst2str(aDct['tree'])
  core=lst2str(aDct['core'])
  detail=lst2str(aDct['detail'])
  str1='tags_: '+aDct['tags']+'\n'+\
    'tree_: '+"'''>"+'\n'+tree+'\n'+"<'''"+'\n'+\
    'concept_: '+aDct['concept']+'\n'+\
    'core_: '+"'''>"+'\n'+core+'\n'+"<'''"+'\n'+\
    'detail_: '+"'''>"+'\n'+detail+'\n'+"<'''"+'\n'+\
    'time_: '+aDct['time']+'\n'
  return str1

def dispDetail(dct):
  dtl=dct['detail']
  dtlLen=len(dtl)
  print 'detail_: '+str(dtlLen)+' lines'
  if dtlLen <=5:
    print 'detail_:'+'\n'+lst2str(dct['detail'])
  elif dtlLen > 5 and raw_input('Display detail Y or N: ').lower()!='n':
    print 'detail_:'+'\n'+lst2str(dct['detail'])
  print '-'*70


def str2file(astring,infile='middleStr.txt'):
  astr=astring
  f1=open(infile,'w')
  f1.write(astr)
  f1.close()

def file2str(outfile='middleStr.txt'):
  f1=open(outfile,'r')
  middleStr=f1.read()
  f1.close()
  return middleStr


def main():
  files=searchDirs(searchDir,sys.argv[1],ext)
  for afile in files:
    print '%20s' % afile
    if raw_input('Display Y or N: ').lower()=='n':
      continue
    front,middle,back=file23str(afile,sys.argv[1])
    middleStr=''
    blocks=middle # block string list
    length=len(blocks)
    n=0

    for block in blocks:
      aObj=aBlkStr2dct(block)
      if type(aObj) == str:
        print aObj
        middleStr=middleStr+aObj
      else:
        dct=aObj

        if 'tree' not in dct:
          tree='empty' 
        else:
          tree=lst2str(dct['tree'])

        # Display
        if length==1:
          display='y'
        elif length>1:
          print dct['tags']
          display=raw_input('Display Y or N: ').lower()
        if display!='n':
          str1='-'*20+'\n'+\
            'tree_: '+"'''>"+'\n'+tree+'\n'+"<'''"+'\n'*2+\
            'tags_: '+dct['tags']+'\n'*2+\
            'concept_: '+dct['concept']+'\n'*2+\
            'core_: '+"'''>"+'\n'+lst2str(dct['core'])+'\n'+"<'''"+'\n'*2+\
            'time_: '+dct['time']+'\n'
          print str1
          dispDetail(dct)

        # Update
        strBlock=dct2str(dct) 
        if display!='n':
          if raw_input('Update Y or N: ').lower()!='n':
            str2file(strBlock)
            print 'This data writed in middleStr.txt, to edit and update it.'
            if raw_input('Edit ok? Y or N: ').lower()!='n':
              strBlock=file2str()
              n=n+1
        middleStr=middleStr+strBlock

    if n>0:
      #only update to rewrite file.
      middle=middleStr
      fileStr=middle+'\n'+front+'\n'+back+'\n'
      str2file(fileStr,afile)
      print 'Update Success'


if __name__=="__main__":
  main()



print '*'*76






