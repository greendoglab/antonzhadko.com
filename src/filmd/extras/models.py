# -*-coding: utf-8-*-
from django.db import models
from django.contrib.sites.models import Site
import datetime
import os.path
from sorl.thumbnail import ImageField

class Menu(models.Model):
    title = models.CharField(max_length=300, help_text="Menu")
    slug = models.CharField(max_length=300)
    order = models.IntegerField(help_text="цифра")

    def get_absolute_url(self):
        return 'http://%s/%s' % (Site.objects.get_current().domain, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['order']
        verbose_name_plural = "Меню"


class Meta(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    description = models.TextField(blank=True, help_text="Описание")
    keywords = models.TextField(blank=True, help_text="Ключевые слова")

    date = models.DateTimeField('Дата', default=datetime.datetime.now)  

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Метатэги"


class SiteTitle(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    description = models.TextField(blank=True, help_text="Описание")

    date = models.DateTimeField('Дата', default=datetime.datetime.now)  

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Заголовок Сайта"

class MyPhoto(models.Model):
    image = ImageField(upload_to='images')
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Фото"