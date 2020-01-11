#!/usr/bin/evn python
#-*-coding:utf-8-*-
#Date:2020/1/4 0004  16:48
#Author:chao
import unittest
import HTMLTestRunner
class Unittest(unittest.TestCase):
    # def test01(self):
    #     print("输出正确！")
    pass
# if __name__ == '__main__':
    # 创建测试套件，并将符合条件的test开头的方法添加其中
    discover = unittest.defaultTestLoader.discover('./',pattern='test_fun.py',top_level_dir=None)
    print(discover)
    # runner = unittest.TextTestRunner()
    # runner.run(discover)

    # 定义一个安装目录，以写的方式打开
    file = open("E:\\2019.12.1\\vip4\\result2.html",'wb')
    # 定义测试报告
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,title="测试报告",description="最终的报告")
    # 执行测试用例
    runner.run(discover)
    # 关闭报告文件
    file.close()