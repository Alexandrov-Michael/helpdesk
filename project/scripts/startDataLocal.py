# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.contrib.auth.models import User


def run():

    mypass = u'123'


    alexandrov = User.objects.get(username = u'alexandrov')
    alexandrov.set_password(mypass)
    alexandrov.save()

    ivanov = User.objects.get(username = u'ivanov')
    ivanov.set_password(mypass)
    ivanov.save()

    petrov = User.objects.get(username = u'petrov')
    petrov.set_password(mypass)
    petrov.save()

    sidorov = User.objects.get(username = u'sidorov')
    sidorov.set_password(mypass)
    sidorov.save()

    panev = User.objects.get(username = u'panev')
    panev.set_password(mypass)
    panev.save()

    maslov = User.objects.get(username= 'maslov')
    maslov.set_password('megapass123')
    maslov.save()