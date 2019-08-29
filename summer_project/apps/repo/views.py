# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,HttpResponse
from apps.accounts.models import User
from .models import Inspiration,Passage,Movie
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic.detail import DetailView,View
from django.db.models import Q
from .forms import Contribute_Form
def inspiration(request):
    users = User.objects.exclude(Q(inspiration__inspire_content=None)|Q(inspiration__status=0))
    # avator = Inspiration.objects.get("avator")
    inspiration = Inspiration.objects.exclude(status=0)
    # inspire_content = Inspiration.objects.get(id=1)
    return render(request,"inspiration.html",{"users":users,"inspiration":inspiration})

class PassageDetail(View):
    def get(self,request):
        id = request.GET.get('id')
        passage_detail=Passage.objects.filter(id=id)
        if passage_detail.count()==0:
            return HttpResponse("页面不存在")
        return render(request,'passage_detail.html',{"passage_detail":passage_detail[0]})

def contribute(request):
    form = Contribute_Form()
    return render(request,'crontribute_modal.html',{'form':form})


def passage(request):
    passage = Passage.objects.all()
    paginator = Paginator(passage, 4)
    page = request.GET.get('page')
    # print(passage[0].id)
    try:
        passage = paginator.page(page)
    except PageNotAnInteger:
        passage = paginator.page(1)
    except EmptyPage:
        passage = paginator.page(paginator.num_pages)
    return render(request,"passage.html",{"passage":passage,"paginator":paginator.page_range})

def movie_love(request):
    movie = Movie.objects.filter(movie_type="Love")
    paginator = Paginator(movie, 9)
    page = request.GET.get('page')
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'movie_love.html', {"movie":movie,"paginator":paginator.page_range})

def movie_action(request):
    movie = Movie.objects.filter(movie_type="Action")
    paginator = Paginator(movie, 9)
    page = request.GET.get('page')
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'movie_action.html', {"movie":movie,"paginator":paginator.page_range})

def movie_comedy(request):
    movie = Movie.objects.filter(movie_type="Comedy")
    paginator = Paginator(movie, 9)
    page = request.GET.get('page')
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'movie_comedy.html', {"movie":movie,"paginator":paginator.page_range})

def movie_cartoon(request):
    movie = Movie.objects.filter(movie_type="Cartoon")
    paginator = Paginator(movie, 9)
    page = request.GET.get('page')
    try:
        movie = paginator.page(page)
    except PageNotAnInteger:
        movie = paginator.page(1)
    except EmptyPage:
        movie = paginator.page(paginator.num_pages)
    return render(request, 'movie_cartoon.html', {"movie":movie,"paginator":paginator.page_range})

