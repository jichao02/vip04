#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/4 0004  16:33
#Author:chao
import unittest
class Cla(unittest.TestCase):
    def test01(self):
        print("第一条")
    def test02(self):
        print("第二条")

if __name__ == '__main__':
    unittest.main()