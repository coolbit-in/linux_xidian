from django.conf.urls import patterns, include, url
#from apps.mirrors_status.views import *
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^mirrors/$', 'linux_xidian.apps.mirrors_status.views.show_mirrors_status'),
    url(r'^help/(\w+)/$', 'linux_xidian.apps.mirrors_status.views.show_mirrors_help'),
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT})
    # url(r'^$', 'linux_xidian.views.home', name='home'),
    # url(r'^linux_xidian/', include('linux_xidian.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)