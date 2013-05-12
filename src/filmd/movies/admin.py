# -*- coding: utf-8 -*-
from models import Movie
from django.contrib import admin

class MovieAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug', 'date', 'draft')
        }),
        ('Содержание', {
            'fields': ('title', 'post',)
        }),
        ('SEO', {
            'fields': ('description', 'keywords')
        })
    )
    list_display = ('title', 'draft')
    list_per_page = 15

admin.site.register(Movie, MovieAdmin)