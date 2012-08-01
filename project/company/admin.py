# -*- coding:utf-8 -*-
__author__ = 'michael'

import models
from django.contrib import admin

class CompanyAdminsAdmin(admin.ModelAdmin):
    list_display = ('company', 'username', 'post')
    list_display_links = list_display
    ordering = ['company']


class CompanyPcInLine(admin.StackedInline):
    model = models.CompanyPC

class CompanyAdminsInLine(admin.StackedInline):
    model = models.CompanyAdmins

class CompanyAdmin(admin.ModelAdmin):
    inlines = [
        CompanyAdminsInLine,
        CompanyPcInLine,
        ]

admin.site.register(models.Company, CompanyAdmin)
admin.site.register(models.CompanyAdmins, CompanyAdminsAdmin)
admin.site.register(models.CompanyPC)
admin.site.register(models.Posts)
admin.site.register(models.PcOptionListHistory)
admin.site.register(models.PcOptions)
admin.site.register(models.PcOptionsList)
admin.site.register(models.Departments)