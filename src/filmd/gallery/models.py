# -*- coding: utf-8 -*-
from django.db import models
import os.path
from django.contrib.sites.models import Site
from sorl.thumbnail import ImageField

# class Gallery(models.Model):
#         title = models.CharField(max_length=500, help_text="Заголовок")
#         slug = models.SlugField(unique=True, help_text="ссылка")

#         def get_absolute_url(self):
#                 return 'http://%s/gallery/%s/' % (Site.objects.get_current().domain, self.slug)

#         def __unicode__(self):
#                 return self.title

#         class Meta:
#                 verbose_name_plural = "Галерея"

class GalleryImage(models.Model):
    image = ImageField("Картинка", upload_to='gallery/images', help_text="Каритинка, .jpg, .png")
    title = models.CharField("Нащвание картинки", max_length=500, help_text="Заголовок", blank=True)

    # gallery = models.ForeignKey('gallery.Gallery', help_text="Галерея")

    def get_title(self):
        return self.title if self.title else u'No name'

    class Meta:
        verbose_name_plural = "Картинки"