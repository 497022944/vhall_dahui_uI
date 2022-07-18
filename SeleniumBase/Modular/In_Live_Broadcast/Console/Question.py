# -*- coding: utf-8 -*-
# @Time : 2022/7/11 17:33
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com

from SeleniumBase.UI.Test_In_Live_Broadcast.console_element import Question
from SeleniumBase.conftest import test_question


def test_live_questionnaire(sb):
    '''直播间问卷'''

    sb.click(Question.Question_button)  # 点击问卷按钮
    sb.click(Question.Database)  # 点击资料库
    sb.type(Question.Search_Question, test_question)  # 输入问卷
    sb.click(Question.Search)  # 点击搜索
    sb.click(Question.Binding)  # 点击绑定
    sb.click(Question.Send)  # 点击发送
