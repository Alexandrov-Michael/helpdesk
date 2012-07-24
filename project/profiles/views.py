# -*- coding:utf-8 -*-
from models import Profile
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from company.Forms import CreateUserForm
from django.contrib.auth.models import User
from django.db.models.base import ValidationError
from django.views.generic.list import ListView
from django.core.urlresolvers import reverse


class CreateUserView(FormView):
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

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user_profile.is_super_user:
            return super(CreateUserView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

    def form_valid(self, form):
        login           = form.cleaned_data['login']
        password1       = form.cleaned_data['password1']
        password2       = form.cleaned_data['password2']
        email           = form.cleaned_data['email']
        first_name      = form.cleaned_data['first_name']
        last_name       = form.cleaned_data['last_name']
        is_super_user   = form.cleaned_data['is_super_user']
        is_report       = form.cleaned_data['is_report']
        telefon         = form.cleaned_data['telefon']
        if password1 != password2:
            return super(CreateUserView, self).form_invalid(form)
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
            self.error_msg = u'Такой логин уже существует'
            return super(CreateUserView, self).form_invalid(form)
        new_user.save()
        new_profile = Profile(
            user=new_user,
            is_company=False,
            is_report=is_report,
            is_super_user=is_super_user,
            telefon=telefon,
        )
        new_profile.save()
        return super(CreateUserView,self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['user_is_company'] = self.user_profile.is_company
        context['user_is_report']  = self.user_profile.is_report
        context['user_is_super']  = self.user_profile.is_super_user
        context['error_msg']  = self.error_msg
        return context


class UserListView(ListView):
    """
    Представления для отображения все сотрудников
    """
    template_name = 'user_list.html'
    model = User
    context_object_name = 'users'
    paginate_by = 40

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user_profile.is_super_user:
            return super(UserListView, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['user_is_company'] = self.user_profile.is_company
        context['user_is_report']  = self.user_profile.is_report
        context['user_is_super']  = self.user_profile.is_super_user
        return context

    def get_queryset(self):
        queryset = User.objects.order_by('username').select_related('profile').filter(profile__is_company=False)
        return queryset

