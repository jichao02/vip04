#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/7 0007 15:52
#Author:chao

# f = open("E:\\2019.12.1\\vip4\data.txt",'w+')
# print(f.read())
# print(f.read(2))

# 获取整行
# print(f.readline())
# 获取所有的行，作为一个列表输出
# print(f.readlines())

# 写入文件内容，覆盖原有的内容，将字符串写入文件，返回的是字符串写入的长度
# seek 控制读的位置，不加则为结尾位置
# write 必须为字符串形式，多个字符串要为writelines
# f.write("Hello World\n")
# f.seek(0)
# m = ["Hello Python!!!"]
# f.writelines(m)
# f.seek(0)
# print(f.read())

# f.close()

with open("E:\\2019.12.1\\vip4\data.txt",'r+') as f:
    content = f.readlines()
    # print(content)

with open("E:\\2019.12.1\\vip4\\backup.txt",'w+') as f1:
    f1.writelines(content)
    f1.seek(0)
    print(f1.readlines())


list1 = []
list1 = str(f2).split( )
print(list1)


