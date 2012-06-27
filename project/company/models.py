# -*- coding:utf-8 -*-
from django.db import models

from django.contrib.auth.models import User



class Company(models.Model):
    """
    модель описывающая компании на обслуживании
    com_user - логин для компании, чтобы могли входить пользователи, один на всю фирму
    info - дополнительная информация о компании
    """
    com_user = models.OneToOneField(User, verbose_name=u'Логин')

    def __unicode__(self):
        return self.com_user.first_name

    class Meta:
        verbose_name = u'Компания'
        verbose_name_plural = u'Компании'


class CompanyPC(models.Model):
    """
    Модель компьютеров в фирме и ФИО пользователя,который за ним сидит
    company - наименование компании в которой стоит компьютер
    name - ФИО пользователя, который сидит за данным компьютером
    """
    company   = models.ForeignKey(Company, verbose_name=u'Компания', related_name=u'rel_company')
    pc_nameId = models.PositiveIntegerField(u'ID', unique=True)
    pc_name   = models.TextField(u'hostname')

    def __unicode__(self):
        return u'%s %s' % (self.pc_nameId, self.pc_name,)

    class Meta:
        ordering = ['company']
        verbose_name = u'Компьютер в компании'
        verbose_name_plural = u'Компьютеры в компании'



class Posts(models.Model):
    """
    Модель должностей сотрудников фирмы, которая обслуживает.
    name - наименование должности
    """
    name = models.CharField(u'Наименование', max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'Должность'
        verbose_name_plural = u'Должности'




class CompanyAdmins(models.Model):
    """
    Модель сопоставляет сотрудников аутсертинговой фирмы и фирмы закащика, и их дожностей.
    username - сотрудник аутсертинговой фирмы
    company - компания которую он обслуживает
    post - должность которую он занимает в этой фирме
    """
    username = models.ForeignKey(User, verbose_name=u'Администратор', related_name=u'rel_username')
    company  = models.ForeignKey(Company, verbose_name=u'Компания', related_name=u'rel_company_admin')
    post     = models.ForeignKey(Posts, verbose_name=u'Должность', related_name=u'ral_post')

    def __unicode__(self):
        return u'%s: %s: %s' % ( self.username, self.company, self.post )

    class Meta:
        verbose_name = u'Куратор'
        verbose_name_plural = u'Кураторы'



class PcOptions(models.Model):
    """
    Модель для различных характеристик к ПК в компаниях
    """
    name = models.TextField(u'Наименование', unique=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = u'Вид характеристики ПК'
        verbose_name_plural = u'Виды характеристик ПК'



class PcOptionsList(models.Model):
    """
    Модель сопасталвения характеристик к каждому компьютеру последнее занчение
    """
    pc      = models.ForeignKey(CompanyPC, verbose_name=u'ПК', related_name='rel_pc')
    option  = models.ForeignKey(PcOptions, verbose_name=u'Характеристика', related_name='rel_pc_option')
    #body blank & null потому что при создании используется get_or_create по полям pc & option
    body    = models.TextField(u'Знaчение', blank=True)
    date    = models.DateTimeField(u'Дата изменения', auto_now=True)
    #user blank & null потому что при создании используется get_or_create по полям pc & option
    user    = models.ForeignKey(User, verbose_name=u'Кто изменил', related_name='rel_pc_option_user', blank=True, null=True)

    def __unicode__(self):
        return self.pc.pc_name

    class Meta:
        ordering = ['option']
        verbose_name = u'Характеристика для каждого ПК'
        verbose_name_plural = u'Характеристики для каждого ПК'


class PcOptionListHistory(models.Model):
    """
    История изменений характеристик для каждого ПК
    """
    pc      = models.ForeignKey(CompanyPC, verbose_name=u'ПК', related_name='rel_pc_pcOptionListHistory')
    option  = models.ForeignKey(PcOptions, verbose_name=u'Характеристика', related_name='rel_pc_option_pcOptionListHistory')
    body    = models.TextField(u'Значение')
    date    = models.DateTimeField(u'Дата изменения', auto_now_add=True)
    user    = models.ForeignKey(User, verbose_name=u'Кто изменил', related_name='rel_pc_option_user_pcOptionListHistory')

    def __unicode__(self):
        return self.pc.pc_name

    class Meta:
        ordering = ['-date']
        verbose_name = u'История характеристика для каждого ПК'
        verbose_name_plural = u'История характеристики для каждого ПК'

