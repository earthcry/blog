#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import requests # ? httplib,urllib
import string  
import time  
import hashlib  # ? md5 
import json  

class Youdao:
  def __init__(self):
    self.api_url="http://openapi.youdao.com/api"  
    self.appKey='16314322c4981d40'
    self.secretKey='3Z4KXkThLr34tAMvsctqJ9dI3eccCHs2'
    self.lower_case = list(string.ascii_lowercase)  
      
  def requests_for_dst(self,word):  
    #init salt and final_sign  
    salt = str(time.time())[:10]  
    final_sign = str(self.appKey)+word+salt+self.secretKey  
    final_sign = hashlib.md5(final_sign.encode("utf-8")).hexdigest()  

    #区别en,zh构造请求参数  
    if list(word)[0] in self.lower_case:  
      fromLang='EN'
      toLang='zh_CHS'
    else:  
      fromLang='zh_CHS'
      toLang='EN'

    paramas = {  
      'q':word,  
      'from':'%s'%fromLang, 
      'to':'%s'%toLang,  
      'appKey':'%s'%self.appKey,  
      'salt':'%s'%salt,  
      'sign':'%s'%final_sign  
      }  
    # my_url = api_url+'?appKey='+str(appKey)+'&q='+word+'&from='+fromLang+'&to='+toLang+'&salt='+salt+'&sign='+final_sign  

    response = requests.get(self.api_url,params = paramas).content  
    content = str(response,encoding = "utf-8")  # == response.read()
    json_reads = json.loads(content)  

    print('-'*78)
    print('Key:',json_reads['query'])  
    if list(word)[0] in self.lower_case:  
      print('US:',json_reads['basic']['us-phonetic'])  
      print('UK:',json_reads['basic']['uk-phonetic'])  
    print(json_reads['query'],':',json_reads['translation'])  
    print(json_reads['web'][0]['key'],':',json_reads['web'][0]['value'])  
    print('explains:',json_reads['basic']['explains'])  
    print(json_reads['web'][1]['key'],':',json_reads['web'][1]['value'])  
    print(json_reads['web'][2]['key'],':',json_reads['web'][2]['value'])  
    print('-'*78)

youdao = Youdao()           
while True:  
  word = input("Input words: ")  
  if word == 'q':
    break
  youdao.requests_for_dst(word)  



'''
# 3 engines: youdao, google, mymemory.translated.net
print '*'*76

from googletrans import Translator

translator = Translator(service_urls=['translate.google.cn',])
translations=translator.translate(['好','翻译','单词'],src='zh-CN',dest='en')
for translation in translations: 
  print translation.origin,' : ',translation.text

print translator.detect('good').lang #en
print '*'*76

'''


'''
yuanli:
  url+args
  args: q,from,to,appid,salt,sign,key

logic.baidu:
  account:appid/key

  http://api.fanyi.baidu.com/api/trans/vip/translate\
    ?q=apple&from=en&to=zh&appid=xxx&salt=xxx&sign=md5(appid+q+salt+key)

logic.youdao:
  http://openapi.youdao.com/api
  sign=md5(appid+q+salt+key)

#baidu demo
#/usr/bin/env python
# -*- coding:utf-8 -*-
import md5
import httplib
import urllib
import random

api_url="http://openapi.youdao.com/api"  
appKey='16314322c4981d40'
secretKey='3Z4KXkThLr34tAMvsctqJ9dI3eccCHs2'
 
httpClient = None
myurl = api_url
q = 'good'
fromLang = 'EN'
toLang = 'zh-CHS'
salt = random.randint(1, 65536)

sign = appKey+q+str(salt)+secretKey
m1 = md5.new()
m1.update(sign)
sign = m1.hexdigest()
myurl = myurl+'?appKey='+appKey+'&q='+urllib.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
 
try:
    httpClient = httplib.HTTPConnection('openapi.youdao.com')
    httpClient.request('GET', myurl)
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()

'''
'''
#init  
api_url="http://api.fanyi.baidu.com/api/trans/vip/translate"  
my_appid='20180122000117720'
cyber='jDm6O6T9kGcOeNeScIA2'
  
paramas = {  
  'from':'en',  
  'to':'zh',  
  'appid':'%s'%my_appid,  
  }  
my_url = api_url+'?appid='+str(my_appid)+'&q='+word+'&from='+'en'+'&to='+'zh'+'&salt='+salt+'&sign='+final_sign  

'''





