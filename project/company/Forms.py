# -*- coding:utf-8 -*-
__author__ = 'michael'

from django import forms
from models import PcOptionsList, PcOptions, CompanyPC, Departments, Posts
from proj.utils.formUtils import MyCheckboxSelectMultiple, FormsCleanUtils, ModelChoiceFieldForUserTo
from django.contrib.auth.models import User






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


class CreateUserlogin(forms.Form, FormsCleanUtils ):
    """
    Форма для наследования
    """
    login           = forms.CharField(label=u'Логин', max_length=30)
    password1       = forms.CharField(widget=forms.PasswordInput(), label=u'Пароль', max_length=128)
    password2       = forms.CharField(widget=forms.PasswordInput(), label=u'Подтверждение пароля', max_length=128)
    image           = forms.ImageField(required=False, label=u'Изображение')


    def clean(self):
        cleaned_data = super(CreateUserlogin, self).clean()
        self.check_passwords(cleaned_data)
        self.check_login_to_unique(cleaned_data)
        return cleaned_data




class CreateUserForm(CreateUserlogin):
    """
    Форма для создания пользователя
    """

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.base_fields.keyOrder = ['login','password1','password2','first_name', 'last_name','email', 'telefon' ,'is_report', 'is_super_user','image']

    email           = forms.EmailField()
    first_name      = forms.CharField(label=u'Имя', max_length=30)
    last_name       = forms.CharField(label=u'Фамилия', max_length=30)
    telefon         = forms.CharField(label=u'Телефон', max_length=18)
    is_super_user   = forms.BooleanField(label=u'Суперпользователь', required=False)
    is_report       = forms.BooleanField(label=u'Доступ к отчетам', required=False)

    def clean(self):
        cleaned_data = super(CreateUserForm, self).clean()
        self.check_email_to_unique(cleaned_data)
        return cleaned_data




class AddFileForm(forms.Form):
    """
    Форма добавления файла
    """
    file = forms.FileField(max_length=100, allow_empty_file=False)


class CreateCompanyForm(CreateUserlogin):
    """
    Форма для создания компании
    """
    def __init__(self, *args, **kwargs):
        super(CreateCompanyForm, self).__init__(*args, **kwargs)
        self.base_fields.keyOrder = ['login','password1','password2','first_name','image']

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


class AddCompanyAdminsForCompanyForm(forms.Form):
    """
    Добавленеие кураторов для пользователя

    """

    def __init__(self, *args, **kwargs):
        initial_data = None
        # Админы данной фирмы, модель User
        users_admins = kwargs.pop('users_admins')
        # Словарь списков, ключи - это User.id админа, значения список должностей
        user_posts = kwargs.pop('user_posts')
        CHOICES = Posts.objects.order_by('id').values_list('id', 'name')
        super(AddCompanyAdminsForCompanyForm, self).__init__( *args, **kwargs)
        for item_user in users_admins:
            if user_posts:
                initial_data = user_posts.get(item_user.id, None)
            self.fields['%s' % (item_user.id)] = forms.MultipleChoiceField(
                widget = MyCheckboxSelectMultiple(),
                choices=CHOICES,
                required=False,
                label=u'%s %s' % (item_user.last_name, item_user.first_name,),

                initial=initial_data,
            )




class ChangeUserToForQuesForm(forms.Form):
    """
    Форма для перенаправления вопроса
    """

    def __init__(self, user, *args, **kwargs):
        super(ChangeUserToForQuesForm, self).__init__(*args, **kwargs)
        self.user = user
        self.fields['user_to'].queryset = self.get_queryset()


    def get_queryset(self):
        queryset = User.objects.select_related('profile').filter(profile__is_company=False).exclude(pk = self.user.pk)
        return queryset

    user_to = ModelChoiceFieldForUserTo(queryset=None, label=u'Перенаправить сотруднику:')



class AddPostForm(forms.Form):
    """
    Форма для добавления должности
    """
    name       = forms.CharField(label=u'Наименование', max_length=100, error_messages={'required':u'Заполните наименование'})
    description = forms.CharField(label=u'Описание', error_messages={'required':u'Заполните описание'}, widget=forms.Textarea(attrs={'cols': 70, 'rows': 10}))

    def clean(self):
        cleaned_data = super(AddPostForm, self).clean()
        try:
            name = cleaned_data['name']
        except KeyError:
            return cleaned_data
        try:
            Posts.objects.get(name = name)
        except Posts.DoesNotExist:
            return cleaned_data
        self._errors['name'] = self.error_class([u'Такая должность уже существует'])
        return cleaned_data



class EditPostForm(forms.ModelForm):
    """
    Форма для изменения должности
    """
    class Meta:
        model = Posts

