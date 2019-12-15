#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/15 0015  14:44
#Author:chao

import requests,json
urlstr = 'https://www.wanandroid.com/user/login'

date = {"username":"jichao","password":"123456"}

print(type(date))
p = requests.post(url=urlstr,data=date)

print(type(p.text))
print(type(p.json()))


# 入参和出参格式没有关系

# 当post要求入参为json，可以用dumps   json=