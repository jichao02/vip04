#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/15 0015  15:59
#Author:chao
import requests
urlStr = 'https://www.wanandroid.com/user/login'
date = {"username": "jichao", "password": "123456"}
s = requests.session()
r1 = s.post(url=urlStr,data=date)

r2 = s.get('https://www.wanandroid.com/lg/todo/list/0')
print(r1.text)
print(r2.text)
