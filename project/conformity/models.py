# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic



class Conform(models.Model):
    """
    Модель соответсвия данных
    """
    perem           = models.CharField(u'Наименование',max_length=50)
    content_type    = models.ForeignKey(ContentType)
    object_id       = models.PositiveIntegerField()
    content_object  = generic.GenericForeignKey('content_type', 'object_id')

    class Meta:
        verbose_name = u'Таблица соответсвий'
        verbose_name_plural = u'Таблицы соответствий'

    def __unicode__(self):
        return self.perem
