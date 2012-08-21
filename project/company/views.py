# -*- coding:utf-8 -*-
from models import CompanyPC, Company, CompanyAdmins, PcOptionListHistory, PcOptionsList, PcOptions, Departments, Posts
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, FormView, CreateView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.models import User
from Forms import ChangePcOptionForm, AddPcOptionForPCForm, AddCompanyPcForm, AddPcOptionsForm, AddDepartamentForm, AddFileForm, AddPostForm, EditPostForm
from django.http import Http404
from django.core.urlresolvers import reverse
from files.models import Files
from proj.utils.mixin import LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin, JSONQuerySetValuesResponseMixin, JSONResponseMixin
from datetime import datetime
from django.utils.timezone import now



##################################################################################
#### test views ####
##################################################################################






class test(LoginRequiredMixin, TemplateView):
    """
    тест представление
    """
    template_name = 'ok.html'

    def get_context_data(self, **kwargs):
        context = super(test, self).get_context_data(**kwargs)
        context['profile'] = self.user_profile
        return context






##################################################################################
#### Static views ####
##################################################################################






class PcDetail(LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin, ListView):
    """
    Представление для детализации информации о ПК

    tested
    """
    template_name = 'pc_detail.html'
    model = PcOptionsList
    context_object_name = 'options'
    paginate_by = 40


    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        pk = self.get_pk()
        try:
            self.pc = CompanyPC.objects.select_related('company__com_user__first_name').get(pk = pk)
        except CompanyPC.DoesNotExist:
            raise Http404
        queryset = PcOptionsList.objects.select_related('option__name').filter(pc = self.pc)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(PcDetail, self).get_context_data(**kwargs)
        context['pc'] = self.pc
        return self.update_context(context)


class AddPcOption(LoginRequiredMixin, GetOdjectMixin, UpdateContextDataMixin, FormView):
    """
    Представление для добавления характеристики к ПК

    tested
    """
    form_class = AddPcOptionForPCForm
    template_name = 'add_pc_option.html'
    success_url = None

    def do_before_handler(self):
        self.skip_only_user()
        self.pc = self.get_parent_obj()


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
        user    = self.user
        new_option = PcOptionsList(
            pc = self.pc,
            option = option,
            body = body,
            user = user,
            date=now(),
        )
        new_option.save()
        new_history_opt = PcOptionListHistory(
            pc = self.pc,
            option = option,
            body = body,
            user = user,
            date=now(),
        )
        new_history_opt.save()
        self.set_message(u'Характеристика успешно добавлена.')
        return super(AddPcOption, self).form_valid(form)


    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddPcOption, self).get_context_data(**kwargs)
        context['pc_pk'] = self.get_pk()
        return self.update_context(context)


class PcOptionHistoryView(LoginRequiredMixin, GetOdjectMixin, UpdateContextDataMixin, ListView):
    """
    Предсталение для вывода истории по ПК

    optimized 20120726
    """
    template_name = 'get_history_to_pc_options.html'
    model = PcOptionListHistory
    context_object_name = 'options'

    def do_before_handler(self):
        self.skip_only_user()

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
        return self.update_context(context)


class AddCompanyPcView(LoginRequiredMixin, UpdateContextDataMixin, CreateView):
    """
    представление для добавления ПК

    optimized 20120726
    """
    form_class = AddCompanyPcForm
    template_name = 'add_pc_to_company.html'
    success_url = None

    def do_before_handler(self):
        self.skip_only_user()


    def get_success_url(self):
        url = reverse('pc_detail', args=[self.object.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddCompanyPcView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def form_valid(self, form):
        self.set_message(u'Компьютер успешно добавлен.')
        return super(AddCompanyPcView, self).form_valid(form)


class ChangePcOption(LoginRequiredMixin, UpdateContextDataMixin, UpdateView):
    """
    Предсталение для формы изменения характеритики ПК

    optimized 20120726
    """
    form_class = ChangePcOptionForm
    success_url = None
    template_name = 'change_pc_option.html'
    model = PcOptionsList

    def do_before_handler(self):
        self.skip_only_user()


    def get_object(self, queryset=None):
        obj = super(ChangePcOption, self).get_object(queryset=None)
        self.pc = obj.pc.id
        return obj

    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc])
        return url


    def get_context_data(self, **kwargs):
        context = super(ChangePcOption, self).get_context_data(**kwargs)
        return self.update_context(context)

    def form_valid(self, form):
        self.object.user = self.user
        pc      = self.object.pc
        option  = self.object.option
        body    = self.object.body
        user    = self.user
        self.object.date = now()
        new_row = PcOptionListHistory(pc = pc, option=option, body=body, user=user, date=now())
        new_row.save()
        self.set_message(u'Характеристика успешно изменена')
        return super(ChangePcOption, self).form_valid(form)


class PcList(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    представление с выбором компании на нем и подгрузкой с другого
    представления аяксом список ПК для изменения

    optimized 20120726
    """
    template_name = 'pc_list.html'


    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        context = super(PcList, self).get_context_data(**kwargs)
        return self.update_context(context)


class ShortCompanyNameListView(LoginRequiredMixin, UpdateContextDataMixin, ListView):
    """
    Представление для получения списка сокращений по вопросам для компаний

    optimized 20120726
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'short_name_company.html'
    paginate_by = 40

    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        queryset = Company.objects.select_related('com_user__username', 'com_user__first_name').all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ShortCompanyNameListView, self).get_context_data(**kwargs)
        return self.update_context(context)


class AddPcOptionForAllView(LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin, CreateView):
    """
    Представление для добавления характеристики ПК

    optimized 20120726
    """
    form_class = AddPcOptionsForm
    template_name = 'add_option_pc_for_all_pc.html'
    success_url = None

    def do_before_handler(self):
        self.skip_only_user()

    def get_success_url(self):
        self.pk = self.get_pk()
        url = reverse('add_option', args=[self.pk] )
        return url

    def get_context_data(self, **kwargs):
        self.pk = self.get_pk()
        context = super(AddPcOptionForAllView, self).get_context_data(**kwargs)
        context['pc_pk'] = self.pk
        return self.update_context(context)

    def form_valid(self, form):
        self.set_message(u'Характеристика успешно добавлена.')
        return super(AddPcOptionForAllView, self).form_valid(form)


class AddDepartamentView(LoginRequiredMixin, UpdateContextDataMixin, CreateView):
    """
    Представление для добавления вида отдела

    tested
    """
    form_class = AddDepartamentForm
    template_name = 'add_departament.html'
    success_url = None
    model = Departments

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        """
        Передаю в шаблон переменные для отображения меню
        """
        context = super(AddDepartamentView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_success_url(self):
        url = reverse('dep_list', args=[])
        result_url = u'%s?company=%s' % (url, self.object.company.pk, )
        return result_url

    def form_valid(self, form):
        self.set_message(u'Отдел успешно добавлен.')
        return super(AddDepartamentView, self).form_valid(form)


class EditDepartamentView(LoginRequiredMixin, UpdateContextDataMixin, UpdateView):
    """
    Представление для изменения отдела

    tested
    """
    form_class = AddDepartamentForm
    template_name = 'edit_department.html'
    success_url = None
    model = Departments

    def do_before_handler(self):
        """
        Пропускаем только пользователей сотрудников компании предаставляющей услуги
        """
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        """
        Добавляем в контекст ответа переменные для корректного отображения меню
        """
        context = super(EditDepartamentView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_success_url(self):
        """
        Определяем урл для удачного изменения, подставлем гет параметр id компании в которой был отдел,
        чтобы не обнулялся выбор пользователя
        """
        url = reverse('dep_list', args=[])
        result_url = u'%s?company=%s' % (url, self.object.company.pk, )
        return result_url


    def form_valid(self, form):
        self.set_message(u'Отдел успешно изменен.')
        return super(EditDepartamentView, self).form_valid(form)


class AddFileForPcView(LoginRequiredMixin, GetOdjectMixin, UpdateContextDataMixin, FormView):
    """
    Представление для добавления файла к ПК
    """
    form_class      = AddFileForm
    template_name   = 'add_file_to_pc.html'
    success_url     = None


    def do_before_handler(self):
        self.skip_only_user()


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
        new_file = Files(content_object=self.pc, name=file.name, file=file, size=file.size, date=now())
        new_file.save()
        self.set_message(u'Файл успешно добавлен.')
        return super(AddFileForPcView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('pc_detail', args=[self.pc.id])
        return url

    def get_context_data(self, **kwargs):
        context = super(AddFileForPcView, self).get_context_data(**kwargs)
        context['pc_pk'] = self.get_pk()
        return self.update_context(context)


class DepartamentsListView(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    Список отделов в компаниях
    """
    template_name = 'dep_list.html'

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        context = super(DepartamentsListView, self).get_context_data(**kwargs)
        return self.update_context(context)




class AddPostView(LoginRequiredMixin, UpdateContextDataMixin, FormView):
    """
    Представление для добавления должности
    """
    form_class = AddPostForm
    template_name = 'add_post.html'
    success_url = None

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(AddPostView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def form_valid(self, form):
        name               = form.cleaned_data['name']
        description        = form.cleaned_data['description']
        new_obj            = Posts()
        new_obj.name       = name
        new_obj.decription = description
        new_obj.save()
        self.set_message(u'Должность успешно добавлена.')
        return super(AddPostView, self).form_valid(form)

    def get_success_url(self):
        url = reverse('posts_list', args=[])
        return url


class PostsListView(LoginRequiredMixin, UpdateContextDataMixin, ListView):
    """
    Представление списка должностей
    """
    model = Posts
    template_name = 'posts_list.html'
    context_object_name = 'posts'

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(PostsListView, self).get_context_data(**kwargs)
        return self.update_context(context)


class PostEditView(LoginRequiredMixin, UpdateContextDataMixin, UpdateView):
    """
    Предсталение для изменение должности
    """
    form_class = EditPostForm
    template_name = 'edit_post.html'
    success_url = None
    model = Posts

    def do_before_handler(self):
        self.skip_only_super_user()

    def get_context_data(self, **kwargs):
        context = super(PostEditView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_success_url(self):
        url = reverse('posts_list', args=[])
        return url

    def form_valid(self, form):
        self.set_message(u'Должность успешно изменена.')
        return super(PostEditView, self).form_valid(form)













##################################################################################
### Ajax views ###
##################################################################################



class GetPcFrom(LoginRequiredMixin, ListView):
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



class GetCompanyForPcList(LoginRequiredMixin, View, JSONResponseMixin):
    """
    Аякс предсталвение для отображения доступных компаний насдуется от списка из создания вопроса

    tested
    """

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        result = []
        if self.user_profile.is_super_user:
            queryset = User.objects.exclude(profile__is_company = False)
            for item in queryset:
                interim = {}
                interim['id'] = item.id
                interim['name'] = item.first_name
                result.append(interim)
        else:
            queryset = CompanyAdmins.objects.filter(username=self.user).select_related('company__com_user__id', 'company__com_user__first_name').order_by('company.id').distinct('company')
            for item in queryset:
                interim = {}
                interim['id'] = item.company.com_user.id
                interim['name'] = item.company.com_user.first_name
                result.append(interim)
        return result


class GetPcForPcList(LoginRequiredMixin, ListView):
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

    def do_before_handler(self):
        self.skip_only_user()

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


class GetOptionsForAdd(LoginRequiredMixin, GetOdjectMixin, ListView):
    """
    Ajax представление для отображения списка доступных для создания характеристик ПК

    optimized 20120705
    """
    template_name = 'ajax_get_options_for_add.html'
    model = PcOptions
    context_object_name = 'options'

    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        pk          = self.get_pk()
        pc_options  = PcOptionsList.objects.filter(pc__id = pk).values_list('option')
        new_options = PcOptions.objects.exclude(id__in = pc_options)
        return new_options


class GetCompanyForPcAddView(LoginRequiredMixin, View, JSONResponseMixin):
    """
    Ajax представление для получения списка компаний в представление по добавлению ПК


    optimized 20120705
    """

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        result = {}
        if self.user_profile.is_super_user:
            queryset = Company.objects.all().select_related('com_user')
            for item in queryset:
                result[item.id] = item.com_user.first_name
        else:
            queryset = CompanyAdmins.objects.select_related('company__id', 'company__com_user__first_name').filter(username = self.user).order_by('company.id').distinct('company')
            for item in queryset:
                result[item.company.id] = item.company.com_user.first_name
        return result


class GetDepartamentForPcListView(LoginRequiredMixin, GetOdjectMixin, View, JSONQuerySetValuesResponseMixin):
    """
    Представление для вывода отделов в компании
    """

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, *args, **kwargs):
        pk = self.get_pk()
        try:
            com_user = User.objects.select_related('company', 'profile').get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        if not com_user.profile.is_company:
            raise Http404
        queryset = Departments.objects.filter(company=com_user.company.id).values('id', 'name')
        return queryset






class GetCompanyForAddDepartametView(LoginRequiredMixin, View, JSONResponseMixin ):
    """
    Ajax Представление для получения списка компаний для пользователя

    tested
    """

    def do_before_handler(self):
        self.skip_only_user()


    def get_context_data(self, **kwargs):
        result = []
        if self.user_profile.is_super_user:
            queryset = Company.objects.select_related('com_user').values('id', 'com_user__first_name')
            if queryset:
                for item in queryset:
                    item_result = {}
                    item_result['id'] = item['id']
                    item_result['name'] = item['com_user__first_name']
                    result.append(item_result)
        else:
            queryset = CompanyAdmins.objects.filter(username=self.user).select_related('company__com_user', 'company').order_by('company.id').distinct('company').values('company__id', 'company__com_user__first_name')
            if queryset:
                for item in queryset:
                    item_result = {}
                    item_result['id'] = item['company__id']
                    item_result['name'] = item['company__com_user__first_name']
                    result.append(item_result)
        return result


class GetDepartamentsForDeplistView(LoginRequiredMixin, JSONQuerySetValuesResponseMixin, GetOdjectMixin, View):
    """
    Ajax представление для получения списка отделов в компании

    tested
    """

    def do_before_handler(self):
        self.skip_only_user()

    def get_object(self):
        pk = self.get_pk()
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
        return company

    def get_context_data(self, **kwargs):
        company = self.get_object()
        queryset = Departments.objects.filter(company=company).values('id', 'name')
        return queryset


class GetDepartamentsForAddPCView(LoginRequiredMixin, JSONQuerySetValuesResponseMixin, GetOdjectMixin, View):
    """
    Ajax представление для получения списка отделов в компании для добавления ПК

    tested
    """

    def do_before_handler(self):
        self.skip_only_user()

    def get_object(self):
        pk = self.get_pk()
        try:
            company = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
        return company

    def get_context_data(self, **kwargs):
        company = self.get_object()
        queryset = Departments.objects.filter(company=company).values('id','name')
        return queryset


class GetPostsForQuestionAddView(LoginRequiredMixin, View, GetOdjectMixin, JSONResponseMixin):
    """
    Ajax предсталвение для получения должности сотрудника в данной компании для вопроса

    tested
    """

    def get_object(self):
        pk = self.get_pk()
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404
        return user

    def get_context_data(self, **kwargs):
        result = {}
        user = self.get_object()
        if self.user_profile.is_super_user:
            queryset = Posts.objects.all().values('id', 'decription')
            for item in queryset:
                result[item['id']] = u'%s ...' % (item['decription'][:60],)
            return result
        elif self.user_profile.is_company:
            queryset = CompanyAdmins.objects.select_related('post', 'company__com_user').filter(username = user, company = self.user.company)
            queryset = queryset.values('post__id', 'post__decription')
            for item in queryset:
                result[item['post__id']] = u'%s ...' % (item['post__decription'][:60],)
            return result
        else:
            if user.profile.is_company:
                queryset = CompanyAdmins.objects.filter(username=self.user, company = user.company)
                queryset = queryset.values('post__id', 'post__decription')
                for item in queryset:
                    result[item['post__id']] = u'%s ...' % (item['post__decription'][:60],)
                return result
            else:
                queryset = Posts.objects.all().values('id', 'decription')
                for item in queryset:
                    result[item['id']] = u'%s ...' % (item['decription'][:60],)
                return result


class GetPcFromForAddQues(LoginRequiredMixin, GetOdjectMixin, View, JSONResponseMixin):
    """
    Ajax представление для получения компьютера по отделу

    tested
    """

    def get_object(self):
        """
        получение отдела из гет параметра
        """
        pk = self.get_pk()
        try:
            dep = Departments.objects.get(pk=pk)
        except Departments.DoesNotExist:
            raise Http404
        return dep

    def get_context_data(self, **kwargs):
        """
        получение данных для возврата
        """
        result = {}
        dep = self.get_object()
        pc_from = CompanyPC.objects.filter(departament=dep)
        for item in pc_from:
            result[item.id] = u'%s %s' % (item.pc_nameId, item.pc_name,)
        return result