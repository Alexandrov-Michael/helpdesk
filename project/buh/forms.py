# -*- coding:utf-8 -*-
__author__ = 'michael'
from django import forms
from company.models import Company
from buh.models import Contracts, Accounting
from datetime import datetime

MONTH_CHOISE = (
    ('1','январь'),
    ('2', 'февраль'),
    ('3' , 'март'),
    ('4' , 'апрель'),
    ('5' , 'май'),
    ('6' , 'июнь'),
    ('7' , 'июль'),
    ('8' , 'август'),
    ('9' , 'сентябрь'),
    ('10' , 'октябрь'),
    ('11' , 'ноябрь'),
    ('12' , 'декабрь'),
)

class AddAccountingForm(forms.Form):
    """
    Форма для добавления отчетности
    """

    company  = forms.ModelChoiceField(queryset=Company.objects.all(), label=u'Компания')
    contract = forms.ModelChoiceField(queryset=Contracts.objects.all(), label=u'Договор')
    month    = forms.ChoiceField(choices=MONTH_CHOISE, label=u'Месяц')
    year     = forms.IntegerField(label='Год', min_value=1990, max_value=2100, initial=datetime.now().year)
    paid     = forms.BooleanField(label=u'Статус', required=False)


    def clean(self):
        cleaned_data = super(AddAccountingForm, self).clean()
        contract = cleaned_data['contract']
        month    = cleaned_data['month']
        year     = cleaned_data['year']
        try:
            Accounting.objects.get(contract=contract, month=month, year=year)
            mess = u'Такая отчетность уже существует, измените ее в списке отчетностей'
            raise forms.ValidationError(mess)
        except Accounting.DoesNotExist:
            return cleaned_data



class AddContractForm(forms.ModelForm):
    """
    Форма добавления контракта
    """
    class Meta:
        model = Contracts