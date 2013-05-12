# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from filmd.blog.models import Post
from filmd.gallery.models import GalleryImage

# def home(request):
#     template = 'index.html'
#     context = {
#     }
#     return render(request, template, context)