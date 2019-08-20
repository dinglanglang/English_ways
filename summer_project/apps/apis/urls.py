from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^mobile_captcha/$',views.get_mobile_captcha,name="mobile_captcha"),
    url(r'^get_captcha/$',views.get_captcha,name="get_captcha"),
    url(r'^check_captcha/$',views.check_captcha,name="check_captcha"),
    url(r'^change_avator/$', views.ChangeAvator.as_view(), name='change_avator'),
]