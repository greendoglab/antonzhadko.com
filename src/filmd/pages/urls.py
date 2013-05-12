# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('filmd.pages.views',
    url(r'^page/(?P<slug>[^\.]+)/$', 'view_page', name='view_page'),
)