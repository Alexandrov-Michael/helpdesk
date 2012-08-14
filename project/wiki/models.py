# -*- coding:utf-8 -*-
from django.db import models

class SimpleWiki(models.Model):
    """
    Модель для простой вики
    """
    title = models.CharField(u'Заголовок', max_length=200)
    date  = models.DateTimeField(u'Дата изменения', auto_now=True)
    body  = models.TextField(u'Содержание')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u'Стараница вики'
        verbose_name_plural = u'Страницы вики'

