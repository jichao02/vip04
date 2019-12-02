#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date: 2019/12/1 0001 14:55
#Author:chaochao

'''
常量：固定不变
变量：分类型
无头文件、无主函数、无大括号、无分号，简洁
不需要定义类型、靠缩进区分语句
服务器不支持任何中文（Linux）

'''

a = 1
b = 2.5
c = "happy"

# 输出函数
print(type(a))
print(type(b))
print(type(c))
print(a,b,c,'三个变量')

# 查看数据类型
type(a)

# 输入函数（不管输入什么类型，均保存为str类型）
# a = input('请输入一个值：')
# print('a的值为：',type(a))

# a,b = input('请输入两个值：').split(',')
# print('a和b的值：',a,b)

# d是整型，s是字符串，f是浮点型（默认小数点后6位）
# 格式化输出：%03d----001    %.2f----75.50
a = 3
b =1.5
print('a的值为%d，b的值为%s'%(a,b))
print('a的值为{}，b的值为{}'.format(a,b))
print(f'a的值为{a}，b的值为{b}')
print('a的值为：%03d'%a)
print('b的值为：%.2f'%b)



'''
tuple：内的值不可以改变
list：内的值可以改变
与数组不同的地方：1、括号2、元素类型
'''

# list = (1,2,3,4,5,6,7,8,9)
# print(list[-3])
# print(list[3:8:2])

list1 = range(10)
list2 = range(1,10)
list3 = range(1,10,2)
print(list1,list2,list3)

print(list(range(9)))
print(list(range(2,9)))
print(list(range(2,9,3)))