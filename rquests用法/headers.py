#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/15 0015  15:12
#Author:chao

import requests,json
urlstr = 'https://www.wanandroid.com/user/login'

date = {"username": "jichao", "password": "123456"}
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36"}

p = requests.post(url=urlstr, data=date, headers=header)

print(p.text)
# print(p.json()['data']['admin'])
if p.status_code == 200:
    if p.json()['errorCode'] == '0':
        print('登录成功')
    if p.json()['errorCode'] == '-1':
        print('登录失败')
else:
    print('接口错误')



