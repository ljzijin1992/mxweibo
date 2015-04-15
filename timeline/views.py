# -*- coding: utf-8 -*-

from django.http import HttpResponseRedirect, HttpResponse, HttpRequest, Http404
from django.template import Context, RequestContext
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.contrib.auth.models import User
from django.contrib import auth
from datetime import datetime

@login_required(login_url='/login/')
def send(request):
    if request.GET:
        user_id = request.GET.get('id','')
        content = request.GET.get()