#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/1 0001 18:35
#Author:chao

# 1、求10的阶乘

# n = 1
# sum = 1
# while n <= 10:
#     sum = sum*n
#     n+=1
# print(sum)

# 2、求100以内能被3整除的数，并将作为列表输出

# list = []
# for n in range(1,101):
#     if n%3==0:
#         list.append(n)
#     else:
#         n+=1
# print(list)

# 3、列表[1,2,3,4,3,4,2,5,5,8,9,7],将此列表去重，得到一个唯一元素的列表

# list = [1,2,3,4,3,4,2,5,5,8,9,7]
# new_list = []
# for n in list:
#     if n not in new_list:
#         new_list.append(n)
# print(new_list)

# 4、求斐波那契数列 1 2 3 5 8 13 ……
# list = []
# for n in range(1,10):
#     if n==1 or n==2:
#         list.append(n)
#     else:
#         list.append(list[n-3]+list[n-2])
# print(list)

# 5、求10000以内的质数
list = []
for n in range(2,101):
    for m in range(2,n):
        if n%m==0:
            break
    else:
        list.append(n)
print(list)


