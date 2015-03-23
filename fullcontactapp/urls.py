from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'fullcontactapp.views.home', name='home'),
	# url(r'(?P<msg>[a-z]+)$', 'fullcontactapp.views.home', name='optional_home'),
    url(r'^contact/', 'fullcontactapp.views.contact', name='contact'),
    url(r'^getmessages', 'fullcontactapp.views.getmessages', name='getmessages'),
    # url(r'^result/$', 'fullcontactapp.views.result', name='result'),
)