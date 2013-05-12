from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',

    # url(r'^$', 'filmd.homepage.views.home', name='home'),

    (r'^$', direct_to_template, {
        'template': 'index.html'
    }),
    
    (r'^', include('filmd.gallery.urls')),
    (r'^', include('filmd.blog.urls')),
    (r'^', include('filmd.pages.urls')),

    (r'^comments/', include('django.contrib.comments.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
