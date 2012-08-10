# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from company.models import CompanyPC, User, Posts



class EditQuestionUser(forms.Form):
    """
    Форма для добавления вопроса для компаний
    """
    worker_from = forms.CharField(label=u'Ваше ФИО')
    #будет браться через ajax
    user_from   = forms.ModelChoiceField(queryset=CompanyPC.objects.all(), label=u'От кого')

    #будет формироваться через ajax
    user_to   = forms.ModelChoiceField(queryset=User.objects.all(), label=u'Кому')
    post      = forms.ModelChoiceField(queryset=Posts.objects.all(), label=u'Тема')
    body      = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')



class EditQuestionAdmin(forms.Form):
    """
    Форма для добавления вопроса для админов
    """
    #будет браться через ajax
    for_all = forms.BooleanField(label=u'Для всех ваших компаний', required=False)
    user_to = forms.ModelChoiceField(queryset=User.objects.all(), label=u'Кому', required=False)
    post    = forms.ModelChoiceField(queryset=Posts.objects.all(), label=u'Тема', required=False)
    body    = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')

    def clean(self):
        cleaned_data = super(EditQuestionAdmin, self).clean()
        for_all = cleaned_data['for_all']
        user_to = cleaned_data['user_to']
        try:
            post = cleaned_data['post']
        except KeyError:
            post = False
        if not for_all:
            if user_to.profile.is_company:
                if not post:
                    mess = u'Укажите тему вопроса'
                    raise forms.ValidationError(mess)
        if not for_all and not user_to:
            mess = u'Вы не выбрали получателя'
            raise forms.ValidationError(mess)
        if for_all and user_to:
            mess = u'Нельзя выбрать одновременно для всех и отдельно для компании'
            raise forms.ValidationError(mess)
        return cleaned_data


class ChatForm(forms.Form):
    """
    Форма чата в вопросе
    """

    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 5}), label=u'Сообщение')
    file = forms.FileField(max_length=100, allow_empty_file=False, label=u'Прикрепить файл', required=False)

