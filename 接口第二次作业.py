#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/8 0008 10:20
#Author:chao
# 第一题：



# 第二题：
# 定义一个类名：Student—学生、类内部含有一个属性：sno—学号，一个方法：study—学习，实现打印：学号为xx的学生，学习xx课程

# class Student(object):
#     def __init__(self,sno,course):
#         self.sno = sno
#         self.course = course
#     def study(self):
#         print("学号为"+self.sno+"的学生，学习"+self.course+"课程！")
# if __name__ == '__main__':
#     s = Student('123',"数学")
#     s.study()

# 第三题：定义一个Teacher类，继承Person类，拥有自身的属性工号：gh，自身的方法：teach教课（课程）；
# 1、实现gh为xx的老师，教xx课
# 2、实现gh为xx老师，在xx上班，一月工资xx
# 3、名字是xx，工号为xx的老师，吃饭

# from clas import Person
# class Teacher(Person):
#     def __init__(self, gh):
#         self.gh = gh
#     def teach(self,course):
#         self.course = course
#         print("工号为"+self.gh+",教"+self.course+"课！")
#     def makeMoney(self,add,wages):
#         self.add = add
#         self.wages = wages
#         print("工号为"+self.gh+",在"+self.add+"上班,一月工资"+self.wages)
#     def eat(self,name):
#         self.name = name
#         print("名字是"+self.name+",工号是"+self.gh+"的老师，吃饭")
# if __name__ == '__main__':
#     a = Teacher("123")
#     a.teach("数学")
#     a.makeMoney("北京","2000")
#     a.eat("张三")

# 第四题：打印小猫爱吃鱼，小猫要喝水
'''
分析步骤：
1、需要定义类--猫
2、类的属性和方法
   2.1 属性：无
   2.2 方法--吃鱼喝水
'''
# class Animal(object):
#     def __init__(self,name):
#         self.name = name
#     def eat(self,food):
#         self.food = food
#         print(self.name+"爱吃"+self.food)
#     def drink(self,water):
#         self.water = water
#         print(self.name+"爱喝"+self.water)
# if __name__ == '__main__':
#     s = Animal("小猫")
#     s.eat("鱼")
#     s.drink("水")

# 第五题：小明爱跑步，爱吃东西。
# 1、小明体重75.0公斤
# 2、每次跑步会减肥0.5公斤
# 3、每次吃东西体重会增加1公斤
# 4、小美的体重是45.0公斤
'''
1、需要定义的类：人
2、需要定义的属性：名字，体重
3、类所具有的方法：跑步，吃东西
'''
# class Exercise(object):
#     def __init__(self):
#         print("小明爱跑步，爱吃东西.")
#         print("每次跑步会减肥0.5公斤.")
#         print("每次吃东西体重会增加1公斤.")
#     def run(self,name,weight):
#         self.name = name
#         self.weight = weight
#         print(self.name+"的体重是"+self.weight+"公斤！")
# if __name__ == '__main__':
#     a = Exercise()
#     a.run("小明","75.0")
#     a.run("小美","45.0")

# 第六题：摆放家具
# 1、房子有户型，总面积和家具名称列表
#    新房子没有任何的家具
# 2、家具有名字和占地面积，其中
#    床：占4平米
#    衣柜：占2平米
#    餐桌：占1.5平米
# 3、将以上三件家具添加到房子中
# 4、打印房子时，要求输出:户型，总面积，剩余面积，家具名称列表

'''
1、需要定义的类：房子，家具
2、房子的属性：户型、总面积、剩余面积、家具列表
3、房子的方法：添加家具
    3.1 剩余面积减少（家具的占地面积）
    3.2 家具的列表增加一个家具
4、家具的属性：名称，占地面积
5、家具的方法
'''

# class Furniture(object):
#     def __init__(self,name,mianji):
#         self.name = name
#         self.mianji = int(mianji)
#     def totle(self):
#         print(self.name+"：占"+self.mianji)
# class Home(Furniture):
#     def __init__(self,area,furniture):
#         self.area = area
#         self.furniture = furniture
#     def baifang(self,house_type):
#         self.house_type = house_type
#         if self.house_type == "new_house":
#             print("新房子的面积是" + self.area + ",无家具")
#         else:
#             shengyu = self.area - Furniture.totle()
#             print("旧房子的面积是" + self.area + "，剩余面积是" + shengyu + ",家具名称列表是：" +
#                   Furniture.name)
# if __name__ == '__main__':
#     a = Home().totle()
#     a.baifang("new_house")

# 第七题：士兵开枪
# 1、士兵瑞恩有一把AK47
# 2、士兵可以开火(士兵开火扣动的是扳机)
# 3、枪 能够 发射子弹(把子弹发射出去)
# 4、枪 能够 装填子弹 --增加子弹的数量

'''
分析步骤：
1、需要定义的类：士兵、枪
2、士兵的属性：瑞恩
3、士兵的方法：开火
4、枪的属性：AK47、子弹数量
5、枪的方法：发射子弹、装填子弹
'''
class Weapons(object):
    def __init__(self,leixing):
        self.leixing = leixing
    def __str__(self):
        print("这把枪是"+self.leixing)
    def fashe(self):
        print("枪能够发射子弹")
    def zhuangtian(self):
        print("枪能够装填子弹")
class Soldier(Weapons):
    def __init__(self,name):
        self.name = name
    def fire(self):
        print(self.name+"开枪")

a = Soldier("肖恩")
a.fashe()
a.zhuangtian()
a.fire()
b = Weapons("AK47")
print(b)
# 第八题：有这样一个文件，文件内容如下：
# Lucy|18601914231|男|19890218
# Jack|18101913132|女|19810311
# Tom|18201912533|女|19830713
# Lily|18301911734|男|19870210
# 任务1-找出所有L开头的人名
# 任务2-按照年龄进行排序
# 任务3-找出所有女性用户的信息


# 第九天：目录下有这些文件：
# A1.txt
# B2.txt
# C1.doc
# D1.excel
# 任务1-将该目录下的文件按照后缀进行分类，然后分别新建且放入不同的文件夹内，比如txt文件放入txt目录下等

# import os       # 用于处理文件和目录
# import shutil   # 用于拷贝文件
# path = "D:\selenium\BeautifulReport\\tests"
# files = os.listdir(path)         # 返回path指定的文件夹包含的文件名字的列表
#
# for f in files:
#     # 取得当前文件名称的格式，（切分文件名，取最后的列表元素）
#     folder_name = 'D:\selenium\BeautifulReport\\tests\\' + f.split('.')[-1]    # 若没有\\，则新建文件夹为tests文件夹同级
#     f_path = "D:\selenium\BeautifulReport\\tests\\"+f      #  告知f所在的路径，否则找不到f
#     if not os.path.exists(folder_name):
#         os.makedirs(folder_name)                           #  创立文件夹
#         shutil.move(f_path,folder_name)                    #  将tests文件夹里的文件按类型移动到相应文件夹中
#     else:
#         shutil.move(f_path,folder_name)
