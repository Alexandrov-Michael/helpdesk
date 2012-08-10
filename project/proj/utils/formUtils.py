# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.forms.widgets import SelectMultiple, CheckboxInput
from django.utils.encoding import force_unicode
from itertools import chain
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User
from django.forms import forms
from django.forms.models import ModelChoiceField

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


class FormsCleanUtils(object):
    """
    Микшин для проверки форм
    """

    def check_passwords(self, cleaned_data):
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')
        if password1 != password2:
            mess = u'Пароли не совпадают'
            raise forms.ValidationError(mess)

    def check_login_to_unique(self, cleaned_data):
        login = cleaned_data.get('login')
        check_fist_2_letter_for_login = User.objects.filter(username__startswith=login[:2])
        if check_fist_2_letter_for_login:
            mess = u'Логин не подходит уникальность по сокращениям (не уникальны первые 2 сивола логин)'
            raise forms.ValidationError(mess)

    def check_email_to_unique(self, cleaned_data):
        email = cleaned_data.get('email')
        check_email_unique = User.objects.filter(email__iexact=email)
        if check_email_unique:
            mess = u'Такой email уже зарегистрирован'
            raise forms.ValidationError(mess)


class ModelChoiceFieldForUserTo(ModelChoiceField):
    """
    Поле для формы перенаправления вопроса
    """
    def label_from_instance(self, obj):
        return "%s %s" % (obj.first_name, obj.last_name,)


class QuestionPostModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.decription