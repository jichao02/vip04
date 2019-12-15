#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/7 0007 15:18
#Author:chao

'''
异常处理
def chu(a,b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError:
        print('注意：除数不能为0')
a = input('输入第一个：')
b = input('输入第二个：')
chu(a,b)
'''

'''
获取原始异常信息
def chu(a,b):
    try:
        print(int(a)/int(b))
    except ZeroDivisionError as result:
        print(result)
a = input('输入第一个：')
b = input('输入第二个：')
chu(a,b)
'''

'''
exception后跟多个异常信息
def chu(a,b):
    try:
        print(a/b+c)
    except (ZeroDivisionError,NameError) as result:
        print(result)
a = int(input('输入第一个：'))
b = int(input('输入第二个：'))
chu(a,b)
'''
'''
# exception后跟多个异常信息
def chu(a,b):
    try:
        print(a/b+c)
    except Exception as result:
        print(result)
a = int(input('输入第一个：'))
b = int(input('输入第二个：'))
chu(a,b)
'''

'''
最终异常情况
def chu(a,b):
    try:
        print(a/b+c)
    except Exception as result:
        print(result)
    else:                           # 没有异常的时候才会执行
        print('程序执行成功)
    finally:                        # 没有异常和有异常都会执行
        print('程序执行结束')
a = int(input('输入第一个：'))
b = int(input('输入第二个：'))
chu(a,b)
'''


