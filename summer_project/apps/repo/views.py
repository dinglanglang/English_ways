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


class contribute(View):
    def get(self,request):
        form = Contribute_Form
        return render(request,'crontribute_modal.html',{'form':form})

    def post(self,request):
        inspire_content=request.POST.get("inspire_content")
        print(inspire_content)
        form = Contribute_Form
        # inspire_content = form.cleaned_data["inspire_content"]
        # print(inspire_content)
        if len(inspire_content) > 8:
            text = Inspiration.objects.create(inspire_content=inspire_content)
            text.save()
            msg = "提交成功，请等待管理员审核"
        else:
            msg = "字数未达8个字，请重新填写"
        return render(request,"crontribute_modal.html",{"msg":msg,'form':form})








def passage(request):
    passage = Passage.objects.all()
    #搜索功能
    if request.GET.get('search') is not None:
        search = request.GET.get('search')
        passage = Passage.objects.filter(Q(passage_title__contains=search)|Q(passage_author__icontains=search)|Q(passage_content__contains=search))
    paginator = Paginator(passage, 4)
    page = request.GET.get('page')
    try:
        passage = paginator.page(page)
    except PageNotAnInteger:
        passage = paginator.page(1)
    except EmptyPage:
        passage = paginator.page(paginator.num_pages)
    kwgs = {"passage":passage,"paginator":paginator.page_range}
    return render(request,"passage.html",kwgs)

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

