#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date: 2019/12/1 0001 17:27
#Author:chaochao

# list = [1,4,2,5,6,3,23,7]
# a = int(input('请输入一个值：'))
# if a in list:
#     print('happy')
#     num = list.index(a)
#     list[num]+=1
#     print(list)
# else:
#     print('not happy')

num = int(input('输入你的分数：'))
if num > 100:
    print("请输入正确分数！！！")
else:
    if num >= 90:
        print("A")
    elif 80 <= num <90:
        print("B")
    elif 70 <= num <80:
        print("C")
    elif 60 <= num <70:
        print("D")
    else:
        print("E")
