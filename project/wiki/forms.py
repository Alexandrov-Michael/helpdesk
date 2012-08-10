# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from models import SimpleWiki
from tinymce.widgets import TinyMCE

class AddWikiPageForm(forms.ModelForm):
    """
    Форма для создания вики страницы
    """

    body = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}), label=u'Содержание')

    class Meta:
        model = SimpleWiki
