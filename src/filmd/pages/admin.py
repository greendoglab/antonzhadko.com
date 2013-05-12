# -*- coding: utf-8 -*-
from models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    
    fieldsets = (
        ('Дополнительно', {
            'classes': ('collapse',),
            'fields': ('slug', 'date',)
        }),
        ('Содержание', {
            'fields': ('draft', 'title', 'post',)
        }),
    )
    list_display = ('title', 'draft',)
    list_per_page = 15

admin.site.register(Page, PageAdmin)