# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime

def login(request):
	if request.POST:
		username=request.POST['username']
		password=request.POST['password']
		user = auth.authenticate(username=username,password=password)
		if user and user.is_active:
			auth.login(request,user)
			return HttpResponseRedirect('index/')#用户的界面
		else:
			c=RequestContext(request,{
				'ErrorMsg': u'用户名或密码错误'
			})
			return render_to_response('')
