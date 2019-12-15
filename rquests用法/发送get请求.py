#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/15 0015  13:37
#Author:chao
# 导入包
import requests
# 引用方法，完成get请求
urlstr = "http://www.wanandroid.com/article/query"
# 参数
params = {'k':'Android'}

r = requests.get(url=urlstr,params=params)
print(type(r.text))             # 字符串方式的响应体，会自动根据响应头部的字符编码进行解码
# print(r.status_code)
# print(r.encoding)         # 编码格式
# print(r.raw)              # 返回原始响应体
# print(r.headers)
# print(r.cookies)
#  json是独立




