# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic


class Files(models.Model):
    """
    Модель для прикрепленных файлов
    """
    name            = models.CharField(max_length=100)
    file            = models.FileField(upload_to='files')
    date            = models.DateTimeField(auto_now_add=True)
    size            = models.PositiveIntegerField()
    content_type    = models.ForeignKey(ContentType)
    object_id       = models.PositiveIntegerField()
    content_object  = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Файл'
        verbose_name_plural = u'Файлы'
        ordering = ['date']

