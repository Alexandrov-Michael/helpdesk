# -*- coding:utf-8 -*-
from django.db import models

from company import models as com


class Questions(models.Model):
    """
    Модель вопросов пользоватлей
    user_from - от кого вопрос если отправлет администратор
    pc_from - от компьютера в фирме
    user_to - кому адресован вопрос из админов
    date - дата создания
    body - тело вопроса
    user_check - пометка от пользователя что вопрос закрыт
    user_check_date - дата закрытия вопроса
    admin_check - пометка от администратора что вопрос закрыт
    admin_check_date - дата закртия вопроса
    """
    user_from        = models.ForeignKey(com.User, verbose_name=u'От кого', related_name=u'rel_user_from')
    pc_from          = models.ForeignKey(com.CompanyPC, verbose_name=u'От пользователя', related_name=u'rel_px_from', blank=True, null=True)
    worker_from      = models.TextField(u'ФИО', blank=True)
    user_to          = models.ForeignKey(com.User, verbose_name=u'Кому', related_name=u'rel_user_to')
    date             = models.DateTimeField(u'Дата создания', auto_now_add=True)
    body             = models.TextField(u'Вопрос')
    user_check       = models.BooleanField(u'Отметка пользователя')
    user_check_date  = models.DateTimeField(u'Дата закрытия вопроса отправителем', null=True, blank=True)
    slug             = models.CharField(u'Идентификатор', unique=True, null=True, blank=True, max_length=8 )

    def __unicode__(self):
        return u'%s : %s' % (self.slug, self.user_to)

    @models.permalink
    def get_absolute_url(self):
        return ('chat', [str(self.id)])

    class Meta:
        ordering = ['-date']
        verbose_name = u'Вопрос'
        verbose_name_plural = u'Вопросы'



class Chat(models.Model):
    """
    Модель чата к определенному вопросу
    question - вопрос к которому идет чат
    admin_name - если сообщение отправляет администратор то его аккаунт
    date - дата создания сообщения
    body - тело сообщения
    """
    question   = models.ForeignKey(Questions, verbose_name=u'Вопрос', related_name=u'rel_question_chat')
    admin_name = models.ForeignKey(com.User, verbose_name=u'От получателя', related_name=u'rel_admin_name', blank=True, null=True)
    date       = models.DateTimeField(u'Дата создания', auto_now_add=True)
    body       = models.TextField(u'Сообщение')

    def __unicode__(self):
        return u'%s' % (self.date, )


    class Meta:
        ordering = ['date']
        verbose_name = u'Сообщение чата'
        verbose_name_plural = u'Сообщения чата'


class Emails(models.Model):
    """
    Модель для отправки почтовых сообщений
    """
    mail_to = models.EmailField()
    subject = models.CharField(max_length=60)
    body    = models.TextField()
    sended  = models.BooleanField()

    def __unicode__(self):
        return self.subject
