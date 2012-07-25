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
    login           = forms.CharField(label=u'Логин', max_length=30)
    password1       = forms.CharField(widget=forms.PasswordInput(), label=u'Пароль', max_length=128)
    password2       = forms.CharField(widget=forms.PasswordInput(), label=u'Подтверждение пароля', max_length=128)
    email           = forms.EmailField()
    first_name      = forms.CharField(label=u'Имя', max_length=30)
    last_name       = forms.CharField(label=u'Фамилия', max_length=30)
    telefon         = forms.CharField(label=u'Телефон', max_length=18)
    is_super_user   = forms.BooleanField(label=u'Суперпользователь', required=False)
    is_report       = forms.BooleanField(label=u'Доступ к отчетам', required=False)



class AddFileForm(forms.Form):
    """
    Форма добавления файла
    """
    file = forms.FileField(max_length=100, allow_empty_file=False)


class CreateCompanyForm(forms.Form):
    """
    Форма для создания компании
    """
    login           = forms.CharField(label=u'Логин', max_length=30)
    password1       = forms.CharField(widget=forms.PasswordInput(), label=u'Пароль', max_length=128)
    password2       = forms.CharField(widget=forms.PasswordInput(), label=u'Подтверждение пароля', max_length=128)
    first_name      = forms.CharField(label=u'Наименование', max_length=30)