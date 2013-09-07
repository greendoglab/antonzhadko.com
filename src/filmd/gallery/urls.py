# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('filmd.gallery.views',
    url(r'^gallery/(?P<slug>[^\.]+)/$', 'gallery', name='gallery'),
    url(r'^gallereis/$', 'gallereis', name='gallereis'),
)