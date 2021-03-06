# -*- encoding:utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    NickName = models.CharField(max_length=50, verbose_name=u"昵称", default="")
    Birthday = models.DateField(verbose_name=u"生日", null=True, blank=True)
    Gender = models.CharField(max_length=6, choices=(("male",u"男"), ("female", u"女")), default="female")
    Address = models.CharField(max_length=100, verbose_name=u"地址", default="")
    Mobile = models.CharField(max_length=11, verbose_name=u"手机", null=True, blank=True)
    Image = models.ImageField(max_length=100,upload_to="image/%Y/%m", default=u"image/default.png")

    class Meta:
        verbose_name = "用户信息"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    Code = models.CharField(max_length=20, verbose_name=u"验证码")
    Email = models.EmailField(max_length=50, verbose_name=u"邮箱")
    SendType = models.CharField(max_length=10, choices=(("register", u"注册"), ("forget", u"找回密码")), verbose_name=u"验证码类型")
    SendTime = models.DateTimeField(default=datetime.now, verbose_name=u"发送时间") # datetime.now()取的是编译时的时间，不加括号才是实例化时的时间
    
    class Meta:
        verbose_name = u"邮箱验证码"
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return "{0}({1})".format(self.Code, self.Email)

class Banner(models.Model):
    Title = models.CharField(max_length=100, verbose_name=u"标题")
    Image = models.ImageField(max_length=100, upload_to = "banner/%Y/%m", verbose_name=u"轮播图")
    Url = models.URLField(max_length=200, verbose_name=u"访问地址")
    Index = models.IntegerField(default=100, verbose_name=u"顺序")
    AddTime = models.DateField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"轮播图"
        verbose_name_plural = verbose_name


