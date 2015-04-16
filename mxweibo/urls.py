from django.conf.urls import patterns, include, url
from django.contrib import admin
from account import views as accountviews

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'account.views.login'),
                       url(r'^login/$', 'account.views.login'),
					   url(r'^register/', 'account.views.register'),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^account/', include('account.urls')),
                       url(r'^timeline/', include('timeline.urls')),
                       url(r'^index/', 'timeline.views.list_timeline'),
                       )
