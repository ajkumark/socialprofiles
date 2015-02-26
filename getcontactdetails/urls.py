from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'getcontactdetails.views.home', name='home'),
    url(r'', include('fullcontactapp.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
