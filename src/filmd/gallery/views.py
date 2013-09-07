# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from endless_pagination.decorators import page_template
from filmd.gallery.models import Gallery, GalleryImage

@page_template("archive_image.html")
def gallery(request, slug, template="gallery.html", extra_context=None):
    gallery = get_object_or_404(Gallery, slug=slug)
    context = {
        # 'url_prefix' : u'Галерея',
        # 'gallery': GalleryImage.objects.all(),
        'gallery' : gallery,
        'photos' : GalleryImage.objects.filter(gallery=gallery)
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

def gallereis(request):
    template = "gallereis.html"
    context = {
        'gallery': Gallery.objects.all(),
    }
    return render(request, template, context)