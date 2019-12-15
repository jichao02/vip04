#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/15 0015  16:51
#Author:chao

import requests
urlStr = 'https://www.wanandroid.com/user/login'
date = {"username": "jichao", "password": "123456"}
r = requests.post(url=urlStr,data=date)
header = {'Cookie':'JSESSIONID='+r.cookies['JSESSIONID']}
# c = {'JSESSIONID':r.cookies['JSESSIONID']}


r1 = requests.get('https://www.wanandroid.com/lg/todo/list/0',headers=header)

result = r.text.find('测试')
print(r1.text)
print(result)
