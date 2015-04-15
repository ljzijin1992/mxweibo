#! -*- coding:UTF-8 -*-
from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^login/', 'account.views.login'),
                       url(r'^register/', 'account.views.register'),
                       )

