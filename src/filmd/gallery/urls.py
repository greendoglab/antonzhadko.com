# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

urlpatterns = patterns('filmd.gallery.views',
    url(r'^gallery/$', 'gallery', name='gallery'),
)