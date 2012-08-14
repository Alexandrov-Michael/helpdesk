__author__ = 'michael'

from django.contrib import admin
import models


class SimpleWikiAdmin(admin.ModelAdmin):
    list_display = ('date', 'title')
    ordering = ['-date']

admin.site.register(models.SimpleWiki, SimpleWikiAdmin)
