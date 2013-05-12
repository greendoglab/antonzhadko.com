# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from filmd.pages.models import Page

def view_page(request, slug):
    template = 'page.html'
    context = {
        'post' : get_object_or_404(Page, slug=slug, draft=True),
    }
    return render(request, template, context)