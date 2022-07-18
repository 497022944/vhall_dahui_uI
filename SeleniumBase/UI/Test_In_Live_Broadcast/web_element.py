# -*- coding: utf-8 -*-
# @Time : 2022/7/11 17:07
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com


class Web_Login:
    """Web登录"""

    # 登录按钮
    Web_Login = 'div.enroll.enroll2 > div.enroll-login > span '

    # 填写手机号或者邮箱
    Phone = '[placeholder="请填写您的报名手机号或邮箱登录"]'

    # 确认登陆
    Confirm = 'div.login-box > div > div.btn'



class Web_Question:
    """Web回复问卷"""

    # 问卷iframe创建
    Iframe = '/html/body/div/div/div[2]/div/div[1]/div/div/iframe'

    # 填写问卷姓名
    Question_Name = '/html/body/div/div/div/div[5]/div[3]/div[2]/div/div[2]/div[2]/div[1]/div[2]/div[2]/textarea'

    # 性别
    Question_Gender = '/html/body/div/div/div/div[5]/div[3]/div[2]/div/div[2]/div[2]/div[2]/div[2]/div[2]/label/span[1]/span'

    # 确定
    Question_Confirm = '[class="el-button onceBtn save el-button--primary"]'