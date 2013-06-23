# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('filmd.blog.views',
    url(r'^reports/$', 'reports_view', name='reports'),
    url(r'^post/(?P<slug>[^\.]+)/$', 'view_blog', name='view_blog'),
    url(r'^tag/(?P<slug>[^\.]+)/$', 'tag_view', name='tag_view'),
    url(r'^movies/$', 'movie_view', name='movies'),
    url(r'^news/$', 'news_view', name='news'),
    url(r'^clips/$', 'clip_view', name='clip'),
)