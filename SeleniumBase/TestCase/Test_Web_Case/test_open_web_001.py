# -*- coding: utf-8 -*-
# @Time : 2022/7/5 22:02
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time
import pytest

from SeleniumBase.Modular.Cms_Web import cms_web_introduction
from SeleniumBase.Modular.Cms_Web import cms_web_room_01


@pytest.mark.cms_web
def test_open_web_001(sb):
    """CMS-WEB观看端回归测试001"""
    """
    sb = seleniumbase缩写（装饰器）
    """
    sb.demo_mode = True  # 开启高亮点击
    sb.save_screenshot_after_test = True  # Automatic if test fails

    # 房间控件
    sb.ad = cms_web_room_01.test_cms_web_room_01(sb=sb)

    # 简介控件
    sb.ad = cms_web_introduction.test_cms_web_introduction(sb=sb)

    # 硬等待
    time.sleep(3)


if __name__ == '__main__':
    pytest.main(['--report=musen.html',
                 '--title=微吼现场测试报告',
                 '--tester=宇',
                 '--desc=报告描述信息',
                 '--template=2'])
