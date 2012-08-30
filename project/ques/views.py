# -*- coding:utf-8 -*-

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView, View
from models import Questions, Chat
from django.db.models import Q
from projForms import EditQuestionUser, EditQuestionAdmin, ChatForm, EditQuestionForKuratorForm
from proj import settings
from django.http import Http404
from company.models import CompanyAdmins, Company, CompanyPC, PcOptionListHistory, Posts
from django.contrib.auth.models import User
from ques.models import Emails
from files.models import Files
from proj.utils.mixin import UpdateContextDataMixin, GetOdjectMixin, LoginRequiredMixin, SummMixen, JSONResponseMixin
from company.Forms import ChangeUserToForQuesForm
from django.core.urlresolvers import reverse
from conformity.models import Conform
from django.shortcuts import redirect
from django.utils.timezone import now
from pytz import timezone





##################################################################################
### Static views ###
##################################################################################

class IndexView(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    Представление для страртовой страницы, использует шаблон main
    в котором через аякс подхватывается список вопросов данного пользователя

    optimized 20120706
    """

    template_name = 'main.html'


    def get_company_admins(self):
        if self.user_profile.is_company:
            queryset = CompanyAdmins.objects.filter(company__com_user=self.user).select_related('post__description', 'username__first_name', 'username__last_name', 'username__profile__telefon').order_by('post')
            return queryset
        else:
            return False

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['company_admins'] = self.get_company_admins()
        return self.update_context(context)






class QuesAdd(LoginRequiredMixin, UpdateContextDataMixin, FormView):
    """
    Представление формы для добавления вопроса

    optimized 20120706
    """
    form_class = None
    success_url = '/'
    template_name = None
    slug_plus = settings.PLUS_SLUG_FIELD


    def get_form(self, form_class):
        if self.user_profile.is_company:
            form_class = EditQuestionUser
            self.template_name = u'add_q.html'
        else:
            form_class = EditQuestionAdmin
            self.template_name = u'add_q_admin.html'
        return form_class(user=self.user, profile=self.user_profile, **self.get_form_kwargs())

    def form_valid(self, form):
        body    = form.cleaned_data['body']
        user_to = form.cleaned_data['user_to']
        post    = form.cleaned_data['post']
        try:
            department = form.cleaned_data['department']
        except KeyError:
            department = None
        if self.user_profile.is_company:
            user_from   = form.cleaned_data['user_from']
            worker_from = form.cleaned_data['worker_from']
            self.create_question(
                user_from=self.user,
                pc_from=user_from,
                worker_from=worker_from,
                user_to=user_to,
                body=body,
                post=post,
                department = department,
            )
            self.send_email(user_to, self.user, body)
        else:
            for_all = form.cleaned_data['for_all']
            if for_all:
                if self.user_profile.is_super_user:
                    comps = Company.objects.all()
                    if comps:
                        for one_comp in comps:
                            self.create_question(
                                user_from=self.user,
                                user_to=one_comp.com_user,
                                body=body,
                                post=post,
                            )
                        self.set_message(u'Вопросы успешно добавлены.')
                        return super(QuesAdd, self).form_valid(form)
                    else:
                        self.set_message(u'Вы не обслуживаете ни одну из компаний', True)
                        return super(QuesAdd, self).form_invalid(form)
                else:
                    comps = CompanyAdmins.objects.select_related('company__com_user').filter(username=self.user).order_by('company.id').distinct('company')
                    if comps:
                        for one_comp in comps:
                            self.create_question(
                                user_from=self.user,
                                user_to=one_comp.company.com_user,
                                body=body,
                                post=post,
                            )
                        self.set_message(u'Вопросы успешно добавлены.')
                        return super(QuesAdd, self).form_valid(form)
                    else:
                        self.set_message(u'Вы не обслуживаете ни одну из компаний', True)
                        return super(QuesAdd, self).form_invalid(form)
            else:
                self.create_question(
                    user_from=self.user,
                    user_to=user_to,
                    body=body,
                    post=post,)
                if not user_to.profile.is_company:
                    self.send_email(user_to, self.user, body)
        self.set_message(u'Вопрос успешно добавлен.')
        return super(QuesAdd, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(QuesAdd, self).get_context_data(**kwargs)
        return self.update_context(context)



    def send_email(self, user_to, user_from, body):
        """
        Функция записывает в очередь email на отправку
        """
        Emails(
            mail_to = user_to.email,
            subject = u'Сообщение от %s' % (user_from.first_name,),
            body = body
        ).save()




    def create_question(self, user_from, user_to, body, post, department=None, pc_from=None, worker_from=''):
        """
        Создание вопроса
        """
        question = Questions(
            user_from=user_from,
            pc_from=pc_from,
            worker_from=worker_from,
            user_to=user_to,
            body=body,
            date=now(),
            post=post,
            department=department,
        )
        question.save()
        self.update_slug_plus(question=question, user=self.user)


    def update_slug_plus(self, question, user):
        """
        Добавляет поле splug_plus в в прос
        """
        slug_first_part = user.username[:2]
        slug_2_part = question.id + self.slug_plus
        question.slug = u'%s%04d' % (slug_first_part, slug_2_part)
        question.save()





class QuesChatForm(SummMixen, FormView):
    """
    Представление формы для чата в обсуждении вопроса


    optimized 20120706
    """
    form_class = ChatForm
    success_url = None
    template_name = 'ques_chat_form.html'
    can_not_send_mess = False

    def get_context_data(self, **kwargs):
        context = super(QuesChatForm, self).get_context_data(**kwargs)
        context['question'] = self.question
        context['msgs_set'] =  self.chat_msgs
        context['can_change'] = self.can_change
        context['can_not_send_mess'] = self.can_not_send_mess
        return self.update_context(context)


    def get_object(self):
        """
        """
        pk = self.get_pk()
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


    def form_valid(self, form):
        if self.can_not_send_mess:
            self.set_message(u'Вы не можете добавлять коментарии не ко своим вопросам', True)
            return self.form_invalid(form)
        body = form.cleaned_data['body']
        file = form.cleaned_data['file']
        new_msg = Chat(question=self.question, admin_name=self.user,body=body, date=now())
        new_msg.save()
        if file:
            new_file = Files(content_object=new_msg, file=file, name=file.name, size=file.size, date=now())
            new_file.save()
        answers_count = Chat.objects.filter(question=self.question).count()
        self.question.answers = answers_count
        self.question.save()
        self.set_message(u'Ответ успешно добавлен.')
        return super(QuesChatForm, self).form_valid(form)

    def get_success_url(self):
        url = self.question.get_absolute_url()
        return url

    def do_before_handler(self):
        self.question  = self.get_object()
        self.chat_msgs = self.get_object_depends()
        user_to = self.question.user_to
        user_from = self.question.user_from
        self.can_change = False
        post = None
        is_admin = False
        try:
            post_pk = Conform.objects.get(perem = settings.KURATOR)
            post = Posts.objects.get(pk=post_pk.object_id)
        except Conform.DoesNotExist:
            self.set_message(u'Не найдина переменная соответсвия', True)
        if post:
            if user_to.profile.is_company:
                is_admin = CompanyAdmins.objects.filter(post=post, username=self.user, company__com_user=user_to)
            elif user_from.profile.is_company:
                is_admin = CompanyAdmins.objects.filter(post=post, username=self.user, company__com_user=user_from)
            if self.user_profile.is_super_user:
                is_admin = True
            if is_admin:
                self.can_change = True
        if not self.can_change:
            if not self.question.user_from == self.user and not self.question.user_to == self.user:
                self.can_not_send_mess = True





class MainReportForQuestionsView(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    Представление для отчетов по вопросам

    optimized 20120706
    """
    template_name = 'main_report_for_ques.html'


    def do_before_handler(self):
        self.skip_only_user()
        self.skip_only_report()


    def get_context_data(self, **kwargs):
        context = super(MainReportForQuestionsView, self).get_context_data(**kwargs)
        return self.update_context(context)



class MainReportForPcHistoryView(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    Представление для получения отчета по истории изменения хараетристик ПК

    optimized 20120706
    """
    template_name = 'main_report_for_pc_history.html'

    def do_before_handler(self):
        self.skip_only_user()
        self.skip_only_report()

    def get_context_data(self, **kwargs):
        context = super(MainReportForPcHistoryView, self).get_context_data(**kwargs)
        return self.update_context(context)


class ChangeUserToForQuestionView(SummMixen, FormView):
    """
    Представление для перенаправления вопроса
    """

    form_class = ChangeUserToForQuesForm
    template_name = 'change_user_to_for_ques.html'
    success_url = '/'

    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Questions.objects.get(pk = pk)
        except Questions.DoesNotExist:
            raise Http404
        return obj

    def get_form_kwargs(self):
        kwargs = super(ChangeUserToForQuestionView, self).get_form_kwargs()
        kwargs['user'] = self.user
        return kwargs


    def form_valid(self, form):
        user_to = form.cleaned_data['user_to']
        question = self.get_object()
        question.user_to = user_to
        question.save()
        sub = u'Перенаправление вопроса от %s %s' % (self.user.first_name, self.user.last_name)
        new_email = Emails(
            mail_to=user_to.email,
            subject=sub,
            body=question.body,
        )
        new_email.save()
        self.set_message(u'Вопрос успешно перенаправлен.')
        return super(ChangeUserToForQuestionView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ChangeUserToForQuestionView, self).get_context_data(**kwargs)
        context['pk'] = self.get_pk()
        return self.update_context(context)




class EditQuesView(LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin, FormView):
    """
    Представление для изменение вопроса, только для кураторов фирмы или суперпользователей
    """
    form_class = EditQuestionForKuratorForm
    success_url = None
    template_name = 'edit_question.html'

    def get_object(self,):
        pk = self.get_pk()
        try:
            obj = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            raise Http404
        return obj

    def do_before_handler(self):
        self.skip_only_user()
        self.question = self.get_object()
        user_to = self.question.user_to
        user_from = self.question.user_from
        try:
            post_pk = Conform.objects.get(perem = settings.KURATOR)
        except Conform.DoesNotExist:
            url = self.get_success_url()
            self.set_message(u'Не найдина переменная соответсвия', True)
            return redirect(url)
        post = Posts.objects.get(pk=post_pk.object_id)
        if not self.user_profile.is_super_user:
            if user_to.profile.is_company:
                try:
                    CompanyAdmins.objects.get(post=post, username=self.user, company__com_user=user_to)
                except CompanyAdmins.DoesNotExist:
                    raise Http404
            if user_from.profile.is_company:
                try:
                    CompanyAdmins.objects.get(post=post, username=self.user, company__com_user=user_from)
                except CompanyAdmins.DoesNotExist:
                    raise Http404


    def get_initial(self):
        body = self.question.body
        return {
            'body':body,
        }


    def form_valid(self, form):
        body = form.cleaned_data['body']
        self.question.body = body
        self.question.save()
        self.set_message(u'Вопрос успешно изменен.')
        return super(EditQuesView, self).form_valid(form)


    def get_context_data(self, **kwargs):
        context = super(EditQuesView, self).get_context_data(**kwargs)
        return self.update_context(context)



    def get_success_url(self):
        url = reverse('chat', args=[self.question.id])
        return url




##################################################################################
### Ajax views ###
##################################################################################



class QuesChangeStatus(LoginRequiredMixin, GetOdjectMixin, JSONResponseMixin, View):
    """
    Представление аякс для изменения статуса вопроса
    """
    url_kwarg_user_check = 'user_check'

    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Questions.objects.get(pk = pk)
        except Questions.DoesNotExist:
            raise Http404
        return obj

    def get_user_check(self):
        user_check = self.kwargs.pop(self.url_kwarg_user_check, None)
        if user_check:
            if user_check == u'False':
                user_check = True
                date       = now()
            elif user_check == u'True':
                user_check = False
                date       = None
            else:
                raise Http404
            return [user_check, date]
        else:
            raise Http404

    def get_context_data(self, **kwagrs):
        result = {}
        result['new_status'] = self.change_status()
        return result

    def change_status(self):
        question = self.get_object()
        user_check, date = self.get_user_check()
        question.user_check = user_check
        question.user_check_date = date
        question.save()
        return question.user_check





class QuestionList(LoginRequiredMixin, ListView):
    """
    Представление для списка вопросов, для каждого пользователя
    model - модель на основе которой составляется список
    paginate_by - количество объектов на странице
    context_object_name - переменная в шаблоне
    template_name - шаблон
    get_queryset - получаем список объектов для каждого пользователя
    dispatch - проверяем пользователя зарегестрированан ли


    optimized 20120705
    """

    model = Questions
    paginate_by = 20
    context_object_name = u'questions'
    template_name = u'ajax_get_index_ques.html'

    def get_queryset(self):
        queryset = Questions.objects.filter(Q(user_to = self.user) | Q(user_from = self.user)).select_related('user_to__first_name', 'pc_from', 'user_from__first_name')
        self.non_check_ques = self.get_open_question(queryset)
        return queryset

    def get_open_question(self, queryset):
        if not queryset:
            return 0
        check_count  = queryset.filter(Q(user_check = False)).count()
        return check_count


    def get_context_data(self, **kwargs):
        context = super(QuestionList, self).get_context_data(**kwargs)
        context['non_check_ques'] = self.non_check_ques
        return context




class GetQuestionForChat(LoginRequiredMixin, GetOdjectMixin, JSONResponseMixin, View):
    """
    Представление аякс для получения вопроса на странице чата

    optimized 20120706
    """


    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Questions.objects.select_related('user_from', 'pc_from', 'user_to', 'user_to__profile').get(pk=pk)
        except Questions.DoesNotExist:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        result = {}
        question = self.get_object()
        result['date'] = self.get_date_to_str(question.date)
        result['user_from_name'] = question.user_from.first_name
        result['user_from_last_name'] = None
        result['pc_from'] = None
        result['worker_from'] = None
        result['user_to_name'] = question.user_to.first_name
        result['user_to_last_name'] = None
        result['user_check'] = question.user_check
        result['user_check_date'] = None
        result['body'] = question.body
        result['image'] = None
        if question.user_from.last_name:
            result['user_from_last_name'] = question.user_from.last_name
        if question.pc_from:
            result['pc_from'] = u'%s %s' % (question.pc_from.pc_nameId, question.pc_from.pc_name,)
            result['worker_from'] = question.worker_from
        if question.user_to.last_name:
            result['user_to_last_name'] = question.user_to.last_name
        if question.user_check_date:
            result['user_check_date'] = self.get_date_to_str(question.user_check_date)
        if question.user_to.profile.image:
            result['image'] = question.user_to.profile.image.url
        return result


    def get_date_to_str(self, date):
        """
        преобразование даты в формат строки с учетом часового пояса
        """
        mytimezone = timezone(settings.TIME_ZONE)
        result = date.astimezone(mytimezone).strftime('%H:%M %d/%m/%Y')
        return result


class GetChatMessages(LoginRequiredMixin, GetOdjectMixin, JSONResponseMixin ,View):
    """
    Представление аякс для получения сообщений в чате

    optimized 20120706
    """


    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Questions.objects.get(pk=pk)
        except Questions.DoesNotExist:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        result = []
        question = self.get_object()
        chats = self.get_chat_queryset(question)
        if chats:
            for item in chats:
                interm = {}
                interm['sender'] = None
                interm['date'] = self.get_date_to_str(item.date)
                interm['body'] = item.body
                interm['files'] = []
                interm['is_that_sender'] = False
                interm['id'] = item.id
                files = item.files.all()
                if file:
                    for one_file in files:
                        interm_files = {}
                        interm_files['url'] = one_file.file.url
                        interm_files['name'] = one_file.name
                        size, izmer = self.get_size(one_file.size)
                        interm_files['size'] = u'%s %s' % (size, izmer)
                        interm['files'].append(interm_files)
                if item.admin_name:
                    if item.admin_name == self.user:
                        interm['is_that_sender'] = True
                    if not item.admin_name.profile.is_company:
                        interm['sender'] = u'%s %s' % (item.admin_name.first_name, item.admin_name.last_name,)
                    else:
                        interm['sender'] = question.worker_from
                result.append(interm)
        return result



    def get_size(self, size):
        """
        Получение размера в человекочетаемом формате
        """
        size = int(size)
        size_kb = size/1024
        size_kb = round(size_kb, 2)
        if len(str(size_kb)) > 5:
            size_mb = size_kb/1024
            result = size_mb
            izmer = 'Mb'
        else:
            result = size_kb
            izmer = 'Kb'
        result = round(result, 2)
        return [result, izmer]

    def get_date_to_str(self, date):
        """
        преобразование даты в формат строки с учетом часового пояса
        """
        mytimezone = timezone(settings.TIME_ZONE)
        result = date.astimezone(mytimezone).strftime('%H:%M %d/%m/%Y')
        return result


    def get_chat_queryset(self, question):
        """
        получение queryset по чату
        """
        queryset = Chat.objects.select_related('admin_name', 'admin_name__profile').filter(question = question).order_by('id')
        return  queryset




class GetCompanyListForReportForQuesView(LoginRequiredMixin, ListView):
    """
    Аякс Представление для получения списка компаний для отчета по вопроса

    optimized 20120706
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'ajax_get_company_for_report_ques.html'

    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        queryset = Company.objects.select_related('com_user__first_name').all()
        return queryset


class GetUserListForReportForQuesView(LoginRequiredMixin, ListView):
    """
    Аякс представление для получения списка сотрудников для отчета по вопросам

    optimized 20120706
    """
    model = User
    context_object_name = 'users'
    template_name = 'ajax_get_users_for_report_for_ques.html'

    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        queryset = User.objects.exclude(pk=1).exclude(profile__is_company = True)
        return queryset


class GetReportListForReportForQuesView(LoginRequiredMixin, ListView):
    """
    Аякс представления для получения вопросов по заданным
    фильтрам для отчета по вопросам

    optimized 20120706
    """
    model = Questions
    context_object_name = 'questions'
    template_name = 'ajax_get_report_list_for_report_ques.html'
    company_post_filter = 'company'
    user_post_filter = 'user'
    paginate_by = 30

    def do_before_handler(self):
        self.skip_only_user()
        self.skip_only_report()


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
            queryset = Questions.objects.select_related('user_from__first_name', 'pc_from__pc_nameId', 'pc_from__pc_name', 'user_to__first_name').filter(Q(user_from = company)|Q(user_to = company))
        if self.user_filter is not None:
            try:
                user = User.objects.get(pk = self.user_filter)
            except User.DoesNotExist:
                raise Http404
            if queryset is None:
                queryset = Questions.objects.select_related('user_from__first_name', 'pc_from__pc_nameId', 'pc_from__pc_name', 'user_to__first_name').filter(Q(user_from = user)|Q(user_to = user))
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


class GetPcListForReportPcHistoryView(LoginRequiredMixin, ListView):
    """
    Аякс представление для получения списка пк в фирме

    optimized 20120706
    """
    model = CompanyPC
    context_object_name = 'pc_list'
    template_name = 'ajax_get_pc_for_report_pc_history.html'
    company_get_filter = 'company'


    def do_before_handler(self):
        self.skip_only_user()

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
        queryset = CompanyPC.objects.filter(company = company).select_related('pc_nameId', 'pc_name')
        return queryset


class GetCompanyListForReportForPcHistoryView(LoginRequiredMixin, ListView):
    """
    Аякс представление для получения скиска компаний в отчету о изменени характеристик

    optimized 20120706
    """
    model = Company
    context_object_name = 'companys'
    template_name = 'ajax_get_company_for_report_pc_history.html'

    def do_before_handler(self):
        self.skip_only_user()

    def get_queryset(self):
        queryset = Company.objects.select_related('com_user__first_name').all()
        return queryset


class GetReportForPcHistoryView(LoginRequiredMixin, ListView):
    """
    Аякс предсталвение для получения отчета по истории измененя характеристик пк

    optimized 20120706
    """
    model = PcOptionListHistory
    context_object_name = 'changes'
    template_name = 'ajax_get_report_for_pc_history.html'
    pc_get_filter = 'pc'
    user_get_filter = 'user'
    company_get_filter = 'company'
    paginate_by = 30

    def do_before_handler(self):
        self.skip_only_user()

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
