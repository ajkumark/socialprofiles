from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^$', 'fullcontactapp.views.home', name='home'),
	# url(r'(?P<msg>[a-z]+)$', 'fullcontactapp.views.home', name='optional_home'),
    url(r'^contact/', 'fullcontactapp.views.contact', name='contact'),
    url(r'^getmessages', 'fullcontactapp.views.getmessages', name='getmessages'),
    url(r'^view_profiles', 'fullcontactapp.views.view_profiles', name='view_profiles'),
    url(r'^test', 'fullcontactapp.views.test', name='test'),
    # url(r'^result/$', 'fullcontactapp.views.result', name='result'),
)