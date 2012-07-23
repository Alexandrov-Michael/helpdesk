# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from models import PcOptionsList, PcOptions, CompanyPC, Departments

class ChangePcOptionForm(forms.ModelForm):
    """
    Форма для зменения храктеристики ПК
    """
    class Meta:
        model = PcOptionsList
        fields = ('body', )

class AddPcOptionForPCForm(forms.Form):
    """
    Форма для добавления характеристики ПК
    """
    option  = forms.ModelChoiceField(queryset=PcOptions.objects.all(), label=u'Характеристика')
    body    = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Значение')

class AddCompanyPcForm(forms.ModelForm):
    """
    Форма для добавления ПК
    """
    class Meta:
        model = CompanyPC


class AddPcOptionsForm(forms.ModelForm):
    """
    Форма для добавления характеристики ПК
    """
    class Meta:
        model = PcOptions


class AddDepartamentForm(forms.ModelForm):
    """
    Форма для добавления отдела
    """
    class Meta:
        model = Departments
        widgets = {
            'name': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            }


class CreateUserForm(forms.Form):
    """
    Форма для создания пользователя
    """
    login           = forms.CharField(label=u'Логин')
#    password        = forms
    first_name      = forms.CharField(label=u'Имя')
    last_name       = forms.CharField(label=u'Фамилия')
    is_super_user   = forms.BooleanField(label=u'Суперпользователь')
    is_report       = forms.BooleanField(label=u'Доступ к отчетам')
    telefon         = forms.CharField(label=u'Телефон')