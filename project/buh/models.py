# -*- coding:utf-8 -*-
from django.db import models
from company.models import Company


class Contracts(models.Model):
    """
    Модель договоров для фирм
    """
    name    = models.CharField(u'Номер договора', max_length=60)
    company = models.ForeignKey(Company, verbose_name=u'Компания', related_name='rel_contracts_company')

    class Meta:
        verbose_name = u'Договор'
        verbose_name_plural = u'Договоры'
        unique_together = ('name', 'company')

    def __unicode__(self):
        return u'%s' % (self.name,)


class Accounting(models.Model):
    """
    Модель учета долгов
    """
    contract = models.ForeignKey(Contracts, verbose_name=u'Договор', related_name='rel_accounting_contract')
    month    = models.SmallIntegerField(u'Месяц', max_length=2)
    year     = models.SmallIntegerField(u'Год', max_length=4)
    paid     = models.BooleanField(u'Оплачено')

    class Meta:
        verbose_name = u'Отчетсность'
        verbose_name_plural = u'Отчетность'
        unique_together = ('contract', 'month', 'year')

    def __unicode__(self):
        return u'%s' % (self.month,)

