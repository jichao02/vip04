#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/7 0007 11:09
#Author:chao

# list1 = [i*i for i in range(1,11)]
# print(list1)
#
# list2 = [i**2 for i in range(1,11) if i%2==0]
# print(list2)
#
# list3 = [[1,2,4],[4,2.4],[6,8,3]]
# list4 = [j**2 for i in list3 for j in i if j%2==0]
# print(list4)
#
list5 = [[1,2,4],[4,2,4],[6,8,3],[3,4]]
list6 = []
for i in list5:
    if len(i)>2:
        for j in i:
            if j % 2==0:
                list6.append(j*j)
print(list6)

list7 = [i for i in range(1,101) if i%2==0 and i%3==0]
print(list7)

list8 = []
for i in range(1,101):
    if i%2==0 and i %3==0:
        list8.append(i)
print(list8)
