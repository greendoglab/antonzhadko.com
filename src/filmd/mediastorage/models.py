# -*-coding: utf-8 -*-
from django.db import models
import datetime
import os.path
from sorl.thumbnail import ImageField

class ImageStorage(models.Model):
    title = models.CharField(blank=True, max_length=300, help_text="Заголовок")
    description = models.TextField(blank=True, help_text="Описание")
    image = ImageField("Картинка", upload_to='images')
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Файлы: Картинки"

class FileStorage(models.Model):
    ufile = models.FileField("Файл", upload_to='files')
    date = models.DateTimeField('Дата', default=datetime.datetime.now)

    class Meta:
        ordering = ['-date']
        verbose_name_plural = "Файлы: Разное(pdf, doc, etc..)"