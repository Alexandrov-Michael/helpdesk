# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.contrib.auth.models import Group, User
from proj import settings

def run():

    #создаем группу для компаний

    comapny_group, created = Group.objects.get_or_create(name = settings.COMPANY_GROUP_NAME)
    reports_group, created = Group.objects.get_or_create(name = settings.GROUP_REPORT_ADMIN)

    #создаем пользователя для выбора всех компаний

    user_all, created2 = User.objects.get_or_create(username = settings.USER_MESS_FOR_ALL_COMPANY)
    user_all.first_name = u'Для всех ваших компаний'
    pass_for_user_all = 'gji34PF5400jjsaiiiqwekvf45a'
    user_all.set_password(pass_for_user_all)
    user_all.save()

    admin = User.objects.get(pk=1)
    admin.first_name = u'Главный куратор'
    admin.goups.add(reports_group)
    admin.save()

