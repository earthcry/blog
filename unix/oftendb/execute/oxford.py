#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''search dir for english word.'''

import sys

simfile='/home/nu/seldomdb/oxford/oxford_simple_txt'
searchdir='/home/nu/seldomdb/oxford'

# findword
def findWord0(keyword):
  '''find1'''
  import sys
  n=0
  filedata=open(simfile,'rU')
  for line in filedata:
    lineLst=[]
    lineLst=line.split()
    if lineLst!=[] and keyword!='' and keyword == lineLst[0]:
      for e in lineLst:
        print e
      break
    n+=1
  filedata.close()


# findword
def findWord(keyword,afile):
  '''find2'''
  filedata=open(afile,'rU')
  n=0
  bang=''
  tableLst=[]
  for line in filedata:
    if len(line)<20 and keyword==line.strip():
      bang=keyword
    if bang!='' and len(line)>20:
      print afile
      tableLst.append((bang,line))
      bang=''
    n+=1
  filedata.close()
  if len(tableLst)==1:          # only one line
    print tableLst[0][0]
    print tableLst[0][1]
  else:
    m=0
    for e,f in tableLst:        # many lines
      print e
      print f
      instr=raw_input('Continue to display Y or N: ')
      if instr.lower()=='n':break  
      m+=1

# iterate dirs find extFiles
def findExtFiles(searchdir,keyword,extname='.txt'):

  import os
  findedfiles=[]
  if '.' not in extname:extname='.'+extname
  dirNum=0
  for pathdir,layerDirs,files in os.walk(searchdir):
    for afile in files:
      if os.path.splitext(afile)[1]==extname and \
                   afile[0].lower()==keyword[0]:      # filename keyword
        afile=os.path.join(pathdir,afile)
        findedfiles.append(afile)
    dirNum+=1
  return findedfiles

def main():
  print '*'*76
  keyword=sys.argv[1]

  findWord0(keyword)

  fileslst=findExtFiles(searchdir,keyword,'txt')
  for afile in fileslst:
    findWord(keyword,afile)
  print '*'*76

if __name__=="__main__":
  main()
