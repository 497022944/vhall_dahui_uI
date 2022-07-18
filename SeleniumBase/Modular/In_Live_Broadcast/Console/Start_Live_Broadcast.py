# -*- coding: utf-8 -*-
# @Time : 2022/7/11 11:45
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time

from SeleniumBase.UI.Public import Public
from SeleniumBase.UI.Test_In_Live_Broadcast.console_element import Live_Broadcast_List
from SeleniumBase.conftest import test_il_id


def test_start_live_broadcast(sb):
    """开启直播"""


    Public.test_console_login(sb=sb)  # 登录控制台

    sb.click(Live_Broadcast_List.Room_List_Test)   # 点击房间列表-测试
    sb.type(Live_Broadcast_List.Search_Room, test_il_id)  # 搜索房间id
    sb.click(Live_Broadcast_List.LookUp)  # 点击查找
    sb.click(Live_Broadcast_List.Play)  # 点击开播

    time.sleep(1)
    sb.switch_to_window(window=1)
    # sb.click(Start_Live_Broadcast.Start_Live_Broadcast)  # 开始推流
    time.sleep(4)  # 目前需要手动点击权限
    # sb.click(Start_Live_Broadcast.Confirm)  # 点击确定按钮




    # time.sleep(3)
    # sb.wait_for_and_switch_to_alert()  # 摄像头，麦克风权限允许

