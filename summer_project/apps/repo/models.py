# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from apps.accounts.models import User
from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from easy_thumbnails.fields import ThumbnailerImageField

# Create your models here.
class Inspiration(models.Model):
    """激励墙"""
    inspire_content = RichTextUploadingField("激励语录",default="例如：加油，大家一起学英语！")
    inspire_time = models.DateTimeField("发布时间",auto_now_add=True,null=True)
    contributor = models.ForeignKey(User,verbose_name="贡献者",null=True)
    status = models.BooleanField("审核状态",default=False)

    class Meta:
        verbose_name = "激励语录"
        verbose_name_plural = verbose_name
        permissions = (
            ('can_change_inspiration',"可以修改激励语录"),
            ('can_add_inspiration',"可以添加激励语录"),
            ('can_change_inspiration_status',"可以修改激励语录状态")
        )

    def __str__(self):
        return "{}".format(self.inspire_content)


class Passage(models.Model):
    """文章"""
    passage_title = models.CharField(max_length=64,verbose_name="文章标题")
    passage_time = models.DateTimeField("发布日期",auto_now_add=True)
    passage_author = models.CharField(max_length=36,verbose_name="文章作者")
    passage_content = models.CharField(max_length=512,verbose_name="文章内容")
    passage_collect_status = models.BooleanField("收藏状态",default=False)
    passage_picture = ThumbnailerImageField(upload_to="passage/%Y%m%d/", verbose_name="文章图片")
    user = models.ForeignKey(User,verbose_name="收藏人",null=True)

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.passage_title)


class Movie(models.Model):
    """电影"""
    movie_name = models.CharField(max_length=16,verbose_name="电影名")
    movie_time = models.DateTimeField("上映时间",auto_now_add=True)
    movie_actor = models.CharField(max_length=36,verbose_name="演员")
    movie_desc = models.CharField(max_length=512,verbose_name="电影简介")
    movie_type = models.CharField(max_length=32,verbose_name="电影类型")
    movie_picture = models.ImageField(upload_to="movie/%Y%m%d/", verbose_name="电影图片")
    movie_source = models.CharField(max_length=512,verbose_name="电影资源")

    class Meta:
        verbose_name = "电影"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{}".format(self.movie_name)
