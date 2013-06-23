# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
import datetime
import random
import re

def random_slug():
    return random.randint(0, 999999)

class Tag(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    slug = models.SlugField(unique=True, help_text="Ссылка")

    def get_absolute_url(self):
        return 'http://%s/tag/%s/' % (Site.objects.get_current().domain, self.slug)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Тэги"


class Post(models.Model):
    title = models.CharField(max_length=300, help_text="Заголовок")
    slug = models.SlugField(default=random_slug, unique=True, help_text="Ссылка")

    post = models.TextField(help_text="Содержание")

    TYPE_OF_POST = (
        ('movie', 'Фильмы'),
        ('reports', 'Репортажи'),
        ('news', 'Новости'),
        ('clip', 'Клипы'),
    )
    type_post = models.CharField("Тип Записи", max_length=20, choices=TYPE_OF_POST)

    draft = models.BooleanField('Опубликовать?', default=False)
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    tags = models.ManyToManyField('Tag', related_name='Tag')

    def get_description(self):
        if '!more' in self.post:
            post = self.post.replace('!more', '<!--more-->')
            post = re.sub(r'(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', \
            r"""<figure><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", post)
            more = u'<div class="post_more"><a href="/post/%s/">Подробности..</a></div>' % self.slug
            a = post.split("<!--more-->")
            a.insert(1, more)
            return a[0] + a[1]
        else:
            return re.sub(r'(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', \
            r"""<figure><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", self.post)

    def get_post(self):
        post = self.post.replace('!more', '<!--more-->')
        post = re.sub(r'(?mu)\[(?P<url>.*)\s*\|\s*(?P<name>.*)\s*\|\s*(?P<desc>.*)\]', \
            r"""<figure><img src="\g<url>" alt="\g<name>" /><figcaption>\g<desc></figcaption></figure>""", post)
        return post

    def get_absolute_url(self):
        # return 'http://%s/post/%s/' % (Site.objects.get_current().domain, self.slug)
        return '/post/%s/' % self.slug

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Запись в блог"