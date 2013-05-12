# -*- coding: utf-8 -*-
from models import Tag, Post
from django.contrib import admin

class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug',)
        }),
        ('Содержание', {
            'fields': ('title',)
        }),
    )
    list_per_page = 15

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

    fieldsets = (        
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug', 'date')
        }),
        ('Содержание', {
            'fields': ('draft', 'type_post', 'tags', 'title', 'post',)
        }),
    )
    filter_horizontal = ('tags',)
    list_display = ('title', 'draft')
    list_per_page = 15


admin.site.register(Tag, TagAdmin)
admin.site.register(Post, PostAdmin)