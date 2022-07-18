# -*- coding: utf-8 -*-
# @Time : 2022/7/5 11:31
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import time

from SeleniumBase.UI.Public import Public
from SeleniumBase.UI.Public.Public import get_dt
from SeleniumBase.UI.Cms_Console.cms_console_element import CmsProjectCreate
from SeleniumBase.conftest import Chinese_Project_Name




def test_cms_create_room_001(sb):


    time_stamp = get_dt()  # 获取当前时间戳、年月日
    Public.test_cms_login(sb=sb)  # cms控制台登录
    sb.click(CmsProjectCreate.Cms_Create_Project)  # 创建项目
    sb.click(CmsProjectCreate.Cms_Chinese_Project)  # 选择中文
    sb.type(CmsProjectCreate.Cms_Chinese_Project_Name, Chinese_Project_Name)  # 输入中文项目名称
    sb.type(CmsProjectCreate.Cms_Online_Time, time_stamp)  # 输入上线时间
    sb.type(CmsProjectCreate.Cms_Offline_Time, time_stamp)  # 输入下线时间
    sb.click(CmsProjectCreate.Cms_Zh_ProjectName)  # 点击项目中文名称文案：用途是让时间弹窗消失


    time.sleep(10)


if __name__ == '__main__':
    test_cms_create_room_001()
