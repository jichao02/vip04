#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date: 2019/12/1 0001 16:17
#Author:chaochao

# s = [1,2,3,4,5,6,7]
# s.reverse()       # 改变原来列表的值
# s1 = [4,7,3,2,6,7,6,5]
# s1.sort()         # 改变原来列表的值
# print(sorted(s1))    # 不改变原来列表中的值，只返回一个排序结果
# print(s1)



'''
求该列表中的最大值，最小值及列表中一共有几个元素
获取56元素在列表的位置
追加元素7
删除元素0
排序列表（由大到小）
将列表[66,67,68]与原列表组合
'''


s = [11,13,0,5,7,56,23,34,72]
# print(max(s),main(s),len(s))
# print(s.index(56))
s.append(7)
print(s)
del s[s.index(0)]
print(s)

s2 = sorted(s)
s2.reverse()
print(s2)

s1 = [66,67,68]
s.extend(s1)
print(s)


