# -*- coding:utf-8 -*-
__author__ = 'michael'
import models
from django.contrib import admin


class ChatInLine(admin.StackedInline):
    model = models.Chat


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('slug', 'date', 'user_from', 'pc_from', 'user_to', 'user_check' )
    list_display_links = ('slug', 'date', 'user_from', 'pc_from', 'user_to')
    inlines = [
        ChatInLine,
        ]

admin.site.register(models.Chat)
admin.site.register(models.Questions, QuestionAdmin)
