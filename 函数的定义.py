#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/7 0007 13:42
#Author:chao


# 1、位置参数
# 函数的定义
'''
def add(a,b):
    print(int(a)+int(b))
def sub(a,b):
    print(int(a)-int(b))
def cheng(a,b):
    print(int(a)*int(b))
def chu(a,b):
    if int(b) != 0:
        print(int(a)/int(b))
    else:
        print('注意：除数不能为0！！！')
x = input('请输入第一个数:')
z = input('请输入方法：')
y = input('请输入第二个数：')
if z == '+':
    add(x,y)
elif z == '-':
    sub(x,y)
elif z == '*':
    cheng(x,y)
elif z == '/':
    chu(x,y)
'''

# 2、默认参数
# def add(a,b=1):
#     return a+b
# add(1,5)
# 默认参数指向不可变对象
'''
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())
print(add_end())
'''
# 3、可变参数，用于接收元组  *args    允许你传入0个或任意个参数    也可以使用已有列表作为入参传入
# def add(*args):
#     print(args)

# list1 = (1,12,3,4)
# add(*list1)

# 4、关键字参数，用于接收字典、字符串    **kwargs
def add(**kwargs):
    print(kwargs)

dict1 = {'name':'jichao','age':'18'}
add(**dict1)