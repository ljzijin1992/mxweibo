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
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/index/')  # 用户的界面
        else:
            c = RequestContext(request, {
                'ErrorMsg': u'用户名或密码错误'
            })
            return render_to_response('login.html', c)
    else:
        c = RequestContext(request, {})
        return render_to_response('login.html', c)


def register(request):
    if request.POST:
        # 需要添加信息校验提示
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        try:
            newuser = User.objects.create_user(
                username=username,
                email=email,
                password=password

            )
            try:
                print 'newuser is staff',newuser.is_staff
                newuser.save()
            except Exception,e:
                print e
                c = RequestContext(request,{'ErrorMsg':u'已经存在用户，轻修改用户名'})
                return render_to_response('register.html',c)

            c=RequestContext(request,{'ErrorMsg':u'注册成功，请登录'})
            return render_to_response('login.html',c)

        except Exception, e:
            print e
            c = RequestContext(request, {
                'ErrorMsg': u'已经存在用户，请修改用户名'
            })
            return render_to_response('register.html',c)
    else:
        c = RequestContext(request, {})
        return render_to_response('register.html', c)

@login_required(login_url='/login/')
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url='/login/')
def index(request):
    return render_to_response('index.html',{})