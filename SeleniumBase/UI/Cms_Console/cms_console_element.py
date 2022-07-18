# -*- coding: utf-8 -*-
# @Time : 2022/7/5 13:53
# @Author : fanyu.zhao
# @Email  : fanyu.zhao@vhall.com

class CmsLogin:
    """CMS登录页"""

    # 请输出账号
    Cms_Account = "[class = 'phone el-input el-input--prefix'] [type='text']"

    # 请输入密码
    Cms_Password = "[class='checkcode el-input el-input--prefix'] [type='text']"

    # 确定登录
    Cms_is_login = '[class="el-button btn large theme-btn_blue el-button--primary"]'



class CmsProjectCreate:
    """CMS项目创建"""

    #创建项目
    Cms_Create_Project = '[class="el-button button-project-create el-button--primary"]'

    # 中文直播
    Cms_Chinese_Project = '[class="el-radio__input is-checked"] [class="el-radio__inner"]'

    # 英文直播
    Cms_English_Project = '[class="el-form-item__content"] :nth-child(2) [class="el-radio__inner"]'

    # 中英文
    Cms_Chinese_and_English = '[class="el-form-item__content"] :nth-child(3) [class="el-radio__inner"]'

    # 项目中文名称
    Cms_Chinese_Project_Name = '[placeholder="请输入项目中文名称"]'

    # 项目英文名称
    Cms_English_Project_Name = '[placeholder="请输入项目英文名称"]'

    # 选择上线时间
    Cms_Online_Time = '[placeholder="选择上线时间"]'

    # 选择下线时间
    Cms_Offline_Time = '[placeholder="选择下线时间"]'

    # 项目封面
    Cms_Project_Img = '[class="el-upload__input"]'

    # 项目创建
    Cms_Project_Create = '[class="el-button el-button--primary"] ["创建"]'

    # 项目中文名称文案
    Cms_Zh_ProjectName = '[for ="zh.projectName"]'
