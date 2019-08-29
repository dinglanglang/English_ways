# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Inspiration,Passage
from django.contrib import admin

# Register your models here.
admin.site.register(Inspiration)
admin.site.register(Passage)