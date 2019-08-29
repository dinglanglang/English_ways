from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^change_password/$',views.ChangePasswdView.as_view(),name='change_passwd'),
    # 待审语录
    url(r'^approval/$', views.ApprovalView.as_view(), name='approval'),
    #贡献语录
    url(r'^inspiration/$',TemplateView.as_view(template_name="crontribute_modal.html"),name='inspiration'),
    # 审核接口
    url(r'^approval/(?P<id>\d+)/$', views.ApprovalPassView.as_view(), name='approval_pass'),
]

