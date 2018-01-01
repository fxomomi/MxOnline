# -*- encoding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models


class Course(models.Model):
    Name = models.CharField(max_length=50, verbose_name=u"课程名")
    Desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    Detail = models.TextField(verbose_name=u"课程详情")
    Degree = models.CharField(max_length=2, choices=(("cj", u"初级"), ("zj", u"中级"), ("gj", u"高级")), verbose_name=u"难度")
    LearnTimes = models.IntegerField(default=0, verbose_name=u"学习时长(分钟)")
    Students = models.IntegerField(default=0, verbose_name=u"学习人数")
    FavNumbers = models.IntegerField(default=0, verbose_name=u"收藏人数")
    Image = models.ImageField(max_length=100, upload_to="course/%Y/%m", verbose_name=u"封面图")
    ClickNumbers = models.IntegerField(default=0, verbose_name=u"点击数")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.Name


class Chapter(models.Model):
    Course = models.ForeignKey(Course, verbose_name=u"课程")
    Name = models.CharField(max_length=100, verbose_name=u"章节名")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节"
        verbose_name_plural = verbose_name


class Video(models.Model):
    Chapter = models.ForeignKey(Chapter, verbose_name=u"课程")
    Name = models.CharField(max_length=100, verbose_name=u"视频名")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频"
        verbose_name_plural = verbose_name


class CourceResource(models.Model):
    Course = models.ForeignKey(Course, verbose_name=u"课程")
    Name = models.CharField(max_length=100, verbose_name=u"名称")
    Download = models.FileField(max_length=100, upload_to='cource/resource/%Y/%m', verbose_name=u"资源文件")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name





