# -*- coding: utf-8 -*-
from models import ImageStorage, FileStorage
from django.contrib import admin
from sorl.thumbnail import default

ADMIN_THUMBS_SIZE = '100x100'

class ImageStorageAdmin(admin.ModelAdmin):
    
    def image_display(self, obj):
        thumb = default.backend.get_thumbnail(obj.image.file, ADMIN_THUMBS_SIZE)
        try:
            return '<img src="%s" width="%s" />' % (thumb.url, thumb.width)
        except:
            return 'no image'

    def code_display(self, obj):
        return '[%s|%s|%s]' % (obj.image.url, obj.title, obj.description)

    def original(self, obj):
        return obj.image.url

    image_display.allow_tags = True
    code_display.allow_tags = True
    list_display = ('id', 'title', 'image_display', 'code_display')
    list_per_page = 10


class FileStorageAdmin(admin.ModelAdmin):
    def get_url(self, obj):
        return obj.ufile.url

    list_display = ('id', 'get_url')
    list_per_page = 20

admin.site.register(ImageStorage, ImageStorageAdmin)
admin.site.register(FileStorage, FileStorageAdmin)