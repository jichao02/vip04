#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date: 2019/12/1 0001 17:01
#Author:chaochao

s = {'a':10,'b':20,'c':15}
s1 = {1,2,3,4,5,6,7}
s1.add(55)
print(s1)
s1.remove(3)
print(s1)

s['d'] = 12
print(s)
del s['b']
print(s)

s2 = list(s.values())
s2.extend(list(s1))
print(s2)

'''
集合和字典的区别：
相同点：无序的，不能通过下表引用，都是大括号
不同点：字典是键值对，集合是单个
'''

