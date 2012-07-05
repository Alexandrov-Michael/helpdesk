#!/bin/bash
# Отправка сообщений на почту для крона

cd /home/f/fregatscom/helpdesk

env/bin/python project/manage.py runscript sendEmails