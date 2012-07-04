# -*- coding:utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from models import Questions, Chat
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from projForms import EditQuestionUser, EditQuestionAdmin, ChatForm
from proj import settings
from django.contrib.auth.models import Group
from django.http import Http404
from company.models import CompanyAdmins, Company, CompanyPC, PcOptionListHistory
from django.contrib.auth.models import User
from datetime import datetime



class IndexView(TemplateView):
    """
    Представление для страртовой страницы, использует шаблон main
    в котором через аякс подхватывается список вопросов данного пользователя
    """

    template_name = 'main.html'
    company_group = settings.COMPANY_GROUP_NAME
    user_is_report_group = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
            self.user_is_report_group = True
        except Group.DoesNotExist:
            pass
        return super(IndexView, self).dispatch(request, *args, **kwargs)

    def is_user_group_company(self):
        try:
            self.user.groups.all().get(name=self.company_group)
            return True
        except Group.DoesNotExist:
            return False

    def get_context_data(self, **kwargs):
        user_is_company = self.is_user_group_company()
        context = super(IndexView, self).get_context_data(**kwargs)
        context['user_is_company'] = user_is_company
        context['user_is_report']  = self.user_is_report_group
        return context




class QuestionList(ListView):
    """
    Представление для списка вопросов, для каждого пользователя
    model - модель на основе которой составляется список
    paginate_by - количество объектов на странице
    context_object_name - переменная в шаблоне
    template_name - шаблон
    get_queryset - получаем список объектов для каждого пользователя
    dispatch - проверяем пользователя зарегестрированан ли
    """

    model = Questions
    paginate_by = 20
    context_object_name = u'questions'
    template_name = u'ajax_get_index_ques.html'

    def get_queryset(self):
        queryset = Questions.objects.filter(Q(user_to = self.user) | Q(user_from = self.user))
        self.non_check_ques = self.get_open_question(queryset)
        return queryset

    def get_open_question(self, queryset):
        if not queryset:
            return 0
        check_count  = queryset.filter(Q(user_check = False)).count()
        return check_count

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(QuestionList, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['non_check_ques'] = self.non_check_ques
        return context



class QuesAdd(FormView):
    """
    Представление формы для добавления вопроса
    """
    form_class = None
    success_url = '/'
    template_name = None
    slug_plus = settings.PLUS_SLUG_FIELD
    all_company_user = settings.USER_MESS_FOR_ALL_COMPANY
    company_group = settings.COMPANY_GROUP_NAME
    user_is_report_group = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
            self.user_is_report_group = True
        except Group.DoesNotExist:
            pass
        return super(QuesAdd, self).dispatch(request, *args, **kwargs)

    def get_form_class(self):
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            self.form_class = EditQuestionUser
            self.template_name = u'add_q.html'
        except Group.DoesNotExist:
            self.form_class = EditQuestionAdmin
            self.template_name = u'add_q_admin.html'
        return self.form_class

    def form_valid(self, form):
        body       = form.cleaned_data['body']
        user_to    = form.cleaned_data['user_to']
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            user_from   = form.cleaned_data['user_from']
            worker_from = form.cleaned_data['worker_from']
            new_question = Questions(
                user_from=self.user,
                pc_from=user_from,
                worker_from=worker_from,
                user_to=user_to,
                body=body,
            )
        except Group.DoesNotExist:
            if user_to.username == self.all_company_user:
                comps = CompanyAdmins.objects.filter(username=self.user).order_by('company.id').distinct('company')
                if comps:
                    for one_comp in comps:
                        new_question = Questions(
                            user_from=self.user,
                            user_to=one_comp.company.com_user,
                            body=body
                        )
                        new_question.save()
                        new_question.slug = new_question.id + self.slug_plus
                        new_question.save()
                    return super(QuesAdd, self).form_valid(form)
                else:
                    return super(QuesAdd, self).form_invalid(form)
            new_question = Questions(
                user_from=self.user,
                user_to=user_to,
                body=body,
            )
        new_question.save()
        new_question.slug = new_question.id + self.slug_plus
        new_question.save()
        return super(QuesAdd, self).form_valid(form)

    def is_user_group_company(self):
        try:
            self.user.groups.all().get(name=self.company_group)
            return True
        except Group.DoesNotExist:
            return False

    def get_context_data(self, **kwargs):
        user_is_company = self.is_user_group_company()
        context = super(QuesAdd, self).get_context_data(**kwargs)
        context['user_is_company'] = user_is_company
        context['user_is_report']  = self.user_is_report_group
        return context


class QuesChatForm(FormView):
    """
    Представление формы для чата в обсуждении вопроса

    """
    form_class = ChatForm
    success_url = None
    template_name = 'ques_chat_form.html'
    pk_url_kwarg = 'pk'
    company_group = settings.COMPANY_GROUP_NAME
    error_msg = None
    user_is_report_group = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
            self.user_is_report_group = True
        except Group.DoesNotExist:
            pass
        return super(QuesChatForm, self).dispatch(request, *args, **kwargs)

    def is_user_group_company(self):
        try:
            self.user.groups.all().get(name=self.company_group)
            return True
        except Group.DoesNotExist:
            return False

    def get_context_data(self, **kwargs):
        user_is_company = self.is_user_group_company()
        kwargs.update({
            'question' : self.question,
            'msgs_set' : self.chat_msgs,
            'user_is_company': user_is_company,
            'error_msg' : self.error_msg,
            'user_is_report': self.user_is_report_group,
        })
        return kwargs


    def get_object(self):
        """
        """
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            try:
                obj = Questions.objects.get(pk=pk)
            except Questions.DoesNotExist:
                obj = Questions.objects.none()
        else:
            obj = Questions.objects.none()
        return obj

    def get_object_depends(self):
        queryset = Chat.objects.filter(question = self.question)
        return queryset

    def get(self, request, *args, **kwargs):
        self.question  = self.get_object()
        self.chat_msgs = self.get_object_depends()
        return super(QuesChatForm, self).get(request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        self.question  = self.get_object()
        self.chat_msgs = self.get_object_depends()
        return super(QuesChatForm, self).post(request, *args, **kwargs)

    def form_valid(self, form):
        if self.question.user_from == self.user:
            self.sender = True
        elif self.question.user_to == self.user:
            self.sender = False
        else:
            self.error_msg = u'Вы не можете добавлять коментарии не ко своим вопросам'
            return self.form_invalid(form)
        body = form.cleaned_data['body']
        if self.sender:
            new_msg = Chat(question=self.question, body=body)
        else:
            new_msg = Chat(question=self.question, body=body, admin_name = self.user)
        new_msg.save()
        return super(QuesChatForm, self).form_valid(form)

    def get_success_url(self):
        url = self.question.get_absolute_url()
        return url



class QuesChangeStatus(TemplateView):
    """
    Представление аякс для изменения статуса вопроса
    """
    pk_url_kwarg = 'pk'
    template_name = 'ok.html'
    post_close_question = 'Close'
    post_open_question = 'Open'
    post_status_question = 'status'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(QuesChangeStatus, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return Http404

    def post(self, request, *args, **kwargs):
        question = self.get_object()
        status   = self.get_status()
        question.user_check = status
        if status:
            question.user_check_date = datetime.now()
        else:
            question.user_check_date = None
        question.save()
        if not self.user == question.user_from and not self.user == question.user_to:
            raise Http404
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)



    def get_object(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            try:
                obj = Questions.objects.get(pk = pk)
            except Questions.DoesNotExist:
                raise Http404
        else:
            raise Http404
        return obj


    def get_status(self):
        status = self.request.POST.get(self.post_status_question, None)
        if status == self.post_close_question:
            return True
        elif status == self.post_open_question:
            return False
        else:
            raise Http404




class GetQuestionForChat(DetailView):
    """
    Представление аякс для получения вопроса на странице чата
    """
    template_name = 'ajax_get_question_for_chat.html'
    model = Questions
    context_object_name = 'question'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(GetQuestionForChat, self).dispatch(request, *args, **kwargs)


class GetButtonForChat(TemplateView):
    """
    Представление аякс для получения кнопки изменения статуса вопроса
    """
    template_name = 'ajax_get_but_for_chat_user.html'
    pk_url_kwarg  = 'pk'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(GetButtonForChat, self).dispatch(request, *args, **kwargs)


    def get_object(self):
        """
        """
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            try:
                obj = Questions.objects.get(pk=pk)
            except Questions.DoesNotExist:
                obj = Questions.objects.none()
        else:
            obj = Questions.objects.none()
        return obj


    def get(self, request, *args, **kwargs):
        self.question  = self.get_object()
        return super(GetButtonForChat, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        kwargs.update({
            'question' : self.question,
            })
        return kwargs


class GetChatMessages(ListView):
    """
    Представление аякс для получения сообщений в чате
    """
    model = Chat
    context_object_name = 'msgs_set'
    template_name = 'ajax_get_chat_mess.html'
    pk_url_kwarg  = 'pk'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(GetChatMessages, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.question = self.kwargs.get(self.pk_url_kwarg, None)
        if self.question is None:
            raise Http404
        return super(GetChatMessages, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = Chat.objects.filter(question = self.question)
        return queryset



class MainReportForQuestionsView(TemplateView):
    """
    Представление для отчетов по вопросам
    """
    template_name = 'main_report_for_ques.html'
    user_is_company_group = False
    user_is_report_group = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            self.user_is_company_group = True
            raise Http404
        except Group.DoesNotExist:
            try:
                self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
                self.user_is_report_group = True
                return super(MainReportForQuestionsView, self).dispatch(request, *args, **kwargs)
            except Group.DoesNotExist:
                raise Http404


    def get_context_data(self, **kwargs):
        context = super(MainReportForQuestionsView, self).get_context_data(**kwargs)
        context['user_is_company'] = self.user_is_company_group
        context['user_is_report']  = self.user_is_report_group
        return context


class GetCompanyListForReportForQuesView(ListView):
    """
    Аякс Представление для получения списка компаний для отчета по вопроса
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'ajax_get_company_for_report_ques.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            return super(GetCompanyListForReportForQuesView, self).dispatch(request, *args, **kwargs)

class GetUserListForReportForQuesView(ListView):
    """
    Аякс представление для получения списка сотрудников для отчета по вопросам
    """
    model = User
    context_object_name = 'users'
    template_name = 'ajax_get_users_for_report_for_ques.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            return super(GetUserListForReportForQuesView, self).dispatch(request, *args, **kwargs)

    def get_queryset(self):
        queryset = User.objects.exclude(pk=1).exclude(groups__name = settings.COMPANY_GROUP_NAME).exclude(username = settings.USER_MESS_FOR_ALL_COMPANY)
        return queryset


class GetReportListForReportForQuesView(ListView):
    """
    Аякс представления для получения вопросов по заданным
    фильтрам для отчета по вопросам
    """
    model = Questions
    context_object_name = 'questions'
    template_name = 'ajax_get_report_list_for_report_ques.html'
    company_post_filter = 'company'
    user_post_filter = 'user'
    paginate_by = 30

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            try:
                self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
                return super(GetReportListForReportForQuesView, self).dispatch(request, *args, **kwargs)
            except Group.DoesNotExist:
                raise Http404

    def get_filters(self):
        self.company_filter = self.kwargs.get(self.company_post_filter, None)
        self.user_filter = self.kwargs.get(self.user_post_filter, None)
        if self.company_filter is not None:
            if self.company_filter == '0':
                self.company_filter = None
        if self.user_filter is not None:
            if self.user_filter == '0':
                self.user_filter = None


    def get(self, request, *args, **kwargs):
        self.get_filters()
        return super(GetReportListForReportForQuesView, self).get(request, *args, **kwargs)


    def get_queryset(self):
        queryset = None
        if self.company_filter is not None:
            try:
                company = User.objects.get(pk = self.company_filter)
            except User.DoesNotExist:
                raise Http404
            queryset = Questions.objects.filter(Q(user_from = company)|Q(user_to = company))
        if self.user_filter is not None:
            try:
                user = User.objects.get(pk = self.user_filter)
            except User.DoesNotExist:
                raise Http404
            if queryset is None:
                queryset = Questions.objects.filter(Q(user_from = user)|Q(user_to = user))
            else:
                queryset = queryset.filter(Q(user_from = user)|Q(user_to = user))
        if queryset is None:
            raise Http404
        self.non_check_ques = self.get_open_question(queryset)
        return queryset

    def get_open_question(self, queryset):
        if not queryset:
            return 0
        check_count  = queryset.filter(Q(user_check = False)).count()
        return check_count


    def get_context_data(self, **kwargs):
        context = super(GetReportListForReportForQuesView, self).get_context_data(**kwargs)
        context['non_check_ques'] = self.non_check_ques
        return context


class MainReportForPcHistoryView(TemplateView):
    """
    Представление для получения отчета по истории изменения хараетристик ПК
    """
    template_name = 'main_report_for_pc_history.html'
    user_is_company_group = False
    user_is_report_group = False

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            self.user_is_company_group = True
            raise Http404
        except Group.DoesNotExist:
            try:
                self.user.groups.all().get(name = settings.GROUP_REPORT_ADMIN)
                self.user_is_report_group = True
                return super(MainReportForPcHistoryView, self).dispatch(request, *args, **kwargs)
            except Group.DoesNotExist:
                raise Http404


    def get_context_data(self, **kwargs):
        context = super(MainReportForPcHistoryView, self).get_context_data(**kwargs)
        context['user_is_company'] = self.user_is_company_group
        context['user_is_report']  = self.user_is_report_group
        return context


class GetPcListForReportPcHistoryView(ListView):
    """
    Аякс представление для получения списка пк в фирме
    """
    model = CompanyPC
    context_object_name = 'pc_list'
    template_name = 'ajax_get_pc_for_report_pc_history.html'
    company_get_filter = 'company'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            return super(GetPcListForReportPcHistoryView, self).dispatch(request, *args, **kwargs)

    def get_filter(self):
        self.company_filter = self.kwargs.get(self.company_get_filter, None)
        if not self.company_filter:
            raise Http404

    def get(self, request, *args, **kwargs):
        self.get_filter()
        return super(GetPcListForReportPcHistoryView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        try:
            company = Company.objects.get(pk = self.company_filter)
        except Company.DoesNotExist:
            raise Http404
        queryset = CompanyPC.objects.filter(company = company)
        return queryset


class GetCompanyListForReportForPcHistoryView(ListView):
    """
    Аякс представление для получения скиска компаний в отчету о изменени характеристик
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'ajax_get_company_for_report_pc_history.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            return super(GetCompanyListForReportForPcHistoryView, self).dispatch(request, *args, **kwargs)


class GetReportForPcHistoryView(ListView):
    """
    Аякс предсталвение для получения отчета по истории измененя характеристик пк
    """
    model = PcOptionListHistory
    context_object_name = 'changes'
    template_name = 'ajax_get_report_for_pc_history.html'
    pc_get_filter = 'pc'
    user_get_filter = 'user'
    company_get_filter = 'company'
    paginate_by = 30

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        try:
            self.user.groups.all().get(name = settings.COMPANY_GROUP_NAME)
            raise Http404
        except Group.DoesNotExist:
            return super(GetReportForPcHistoryView, self).dispatch(request, *args, **kwargs)

    def get_filters(self):
        pc_filter = self.kwargs.get(self.pc_get_filter, None)
        user_filter = self.kwargs.get(self.user_get_filter, None)
        company_filter = self.kwargs.get(self.company_get_filter, None)
        if pc_filter is None or user_filter is None or company_filter is None:
            raise Http404
        if pc_filter == '0':
            self.pc = None
        else:
            try:
                self.pc = CompanyPC.objects.get(pk = pc_filter)
            except CompanyPC.DoesNotExist:
                raise Http404
        if user_filter == '0':
            self.user_obj = None
        else:
            try:
                self.user_obj = User.objects.get(pk = user_filter)
            except User.DoesNotExist:
                raise Http404
        if company_filter == '0':
            self.company = None
        else:
            try:
                self.company = Company.objects.get(pk = company_filter)
            except Company.DoesNotExist:
                raise Http404


    def get(self, request, *args, **kwargs):
        self.get_filters()
        return super(GetReportForPcHistoryView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset = None
        if self.pc is not None:
            queryset = PcOptionListHistory.objects.filter(pc = self.pc)
        if self.user_obj is not None:
            if queryset is None:
                queryset = PcOptionListHistory.objects.filter(user = self.user_obj)
            else:
                queryset = queryset.filter(user = self.user_obj)
        if self.company is not None:
            if queryset is None:
                queryset = PcOptionListHistory.objects.filter(pc__company = self.company)
            else:
                queryset = queryset.filter(pc__company = self.company)
        if queryset is None:
            raise Http404
        return queryset