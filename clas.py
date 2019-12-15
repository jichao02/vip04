#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2019/12/7 0007 17:33
#Author:chao

'''
属性和方法可以为空，里面直接写pass即可，表示是一个空类
python2 默认为空，经典类
python3 默认含有 object，新式类
'''
class Person(object):
    def __init__(self,name,age):       # 构造方法，实例化的时候执行，用于创建实例属性    在类里，变量就叫做属性
        self.name = name
        self.age = age
        print('初始化对象')

    def eat(self,food):       # self 代表对象或实例本身 id()查看所在内存地址
        print('吃',food)
        print('对象的属性是：',self.name,self.age)

    def sleep(self):
        print('睡觉')
if __name__ == '__main__':
    a = Person('jichao',20)     # 实例化的时候相当于调用的是init方法，所以要看init方法，是否需要传参
    a.eat('米饭')
    a.sleep()


# 定义一个学生类：Student、内部含有一个方法：study，实现打印：xx学习xx课程
# class Student(object):
#     def __init__(self,name,course):
#         self.name = name
#         self.course = course
#     def study(self):
#         print(self.name+','+'学习'+self.course+'课程')
#
# s = Student("jichao","数学")
# s.study()

#  继承，继承谁就在括号中写谁--类名
#        继承后子类具有父类所有的属性，父类不具备子类的属性
#        子类可以自己定义自己的属性




