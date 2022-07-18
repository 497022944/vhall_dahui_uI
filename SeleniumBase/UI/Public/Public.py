# -*- coding: utf-8 -*-
# @Time : 2022/7/5 15:08
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com
import json
import time

import pytest
from airtest.core.api import *
from SeleniumBase.UI.Cms_Console.cms_console_element import CmsLogin
from SeleniumBase.UI.Test_In_Live_Broadcast.console_element import ConsoleLogin
from SeleniumBase.UI.Test_In_Live_Broadcast.web_element import Web_Login
from SeleniumBase.conftest import test_cms_console_url, phone, password, test_cms_watch_url, test_project, test_console,\
    nick_name, \
    watch_phone, H5_IP, watch_phone2
from SeleniumBase.conftest import DATA_DIR
import os


# cms控制台登录
def test_cms_login(sb):
    sb.open(test_cms_console_url + "/login")  # 打开Cms控制台登录
    sb.driver.maximize_window()  # 窗口最大化
    sb.type(CmsLogin.Cms_Account, phone)  # 输入用户名
    sb.type(CmsLogin.Cms_Password, password)  # 输入密码
    sb.click(CmsLogin.Cms_is_login)  # 点击登录


# 进入web观看端
def test_open_cms_web(sb):
    sb.open(test_cms_watch_url + f"/pc/{test_project}?channel=main")  # 打开web观看端地址
    sb.driver.maximize_window()  # 窗口最大化


# 进入h5观看端
@pytest.fixture
def test_open_cms_h5():
    __author__ = "vhall_dahui"
    connect_device(H5_IP)  # 连接H5
    auto_setup(__file__)  # Airtest初始化
    touch(wait(Template(DATA_DIR + r"/桌面微信icon.png")))  # 打开微信
    touch(wait(Template(DATA_DIR + r"/微信我的.png")), times=2)  # 进入微信我的个人中心
    touch(wait(Template(DATA_DIR + r"/微信收藏.png")), times=2)  # 进入收藏
    touch(wait(Template(DATA_DIR + r"/收藏cms地址.png")), times=2)  # 点击收藏的cms落地页地址
    time.sleep(2)
    touch(wait(Template(DATA_DIR + r"/收藏cms地址点击.png")), times=2)  # 点击cms落地页地址进入


# 控制台登录
def test_console_login(sb):
    sb.open(test_console + "/fe/login?VNK=afabd9e2")  #打开控制台地址
    sb.driver.maximize_window()  # 窗口最大化
    sb.type(ConsoleLogin.NickName, nick_name)  # 输入昵称
    sb.type(ConsoleLogin.Account, phone)  # 输入用户名
    sb.type(ConsoleLogin.Password, password)  # 输入密码
    sb.click(ConsoleLogin.is_login)  # 点击登录


# web观众登录
def test_web_login(sb):

    test_open_cms_web(sb=sb)  # 进入观看端
    sb.driver.maximize_window()  # 窗口最大化
    sb.click(Web_Login.Web_Login)  # 点击登陆
    sb.type(Web_Login.Phone, watch_phone)  # 输入手机号
    sb.click(Web_Login.Confirm)  # 确认登陆


# h5观众登陆
def test_h5_login(test_open_cms_h5):  # 初始化进入h5落地页
    touch(wait(Template(DATA_DIR + r"/点击登陆.png")), times=2)  # 点击登陆
    touch(wait(Template(DATA_DIR + r"/输入手机号.png")), times=2)  # 输入手机号
    text(watch_phone2)  # 输入手机号
    touch(wait(Template(DATA_DIR + r"/立即登陆.png")), times=2)  # 打开微信


# h5退出登陆
def test_log_out():
    touch(wait(Template(DATA_DIR + r"/个人中心设置.png")), times=2)  # 点击右上角设置
    touch(wait(Template(DATA_DIR + r"/退出登陆.png")), times=2)  # 点击退出登陆


def get_dt():
    """
    获取当前的日期和时间
    :return:
    """
    dt = time.strftime("%Y-%m-%d")
    return dt


# 获取控制台token
def get_cms_console_token(sb):
    cms_admin_userinfo = sb.execute_script('return localStorage.getItem("cms_admin_userinfo");')
    cms_admin_userinfo = json.loads(cms_admin_userinfo)
    token = cms_admin_userinfo["token"]
    return token


def uploadFile(self, file_name):
    """
    通过Windows,mac系统上传文件
    """
    """
    针对非input类型的上传框，使用pywin32或者PyKeyboard处理
    file_name：文档名称
    :return:
    """
    now_platform = self.common.get_platform_info()
    if "Windows" in now_platform:
        try:
            win_file_path = os.path.join(self.common.get_file_base_path(), file_name)
            self.common.upload_file_for_win(win_file_path)
        except Exception as e:
            print("上传图片失败：", e)
    elif "mac" in now_platform:
        try:
            mac_file_path = os.path.join(self.common.get_file_base_path(), file_name)
            self.common.upload_file_for_mac(mac_file_path)
        except Exception as e:
            print("上传图片失败：", e)
    else:
        pass
