from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^login/$',views.Login.as_view(),name="login"),
    url(r'^register/$',views.Register.as_view(),name="register"),
    url(r'^index/$',TemplateView.as_view(template_name="index.html"),name="index"),
    # url(r'^index2/$',TemplateView.as_view(template_name="index2.html"),name="index2"),
    url(r'^logout/$',views.logout,name="logout"),
    # 忘记密码
    url(r'password/forget/$', views.PasswordForget.as_view(), name="password_forget"),
    # 重置密码
    url(r'password/reset/(\w+)/$', views.PasswordReset.as_view(), name="password_reset"),
]