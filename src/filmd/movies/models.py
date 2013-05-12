# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
import datetime


class Movie(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    slug = models.SlugField(unique=True, help_text="Ссылка")
    description = models.TextField(blank=True, help_text="Описание")
    keywords = models.TextField(blank=True, help_text="Ключевые слова")

    post = models.TextField(help_text="Содержание")

    draft = models.BooleanField('Опубликовать?', default=False)
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Фильм"