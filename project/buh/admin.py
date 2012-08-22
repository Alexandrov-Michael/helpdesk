# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.contrib import admin
import models


class ContractsAdmin(admin.ModelAdmin):
    list_display = ('company', 'name')


class AccountigAdmin(admin.ModelAdmin):
    list_display = ('get_company','contract', 'month', 'year','paid')

    def get_company(self, obj):
        return u'%s' % (obj.contract.company.com_user.first_name,)
    get_company.short_description = u'Компания'


admin.site.register(models.Accounting, AccountigAdmin)
admin.site.register(models.Contracts, ContractsAdmin)
