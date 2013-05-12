# -*- coding: utf-8 -*-
from filmd.blog.models import Tag, Post
from django.shortcuts import render, render_to_response, get_object_or_404
from django.template import RequestContext
from endless_pagination.decorators import page_template
from django.db.models import Avg, Max, Min, Count

@page_template("archive_page.html")
def blog(request, template="blog.html", extra_context=None):
    context = {
        'url_prefix' : u'Блог',
        'post': Post.objects.filter(draft=True)
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

@page_template("archive_page.html")
def tag_view(request, slug, template="blog.html", extra_context=None):
    tag = get_object_or_404(Tag, slug=slug)
    context = {
        'url_prefix' : tag.title,
        'post': Post.objects.filter(draft=True).filter(tags=tag)
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

@page_template("archive_page.html")
def movie_view(request, template="blog.html", extra_context=None):
    context = {
        'url_prefix' : u'Фильмы',
        'post': Post.objects.filter(draft=True).filter(type_post='movie')
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))


@page_template("archive_page.html")
def clip_view(request, template="blog.html", extra_context=None):
    context = {
        'url_prefix' : u'Клипы',
        'post': Post.objects.filter(draft=True).filter(type_post='clip')
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

@page_template("archive_page.html")
def news_view(request, template="blog.html", extra_context=None):
    context = {
        'url_prefix' : u'Новости',
        'post': Post.objects.filter(draft=True).filter(type_post='news')
    }
    if extra_context is not None:
        context.update(extra_context)
    return render_to_response(template, context, context_instance=RequestContext(request))

def view_blog(request, slug):
    template = 'post.html'
    context = {
        'post' : get_object_or_404(Post, slug=slug),
    }
    return render(request, template, context)