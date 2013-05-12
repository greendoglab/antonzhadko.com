# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import RequestContext
from endless_pagination.decorators import page_template
from filmd.gallery.models import GalleryImage

@page_template("archive_image.html")
def gallery(request, template="gallery.html", extra_context=None):
    context = {
        'url_prefix' : u'Галерея',
        'gallery': GalleryImage.objects.all(),
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

# @render_to('gallery.html')
# def gallery(request):
#     return {
#         'gallery': GalleryImage.objects.all(),
#     }