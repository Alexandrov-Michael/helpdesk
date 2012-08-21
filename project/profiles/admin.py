# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.contrib import admin
import models

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('get_user_id', 'get_username', 'is_company')

    def get_user_id(self, obj):
        return u'%s' % (obj.user.id)
    get_user_id.short_description = 'User id'

    def get_username(self, obj):
        return u'%s %s' % (obj.user.first_name, obj.user.last_name)
    get_username.short_description = 'User'

admin.site.register(models.Profile, ProfileAdmin)