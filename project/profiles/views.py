# -*- coding:utf-8 -*-
from models import Profile
from django.views.generic.edit import FormView
from django.views.generic.base import View
from django.http import Http404
from company.Forms import CreateUserForm, CreateCompanyForm, AddCompanyAdminsForUserForm, AddCompanyAdminsForCompanyForm
from django.contrib.auth.models import User
from django.db.models.base import ValidationError
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse
from company.models import Posts, Company, CompanyAdmins
from proj.utils.mixin import JSONResponseMixin, LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin, SummMixen



##############################################################
### Static views
##############################################################

class CreateUserView(LoginRequiredMixin, UpdateContextDataMixin, FormView):
    """
    Представление для создания пользователя и профайла
    """

    form_class = CreateUserForm
    success_url = None
    template_name = 'add_user.html'
    error_msg = None

    def get_success_url(self):
        url = reverse('user_list', args=[])
        return url

    def do_before_handler(self):
        self.skip_only_super_user()

    def form_valid(self, form):
        login           = form.cleaned_data['login']
        password1       = form.cleaned_data['password1']
        email           = form.cleaned_data['email']
        first_name      = form.cleaned_data['first_name']
        last_name       = form.cleaned_data['last_name']
        is_super_user   = form.cleaned_data['is_super_user']
        is_report       = form.cleaned_data['is_report']
        telefon         = form.cleaned_data['telefon']
        image           = form.cleaned_data['image']
        new_user = User(
            username=login,
            first_name=first_name,
            last_name=last_name,
            email=email,
        )
        new_user.set_password(password1)
        try:
            new_user.full_clean()
        except ValidationError:
            self.error_msg = u'Не правильно заполненна форма'
            return super(CreateUserView, self).form_invalid(form)
        new_user.save()
        new_profile = Profile(
            user=new_user,
            is_company=False,
            is_report=is_report,
            is_super_user=is_super_user,
            telefon=telefon,
            image=image,
        )
        new_profile.save()
        self.set_success_message(u'Пользователь успешно добавлен.')
        return super(CreateUserView,self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['error_msg']  = self.error_msg
        return self.update_context(context)


class UserListView(LoginRequiredMixin, UpdateContextDataMixin, ListView):
    """
    Представления для отображения все сотрудников
    """
    template_name = 'user_list.html'
    model = User
    context_object_name = 'users'
    paginate_by = 40

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_queryset(self):
        queryset = User.objects.order_by('username').select_related('profile').filter(profile__is_company=False)
        return queryset


class CompanyListView(UserListView):
    """
    Представление для получения списка компаний
    """
    template_name = 'company_list.html'

    def get_queryset(self):
        queryset = User.objects.order_by('username').select_related('profile').filter(profile__is_company=True)
        return queryset


class CreateCompanyView(LoginRequiredMixin, UpdateContextDataMixin, FormView):
    """
    Представление для создания компании и профайла
    """

    form_class = CreateCompanyForm
    success_url = None
    template_name = 'add_company.html'
    error_msg = None

    def get_success_url(self):
        url = reverse('company_list', args=[])
        return url

    def do_before_handler(self):
        self.skip_only_super_user()

    def form_valid(self, form):
        login           = form.cleaned_data['login']
        password1       = form.cleaned_data['password1']
        first_name      = form.cleaned_data['first_name']
        image           = form.cleaned_data['image']
        new_user = User(
            username=login,
            first_name=first_name,
        )
        new_user.set_password(password1)
        try:
            new_user.full_clean()
        except ValidationError:
            self.error_msg = u'Не правильно заполненна форма'
            return super(CreateCompanyView, self).form_invalid(form)
        new_user.save()
        new_profile = Profile(
            user=new_user,
            is_company=True,
            is_report=False,
            is_super_user=False,
            image=image,
        )
        new_profile.save()
        new_company = Company(com_user=new_user)
        new_company.save()
        self.set_success_message(u'Компания успешно добавлена.')
        return super(CreateCompanyView,self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreateCompanyView, self).get_context_data(**kwargs)
        context['error_msg']  = self.error_msg
        return self.update_context(context)


class AddCompanyAdminsForUserView(LoginRequiredMixin, GetOdjectMixin, UpdateContextDataMixin, FormView):
    """
    Форма для добавления кураторства у сотрудников


    доделать выбор пользователя
    """
    form_class = AddCompanyAdminsForUserForm
    success_url = None
    template_name = 'add_companyadmins_for_user.html'


    def get_object(self):
        self.pk = self.get_pk()
        try:
            user = User.objects.get(pk=self.pk)
        except User.DoesNotExist:
            raise Http404
        return user

    def do_before_handler(self):
        self.skip_only_super_user()


    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                })
        user_companyadmins = CompanyAdmins.objects.filter(username=self.user_to).select_related('company', 'post')
        companys = user_companyadmins.order_by('company.id').distinct('company')
        user_posts = {}
        if companys:
            for one_com in companys:
                posts = user_companyadmins.filter(company=one_com.company)
                user_posts[one_com.company.id] = []
                for one_post in posts:
                    user_posts[one_com.company.id].append(one_post.post.id)
        kwargs['companys'] = self.get_companys()
        kwargs['user_posts'] = user_posts
        return kwargs

    def get_posts(self):
        posts = Posts.objects.all().order_by('id')
        return posts

    def get_companys(self):
        companys = Company.objects.all().select_related()
        return companys

    def get_success_url(self):
        url = reverse('companyadmins_for_user', args=[self.pk])
        return url

    def form_valid(self, form):
        CompanyAdmins.objects.filter(username=self.user_to).delete()
        for field_name, field_value in form.cleaned_data.iteritems():
            company = Company.objects.get(pk=field_name)
            if len(field_value) > 1:
                for one_value in field_value:
                    post = Posts.objects.get(pk=one_value)
                    new_companyadmins= CompanyAdmins(
                        username=self.user_to,
                        company=company,
                        post=post,
                    )
                    new_companyadmins.save()
            else:
                if field_value:
                    post = Posts.objects.get(pk=field_value[0])
                    new_companyadmins= CompanyAdmins(
                        username=self.user_to,
                        company=company,
                        post=post,
                    )
                    new_companyadmins.save()
        self.set_success_message(u'Кураторство успешно добавлено.')
        return super(AddCompanyAdminsForUserView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.user_to = self.get_object()
        return super(AddCompanyAdminsForUserView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.user_to = self.get_object()
        return super(AddCompanyAdminsForUserView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddCompanyAdminsForUserView, self).get_context_data(**kwargs)
        context['pk']=self.pk
        context['user_to'] = self.user_to
        context['posts'] = self.get_posts()
        return self.update_context(context)


class CompanyAdminsForUserListView(LoginRequiredMixin, GetOdjectMixin, UpdateContextDataMixin, ListView):
    """
    представление для списка компаний в которых работает сотрудник
    """

    template_name = 'companyadmins_list_for_user.html'
    model = CompanyAdmins
    context_object_name = 'companyAdmins'

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(CompanyAdminsForUserListView, self).get_context_data(**kwargs)
        context['posts'] = self.get_posts()
        context['table'] = self.table
        context['user_to'] = self.user_to
        return self.update_context(context)

    def get_object(self):
        try:
            user = User.objects.get(pk=self.pk)
        except User.DoesNotExist:
            raise Http404
        return user

    def get_queryset(self):
        self.pk = self.get_pk()
        self.user_to = self.get_object()
        self.init_posts()
        queryset = CompanyAdmins.objects.select_related().filter(username=self.user_to)
        if not queryset:
            return queryset
        companys = queryset.order_by('company.id').distinct('company').select_related('company', 'post', 'company__com_user__first_name')
        for one_com in companys:
            user_posts = queryset.filter(company=one_com.company)
            posts_for_company = self.posts_dict.copy()
            for one_post in user_posts:
                posts_for_company[one_post.post.id] = True
            self.table[one_com.company.com_user.first_name]= posts_for_company
        return queryset



    def get_posts(self):
        posts = Posts.objects.all().order_by('id')
        return posts

    def init_posts(self):
        self.table = {}
        self.posts_dict = {}
        posts = Posts.objects.all().order_by('id')
        for item in posts:
            self.posts_dict[item.id] = False


class CompanyAdminsForCompanyListView(SummMixen, ListView):
    """
    представление для списка сотрудников в компании
    """

    template_name = 'companyadmins_list_for_company.html'
    model = CompanyAdmins
    context_object_name = 'companyAdmins'

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(CompanyAdminsForCompanyListView, self).get_context_data(**kwargs)
        context['posts'] = self.get_posts()
        context['table'] = self.table
        context['user_to'] = self.company
        return self.update_context(context)


    def get_object(self):
        try:
            user = User.objects.get(pk=self.pk)
            company = Company.objects.get(com_user=user)
        except User.DoesNotExist:
            raise Http404
        except Company.DoesNotExist:
            raise Http404
        return company

    def get_queryset(self):
        self.pk = self.get_pk()
        self.company = self.get_object()
        self.init_posts()
        queryset = CompanyAdmins.objects.select_related().filter(company=self.company)
        if not queryset:
            return queryset
        comadmins = queryset.order_by('username.id').distinct('username').select_related('post')
        for one_admin in comadmins:
            user_posts = queryset.filter(username=one_admin.username)
            posts_for_company = self.posts_dict.copy()
            for one_post in user_posts:
                posts_for_company[one_post.post.id] = True
            self.table[one_admin.username]= posts_for_company
        return queryset



    def get_posts(self):
        posts = Posts.objects.all().order_by('id')
        return posts

    def init_posts(self):
        self.table = {}
        self.posts_dict = {}
        posts = Posts.objects.all().order_by('id')
        for item in posts:
            self.posts_dict[item.id] = False


class AddCompanyAdminsForCompanyView(SummMixen, FormView):
    """
    Форма для добавления кураторства у сотрудников


    доделать выбор пользователя
    """
    form_class = AddCompanyAdminsForCompanyForm
    success_url = None
    template_name = 'add_companyadmins_for_company.html'

    def get_object(self):
        self.pk = self.get_pk()
        try:
            user = User.objects.get(pk=self.pk)
            company = Company.objects.get(com_user=user)
        except User.DoesNotExist:
            raise Http404
        except Company.DoesNotExist:
            raise Http404
        return company

    def do_before_handler(self):
        self.skip_only_super_user()


    def get_form_kwargs(self):
        kwargs = {'initial': self.get_initial()}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
                'data': self.request.POST,
                'files': self.request.FILES,
                })
        user_companyadmins = CompanyAdmins.objects.filter(company=self.user_to).select_related('post', 'username')
        com_admins = user_companyadmins.order_by('username.id').distinct('username')
        user_posts = {}
        if com_admins:
            for one_user in com_admins:
                posts = user_companyadmins.filter(username=one_user.username)
                user_posts[one_user.username.id] = []
                for one_post in posts:
                    user_posts[one_user.username.id].append(one_post.post.id)
        kwargs['users_admins'] = self.get_users_admins()
        kwargs['user_posts'] = user_posts
        return kwargs

    def get_posts(self):
        queryset = Posts.objects.all().order_by('id')
        return queryset

    def get_users_admins(self):
        queryset = User.objects.select_related('profile').filter(profile__is_company=False)
        return queryset

    def get_success_url(self):
        url = reverse('companyadmins_for_company', args=[self.pk])
        return url

    def form_valid(self, form):
        CompanyAdmins.objects.filter(company=self.user_to).delete()
        for field_name, field_value in form.cleaned_data.iteritems():
            user = User.objects.get(pk=field_name)
            if len(field_value) > 1:
                for one_value in field_value:
                    post = Posts.objects.get(pk=one_value)
                    new_companyadmins= CompanyAdmins(
                        company=self.user_to,
                        username=user,
                        post=post,
                    )
                    new_companyadmins.save()
            else:
                if field_value:
                    post = Posts.objects.get(pk=field_value[0])
                    new_companyadmins= CompanyAdmins(
                        company=self.user_to,
                        username=user,
                        post=post,
                    )
                    new_companyadmins.save()
        self.set_success_message(u'Кураторство успешно добавлено.')
        return super(AddCompanyAdminsForCompanyView, self).form_valid(form)

    def get(self, request, *args, **kwargs):
        self.user_to = self.get_object()
        return super(AddCompanyAdminsForCompanyView, self).get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.user_to = self.get_object()
        return super(AddCompanyAdminsForCompanyView, self).post(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AddCompanyAdminsForCompanyView, self).get_context_data(**kwargs)
        context['pk']=self.pk
        context['user_to'] = self.user_to
        context['posts'] = self.get_posts()
        return self.update_context(context)



##############################################################
### Ajax views
##############################################################




class GetProfileImgView(JSONResponseMixin, LoginRequiredMixin, GetOdjectMixin, View):
    """
    Ajax для получения адреса картинки из профиля
    """

    def get_object(self, pk):
        try:
            odj = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        return odj

    def get_context_data(self, **kwargs):
        pk = self.get_pk()
        user = self.get_object(pk)
        user_profile = Profile.objects.get(user=user)
        if user_profile.image:
            img = user_profile.image.url
        else:
            img = False
        return {
            'img_src' : img,
        }