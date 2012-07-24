# -*- coding:utf-8 -*-
from models import CompanyPC, Company, CompanyAdmins, PcOptionListHistory, PcOptionsList, PcOptions, Departments
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from Forms import ChangePcOptionForm, AddPcOptionForPCForm, AddCompanyPcForm, AddPcOptionsForm, AddDepartamentForm, AddFileForm
from django.http import Http404
from django.core.urlresolvers import reverse
from profiles.models import Profile
from files.models import Files





from django.shortcuts import render
def test(request):
    return render(request, 'ok.html', locals())

##################################################################################
#### Static views ####
##################################################################################



class GetPcFrom(ListView):
    """
    Предсталвение которое доет список селектов для аякса список пк для отпраки вопроса


    optimized 20120705
    """
    model = CompanyPC
    context_object_name = u'pc'
    template_name = u'ajax_pc_from.html'

    def get_queryset(self):
        queryset = CompanyPC.objects.filter(company__com_user = self.user)
        return queryset

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(GetPcFrom, self).dispatch(request, *args, **kwargs)


class PcDetail(ListView):
    """
    Представление для детализации информации о ПК

    optimized 20120705
    """
    template_name = 'pc_detail.html'
    model = PcOptionsList
    context_object_name = 'options'
    pk_url_kwarg  = 'pk'
    paginate_by = 40


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(PcDetail, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        pk = self.get_pk()
        try:
            self.pc = CompanyPC.objects.select_related('company__com_user__first_name').get(pk = pk)
        except CompanyPC.DoesNotExist:
            raise Http404
        queryset = PcOptionsList.objects.select_related('option__name').filter(pc = self.pc)
        return queryset

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_context_data(self, **kwargs):
        context = super(PcDetail, self).get_context_data(**kwargs)
        context['pc'] = self.pc
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class AddPcOption(FormView):
    """
    Представление для добавления характеристики к ПК

    optimized 20120705
    """
    form_class = AddPcOptionForPCForm
    template_name = 'add_pc_option.html'
    success_url = None
    pk_url_kwarg  = 'pk'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(AddPcOption, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_parent_obj(self):
        pk = self.get_pk()
        try:
            obj = CompanyPC.objects.get(pk=pk)
        except CompanyPC.DoesNotExist:
            raise Http404
        return obj

    def form_valid(self, form):
        option  = form.cleaned_data['option']
        body    = form.cleaned_data['body']
        self.pc = self.get_parent_obj()
        user    = self.user
        new_option = PcOptionsList(
            pc = self.pc,
            option = option,
            body = body,
            user = user,
        )
        new_option.save()
        new_history_opt = PcOptionListHistory(
            pc = self.pc,
            option = option,
            body = body,
            user = user,
        )
        new_history_opt.save()
        return super(AddPcOption, self).form_valid(form)


    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddPcOption, self).get_context_data(**kwargs)
        context['pc_pk'] = self.get_pk()
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class PcOptionHistoryView(ListView):
    """
    Предсталение для вывода истории по ПК

    optimized 20120705
    """
    template_name = 'get_history_to_pc_options.html'
    pk_url_kwarg  = 'pk'
    model = PcOptionListHistory
    context_object_name = 'options'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(PcOptionHistoryView, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_queryset(self):
        pk = self.get_pk()
        try:
            self.pc = CompanyPC.objects.select_related('company__com_user__first_name').get(id = pk)
        except CompanyPC.DoesNotExist:
            raise Http404
        queryset = PcOptionListHistory.objects.filter(pc = self.pc)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PcOptionHistoryView, self).get_context_data(**kwargs)
        context['pc'] = self.pc
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class AddCompanyPcView(CreateView):
    """
    представление для добавления ПК

    optimized 20120705
    """
    form_class = AddCompanyPcForm
    template_name = 'add_pc_to_company.html'
    success_url = None

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(AddCompanyPcView, self).dispatch(request, *args, **kwargs)


    def get_success_url(self):
        url = reverse('/pc_detail', args=[self.object.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddCompanyPcView, self).get_context_data(**kwargs)
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class ChangePcOption(UpdateView):
    """
    Предсталение для формы изменения характеритики ПК

    optimized 20120705
    """
    form_class = ChangePcOptionForm
    success_url = None
    template_name = 'change_pc_option.html'
    model = PcOptionsList

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company', 'profile__is_report').get(pk = request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(ChangePcOption, self).dispatch(request, *args, **kwargs)


    def get_object(self, queryset=None):
        obj = super(ChangePcOption, self).get_object(queryset=None)
        self.pc = obj.pc.id
        return obj

    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc])
        return url


    def get_context_data(self, **kwargs):
        context = super(ChangePcOption, self).get_context_data(**kwargs)
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context

    def form_valid(self, form):
        self.object.user = self.user
        pc      = self.object.pc
        option  = self.object.option
        body    = self.object.body
        user    = self.user
        new_row = PcOptionListHistory(pc = pc, option=option, body=body, user=user)
        new_row.save()
        return super(ChangePcOption, self).form_valid(form)


class PcList(TemplateView):
    """
    представление с выбором компании на нем и подгрузкой с другого
    представления аяксом список ПК для изменения

    optimized 20120705
    """
    template_name = 'pc_list.html'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company', 'profile__is_report').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(PcList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(PcList, self).get_context_data(**kwargs)
        context['user_is_company'] = self.user.profile.is_company
        context['user_is_report']  = self.user.profile.is_report
        return context


class ShortCompanyNameListView(ListView):
    """
    Представление для получения списка сокращений по вопросам для компаний

    optimized 20120705
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'short_name_company.html'
    paginate_by = 40

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(ShortCompanyNameListView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Company.objects.select_related('com_user__username', 'com_user__first_name').all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ShortCompanyNameListView, self).get_context_data(**kwargs)
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class AddPcOptionForAllView(CreateView):
    """
    Представление для добавления характеристики ПК

    optimized 20120705
    """
    form_class = AddPcOptionsForm
    template_name = 'add_option_pc_for_all_pc.html'
    success_url = None
    pk_url_kwarg  = 'pk'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(AddPcOptionForAllView, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_success_url(self):
        self.pk = self.get_pk()
        url = reverse('add_option', args=[self.pk] )
        return url

    def get_context_data(self, **kwargs):
        self.pk = self.get_pk()
        context = super(AddPcOptionForAllView, self).get_context_data(**kwargs)
        context['pc_pk'] = self.pk
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class AddDepartamentView(CreateView):
    """
    Представление для добавления вида отдела
    """
    form_class = AddDepartamentForm
    template_name = 'add_departament.html'
    success_url = '/'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        """
        Проверка юзера на наличие статуса компании
        """
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(AddDepartamentView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Передаю в шаблон переменные для отображения меню
        """
        context = super(AddDepartamentView, self).get_context_data(**kwargs)
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context


class AddFileForPcView(FormView):
    """
    Представление для добавления файла к ПК
    """
    form_class      = AddFileForm
    template_name   = 'add_file_to_pc.html'
    success_url     = None
    pk_url_kwarg    = 'pk'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user_profile.is_company:
            raise Http404
        return super(AddFileForPcView, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_parent_obj(self):
        pk = self.get_pk()
        try:
            obj = CompanyPC.objects.get(pk=pk)
        except CompanyPC.DoesNotExist:
            raise Http404
        return obj

    def form_valid(self, form):
        self.pc = self.get_parent_obj()
        file = form.cleaned_data['file']
        new_file = Files(content_object=self.pc, name=file.name, file=file, size=file.size)
        new_file.save()
        return super(AddFileForPcView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddFileForPcView, self).get_context_data(**kwargs)
        context['pc_pk'] = self.get_pk()
        context['user_is_company'] = False
        context['user_is_report']  = self.user.profile.is_report
        return context



##################################################################################
### Ajax views ###
##################################################################################


class GetCompanyTo(ListView):
    """
    представление которое возвращает список компаний которых данный админ курирует аякс

    optimized 20120705
    """
    model = CompanyAdmins
    context_object_name = u'companys'
    template_name = u'ajax_get_company_for_admin.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user.profile.is_company:
            raise Http404
        return super(GetCompanyTo, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.user_profile.is_super_user:
            queryset = CompanyAdmins.objects.select_related('company__com_user__id', 'company__com_user__first_name').order_by('company.id').distinct('company')
        else:
            queryset = CompanyAdmins.objects.filter(username=self.user).select_related('company__com_user__id', 'company__com_user__first_name').order_by('company.id').distinct('company')
        return queryset


class GetCompanyForPcList(GetCompanyTo):
    """
    Аякс предсталвение для отображения доступных компаний насдуется от списка из создания вопроса
    """

    def get_context_data(self, **kwargs):
        context = super(GetCompanyForPcList, self).get_context_data(**kwargs)
        context['block_for_all'] = True
        return context


class GetPcForPcList(ListView):
    """
    аякс представление для получения списка пк по выбранной фирме

    optimized 20120705
    """
    template_name = 'ajax_get_pc_for_list.html'
    model = CompanyPC
    context_object_name = 'pc_list'
    company_url_kwarg  = 'company'
    dep_url_kwarg = 'dep'
    paginate_by = 40

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(GetPcForPcList, self).dispatch(request, *args, **kwargs)

    def get_user_kwargs(self):
        company_user_pk = self.kwargs.get(self.company_url_kwarg, None)
        dep_pk = self.kwargs.get(self.dep_url_kwarg, None)
        if company_user_pk is None or dep_pk is None:
            raise Http404
        if company_user_pk == '0':
            company_user_pk = None
        if dep_pk == '0':
            dep_pk = None
        return [company_user_pk, dep_pk]


    def get_queryset(self):
        company_user_pk, dep_pk = self.get_user_kwargs()
        queryset = None
        if company_user_pk:
            try:
                com_user = User.objects.select_related('company').get(pk = company_user_pk)
            except User.DoesNotExist:
                raise Http404
            queryset = CompanyPC.objects.filter(company=com_user.company).select_related('departament__name')
        if dep_pk:
            try:
                dep = Departments.objects.get(pk = dep_pk)
            except Departments.DoesNotExist:
                raise Http404
            if queryset:
                queryset = queryset.filter(departament = dep)
            else:
                queryset = CompanyPC.objects.filter(departament = dep)
        if queryset is None:
            raise Http404
        return queryset


class GetOptionsForAdd(ListView):
    """
    Ajax представление для отображения списка доступных для создания характеристик ПК

    optimized 20120705
    """
    template_name = 'ajax_get_options_for_add.html'
    pk_url_kwarg  = 'pk'
    model = PcOptions
    context_object_name = 'options'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(GetOptionsForAdd, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_queryset(self):
        pk          = self.get_pk()
        pc_options  = PcOptionsList.objects.filter(pc__id = pk).values_list('option')
        new_options = PcOptions.objects.exclude(id__in = pc_options)
        return new_options


class GetCompanyForPcAddView(ListView):
    """
    Ajax представление для получения списка компаний в представление по добавлению ПК


    optimized 20120705
    """
    model = CompanyAdmins
    context_object_name = u'company_admins_list'
    template_name = 'ajax_get_company_for_pc_add.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user_profile.is_company:
            raise Http404
        return super(GetCompanyForPcAddView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.user_profile.is_super_user:
            queryset = CompanyAdmins.objects.select_related('company__id', 'company__com_user__first_name').order_by('company.id').distinct('company')
        else:
            queryset = CompanyAdmins.objects.select_related('company__id', 'company__com_user__first_name').filter(username = self.user).order_by('company.id').distinct('company')
        return queryset


class GetDepartamentForPcListView(ListView):
    """
    Представление для вывода отделов в компании

    optimized 20120705
    """
    model = CompanyPC
    context_object_name = 'comPcList'
    template_name = 'ajax_get_departament_for_pc_list.html'
    pk_url_kwarg  = 'pk'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        if self.user.profile.is_company:
            raise Http404
        return super(GetDepartamentForPcListView, self).dispatch(request, *args, **kwargs)

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404

    def get_queryset(self):
        pk = self.get_pk()
        try:
            com_user = User.objects.select_related('company').get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        queryset = CompanyPC.objects.filter(company=com_user.company.id).select_related('departament__id', 'departament__name').order_by('departament.id').distinct('departament')
        return queryset


class GetUserTo(ListView):
    """
    Представление возвращает список кому отправлять вопрос для аякса
    если это пользователь который состоит в группе company то возвращает
    админов данной компании, если это админ то показывает всех админов

    optimized 20120705
    """
    model = User
    context_object_name = u'users'
    template_name = None
    template_for_company = u'ajax_users_to_for_company.html'
    template_for_admins = u'ajax_users_to_for_admins.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = User.objects.select_related('profile__is_company').get(pk=request.user.id)
        return super(GetUserTo, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        if self.user.profile.is_company:
            queryset = CompanyAdmins.objects.select_related('username__id', 'username__first_name', 'username__last_name', 'post__id', 'post__name').filter(company__com_user = self.user).order_by('username.id').distinct('username')
        else:
            queryset = User.objects.exclude(profile__is_company = True).exclude(username=self.user.username)
        return queryset


    def get_template_names(self):
        if self.user.profile.is_company:
            template = self.template_for_company
        else:
            template = self.template_for_admins
        return template


