# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime
from timeline.models import Timeline



@login_required(login_url='/login/')
def send(request):
	'''
	从前端获得数据Ajax
	再把数据输入数据库
	'''
	if request.POST:
		owner = request.user#
		timeline_content = request.POST.get('weibo_content')
		created_at=datetime.now()
		print owner
		print timeline_content
		print created_at
		print User.objects.get(username=owner)
		timeline = Timeline.objects.create(
			owner=owner,#为什么用户名进入，表内变成了id？如果设为外键，那么添加到数据库其实是id？
			owner_name=User.objects.get(username=owner),
			content=timeline_content,
			created_at=created_at
		)
		resp='200'
		return HttpResponse(resp)
	elif request.GET:
		resp='200'
		return HttpResponse(resp)



@login_required(login_url='/login/')
def list_timeline(request):
	'''
	从数据库获取特定的信息
	传输到模板中显示
	'''
	owner = request.user#当前登录的用户名字
	user_id = (User.objects.get(username=owner)).id
	timeline_list=Timeline.objects.filter(owner=user_id)
	#timeline_comment=Timeline.objects.get(timeline_id)
	return render_to_response('index.html',{'timeline_list':timeline_list})


@login_required(login_url='/login/')
def likes(request):
	if request.POST:
		timeline_dic=Timeline.objects.filter(id=request.POST.get("timeline_id"))
		timeline=timeline_dic[0]
		timeline.likes=timeline.likes+1
		timeline.save()

		resp='200'
		return HttpResponse(resp)
	elif request.GET:
		resp='200'
		return HttpResponse(resp)

