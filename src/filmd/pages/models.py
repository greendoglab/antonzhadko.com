# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
import datetime
import random
import re

class Page(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    slug = models.SlugField(unique=True, help_text="Ссылка")

    post = models.TextField(help_text="Содержание")

    draft = models.BooleanField('Опубликовать?', default=False)
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    def get_post(self):
        post = self.post.replace('!more', '<!--more-->')
        post = re.sub(r'(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', \
            r"""<figure><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", post)
        return post

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Страницы"