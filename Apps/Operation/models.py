# -*- encoding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from Users.models import UserProfile
from Courses.models import Course


class UserAsk(models.Model):
    Name = models.CharField(max_length=20, verbose_name=u"姓名")
    Mobile = models.CharField(max_length=11, verbose_name=u"手机")
    CourseName = models.CharField(max_length=50, verbose_name=u"课程名称")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户咨询"
        verbose_name_plural = verbose_name


class CourseComments(models.Model):
    User = models.ForeignKey(UserProfile, verbose_name=u"用户名")
    Course = models.ForeignKey(Course, verbose_name=u"课程")
    Comments = models.CharField(max_length=200, verbose_name=u"评论")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程评论"
        verbose_name_plural = verbose_name


class UserFavorite(models.Model):
    User = models.ForeignKey(UserProfile, verbose_name=u"用户名")
    FavId = models.IntegerField(default=0, verbose_name=u"数据Id")
    FavType = models.IntegerField(choices=((1, "课程"), (2, "课程机构"), (3, "讲师")), default=1, verbose_name=u"收藏类型")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户收藏"
        verbose_name_plural = verbose_name

class UserMessage(models.Model):
    User = models.IntegerField(default=0, verbose_name=u"接收用户")
    Message = models.CharField(max_length=500, verbose_name=u"消息内容") 
    HasRead = models.BooleanField(default=False, verbose_name=u"是否已读")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户消息"
        verbose_name_plural = verbose_name


class UserCourse(models.Model):
    User = models.ForeignKey(UserProfile, verbose_name=u"用户名")
    Course = models.ForeignKey(Course, verbose_name=u"课程")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"用户课程"
        verbose_name_plural = verbose_name