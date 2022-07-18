# -*- coding: utf-8 -*-
# @Time : 2022/7/13 13:51
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time

import pytest
from SeleniumBase.Modular.In_Live_Broadcast.Console import Start_Live_Broadcast
from SeleniumBase.Modular.In_Live_Broadcast.H5.H5_Question import test_h5_question
from SeleniumBase.UI.Public.Public import test_h5_login, test_open_cms_h5, test_log_out
from SeleniumBase.Modular.In_Live_Broadcast.Console import Question


@pytest.mark.h5_room
def test_live_broadcast_h5_001(sb, test_open_cms_h5):
    """主持人开启直播、发送问卷、H5观众端参与问卷"""
    sb.demo_mode = True  # 开启高亮点击
    sb.save_screenshot_after_test = True  # Automatic if test fails

    # H5 观众登陆
    test_h5_login(test_open_cms_h5)

    # 主播端
    sb.ad = Start_Live_Broadcast.test_start_live_broadcast(sb=sb)  # 主持人开播
    time.sleep(15)
    sb.ad = Question.test_live_questionnaire(sb=sb)  # 主持人发送问卷

    # 观众端填写问卷
    test_h5_question()

    # 观众退出登陆
    time.sleep(8)
    test_log_out()
