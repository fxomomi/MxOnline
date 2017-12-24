# -*- encoding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class CityDict(models.Model):
    Name = models.CharField(max_length=20, verbose_name=u"城市名称")
    Desc = models.CharField(max_length=200, verbose_name=u"城市描述")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"城市"
        verbose_name_plural = verbose_name


class CourseOrg(models.Model):
    Name = models.CharField(max_length=50, verbose_name=u"机构名称")
    Desc = models.TextField(verbose_name=u"机构描述")
    ClickNumbers = models.IntegerField(default=0, verbose_name=u"点击数")
    FavNumbers = models.IntegerField(default=0, verbose_name=u"收藏数")
    Image = models.ImageField(max_length=100, upload_to="course/%Y/%m", verbose_name=u"封面图")
    Address = models.CharField(max_length=150, verbose_name=u"机构地址")
    City = models.ForeignKey(CityDict, verbose_name=u"所在城市")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程机构"
        verbose_name_plural = verbose_name


class Teacher(models.Model):
    Org = models.ForeignKey(CourseOrg, verbose_name=u"所属机构")
    Name = models.CharField(max_length=50, verbose_name=u"教师名称")
    WorkYears = models.IntegerField(default=0, verbose_name=u"工作年限")
    WorkCompany = models.CharField(max_length=50, verbose_name=u"就职公司")
    WorkPosition = models.CharField(max_length=50, verbose_name=u"公司职位")
    Points = models.CharField(max_length=50, verbose_name=u"教学特点")
    ClickNumbers = models.IntegerField(default=0, verbose_name=u"点击数")
    FavNumbers = models.IntegerField(default=0, verbose_name=u"收藏数")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"教师"
        verbose_name_plural = verbose_name