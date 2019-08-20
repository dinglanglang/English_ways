# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class User(AbstractUser):
    realname = models.CharField(max_length=8,verbose_name="真实姓名")
    mobile = models.CharField(max_length=11,verbose_name="手机号码")
    qq = models.CharField(max_length=11,verbose_name="QQ号")
    avator_sor = ThumbnailerImageField(upload_to="avator/%Y%m%d/",default="avator/default.jpg",verbose_name="头像")



class FindPassword(models.Model):
    verify_code = models.CharField(max_length=128, verbose_name="验证码")
    email = models.EmailField(verbose_name="邮箱")
    creat_time = models.DateTimeField(auto_now=True, verbose_name="重置时间")
    status = models.BooleanField(default=False, verbose_name="是否已重置")

    class Meta:
        verbose_name = "找回密码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.email