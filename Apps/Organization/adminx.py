# -*- coding:utf-8 -*-
import xadmin

from .models import CityDict, CourseOrg, Teacher

class CityDictAdmin(object):
    list_display = ["Name", "Desc", "AddTime"] # 显示列表
    search_fields = ["Name", "Desc"] # 搜索字段
    list_filter = ["Name", "Desc", "AddTime"] # 过滤器 


class CourseOrgAdmin(object):
    list_display = ["Name", "Desc", "ClickNumbers", "FavNumbers", "Image", "Address", "City", "AddTime"] # 显示列表
    search_fields = ["Name", "Desc", "ClickNumbers", "FavNumbers", "Image", "Address", "City"] # 搜索字段
    list_filter = ["Name", "Desc", "ClickNumbers", "FavNumbers", "Image", "Address", "City", "AddTime"] # 过滤器 


class TeacherAdmin(object):
    list_display = ["Org", "Name", "WorkYears", "WorkCompany", "WorkPosition", "Points", "ClickNumbers", "FavNumbers", "AddTime"] # 显示列表
    search_fields = ["Org", "Name", "WorkYears", "WorkCompany", "WorkPosition", "Points", "ClickNumbers", "FavNumbers"] # 搜索字段
    list_filter = ["Org", "Name", "WorkYears", "WorkCompany", "WorkPosition", "Points", "ClickNumbers", "FavNumbers", "AddTime"] # 过滤器 


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)