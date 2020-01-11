#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/2 0002  22:22
#Author:chao
'''
导入ddt包
用装饰器@ddt
传入参数，执行
'''
import unittest
from ddt import ddt,data,unpack,file_data
tuple1 = ('橘子')
tuple2 = ('苹果','梨子','香蕉')
@ddt
class Mytest(unittest.TestCase):
    @data(tuple1)
    def test_001(self,name):
        print(name)
    @data(tuple2)
    def test_002(self,name):
        print(name)
if __name__ == '__main__':
    unittest.main()