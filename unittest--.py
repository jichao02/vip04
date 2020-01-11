#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/4 0004  16:20
#Author:chao
import unittest
import HTMLTestRunner
class Unittest(unittest.TestCase):
    def test01(self):
        print("输出正确！")

if __name__ == '__main__':
    # 创建测试套件，并将符合条件的test开头的方法添加其中
    discover = unittest.defaultTestLoader.discover('./',pattern='test_fun.py',top_level_dir=None)
    runner = unittest.TextTestRunner()
    runner.run(discover)