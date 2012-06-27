# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from company.models import CompanyPC, User



class EditQuestionUser(forms.Form):
    """
    Форма для добавления вопроса для компаний
    """
    worker_from = forms.CharField(label=u'Ваше ФИО')
    #будет браться через ajax
    user_from   = forms.ModelChoiceField(queryset=CompanyPC.objects.all(), label=u'От кого')

    #будет формироваться через ajax
    user_to   = forms.ModelChoiceField(queryset=User.objects.all(), label=u'Кому')
    body      = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')



class EditQuestionAdmin(forms.Form):
    """
    Форма для добавления вопроса для админов
    """
    #будет браться через ajax
    user_to    = forms.ModelChoiceField(queryset=User.objects.all(), label=u'Кому')
    body      = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')


class ChatForm(forms.Form):
    """
    Форма чата в вопросе
    """

    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}), label=u'Сообщение')

