# -*- coding: utf-8 -*-
# @Time : 2022/7/5 22:02
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time
import pytest

from SeleniumBase.Modular.Cms_Web import cms_web_introduction
from SeleniumBase.Modular.Cms_Web import cms_web_room_01
from SeleniumBase.TestCase.Test_Cms_Console import test_cms_create_room_001

@pytest.mark.web
def test_open_web_001(sb):
    """CMS-WEB观看端回归测试001"""
    """
    test_open_cms_web：初始化web浏览器
    sb = seleniumbase缩写（装饰器）
    """
    sb.demo_mode = True  # 开启高亮点击
    sb.save_screenshot_after_test = True  # Automatic if test fails


    sb.driver1 = sb.get_new_driver()  # 生成第一个chrome
    # self.driver1.setUp()
    sb.switch_to_driver(sb.driver1)  # 切换第一个chrome
    # 房间控件
    sb.ad = cms_web_room_01.test_cms_web_room_01(sb=sb)

    # 简介控件
    sb.ad = cms_web_introduction.test_cms_web_introduction(sb=sb)



    sb.driver2 = sb.get_new_driver()  # 生成第二个chrome
    # self.driver1.setUp()
    sb.switch_to_driver(sb.driver2)  # 切换第二个chrome
    sb.ad = test_cms_create_room_001.test_cms_create_room_001(sb=sb)

    # 硬等待
    time.sleep(3)


if __name__ == '__main__':
    pytest.main(['--report=musen.html',
                 '--title=微吼现场测试报告',
                 '--tester=宇',
                 '--desc=报告描述信息',
                 '--template=2'])
