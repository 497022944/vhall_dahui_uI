# -*- coding: utf-8 -*-
# @Time : 2022/7/11 11:17
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com

class ConsoleLogin:
    """控制台登录"""

    # 请输入昵称
    NickName = '[class="nickname el-input el-input--prefix"] [type="text"]'

    # 请输出账号
    Account = "[class = 'phone el-input el-input--prefix'] [type='text']"

    # 请输入密码
    Password = "[class='checkcode el-input el-input--prefix'] [type='text']"

    # 确定登录
    is_login = '[class="el-button btn large theme-btn_blue el-button--primary"]'



class Start_Live_Broadcast:
    """开启直播 / 关闭直播"""

    # 开播
    Start_Live_Broadcast = '[class="vhall-main-left--tools__btn"]'
    # 确认按钮
    Confirm = '/html/body/div/div/div[1]/div[5]/div/div[3]/span[1]'



class Live_Broadcast_List:
    """直播间列表"""
    
    # 房间列表-测试
    Room_List_Test = '[class="childlds"]'

    # 搜索房间
    Search_Room = '[placeholder="房间ID"]'

    # 房间列表查找
    LookUp = '[class="room-wrap"] [class="el-button search el-button--primary"]'

    # 开播
    Play = '/html/body/div/div/div[2]/div[2]/div/div[3]/div[3]/table/tbody/tr/td[6]/div/div/button[1]'


class Question:
    """问卷"""

    # 问卷按钮
    Question_button = '#app > div > div.vh-room-publish > div.vh-room-publish-content > div.vhall-main-left > ' \
              'div.vhall-main-left--tools > div:nth-child(1) > button:nth-child(3)'

    # 资料库
    Database = '#app > div > div.vh-room-publish > div.vh-que > div.vh-que-tool > div:nth-child(1) ' \
               '> button.el-button.vh-que-btn.vh-que_add-btn.el-button--primary'

    # 搜问卷
    Search_Question = '[placeholder="搜问卷"]'

    # 搜索
    Search = '[class="vh-que-tool-search-btn"]'

    # 绑定
    Binding = '[class="vh-que__list-card-btn bind"]'

    # 发送
    Send = '/html/body/div[1]/div/div[1]/div[4]/div[3]/div/div[1]/div/div[1]/div/div/span[1]'

    # 问卷设置
    Question_Setting = '/html/body/div[1]/div/div[1]/div[4]/div[3]/div/div[1]/div/div[1]/div/span/span/span'

