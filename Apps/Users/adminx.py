# -*- coding:utf-8 -*-
import xadmin
from xadmin import views

from .models import EmailVerifyRecord, Banner

class BaseSetting(object):
    # xadmin主题功能
    enable_themes = True    
    use_bootwatch = True


class GlobalSetting(object):
    site_title = "Momi后台管理系统" # 左上角页眉
    site_footer = "Momi在线网" # 页脚
    menu_style = "accordion" # 菜单样式（收起）


# NOTE:xadmin 管理类注册
class EmailVerifyRecordAdmin(object):
    list_display = ["Code", "Email", "SendType", "SendTime"] # 显示列表
    search_fields = ["Code", "Email", "SendType"] # 搜索字段
    list_filter = ["Code", "Email", "SendType", "SendTime"] # 过滤器 


class BannerAdmin(object):
    list_display = ["Title", "Image", "Url", "Index", "AddTime"]
    search_fields = ["Title", "Image", "Url", "Index"]
    list_filter = ["Title", "Image", "Url", "Index", "AddTime"]


# NOTE:前端显示的顺序与此处一致
xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
# NOTE:注册xadminSetting
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSetting)