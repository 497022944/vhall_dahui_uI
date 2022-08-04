# -*- coding: utf-8 -*-
# @Time : 2022/7/7 17:16
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import pytest

path = "./"


if __name__ == '__main__':
    pytest.main(['-m', 'web_room', path, '--report=musen.html',
                 '--title=微吼现场测试报告',
                 '--tester=宇',
                 '--desc=报告描述信息',
                 '--template=2'])

"""
注意：main配置路径要在当前项目下

（1）运行所有 pytest.main()

(2)指定模块 pytest.main('[-vs],','./testcase/baseclass.py')

(3)指定目录pytest.main('[-vs]'),'./testcase')

(4)运行单个用例pytest -v test_day01.py::test_simple_case1

(5)-k 参数、可以使用表达式来筛选想要运行的测试用例pytest -k "case1 or case2"

(6)-m 参数、装饰器、运行已经标记过的用例、（pytest.ini里面配置）

(7)-x 出现失败测试用例就停止执行

(8)-s 允许在测试时输出信息

(9)-v 输出更详细的信息

(10)-q 简化输出信息

"""