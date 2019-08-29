from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    url(r'^inspration/$',views.inspiration,name="inspiration"),
    url(r'^passage/$',views.passage,name="passage"),
    url(r'^passage_detail/$', views.PassageDetail.as_view(), name="passage_detail"),
    url(r'^contribute/$',views.contribute,name="contribute"),
    url(r'^movie_love/$',views.movie_love,name="movie_love"),
    url(r'^movie_action/$',views.movie_action,name="movie_action"),
    url(r'^movie_comedy/$',views.movie_comedy,name="movie_comedy"),
    url(r'^movie_cartoon/$',views.movie_cartoon,name="movie_cartoon"),
    url(r'^music_classical/$',TemplateView.as_view(template_name="music_classical.html"),name="music_classical")
]