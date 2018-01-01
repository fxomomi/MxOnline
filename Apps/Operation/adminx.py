# -*- coding:utf-8 -*-
import xadmin

from .models import UserAsk, UserCourse, UserMessage, UserFavorite, CourseComments

class UserAskAdmin(object):
    list_display = ["Name", "Mobile", "CourseName", "AddTime"] # 显示列表
    search_fields = ["Name", "Mobile", "CourseName"] # 搜索字段
    list_filter = ["Name", "Mobile", "CourseName", "AddTime"] # 过滤器 


class UserCourseAdmin(object):
    list_display = ["User", "Course", "AddTime"] # 显示列表
    search_fields = ["User", "Course"] # 搜索字段
    list_filter = ["User", "Course", "AddTime"] # 过滤器 


class UserMessageAdmin(object):
    list_display = ["User", "Message", "HasRead", "AddTime"] # 显示列表
    search_fields = ["User", "Message", "HasRead"] # 搜索字段
    list_filter = ["User", "Message", "HasRead", "AddTime"] # 过滤器 
    

class UserFavoriteAdmin(object):
    list_display = ["User", "FavId", "FavType", "AddTime"] # 显示列表
    search_fields = ["User", "FavId", "FavType"] # 搜索字段
    list_filter = ["User", "FavId", "FavType", "AddTime"] # 过滤器 


class CourseCommentsAdmin(object):
    list_display = ["User", "Course", "Comments", "AddTime"] # 显示列表
    search_fields = ["User", "Course", "Comments"] # 搜索字段
    list_filter = ["User", "Course", "Comments", "AddTime"] # 过滤器 


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)