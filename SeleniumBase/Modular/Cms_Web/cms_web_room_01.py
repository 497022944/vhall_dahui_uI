# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:56
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
from SeleniumBase.UI.Public import Public
from SeleniumBase.UI.Public.Enum import Cms_Web_Room02
from SeleniumBase.UI.Cms_Web.cms_web_element import CmsWebRoom02


def test_cms_web_room_01(sb):
    """
    test_open_cms_web：初始化web浏览器
    sb = seleniumbase缩写（装饰器）
    """

    # 进入web观看端
    Public.test_open_cms_web(sb=sb)

    # 房间控件
    sb.click(CmsWebRoom02.SignUp_Text)  # 点击距直播开始还有
    SignUp_Text = sb.get_text(CmsWebRoom02.SignUp_Text)  # 验证房间模式二倒计时
    if SignUp_Text.find(Cms_Web_Room02.CountDown.value) == 0:  # 断言距直播开始还有在页面中
        print("房间倒计时验证通过")
    else:
        print("房间倒计时验证错误")



    sb.save_screenshot("web_room2.png", folder="./downloaded_files")  # 保存房间控件2KV截图
    sb.assert_downloaded_file("web_room2.png")  # 验证截图是否存在
