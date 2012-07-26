# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from models import PcOptionsList, PcOptions, CompanyPC, Departments
from company.models import Posts
from django.forms import widgets
from django.forms.widgets import SelectMultiple, CheckboxInput
from django.utils.encoding import force_unicode
from itertools import chain
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe




class MyCheckboxSelectMultiple(SelectMultiple):
    def render(self, name, value, attrs=None, choices=()):
        if value is None: value = []
        has_id = attrs and 'id' in attrs
        final_attrs = self.build_attrs(attrs, name=name)
        output = []
        # Normalize to strings
        str_values = set([force_unicode(v) for v in value])
        for i, (option_value, option_label) in enumerate(chain(self.choices, choices)):
            # If an ID attribute was given, add a numeric index as a suffix,
            # so that the checkboxes don't all have the same ID attribute.
            if has_id:
                final_attrs = dict(final_attrs, id='%s_%s' % (attrs['id'], i))
                label_for = u' for="%s"' % final_attrs['id']
            else:
                label_for = ''

            cb = CheckboxInput(final_attrs, check_test=lambda value: value in str_values)
            option_value = force_unicode(option_value)
            rendered_cb = cb.render(name, option_value)
            option_label = conditional_escape(force_unicode(option_label))
            output.append(u'<td class="input_td">%s</td>' % (rendered_cb,))
        return mark_safe(u'\n'.join(output))

    def id_for_label(self, id_):
        # See the comment for RadioSelect.id_for_label()
        if id_:
            id_ += '_0'
        return id_


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






class AddCompanyAdminsForUserForm(forms.Form):
    """
    Добавленеие кураторов для пользователя

    """

    def __init__(self, *args, **kwargs):
        initial_data = None
        companys = kwargs.pop('companys')
        user_posts = kwargs.pop('user_posts')
        CHOICES = Posts.objects.order_by('id').values_list('id', 'name')
        super(AddCompanyAdminsForUserForm, self).__init__( *args, **kwargs)
        for item_com in companys:
            if user_posts:
                initial_data = user_posts.get(item_com.id, None)
            self.fields['%s' % (item_com.id)] = forms.MultipleChoiceField(
                widget = MyCheckboxSelectMultiple(),
                choices=CHOICES,
                required=False,
                label=item_com.com_user.first_name,

                initial=initial_data,
            )

