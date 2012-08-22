# -*- coding:utf-8 -*-
__author__ = 'michael'
from proj.utils.formUtils import FormsCleanUtils
from django import forms



class EditUserlogin(forms.Form, FormsCleanUtils ):
    """
    Форма для наследования
    """
    def __init__(self, user, profile, *args, **kwargs):
        super(EditUserlogin, self).__init__(*args, **kwargs)
        self.user = user
        self.profile = profile
        self.initial = {
            'login' : user.username,
            'image' : profile.image
        }


    login = forms.RegexField(label=u'Логин', max_length=30, regex=r'^[\w.@+-]+$',)
    image = forms.ImageField(required=False, label=u'Изображение')


    def clean(self):
        cleaned_data = super(EditUserlogin, self).clean()
        login = cleaned_data['login']
        if login != self.user.username:
            self.check_login_to_unique(cleaned_data)
        return cleaned_data




class EditUserForm(EditUserlogin):
    """
    Форма для изменения пользователя
    """

    def __init__(self, user, profile, *args, **kwargs):
        super(EditUserForm, self).__init__(user, profile, *args, **kwargs)
        self.initial.update({
            'email': user.email,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'telefon': profile.telefon,
            'is_super_user': profile.is_super_user,
            'is_report': profile.is_report,
        })
        self.base_fields.keyOrder = ['login','first_name', 'last_name','email', 'telefon' ,'is_report', 'is_super_user','is_buh','image']

    email           = forms.EmailField()
    first_name      = forms.CharField(label=u'Имя', max_length=30)
    last_name       = forms.CharField(label=u'Фамилия', max_length=30)
    telefon         = forms.CharField(label=u'Телефон', max_length=18)
    is_super_user   = forms.BooleanField(label=u'Суперпользователь', required=False)
    is_report       = forms.BooleanField(label=u'Доступ к отчетам', required=False)
    is_buh          = forms.BooleanField(label=u'Это бухгалтер', required=False)

    def clean(self):
        cleaned_data = super(EditUserForm, self).clean()
        email = cleaned_data['email']
        if email != self.user.email:
            self.check_email_to_unique(cleaned_data)
        return cleaned_data


class EditCompanyForm(EditUserlogin):
    """
    Форма для изменение компании
    """
    def __init__(self, user, profile, *args, **kwargs):
        super(EditCompanyForm, self).__init__(user, profile, *args, **kwargs)
        self.initial.update({
            'first_name': user.first_name,
            })
        self.base_fields.keyOrder = ['login','first_name','image']


    first_name = forms.CharField(label=u'Наименование', max_length=30)
