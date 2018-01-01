# -*- coding:utf-8 -*-
import xadmin

from .models import Course, Chapter, Video, CourceResource

# NOTE:xadmin 管理类注册
class CourseAdmin(object):
    list_display = ["Name", "Desc", "Detail", "Degree", "LearnTimes", "Students", "FavNumbers", "Image", "ClickNumbers", "AddTime"] # 显示列表
    search_fields = ["Name", "Desc", "Detail", "Degree", "LearnTimes", "Students", "FavNumbers", "Image", "ClickNumbers"] # 搜索字段
    list_filter = ["Name", "Desc", "Detail", "Degree", "LearnTimes", "Students", "FavNumbers", "Image", "ClickNumbers", "AddTime"] # 过滤器 


class ChapterAdmin(object):
    list_display = ["Course", "Name", "AddTime"] # 显示列表
    search_fields = ["Course", "Name"] # 搜索字段
    # NOTE:xadmin 需指定外键的搜索字段(利用双下划线指定__)
    list_filter = ["Course__Name", "Name", "AddTime"] # 过滤器 


class VideoAdmin(object):
    list_display = ["Chapter", "Name", "AddTime"] # 显示列表
    search_fields = ["Chapter", "Name"] # 搜索字段
    list_filter = ["Chapter__Name", "Name", "AddTime"] # 过滤器 


class CourceResourceAdmin(object):
    list_display = ["Course", "Name", "Download", "AddTime"] # 显示列表
    search_fields = ["Course", "Name", "Download"] # 搜索字段
    list_filter = ["Course", "Name", "Download", "AddTime"] # 过滤器 


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Chapter, ChapterAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourceResource, CourceResourceAdmin)