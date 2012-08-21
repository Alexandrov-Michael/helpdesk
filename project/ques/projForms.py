# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from company.models import CompanyPC, User, Posts, Departments, CompanyAdmins, Company
from django.http import Http404
from proj.utils.formUtils import ModelChoiceFieldForUserTo
from django.db.models import Q



class EditQuestionUser(forms.Form):
    """
    Форма для добавления вопроса для компаний
    """
    def __init__(self, user, *args, **kwargs):
        try:
            company = Company.objects.get(com_user=user)
        except Company.DoesNotExist:
            raise Http404
        departments = Departments.objects.filter(company = company)
        companyAdmins = CompanyAdmins.objects.filter(company = company).select_related('username').order_by('username.id').distinct('username')
        ids_user_to = []
        for item in companyAdmins:
            ids_user_to.append(item.username.id)
        user_to = User.objects.filter(id__in = ids_user_to)


        user_from = CompanyPC.objects.filter(company = company).order_by('pc_nameId')

        super(EditQuestionUser, self).__init__(*args, **kwargs)
        self.fields['department'].queryset = departments
        self.fields['user_to'].queryset = user_to
        self.fields['user_from'].queryset = user_from


    worker_from = forms.CharField(label=u'Ваше ФИО')
    department  = forms.ModelChoiceField(queryset=None, label=u'Отдел')
    user_from   = forms.ModelChoiceField(queryset=None, label=u'От кого')
    user_to     = ModelChoiceFieldForUserTo(queryset=None, label=u'Кому')
    post        = forms.ModelChoiceField(queryset=Posts.objects.all(), label=u'Тема')
    body        = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')



class EditQuestionAdmin(forms.Form):
    """
    Форма для добавления вопроса для админов
    """

    def __init__(self, user, *args, **kwargs):
        if user.profile.is_super_user:
            user_to = User.objects.exclude(id = user.id).order_by('profile__is_company')
        else:
            user_ids = []
            company_admins = CompanyAdmins.objects.filter(username=user)
            for item in company_admins:
                user_ids.append(item.company.com_user.id)
            user_to = User.objects.filter((~Q(id = user.id) & ~Q(profile__is_company = True)) | Q(id__in = user_ids)).order_by('profile__is_company')
        super(EditQuestionAdmin, self).__init__(*args, **kwargs)
        self.fields['user_to'].queryset = user_to



    for_all = forms.BooleanField(label=u'Для всех ваших компаний', required=False)
    user_to = ModelChoiceFieldForUserTo(queryset=None, label=u'Кому', required=False)
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



class EditQuestionForKuratorForm(forms.Form):
    """
    Форма для изменения тела вопроса
    """
    body = forms.CharField(widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}), label=u'Вопрос')

