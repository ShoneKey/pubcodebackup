#!/usr/bin/env python
# -*- coding: utf-8 -*-
# __author__:hp

__mtime__ = '2020-05-10'

import unittest
from ddt import ddt,data

data1 = [1,2,3]

def dataProcess():
    """数据处理"""
    print("数据处理")

def readExcel():
    """该方法需要在Test2中调用执行"""
    print("该方法只能在Test2中调用执行,return的数据作为Test2中ddt的data")
    return [4,5,6,8]

@ddt
class Test1(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("###test1_classmethod###")

    @data(*readExcel())
    def test_01(self,data1):
        print(data1)


    @classmethod
    def tearDownClass(cls):
        dataProcess()


@ddt
class Test2(unittest.TestCase):
    data2 = ""

    # @classmethod
    # def setUpClass(cls):
    #     global data2
    #     data2 = readExcel()

    @data(*readExcel())
    def test01(self,data1):
        print(data1)
        print("#####Test02_01######")


if __name__ == '__main__':
    unittest.main()

