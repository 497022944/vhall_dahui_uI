# -*- coding: utf-8 -*-
# @Time : 2022/7/11 11:15
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import pytest

from SeleniumBase.Modular.In_Live_Broadcast.Console import Start_Live_Broadcast
from SeleniumBase.Modular.In_Live_Broadcast.Console import Question
from SeleniumBase.Modular.In_Live_Broadcast.Web import Web_Question
from SeleniumBase.UI.Public import Public


@pytest.mark.web_room
def test_live_broadcast_web_001(sb):
    """主持人开启直播、发送问卷、Web观众端参与问卷"""

    sb.demo_mode = True  # 开启高亮点击
    sb.save_screenshot_after_test = True  # Automatic if test fails

    # 主播端
    sb.driver1 = sb.get_new_driver()  # 生成第一个chrome
    # self.driver1.setUp()
    sb.switch_to_driver(sb.driver1)  # 切换第一个chrome
    sb.ad = Start_Live_Broadcast.test_start_live_broadcast(sb=sb)  # 主持人开播

    # 观众端
    sb.driver2 = sb.get_new_driver()  # 生成第二个chrome
    sb.switch_to_driver(sb.driver2)  # 切换第二个chrome
    sb.ad = Public.test_web_login(sb)  # 观众端登录

    # 主持端
    sb.switch_to_driver(sb.driver1)  # 切换第一个chrome
    sb.ad = Question.test_live_questionnaire(sb=sb)  # 主持人发送问卷

    # 观众端
    sb.switch_to_driver(sb.driver2)  # 切换第二个chrome
    # 回答问卷
    sb.ad = Web_Question.test_web_question(sb=sb)
