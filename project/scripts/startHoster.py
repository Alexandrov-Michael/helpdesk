# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.contrib.auth.models import User
from profiles.models import Profile

def run():
    admin = User.objects.get(pk=1)
    admin.first_name = u'Главный куратор'
    admin.save()
    admin_profile = Profile(user=admin, is_company=False, is_report=True, is_super_user=True, telefon = '+7 921 9142583')
    admin_profile.save()
