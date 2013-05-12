# -*- coding: utf-8 -*-
from models import Menu, Meta, MyPhoto, SiteTitle
from django.contrib import admin
from sorl.thumbnail import default

ADMIN_THUMBS_SIZE = '100x100'

class MyPhotoAdmin(admin.ModelAdmin):

    def image_display(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
        return '<img src="%s" width="%s" />' % (thumb.url, thumb.width)

    def original(self, obj):
        return obj.image.url

    image_display.allow_tags = True
    list_display = ('id', 'image_display', 'original')
    list_per_page = 10

class MenuAdmin(admin.ModelAdmin):
    list_per_page = 15

    list_display = ('title', 'order')
    list_editable = ['order']

    class Media:
        js = (
            'http://code.jquery.com/jquery-latest.js',
            'http://code.jquery.com/ui/1.9.2/jquery-ui.js',
            '/static/js/list-order.js',
            )
        css = {
            'screen': ('/static/modeltranslation/css/tabbed_translation_fields.css',),
            }

admin.site.register(Menu, MenuAdmin)
admin.site.register(Meta)
admin.site.register(SiteTitle)
admin.site.register(MyPhoto, MyPhotoAdmin)