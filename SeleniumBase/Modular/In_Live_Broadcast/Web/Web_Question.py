# -*- coding: utf-8 -*-
# @Time : 2022/7/11 19:11
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time
from SeleniumBase.UI.Test_In_Live_Broadcast.web_element import Web_Question
from SeleniumBase.conftest import nick_name


def test_web_question(sb):
    """观众端填写问答"""

    max_retry = 0

    while max_retry < 3:
        try:
            time.sleep(20)
            sb.switch_to_frame(Web_Question.Iframe)  # 切换到iframe窗口

            sb.type(Web_Question.Question_Name, nick_name)  # 输入姓名

            sb.click(Web_Question.Question_Gender)  # 输入性别

            sb.click(Web_Question.Question_Confirm)
            break
        except Exception:
            time.sleep(2)
        max_retry += 1
