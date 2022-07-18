# -*- coding: utf-8 -*-
# @Time : 2022/7/13 15:06
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com

from airtest.core.api import *

from SeleniumBase.conftest import DATA_DIR


def test_h5_question():
    """观众端填写问答"""
    touch(wait(Template(DATA_DIR + r"/输入问卷姓名.png")))  # 输入问卷姓名
    touch(wait(Template(DATA_DIR + r"/输入性别.png")))  # 输入性别
    touch(wait(Template(DATA_DIR + r"/提交.png")))  # 点击提交问卷

