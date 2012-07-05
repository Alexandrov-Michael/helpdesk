# -*- coding:utf-8 -*-
__author__ = 'michael'

from django.core.mail import send_mail
from ques.models import Emails

def run():

    mails = Emails.objects.filter(sended = False)
    if mails:
        for item in mails:
            if item.mail_to:
                send_mail(
                    subject = item.subject,
                    message = item.body,
                    from_email = 'help@fregatsoft.com',
                    recipient_list = [item.mail_to],
                )
                item.sended = True
                item.save()
