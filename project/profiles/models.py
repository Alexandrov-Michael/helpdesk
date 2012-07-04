# -*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    """
    Профайл пользователя
    """
    user    = models.OneToOneField(User, verbose_name=u'Пользователь', related_name='profile')
    telefon = models.CharField(u'Телефон', max_length=18, blank=True)

    def __unicode__(self):
        return self.user

    class Meta:
        verbose_name = u'Профиль'
        verbose_name_plural = u'Профили'
