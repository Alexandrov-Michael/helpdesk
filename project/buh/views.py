# -*- coding:utf-8 -*-
from proj.utils.mixin import LoginRequiredMixin, JSONResponseMixin, UpdateContextDataMixin, GetOdjectMixin
from django.views.generic.base import View, TemplateView
from models import Accounting, Contracts
from company.models import CompanyAdmins, Company
from django.http import Http404
from django.views.generic.edit import FormView, CreateView, UpdateView
from django.views.generic.list import ListView
from forms import AddAccountingForm, AddContractForm
from django.core.urlresolvers import reverse





#################################################################################
####### Static views                                               ##############
#################################################################################



class IndexAccountingView(LoginRequiredMixin, UpdateContextDataMixin, TemplateView):
    """
    Представление для списка долгов по фирме
    """
    template_name = 'buh_accounting.html'

    def do_before_handler(self):
        self.skip_only_user()
        if not self.user_profile.is_super_user:
            self.skip_only_buh()


    def get_context_data(self, **kwargs):
        context = super(IndexAccountingView, self).get_context_data(**kwargs)
        return self.update_context(context)


class AddAccountingView(LoginRequiredMixin, UpdateContextDataMixin, FormView):
    """
    Предсталвние для добавления отчетности
    """
    form_class = AddAccountingForm
    template_name = 'add_accounting.html'
    success_url = None

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()

    def get_success_url(self):
        url = reverse('buh_index', args=[])
        result = u'%s?company=%s' % (url, self.object_company.id)
        return result

    def get_context_data(self, **kwargs):
        context = super(AddAccountingView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def form_valid(self, form):
        contract = form.cleaned_data['contract']
        company  = form.cleaned_data['company']
        paid     = form.cleaned_data['paid']
        month    = form.cleaned_data['month']
        year     = form.cleaned_data['year']
        new_obj  = Accounting()
        new_obj.contract = contract
        new_obj.month    = month
        new_obj.year     = year
        new_obj.paid     = paid
        new_obj.save()
        self.object_company = company
        self.set_message(u'Новое значение успешно добавлено')
        return super(AddAccountingView, self).form_valid(form)


class AddContractView(LoginRequiredMixin, UpdateContextDataMixin, CreateView ):
    """
    Представление для добавления контракта
    """
    form_class = AddContractForm
    model = Contracts
    template_name = 'add_contract.html'
    success_url = None

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()

    def get_context_data(self, **kwargs):
        context = super(AddContractView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_success_url(self):
        url = reverse('list_contracts', args=[])
        self.set_message(u'Договор успешно добавлен.')
        return url


class ListContractsView(LoginRequiredMixin, UpdateContextDataMixin, ListView):
    """
    Представление для списка догооворов
    """
    template_name = 'contracts_list.html'
    model = Contracts
    context_object_name = 'contracts'
    paginate_by = 35

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()

    def get_context_data(self, **kwargs):
        context = super(ListContractsView, self).get_context_data(**kwargs)
        return self.update_context(context)


class EditContractView(LoginRequiredMixin, UpdateContextDataMixin, UpdateView):
    """
    Предситалвение для изменние договора
    """
    template_name = 'edit_contract.html'
    success_url = None
    form_class = AddContractForm
    model = Contracts

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()

    def get_context_data(self, **kwargs):
        context = super(EditContractView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_success_url(self):
        url = reverse('list_contracts', args=[])
        self.set_message(u'Договор успешно изменен.')
        return url






#################################################################################
####### Ajax views                                                 ##############
#################################################################################





class GetDebtsView(LoginRequiredMixin, JSONResponseMixin, View):
    """
    Ajax представление для получения долгов по фирме
    """

    def get_context_data(self, **kwargs):
        result = []
        queryset = None
        if self.user_profile.is_company:
            queryset = Accounting.objects.select_related('contract__company', 'contract__company__com_user').filter(contract__company = self.user.company, paid = False)
        else:
            companys = CompanyAdmins.objects.filter(username=self.user).select_related('company')
            company_list = []
            if companys:
                for item in companys:
                    company_list.append(item.company.id)
            if company_list:
                queryset = Accounting.objects.select_related('contract__company', 'contract__company__com_user').filter(contract__company__in = company_list, paid=False)
        if self.user_profile.is_super_user:
            queryset = Accounting.objects.select_related('contract__company', 'contract__company__com_user').filter(paid=False)
        if queryset:
            for item in queryset:
                iterm = {}
                iterm['company']  = item.contract.company.com_user.first_name
                iterm['contract'] = item.contract.name
                iterm['month']    = item.month
                iterm['year']     = item.year
                result.append(iterm)
        return result


class GetCompanyForAccountingView(LoginRequiredMixin, JSONResponseMixin, View):
    """
    Ajax представление для получения компаний
    """

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()

    def get_context_data(self, **kwargs):
        resutl = {}
        queryset = Company.objects.all()
        if queryset:
            for item in queryset:
                resutl[item.id] = item.com_user.first_name
        return resutl


class GetDebsForOneCompanyView(LoginRequiredMixin, GetOdjectMixin, JSONResponseMixin, View):
    """
    Ajax представление для получения долгов по фирме
    """

    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        result = []
        company = self.get_object()
        queryset = Accounting.objects.filter(contract__company = company)
        if queryset:
            for item in queryset:
                iterm = {}
                iterm['year']  = item.year
                iterm['month'] = item.month
                iterm['paid']  = item.paid
                iterm['id']    = item.id
                result.append(iterm)
        return result


class GetContractsView(LoginRequiredMixin, GetOdjectMixin, JSONResponseMixin, View):
    """
    Ajax представление для получение контрактов фирм
    """

    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            raise Http404
        return obj

    def get_context_data(self, **kwargs):
        result = {}
        company = self.get_object()
        queryset = Contracts.objects.filter(company = company)
        if queryset:
            for item in queryset:
                result[item.id] = item.name
        return result



class EditAccountingView(LoginRequiredMixin,  View, GetOdjectMixin, UpdateContextDataMixin, JSONResponseMixin):
    """
    Ajax Представление для изменение отчетсности
    """

    url_status_kwarg = 'status'

    def do_before_handler(self):
        if not self.user_profile.is_super_user:
            self.skip_only_buh()


    def get_object(self):
        pk = self.get_pk()
        try:
            obj = Accounting.objects.get(pk=pk)
        except Accounting.DoesNotExist:
            raise Http404
        return obj

    def get_status(self):
        status = self.kwargs.get(self.url_status_kwarg, None)
        if status:
            if status == 'True':
                status = True
            elif status == 'False':
                status = False
            else:
                raise Http404
            return status
        else:
            raise Http404

    def get_context_data(self, *args, **kwargs):
        accounting = self.get_object()
        status = self.get_status()
        accounting.paid = status
        accounting.save()
        self.set_message(u'Статус успешно изменен.')
        return ['ok']



