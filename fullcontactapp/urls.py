from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'fullcontactapp.views.home', name='home'),
    # url(r'^result/$', 'fullcontactapp.views.result', name='result'),
)