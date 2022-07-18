# -*- coding: utf-8 -*-
# @Time : 2022/7/6 18:58
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
from SeleniumBase.UI.Public import Public
from SeleniumBase.UI.Cms_Web.cms_web_element import CmsWebIntroduction
from SeleniumBase.UI.Public.Enum import Cms_Web_Introduction

def test_cms_web_introduction(sb):
    """
    test_open_cms_web：初始化web浏览器
    sb = seleniumbase缩写（装饰器）
    """

    # 进入web观看端
    Public.test_open_cms_web(sb=sb)

    # 简介控件
    sb.click(CmsWebIntroduction.Introduction_Title)  # 点击简介控件
    Introduction_Title_Text = sb.get_text(CmsWebIntroduction.Introduction_Title)  # 获取简介控件文本
    Introduction_Title_Bg_Text = sb.get_text(CmsWebIntroduction.Introduction_Title_Bg)  # 获取简介控件背景
    Introduction_Title_Vice_Text = sb.get_text(CmsWebIntroduction.Introduction_Title_Vice)  #获取简介控件副标题


    if Introduction_Title_Text == Cms_Web_Introduction.Introduction_Title.value:
        print("验证简介控件通过")
    else:
        print("验证简介控件失败")


    if Introduction_Title_Bg_Text == Cms_Web_Introduction.Introduction_Title_Bg.value:
        print("验证简介控件背景通过")
    else:
        print("验证简介控件背景失败")

    if Introduction_Title_Vice_Text == Cms_Web_Introduction.Introduction_Title_Vice.value:
        print("验证简介控件副标题通过")
    else:
        print("验证简介控件副标题失败")
