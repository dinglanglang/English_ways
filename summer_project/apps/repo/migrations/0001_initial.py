# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-08-20 07:13
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inspiration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('inspire_content', ckeditor_uploader.fields.RichTextUploadingField(null=True, verbose_name='激励语录')),
                ('inspire_time', models.DateTimeField(auto_now_add=True, null=True, verbose_name='发布时间')),
                ('status', models.BooleanField(default=False, verbose_name='审核状态')),
                ('contributor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='贡献者')),
            ],
            options={
                'verbose_name': '激励语录',
                'verbose_name_plural': '激励语录',
            },
        ),
    ]
