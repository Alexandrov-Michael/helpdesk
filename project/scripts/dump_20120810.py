#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated, changes may be lost if you
# go and generate it again. It was generated with the following command:
# manage.py dumpscript

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType
from django.utils.timezone import utc

def run():



    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.username = u'geodez'
    auth_user_1.first_name = u'\u0417\u0410\u041e \u0413\u0435\u043e\u0434\u0435\u0437\u0438\u0447\u0435\u0441\u043a\u0438\u0435 \u043f\u0440\u0438\u0431\u043e\u0440\u044b'
    auth_user_1.last_name = u''
    auth_user_1.email = u''
    auth_user_1.password = u'pbkdf2_sha256$10000$vdElxO4KswNX$ZNoUUfG2sDG6Vf8EY6ZwUQaphxAgiAdrmGNWXrVnaeo='
    auth_user_1.is_staff = False
    auth_user_1.is_active = True
    auth_user_1.is_superuser = False
    auth_user_1.last_login = datetime.datetime(2012, 8, 9, 10, 23, 45, 808852, tzinfo=utc)
    auth_user_1.date_joined = datetime.datetime(2012, 8, 1, 5, 8, 19, 387000, tzinfo=utc)
    auth_user_1.save()

    auth_user_2 = User()
    auth_user_2.username = u'kiselev'
    auth_user_2.first_name = u'\u0424\u0438\u043b\u0438\u043f\u043f'
    auth_user_2.last_name = u'\u041a\u0438\u0441\u0435\u043b\u0435\u0432'
    auth_user_2.email = u'shon@fregatsoft.com'
    auth_user_2.password = u'pbkdf2_sha256$10000$epSN2EIRjARK$apf8npPPQOM7F7ej/I0JK9owZdMxwQGhajjRUJC9His='
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.is_superuser = False
    auth_user_2.last_login = datetime.datetime(2012, 8, 1, 12, 33, 21, 361836, tzinfo=utc)
    auth_user_2.date_joined = datetime.datetime(2012, 8, 1, 4, 57, 23, 304000, tzinfo=utc)
    auth_user_2.save()

    auth_user_3 = User()
    auth_user_3.username = u'stogorod'
    auth_user_3.first_name = u'\u041e\u041e\u041e "\u0413\u041e\u0420\u041e\u0414"'
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.password = u'pbkdf2_sha256$10000$HHKrv9LIvHMb$jV3QTuvJr3OWvEypszwtsyOHtqd+gjXa6shGhO/h2c0='
    auth_user_3.is_staff = False
    auth_user_3.is_active = True
    auth_user_3.is_superuser = False
    auth_user_3.last_login = datetime.datetime(2012, 8, 9, 21, 44, 11, 69174, tzinfo=utc)
    auth_user_3.date_joined = datetime.datetime(2012, 8, 9, 21, 30, 15, 831196, tzinfo=utc)
    auth_user_3.save()

    auth_user_4 = User()
    auth_user_4.username = u'lipisinov'
    auth_user_4.first_name = u'\u041e\u041e\u041e "\u0412\u0435\u043a\u0442\u043e\u0440-\u041b"'
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.password = u'pbkdf2_sha256$10000$CcjOlbadTKHT$iA+u0r2vVSzpih/7+rax7Xjwq1qIACu+H724LL1zcFA='
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.is_superuser = False
    auth_user_4.last_login = datetime.datetime(2012, 8, 9, 22, 3, 59, 310891, tzinfo=utc)
    auth_user_4.date_joined = datetime.datetime(2012, 8, 9, 22, 2, 26, 388660, tzinfo=utc)
    auth_user_4.save()

    auth_user_5 = User()
    auth_user_5.username = u'maslov'
    auth_user_5.first_name = u'\u0410\u043b\u0435\u043a\u0441\u0435\u0439'
    auth_user_5.last_name = u'\u041c\u0430\u0441\u043b\u043e\u0432'
    auth_user_5.email = u'79215923515@mail.ru'
    auth_user_5.password = u'pbkdf2_sha256$10000$mCYagP7mU3SP$mycuQzkC/e5Xr8oSSoHo892Ex6YlrwKSr9EAKD+FHXA='
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.is_superuser = False
    auth_user_5.last_login = datetime.datetime(2012, 8, 9, 22, 10, 16, 328719, tzinfo=utc)
    auth_user_5.date_joined = datetime.datetime(2012, 8, 1, 5, 0, 53, 573000, tzinfo=utc)
    auth_user_5.save()

    auth_user_6 = User()
    auth_user_6.username = u'fregatadmin'
    auth_user_6.first_name = u'\u0413\u043b\u0430\u0432\u043d\u044b\u0439 \u043a\u0443\u0440\u0430\u0442\u043e\u0440'
    auth_user_6.last_name = u''
    auth_user_6.email = u'admin@fregatsoft.com'
    auth_user_6.password = u'pbkdf2_sha256$10000$PMnUhFFTYJ9b$YFOUYEIo69tEkmgm+yUvkfZaN0v02Ik9YXmP9aj9Fxc='
    auth_user_6.is_staff = True
    auth_user_6.is_active = True
    auth_user_6.is_superuser = True
    auth_user_6.last_login = datetime.datetime(2012, 8, 10, 4, 28, 51, 236418, tzinfo=utc)
    auth_user_6.date_joined = datetime.datetime(2012, 7, 26, 11, 9, 24, tzinfo=utc)
    auth_user_6.save()

    auth_user_7 = User()
    auth_user_7.username = u'alexandrov'
    auth_user_7.first_name = u'\u041c\u0438\u0445\u0430\u0438\u043b'
    auth_user_7.last_name = u'\u0410\u043b\u0435\u043a\u0441\u0430\u043d\u0434\u0440\u043e\u0432'
    auth_user_7.email = u'mikle.alex@gmail.com'
    auth_user_7.password = u'pbkdf2_sha256$10000$vgWr5lSCEzil$uvzRSbJHXjINp1POJ9emGwCFTyXi3KmhWgfWZuhW46w='
    auth_user_7.is_staff = False
    auth_user_7.is_active = True
    auth_user_7.is_superuser = False
    auth_user_7.last_login = datetime.datetime(2012, 8, 10, 4, 31, 4, 50171, tzinfo=utc)
    auth_user_7.date_joined = datetime.datetime(2012, 7, 26, 11, 20, 29, tzinfo=utc)
    auth_user_7.save()

    auth_user_8 = User()
    auth_user_8.username = u'grachev'
    auth_user_8.first_name = u'\u0410\u043b\u0435\u043a\u0441\u0435\u0439'
    auth_user_8.last_name = u'\u0413\u0440\u0430\u0447\u0435\u0432'
    auth_user_8.email = u'alexgrachev1806@gmail.com'
    auth_user_8.password = u'pbkdf2_sha256$10000$wTb4CIvxzRB0$vUm2m0ywm1bHN0utXj91clkQsTmTTHKjZgMXCzyCf8g='
    auth_user_8.is_staff = False
    auth_user_8.is_active = True
    auth_user_8.is_superuser = False
    auth_user_8.last_login = datetime.datetime(2012, 8, 10, 11, 24, 8, 924218, tzinfo=utc)
    auth_user_8.date_joined = datetime.datetime(2012, 8, 3, 10, 16, 12, 800627, tzinfo=utc)
    auth_user_8.save()






    from company.models import Company

    company_company_1 = Company()
    company_company_1.com_user = auth_user_1
    company_company_1.save()

    company_company_2 = Company()
    company_company_2.com_user = auth_user_3
    company_company_2.save()

    company_company_3 = Company()
    company_company_3.com_user = auth_user_4
    company_company_3.save()

    from company.models import Departments

    company_departments_1 = Departments()
    company_departments_1.company = company_company_1
    company_departments_1.name = u'\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f'
    company_departments_1.save()

    company_departments_2 = Departments()
    company_departments_2.company = company_company_1
    company_departments_2.name = u'\u0411\u0443\u0445\u0433\u0430\u043b\u0442\u0435\u0440\u0438\u044f'
    company_departments_2.save()

    company_departments_3 = Departments()
    company_departments_3.company = company_company_1
    company_departments_3.name = u'\u0413\u0440\u0443\u043f\u043f\u0430 IT'
    company_departments_3.save()

    company_departments_4 = Departments()
    company_departments_4.company = company_company_1
    company_departments_4.name = u'\u0413\u0440\u0443\u043f\u043f\u0430 \u0413\u041d\u0421\u0421'
    company_departments_4.save()

    company_departments_5 = Departments()
    company_departments_5.company = company_company_1
    company_departments_5.name = u'\u0413\u0440\u0443\u043f\u043f\u0430 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u043e\u0432'
    company_departments_5.save()

    company_departments_6 = Departments()
    company_departments_6.company = company_company_1
    company_departments_6.name = u'\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439'
    company_departments_6.save()

    company_departments_7 = Departments()
    company_departments_7.company = company_company_1
    company_departments_7.name = u'\u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e'
    company_departments_7.save()

    company_departments_8 = Departments()
    company_departments_8.company = company_company_1
    company_departments_8.name = u'\u0421\u0435\u0440\u0432\u0438\u0441\u043d\u044b\u0439 \u0446\u0435\u043d\u0442\u0440'
    company_departments_8.save()

    company_departments_9 = Departments()
    company_departments_9.company = company_company_1
    company_departments_9.name = u'\u0421\u043a\u043b\u0430\u0434'
    company_departments_9.save()

    company_departments_10 = Departments()
    company_departments_10.company = company_company_1
    company_departments_10.name = u'\u0422\u043e\u0440\u0433\u043e\u0432\u044b\u0439 \u0437\u0430\u043b\r\n'
    company_departments_10.save()

    company_departments_11 = Departments()
    company_departments_11.company = company_company_1
    company_departments_11.name = u'\u0423\u0447\u0435\u0431\u043d\u044b\u0439 \u043a\u043b\u0430\u0441\u0441'
    company_departments_11.save()

    company_departments_12 = Departments()
    company_departments_12.company = company_company_2
    company_departments_12.name = u'\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0446\u0438\u044f'
    company_departments_12.save()

    company_departments_13 = Departments()
    company_departments_13.company = company_company_3
    company_departments_13.name = u'\u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439'
    company_departments_13.save()

    from company.models import Posts

    company_posts_1 = Posts()
    company_posts_1.name = u'WEB \u0430\u0434\u043c\u0438\u043d.'
    company_posts_1.decription = u'\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430 WEB \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0439, on-line \u0441\u0438\u0441\u0442\u0435\u043c, \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442 \u043c\u0430\u0433\u0430\u0437\u0438\u043d\u043e\u0432, \u0431\u0430\u0437 \u0434\u0430\u043d\u043d\u044b\u0445.'
    company_posts_1.save()

    company_posts_2 = Posts()
    company_posts_2.name = u'\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 *NIX \u0441\u0438\u0441\u0442\u0435\u043c.'
    company_posts_2.decription = u'\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430, \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u043e\u043f\u0435\u0440\u0430\u0446\u0438\u043e\u043d\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u0441 \u043e\u0442\u043a\u0440\u044b\u0442\u044b\u043c \u0438\u0441\u0445\u043e\u0434\u043d\u044b\u043c \u043a\u043e\u0434\u043e\u043c.'
    company_posts_2.save()

    company_posts_3 = Posts()
    company_posts_3.name = u'\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435 WIN \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432.'
    company_posts_3.decription = u'\u0423\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430, \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0441\u0435\u0440\u0432\u0435\u0440\u043e\u0432 \u043d\u0430 \u0431\u0430\u0437\u0435 \u0441\u0438\u0441\u0442\u0435\u043c Microsoft.'
    company_posts_3.save()

    company_posts_4 = Posts()
    company_posts_4.name = u'\u041a\u0443\u0440\u0430\u0442\u043e\u0440'
    company_posts_4.decription = u'\u0410\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u0438\u0432\u043d\u043e-\u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u043e\u043d\u043d\u0435 \u0432\u043e\u043f\u0440\u043e\u0441\u044b.'
    company_posts_4.save()

    company_posts_5 = Posts()
    company_posts_5.name = u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442 1\u0421'
    company_posts_5.decription = u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0440\u043e\u0432\u0430\u043d\u0438\u0435, \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0421\u0423\u0411\u0414 1\u0421.'
    company_posts_5.save()

    company_posts_6 = Posts()
    company_posts_6.name = u'\u041f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u0438\u0441\u0442 Access'
    company_posts_6.decription = u'\u0420\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430, \u0432\u043d\u0435\u0434\u0440\u0435\u043d\u0438\u0435 \u0438 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0421\u0423\u0411\u0414 Access.'
    company_posts_6.save()

    company_posts_7 = Posts()
    company_posts_7.name = u'\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u044b\u0439 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0430\u0442\u043e\u0440.'
    company_posts_7.decription = u'\u0421\u0438\u0441\u0442\u0435\u043c\u043d\u043e\u0435 \u0430\u0434\u043c\u0438\u043d\u0438\u0441\u0442\u0440\u0438\u043e\u0432\u0430\u043d\u0438\u0435, \u0443\u0441\u0442\u0430\u043d\u043e\u0432\u043a\u0430, \u043d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0430 \u0438 \u0441\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0440\u0430\u0437\u043b\u0438\u0447\u043d\u043e\u0433\u043e \u041f\u041e.'
    company_posts_7.save()

    company_posts_8 = Posts()
    company_posts_8.name = u'\u0422\u0435\u0445\u043d\u0438\u0447\u0435\u0441\u043a\u0438\u0439 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442 \u0441\u043b\u0430\u0431\u043e\u0442\u043e\u0447\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c.'
    company_posts_8.decription = u'\u0421\u043e\u043f\u0440\u043e\u0432\u043e\u0436\u0434\u0435\u043d\u0438\u0435 \u0421\u041a\u0421, \u0441\u0438\u0441\u0442\u0435\u043c \u0432\u0438\u0434\u0435\u043e \u043d\u0430\u0431\u043b\u044e\u0434\u0435\u043d\u0438\u044f, \u0442\u0435\u043b\u0435\u0444\u043e\u043d\u0438\u0438, \u0441\u043b\u0430\u0431\u043e\u0442\u043e\u0447\u043d\u044b\u0445 \u0438 \u0431\u0435\u0441\u043f\u0440\u043e\u0432\u043e\u0434\u043d\u044b\u0445 \u0441\u0438\u0441\u0442\u0435\u043c \u043f\u0435\u0440\u0435\u0434\u0430\u0447\u0438 \u0434\u0430\u043d\u043d\u044b\u0445.'
    company_posts_8.save()

    from company.models import CompanyAdmins

    company_companyadmins_1 = CompanyAdmins()
    company_companyadmins_1.username = auth_user_8
    company_companyadmins_1.company = company_company_1
    company_companyadmins_1.post = company_posts_7
    company_companyadmins_1.save()

    company_companyadmins_2 = CompanyAdmins()
    company_companyadmins_2.username = auth_user_8
    company_companyadmins_2.company = company_company_1
    company_companyadmins_2.post = company_posts_8
    company_companyadmins_2.save()

    company_companyadmins_3 = CompanyAdmins()
    company_companyadmins_3.username = auth_user_7
    company_companyadmins_3.company = company_company_1
    company_companyadmins_3.post = company_posts_1
    company_companyadmins_3.save()

    company_companyadmins_4 = CompanyAdmins()
    company_companyadmins_4.username = auth_user_7
    company_companyadmins_4.company = company_company_1
    company_companyadmins_4.post = company_posts_2
    company_companyadmins_4.save()

    company_companyadmins_5 = CompanyAdmins()
    company_companyadmins_5.username = auth_user_5
    company_companyadmins_5.company = company_company_1
    company_companyadmins_5.post = company_posts_3
    company_companyadmins_5.save()

    company_companyadmins_6 = CompanyAdmins()
    company_companyadmins_6.username = auth_user_5
    company_companyadmins_6.company = company_company_1
    company_companyadmins_6.post = company_posts_4
    company_companyadmins_6.save()

    company_companyadmins_7 = CompanyAdmins()
    company_companyadmins_7.username = auth_user_2
    company_companyadmins_7.company = company_company_2
    company_companyadmins_7.post = company_posts_2
    company_companyadmins_7.save()

    company_companyadmins_8 = CompanyAdmins()
    company_companyadmins_8.username = auth_user_2
    company_companyadmins_8.company = company_company_2
    company_companyadmins_8.post = company_posts_7
    company_companyadmins_8.save()

    company_companyadmins_9 = CompanyAdmins()
    company_companyadmins_9.username = auth_user_2
    company_companyadmins_9.company = company_company_2
    company_companyadmins_9.post = company_posts_8
    company_companyadmins_9.save()

    company_companyadmins_10 = CompanyAdmins()
    company_companyadmins_10.username = auth_user_5
    company_companyadmins_10.company = company_company_2
    company_companyadmins_10.post = company_posts_3
    company_companyadmins_10.save()

    company_companyadmins_11 = CompanyAdmins()
    company_companyadmins_11.username = auth_user_5
    company_companyadmins_11.company = company_company_2
    company_companyadmins_11.post = company_posts_4
    company_companyadmins_11.save()

    company_companyadmins_12 = CompanyAdmins()
    company_companyadmins_12.username = auth_user_7
    company_companyadmins_12.company = company_company_3
    company_companyadmins_12.post = company_posts_2
    company_companyadmins_12.save()

    company_companyadmins_13 = CompanyAdmins()
    company_companyadmins_13.username = auth_user_7
    company_companyadmins_13.company = company_company_3
    company_companyadmins_13.post = company_posts_7
    company_companyadmins_13.save()

    company_companyadmins_14 = CompanyAdmins()
    company_companyadmins_14.username = auth_user_7
    company_companyadmins_14.company = company_company_3
    company_companyadmins_14.post = company_posts_8
    company_companyadmins_14.save()

    company_companyadmins_15 = CompanyAdmins()
    company_companyadmins_15.username = auth_user_5
    company_companyadmins_15.company = company_company_3
    company_companyadmins_15.post = company_posts_3
    company_companyadmins_15.save()

    company_companyadmins_16 = CompanyAdmins()
    company_companyadmins_16.username = auth_user_5
    company_companyadmins_16.company = company_company_3
    company_companyadmins_16.post = company_posts_4
    company_companyadmins_16.save()

    from company.models import PcOptions

    company_pcoptions_1 = PcOptions()
    company_pcoptions_1.name = u'HDD 2'
    company_pcoptions_1.save()

    company_pcoptions_2 = PcOptions()
    company_pcoptions_2.name = u'HDD SYS'
    company_pcoptions_2.save()

    company_pcoptions_3 = PcOptions()
    company_pcoptions_3.name = u'\u041f\u0430\u043c\u044f\u0442\u044c'
    company_pcoptions_3.save()

    company_pcoptions_4 = PcOptions()
    company_pcoptions_4.name = u'\u041f\u0440\u043e\u0446\u0435\u0441\u0441\u043e\u0440'
    company_pcoptions_4.save()

    from profiles.models import Profile

    profiles_profile_1 = Profile()
    profiles_profile_1.user = auth_user_6
    profiles_profile_1.is_company = False
    profiles_profile_1.is_report = True
    profiles_profile_1.is_super_user = True
    profiles_profile_1.telefon = u'+7 921 914-25-83'
    profiles_profile_1.image = u''
    profiles_profile_1.save()

    profiles_profile_2 = Profile()
    profiles_profile_2.user = auth_user_5
    profiles_profile_2.is_company = False
    profiles_profile_2.is_report = True
    profiles_profile_2.is_super_user = True
    profiles_profile_2.telefon = u'+7 921 592 3515'
    profiles_profile_2.image = u''
    profiles_profile_2.save()

    profiles_profile_3 = Profile()
    profiles_profile_3.user = auth_user_1
    profiles_profile_3.is_company = True
    profiles_profile_3.is_report = False
    profiles_profile_3.is_super_user = False
    profiles_profile_3.telefon = u''
    profiles_profile_3.image = u''
    profiles_profile_3.save()

    profiles_profile_4 = Profile()
    profiles_profile_4.user = auth_user_7
    profiles_profile_4.is_company = False
    profiles_profile_4.is_report = True
    profiles_profile_4.is_super_user = True
    profiles_profile_4.telefon = u'+7 951 677-22-50'
    profiles_profile_4.image = u''
    profiles_profile_4.save()

    profiles_profile_5 = Profile()
    profiles_profile_5.user = auth_user_8
    profiles_profile_5.is_company = False
    profiles_profile_5.is_report = False
    profiles_profile_5.is_super_user = False
    profiles_profile_5.telefon = u'+7 952 237 0686'
    profiles_profile_5.image = u''
    profiles_profile_5.save()

    profiles_profile_6 = Profile()
    profiles_profile_6.user = auth_user_2
    profiles_profile_6.is_company = False
    profiles_profile_6.is_report = False
    profiles_profile_6.is_super_user = False
    profiles_profile_6.telefon = u'+7 965 059 0009'
    profiles_profile_6.image = u''
    profiles_profile_6.save()

    profiles_profile_7 = Profile()
    profiles_profile_7.user = auth_user_3
    profiles_profile_7.is_company = True
    profiles_profile_7.is_report = False
    profiles_profile_7.is_super_user = False
    profiles_profile_7.telefon = u'+7 812 328 2080'
    profiles_profile_7.image = u'profile_img/logo.png'
    profiles_profile_7.save()

    profiles_profile_8 = Profile()
    profiles_profile_8.user = auth_user_4
    profiles_profile_8.is_company = True
    profiles_profile_8.is_report = False
    profiles_profile_8.is_super_user = False
    profiles_profile_8.telefon = u''
    profiles_profile_8.image = u'profile_img/logoa.png'
    profiles_profile_8.save()

    from files.models import Files

    files_files_1 = Files()
    files_files_1.name = u'201.zip'
    files_files_1.file = u'files/201.zip'
    files_files_1.date = datetime.datetime(2012, 8, 9, 10, 59, 53, 296108, tzinfo=utc)
    files_files_1.size = 92974
    files_files_1.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_1.object_id = 39
    files_files_1.save()

    files_files_2 = Files()
    files_files_2.name = u'201.rar'
    files_files_2.file = u'files/201.rar'
    files_files_2.date = datetime.datetime(2012, 8, 9, 13, 1, 10, 541752, tzinfo=utc)
    files_files_2.size = 81023
    files_files_2.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_2.object_id = 39
    files_files_2.save()

    files_files_3 = Files()
    files_files_3.name = u'202.rar'
    files_files_3.file = u'files/202.rar'
    files_files_3.date = datetime.datetime(2012, 8, 9, 13, 1, 55, 406611, tzinfo=utc)
    files_files_3.size = 174511
    files_files_3.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_3.object_id = 40
    files_files_3.save()

    files_files_4 = Files()
    files_files_4.name = u'203.rar'
    files_files_4.file = u'files/203.rar'
    files_files_4.date = datetime.datetime(2012, 8, 9, 13, 3, 44, 103005, tzinfo=utc)
    files_files_4.size = 153439
    files_files_4.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_4.object_id = 41
    files_files_4.save()

    files_files_5 = Files()
    files_files_5.name = u'200.rar'
    files_files_5.file = u'files/200.rar'
    files_files_5.date = datetime.datetime(2012, 8, 9, 13, 4, 31, 701391, tzinfo=utc)
    files_files_5.size = 143304
    files_files_5.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_5.object_id = 42
    files_files_5.save()

    files_files_6 = Files()
    files_files_6.name = u'204.rar'
    files_files_6.file = u'files/204.rar'
    files_files_6.date = datetime.datetime(2012, 8, 9, 13, 4, 59, 293984, tzinfo=utc)
    files_files_6.size = 140591
    files_files_6.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_6.object_id = 43
    files_files_6.save()

    files_files_7 = Files()
    files_files_7.name = u'205.rar'
    files_files_7.file = u'files/205.rar'
    files_files_7.date = datetime.datetime(2012, 8, 9, 13, 5, 20, 605819, tzinfo=utc)
    files_files_7.size = 204911
    files_files_7.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_7.object_id = 44
    files_files_7.save()

    files_files_8 = Files()
    files_files_8.name = u'206.rar'
    files_files_8.file = u'files/206.rar'
    files_files_8.date = datetime.datetime(2012, 8, 9, 13, 5, 44, 559223, tzinfo=utc)
    files_files_8.size = 163535
    files_files_8.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_8.object_id = 45
    files_files_8.save()

    files_files_9 = Files()
    files_files_9.name = u'207.rar'
    files_files_9.file = u'files/207.rar'
    files_files_9.date = datetime.datetime(2012, 8, 9, 13, 6, 5, 497977, tzinfo=utc)
    files_files_9.size = 177695
    files_files_9.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_9.object_id = 46
    files_files_9.save()

    files_files_10 = Files()
    files_files_10.name = u'208.rar'
    files_files_10.file = u'files/208.rar'
    files_files_10.date = datetime.datetime(2012, 8, 9, 13, 6, 23, 575615, tzinfo=utc)
    files_files_10.size = 186175
    files_files_10.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_10.object_id = 47
    files_files_10.save()

    files_files_11 = Files()
    files_files_11.name = u'209.rar'
    files_files_11.file = u'files/209.rar'
    files_files_11.date = datetime.datetime(2012, 8, 9, 13, 6, 47, 75900, tzinfo=utc)
    files_files_11.size = 193871
    files_files_11.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_11.object_id = 48
    files_files_11.save()

    files_files_12 = Files()
    files_files_12.name = u'210.rar'
    files_files_12.file = u'files/210.rar'
    files_files_12.date = datetime.datetime(2012, 8, 9, 13, 7, 10, 97924, tzinfo=utc)
    files_files_12.size = 110175
    files_files_12.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_12.object_id = 49
    files_files_12.save()

    files_files_13 = Files()
    files_files_13.name = u'211.rar'
    files_files_13.file = u'files/211.rar'
    files_files_13.date = datetime.datetime(2012, 8, 9, 13, 7, 35, 966411, tzinfo=utc)
    files_files_13.size = 110751
    files_files_13.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_13.object_id = 50
    files_files_13.save()

    files_files_14 = Files()
    files_files_14.name = u'212.rar'
    files_files_14.file = u'files/212.rar'
    files_files_14.date = datetime.datetime(2012, 8, 9, 13, 8, 1, 451847, tzinfo=utc)
    files_files_14.size = 120916
    files_files_14.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_14.object_id = 51
    files_files_14.save()

    files_files_15 = Files()
    files_files_15.name = u'213.rar'
    files_files_15.file = u'files/213.rar'
    files_files_15.date = datetime.datetime(2012, 8, 9, 13, 8, 26, 651491, tzinfo=utc)
    files_files_15.size = 123892
    files_files_15.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_15.object_id = 52
    files_files_15.save()

    files_files_16 = Files()
    files_files_16.name = u'214.rar'
    files_files_16.file = u'files/214.rar'
    files_files_16.date = datetime.datetime(2012, 8, 9, 13, 8, 52, 116488, tzinfo=utc)
    files_files_16.size = 156207
    files_files_16.content_type = ContentType.objects.get(app_label="company", model="companypc")
    files_files_16.object_id = 53
    files_files_16.save()

    from admin_tools.menu.models import Bookmark


    from admin_tools.dashboard.models import DashboardPreferences

    admin_tools_dashboard_preferences_1 = DashboardPreferences()
    admin_tools_dashboard_preferences_1.user = auth_user_6
    admin_tools_dashboard_preferences_1.data = u'{}'
    admin_tools_dashboard_preferences_1.dashboard_id = u'dashboard'
    admin_tools_dashboard_preferences_1.save()

    admin_tools_dashboard_preferences_2 = DashboardPreferences()
    admin_tools_dashboard_preferences_2.user = auth_user_6
    admin_tools_dashboard_preferences_2.data = u'{}'
    admin_tools_dashboard_preferences_2.dashboard_id = u'profiles-dashboard'
    admin_tools_dashboard_preferences_2.save()

    from company.models import CompanyPC

    company_companypc_1 = CompanyPC()
    company_companypc_1.company = company_company_1
    company_companypc_1.departament = company_departments_6
    company_companypc_1.pc_nameId = u'10'
    company_companypc_1.pc_name = u'\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440'
    company_companypc_1.save()

    company_companypc_2 = CompanyPC()
    company_companypc_2.company = company_company_1
    company_companypc_2.departament = company_departments_2
    company_companypc_2.pc_nameId = u'ge0001'
    company_companypc_2.pc_name = u'\u0422\u0435\u0441\u0442\u043e\u0432\u044b\u0439 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440 2'
    company_companypc_2.save()

    company_companypc_3 = CompanyPC()
    company_companypc_3.company = company_company_1
    company_companypc_3.departament = company_departments_3
    company_companypc_3.pc_nameId = u'ge00-090-081'
    company_companypc_3.pc_name = u'friday'
    company_companypc_3.save()

    company_companypc_4 = CompanyPC()
    company_companypc_4.company = company_company_1
    company_companypc_4.departament = company_departments_2
    company_companypc_4.pc_nameId = u'ge00-090-075'
    company_companypc_4.pc_name = u'rodionova'
    company_companypc_4.save()

    company_companypc_5 = CompanyPC()
    company_companypc_5.company = company_company_1
    company_companypc_5.departament = company_departments_8
    company_companypc_5.pc_nameId = u'ge00-090-076'
    company_companypc_5.pc_name = u'strizhak'
    company_companypc_5.save()

    company_companypc_6 = CompanyPC()
    company_companypc_6.company = company_company_1
    company_companypc_6.departament = company_departments_1
    company_companypc_6.pc_nameId = u'ge00-090-077'
    company_companypc_6.pc_name = u'panov'
    company_companypc_6.save()

    company_companypc_7 = CompanyPC()
    company_companypc_7.company = company_company_1
    company_companypc_7.departament = company_departments_4
    company_companypc_7.pc_nameId = u'ge00-090-078'
    company_companypc_7.pc_name = u'molostov'
    company_companypc_7.save()

    company_companypc_8 = CompanyPC()
    company_companypc_8.company = company_company_1
    company_companypc_8.departament = company_departments_10
    company_companypc_8.pc_nameId = u'ge00-090-079'
    company_companypc_8.pc_name = u'zhizhikina'
    company_companypc_8.save()

    company_companypc_9 = CompanyPC()
    company_companypc_9.company = company_company_1
    company_companypc_9.departament = company_departments_10
    company_companypc_9.pc_nameId = u'ge00-090-080'
    company_companypc_9.pc_name = u'grigorieva'
    company_companypc_9.save()

    company_companypc_10 = CompanyPC()
    company_companypc_10.company = company_company_1
    company_companypc_10.departament = company_departments_10
    company_companypc_10.pc_nameId = u'ge00-090-082'
    company_companypc_10.pc_name = u'zorina'
    company_companypc_10.save()

    company_companypc_11 = CompanyPC()
    company_companypc_11.company = company_company_1
    company_companypc_11.departament = company_departments_10
    company_companypc_11.pc_nameId = u'ge00-090-085'
    company_companypc_11.pc_name = u'nikitina'
    company_companypc_11.save()

    company_companypc_12 = CompanyPC()
    company_companypc_12.company = company_company_1
    company_companypc_12.departament = company_departments_10
    company_companypc_12.pc_nameId = u'ge00-090-086'
    company_companypc_12.pc_name = u'avanesov'
    company_companypc_12.save()

    company_companypc_13 = CompanyPC()
    company_companypc_13.company = company_company_1
    company_companypc_13.departament = company_departments_10
    company_companypc_13.pc_nameId = u'ge00-090-087'
    company_companypc_13.pc_name = u'bushuev'
    company_companypc_13.save()

    company_companypc_14 = CompanyPC()
    company_companypc_14.company = company_company_1
    company_companypc_14.departament = company_departments_10
    company_companypc_14.pc_nameId = u'ge00-090-088'
    company_companypc_14.pc_name = u'korolev'
    company_companypc_14.save()

    company_companypc_15 = CompanyPC()
    company_companypc_15.company = company_company_1
    company_companypc_15.departament = company_departments_1
    company_companypc_15.pc_nameId = u'ge00-090-089'
    company_companypc_15.pc_name = u'alekseev'
    company_companypc_15.save()

    company_companypc_16 = CompanyPC()
    company_companypc_16.company = company_company_1
    company_companypc_16.departament = company_departments_8
    company_companypc_16.pc_nameId = u'ge00-090-091'
    company_companypc_16.pc_name = u'lipatova'
    company_companypc_16.save()

    company_companypc_17 = CompanyPC()
    company_companypc_17.company = company_company_1
    company_companypc_17.departament = company_departments_8
    company_companypc_17.pc_nameId = u'ge00-090-092'
    company_companypc_17.pc_name = u'bogdanova'
    company_companypc_17.save()

    company_companypc_18 = CompanyPC()
    company_companypc_18.company = company_company_1
    company_companypc_18.departament = company_departments_2
    company_companypc_18.pc_nameId = u'ge00-090-094'
    company_companypc_18.pc_name = u'rivkina'
    company_companypc_18.save()

    company_companypc_19 = CompanyPC()
    company_companypc_19.company = company_company_1
    company_companypc_19.departament = company_departments_2
    company_companypc_19.pc_nameId = u'ge00-090-101'
    company_companypc_19.pc_name = u'vabank'
    company_companypc_19.save()

    company_companypc_20 = CompanyPC()
    company_companypc_20.company = company_company_1
    company_companypc_20.departament = company_departments_4
    company_companypc_20.pc_nameId = u'ge00-090-096'
    company_companypc_20.pc_name = u'lesnikov'
    company_companypc_20.save()

    company_companypc_21 = CompanyPC()
    company_companypc_21.company = company_company_1
    company_companypc_21.departament = company_departments_4
    company_companypc_21.pc_nameId = u'ge00-090-097'
    company_companypc_21.pc_name = u'molostov'
    company_companypc_21.save()

    company_companypc_22 = CompanyPC()
    company_companypc_22.company = company_company_1
    company_companypc_22.departament = company_departments_8
    company_companypc_22.pc_nameId = u'ge00-090-098'
    company_companypc_22.pc_name = u'timofeev'
    company_companypc_22.save()

    company_companypc_23 = CompanyPC()
    company_companypc_23.company = company_company_1
    company_companypc_23.departament = company_departments_4
    company_companypc_23.pc_nameId = u'ge00-090-099'
    company_companypc_23.pc_name = u'm-control'
    company_companypc_23.save()

    company_companypc_24 = CompanyPC()
    company_companypc_24.company = company_company_1
    company_companypc_24.departament = company_departments_1
    company_companypc_24.pc_nameId = u'ge00-090-115'
    company_companypc_24.pc_name = u'vendor'
    company_companypc_24.save()

    company_companypc_25 = CompanyPC()
    company_companypc_25.company = company_company_1
    company_companypc_25.departament = company_departments_8
    company_companypc_25.pc_nameId = u'ge00-090-119'
    company_companypc_25.pc_name = u'vinogradov'
    company_companypc_25.save()

    company_companypc_26 = CompanyPC()
    company_companypc_26.company = company_company_1
    company_companypc_26.departament = company_departments_1
    company_companypc_26.pc_nameId = u'ge00-090-122'
    company_companypc_26.pc_name = u'tarpop'
    company_companypc_26.save()

    company_companypc_27 = CompanyPC()
    company_companypc_27.company = company_company_1
    company_companypc_27.departament = company_departments_10
    company_companypc_27.pc_nameId = u'ge00-090-123'
    company_companypc_27.pc_name = u'undeground'
    company_companypc_27.save()

    company_companypc_28 = CompanyPC()
    company_companypc_28.company = company_company_1
    company_companypc_28.departament = company_departments_10
    company_companypc_28.pc_nameId = u'ge00-090-132'
    company_companypc_28.pc_name = u'class-samsung'
    company_companypc_28.save()

    company_companypc_29 = CompanyPC()
    company_companypc_29.company = company_company_1
    company_companypc_29.departament = company_departments_10
    company_companypc_29.pc_nameId = u'ge00-090-133'
    company_companypc_29.pc_name = u'class-lenovo'
    company_companypc_29.save()

    company_companypc_30 = CompanyPC()
    company_companypc_30.company = company_company_1
    company_companypc_30.departament = company_departments_10
    company_companypc_30.pc_nameId = u'ge00-090-150'
    company_companypc_30.pc_name = u'stepanova'
    company_companypc_30.save()

    company_companypc_31 = CompanyPC()
    company_companypc_31.company = company_company_1
    company_companypc_31.departament = company_departments_10
    company_companypc_31.pc_nameId = u'ge00-090-153'
    company_companypc_31.pc_name = u'ermakova'
    company_companypc_31.save()

    company_companypc_32 = CompanyPC()
    company_companypc_32.company = company_company_1
    company_companypc_32.departament = company_departments_8
    company_companypc_32.pc_nameId = u'ge00-090-170'
    company_companypc_32.pc_name = u'morozova'
    company_companypc_32.save()

    company_companypc_33 = CompanyPC()
    company_companypc_33.company = company_company_1
    company_companypc_33.departament = company_departments_2
    company_companypc_33.pc_nameId = u'ge00-090-173'
    company_companypc_33.pc_name = u'malysheva'
    company_companypc_33.save()

    company_companypc_34 = CompanyPC()
    company_companypc_34.company = company_company_1
    company_companypc_34.departament = company_departments_4
    company_companypc_34.pc_nameId = u'ge00-090-175'
    company_companypc_34.pc_name = u'starikov'
    company_companypc_34.save()

    company_companypc_35 = CompanyPC()
    company_companypc_35.company = company_company_1
    company_companypc_35.departament = company_departments_8
    company_companypc_35.pc_nameId = u'ge00-090-176'
    company_companypc_35.pc_name = u'belenkov'
    company_companypc_35.save()

    company_companypc_36 = CompanyPC()
    company_companypc_36.company = company_company_1
    company_companypc_36.departament = company_departments_9
    company_companypc_36.pc_nameId = u'ge00-090-083'
    company_companypc_36.pc_name = u'kolokolnina'
    company_companypc_36.save()

    company_companypc_37 = CompanyPC()
    company_companypc_37.company = company_company_1
    company_companypc_37.departament = company_departments_9
    company_companypc_37.pc_nameId = u'ge00-090-084'
    company_companypc_37.pc_name = u'transport'
    company_companypc_37.save()

    company_companypc_38 = CompanyPC()
    company_companypc_38.company = company_company_1
    company_companypc_38.departament = company_departments_11
    company_companypc_38.pc_nameId = u'ge00-090-201'
    company_companypc_38.pc_name = u'class01'
    company_companypc_38.save()

    company_companypc_38.files.add(files_files_1)
    company_companypc_38.files.add(files_files_2)

    company_companypc_39 = CompanyPC()
    company_companypc_39.company = company_company_1
    company_companypc_39.departament = company_departments_11
    company_companypc_39.pc_nameId = u'ge00-090-202'
    company_companypc_39.pc_name = u'class02'
    company_companypc_39.save()

    company_companypc_39.files.add(files_files_3)

    company_companypc_40 = CompanyPC()
    company_companypc_40.company = company_company_1
    company_companypc_40.departament = company_departments_11
    company_companypc_40.pc_nameId = u'ge00-090-203'
    company_companypc_40.pc_name = u'class03'
    company_companypc_40.save()

    company_companypc_40.files.add(files_files_4)

    company_companypc_41 = CompanyPC()
    company_companypc_41.company = company_company_1
    company_companypc_41.departament = company_departments_11
    company_companypc_41.pc_nameId = u'ge00-090-200'
    company_companypc_41.pc_name = u'teacher'
    company_companypc_41.save()

    company_companypc_41.files.add(files_files_5)

    company_companypc_42 = CompanyPC()
    company_companypc_42.company = company_company_1
    company_companypc_42.departament = company_departments_11
    company_companypc_42.pc_nameId = u'ge00-090-204'
    company_companypc_42.pc_name = u'class04'
    company_companypc_42.save()

    company_companypc_42.files.add(files_files_6)

    company_companypc_43 = CompanyPC()
    company_companypc_43.company = company_company_1
    company_companypc_43.departament = company_departments_11
    company_companypc_43.pc_nameId = u'ge00-090-205'
    company_companypc_43.pc_name = u'class05\r\n'
    company_companypc_43.save()

    company_companypc_43.files.add(files_files_7)

    company_companypc_44 = CompanyPC()
    company_companypc_44.company = company_company_1
    company_companypc_44.departament = company_departments_11
    company_companypc_44.pc_nameId = u'ge00-090-206'
    company_companypc_44.pc_name = u'class06'
    company_companypc_44.save()

    company_companypc_44.files.add(files_files_8)

    company_companypc_45 = CompanyPC()
    company_companypc_45.company = company_company_1
    company_companypc_45.departament = company_departments_11
    company_companypc_45.pc_nameId = u'ge00-090-207'
    company_companypc_45.pc_name = u'class07'
    company_companypc_45.save()

    company_companypc_45.files.add(files_files_9)

    company_companypc_46 = CompanyPC()
    company_companypc_46.company = company_company_1
    company_companypc_46.departament = company_departments_11
    company_companypc_46.pc_nameId = u'ge00-090-208'
    company_companypc_46.pc_name = u'class08'
    company_companypc_46.save()

    company_companypc_46.files.add(files_files_10)

    company_companypc_47 = CompanyPC()
    company_companypc_47.company = company_company_1
    company_companypc_47.departament = company_departments_11
    company_companypc_47.pc_nameId = u'ge00-090-209'
    company_companypc_47.pc_name = u'class09'
    company_companypc_47.save()

    company_companypc_47.files.add(files_files_11)

    company_companypc_48 = CompanyPC()
    company_companypc_48.company = company_company_1
    company_companypc_48.departament = company_departments_11
    company_companypc_48.pc_nameId = u'ge00-090-210'
    company_companypc_48.pc_name = u'class10'
    company_companypc_48.save()

    company_companypc_48.files.add(files_files_12)

    company_companypc_49 = CompanyPC()
    company_companypc_49.company = company_company_1
    company_companypc_49.departament = company_departments_11
    company_companypc_49.pc_nameId = u'ge00-090-211'
    company_companypc_49.pc_name = u'class11'
    company_companypc_49.save()

    company_companypc_49.files.add(files_files_13)

    company_companypc_50 = CompanyPC()
    company_companypc_50.company = company_company_1
    company_companypc_50.departament = company_departments_11
    company_companypc_50.pc_nameId = u'ge00-090-212'
    company_companypc_50.pc_name = u'class12'
    company_companypc_50.save()

    company_companypc_50.files.add(files_files_14)

    company_companypc_51 = CompanyPC()
    company_companypc_51.company = company_company_1
    company_companypc_51.departament = company_departments_11
    company_companypc_51.pc_nameId = u'ge00-090-213'
    company_companypc_51.pc_name = u'class13'
    company_companypc_51.save()

    company_companypc_51.files.add(files_files_15)

    company_companypc_52 = CompanyPC()
    company_companypc_52.company = company_company_1
    company_companypc_52.departament = company_departments_11
    company_companypc_52.pc_nameId = u'ge00-090-214'
    company_companypc_52.pc_name = u'class14'
    company_companypc_52.save()

    company_companypc_52.files.add(files_files_16)

    company_companypc_53 = CompanyPC()
    company_companypc_53.company = company_company_2
    company_companypc_53.departament = company_departments_12
    company_companypc_53.pc_nameId = u'test'
    company_companypc_53.pc_name = u'test'
    company_companypc_53.save()

    company_companypc_54 = CompanyPC()
    company_companypc_54.company = company_company_3
    company_companypc_54.departament = company_departments_13
    company_companypc_54.pc_nameId = u'li-test'
    company_companypc_54.pc_name = u'test'
    company_companypc_54.save()

    from company.models import PcOptionsList

    company_pcoptionslist_1 = PcOptionsList()
    company_pcoptionslist_1.pc = company_companypc_3
    company_pcoptionslist_1.option = company_pcoptions_1
    company_pcoptionslist_1.body = u'ST/80/SATA'
    company_pcoptionslist_1.date = datetime.datetime(2012, 8, 3, 10, 29, 51, 689132, tzinfo=utc)
    company_pcoptionslist_1.user = auth_user_8
    company_pcoptionslist_1.save()

    company_pcoptionslist_2 = PcOptionsList()
    company_pcoptionslist_2.pc = company_companypc_1
    company_pcoptionslist_2.option = company_pcoptions_1
    company_pcoptionslist_2.body = u'WD/320Gb/SATA'
    company_pcoptionslist_2.date = datetime.datetime(2012, 8, 1, 5, 59, 39, 849000, tzinfo=utc)
    company_pcoptionslist_2.user = auth_user_5
    company_pcoptionslist_2.save()

    company_pcoptionslist_3 = PcOptionsList()
    company_pcoptionslist_3.pc = company_companypc_2
    company_pcoptionslist_3.option = company_pcoptions_1
    company_pcoptionslist_3.body = u'ST/250Gb/SATA'
    company_pcoptionslist_3.date = datetime.datetime(2012, 8, 1, 6, 17, 14, 241000, tzinfo=utc)
    company_pcoptionslist_3.user = auth_user_5
    company_pcoptionslist_3.save()

    company_pcoptionslist_4 = PcOptionsList()
    company_pcoptionslist_4.pc = company_companypc_44
    company_pcoptionslist_4.option = company_pcoptions_2
    company_pcoptionslist_4.body = u'ST/320/SATA'
    company_pcoptionslist_4.date = datetime.datetime(2012, 8, 9, 12, 26, 53, 360622, tzinfo=utc)
    company_pcoptionslist_4.user = auth_user_8
    company_pcoptionslist_4.save()

    company_pcoptionslist_5 = PcOptionsList()
    company_pcoptionslist_5.pc = company_companypc_3
    company_pcoptionslist_5.option = company_pcoptions_2
    company_pcoptionslist_5.body = u'ST/200/SATA'
    company_pcoptionslist_5.date = datetime.datetime(2012, 8, 3, 10, 27, 10, 508993, tzinfo=utc)
    company_pcoptionslist_5.user = auth_user_8
    company_pcoptionslist_5.save()

    company_pcoptionslist_6 = PcOptionsList()
    company_pcoptionslist_6.pc = company_companypc_47
    company_pcoptionslist_6.option = company_pcoptions_2
    company_pcoptionslist_6.body = u'ST/500/SATA'
    company_pcoptionslist_6.date = datetime.datetime(2012, 8, 9, 12, 31, 55, 676805, tzinfo=utc)
    company_pcoptionslist_6.user = auth_user_8
    company_pcoptionslist_6.save()

    company_pcoptionslist_7 = PcOptionsList()
    company_pcoptionslist_7.pc = company_companypc_45
    company_pcoptionslist_7.option = company_pcoptions_2
    company_pcoptionslist_7.body = u'ST/500/SATA'
    company_pcoptionslist_7.date = datetime.datetime(2012, 8, 9, 12, 28, 37, 267062, tzinfo=utc)
    company_pcoptionslist_7.user = auth_user_8
    company_pcoptionslist_7.save()

    company_pcoptionslist_8 = PcOptionsList()
    company_pcoptionslist_8.pc = company_companypc_46
    company_pcoptionslist_8.option = company_pcoptions_2
    company_pcoptionslist_8.body = u'ST/500/SATA'
    company_pcoptionslist_8.date = datetime.datetime(2012, 8, 9, 12, 30, 24, 163425, tzinfo=utc)
    company_pcoptionslist_8.user = auth_user_8
    company_pcoptionslist_8.save()

    company_pcoptionslist_9 = PcOptionsList()
    company_pcoptionslist_9.pc = company_companypc_38
    company_pcoptionslist_9.option = company_pcoptions_2
    company_pcoptionslist_9.body = u'ST/320/SATA'
    company_pcoptionslist_9.date = datetime.datetime(2012, 8, 9, 10, 55, 47, 744391, tzinfo=utc)
    company_pcoptionslist_9.user = auth_user_8
    company_pcoptionslist_9.save()

    company_pcoptionslist_10 = PcOptionsList()
    company_pcoptionslist_10.pc = company_companypc_35
    company_pcoptionslist_10.option = company_pcoptions_2
    company_pcoptionslist_10.body = u'ST/80/'
    company_pcoptionslist_10.date = datetime.datetime(2012, 8, 10, 11, 24, 43, 688071, tzinfo=utc)
    company_pcoptionslist_10.user = auth_user_8
    company_pcoptionslist_10.save()

    company_pcoptionslist_11 = PcOptionsList()
    company_pcoptionslist_11.pc = company_companypc_52
    company_pcoptionslist_11.option = company_pcoptions_2
    company_pcoptionslist_11.body = u'ST/500/SATA'
    company_pcoptionslist_11.date = datetime.datetime(2012, 8, 9, 12, 45, 0, 818205, tzinfo=utc)
    company_pcoptionslist_11.user = auth_user_8
    company_pcoptionslist_11.save()

    company_pcoptionslist_12 = PcOptionsList()
    company_pcoptionslist_12.pc = company_companypc_39
    company_pcoptionslist_12.option = company_pcoptions_2
    company_pcoptionslist_12.body = u'ST/320/SATA'
    company_pcoptionslist_12.date = datetime.datetime(2012, 8, 9, 11, 7, 51, 420241, tzinfo=utc)
    company_pcoptionslist_12.user = auth_user_8
    company_pcoptionslist_12.save()

    company_pcoptionslist_13 = PcOptionsList()
    company_pcoptionslist_13.pc = company_companypc_16
    company_pcoptionslist_13.option = company_pcoptions_2
    company_pcoptionslist_13.body = u'ST/240/SATA'
    company_pcoptionslist_13.date = datetime.datetime(2012, 8, 10, 11, 13, 15, 190067, tzinfo=utc)
    company_pcoptionslist_13.user = auth_user_8
    company_pcoptionslist_13.save()

    company_pcoptionslist_14 = PcOptionsList()
    company_pcoptionslist_14.pc = company_companypc_51
    company_pcoptionslist_14.option = company_pcoptions_2
    company_pcoptionslist_14.body = u'WD/40/'
    company_pcoptionslist_14.date = datetime.datetime(2012, 8, 9, 12, 43, 0, 659684, tzinfo=utc)
    company_pcoptionslist_14.user = auth_user_8
    company_pcoptionslist_14.save()

    company_pcoptionslist_15 = PcOptionsList()
    company_pcoptionslist_15.pc = company_companypc_40
    company_pcoptionslist_15.option = company_pcoptions_2
    company_pcoptionslist_15.body = u'ST/320/SATA'
    company_pcoptionslist_15.date = datetime.datetime(2012, 8, 9, 11, 10, 29, 609690, tzinfo=utc)
    company_pcoptionslist_15.user = auth_user_8
    company_pcoptionslist_15.save()

    company_pcoptionslist_16 = PcOptionsList()
    company_pcoptionslist_16.pc = company_companypc_41
    company_pcoptionslist_16.option = company_pcoptions_2
    company_pcoptionslist_16.body = u'ST/160/'
    company_pcoptionslist_16.date = datetime.datetime(2012, 8, 9, 12, 8, 32, 163743, tzinfo=utc)
    company_pcoptionslist_16.user = auth_user_8
    company_pcoptionslist_16.save()

    company_pcoptionslist_17 = PcOptionsList()
    company_pcoptionslist_17.pc = company_companypc_50
    company_pcoptionslist_17.option = company_pcoptions_2
    company_pcoptionslist_17.body = u'WD/40/'
    company_pcoptionslist_17.date = datetime.datetime(2012, 8, 9, 12, 38, 34, 943596, tzinfo=utc)
    company_pcoptionslist_17.user = auth_user_8
    company_pcoptionslist_17.save()

    company_pcoptionslist_18 = PcOptionsList()
    company_pcoptionslist_18.pc = company_companypc_42
    company_pcoptionslist_18.option = company_pcoptions_2
    company_pcoptionslist_18.body = u'ST/320/SATA'
    company_pcoptionslist_18.date = datetime.datetime(2012, 8, 9, 12, 11, 58, 911422, tzinfo=utc)
    company_pcoptionslist_18.user = auth_user_8
    company_pcoptionslist_18.save()

    company_pcoptionslist_19 = PcOptionsList()
    company_pcoptionslist_19.pc = company_companypc_49
    company_pcoptionslist_19.option = company_pcoptions_2
    company_pcoptionslist_19.body = u'ST/80/'
    company_pcoptionslist_19.date = datetime.datetime(2012, 8, 9, 12, 36, 6, 712928, tzinfo=utc)
    company_pcoptionslist_19.user = auth_user_8
    company_pcoptionslist_19.save()

    company_pcoptionslist_20 = PcOptionsList()
    company_pcoptionslist_20.pc = company_companypc_53
    company_pcoptionslist_20.option = company_pcoptions_2
    company_pcoptionslist_20.body = u'40 Gb'
    company_pcoptionslist_20.date = datetime.datetime(2012, 8, 9, 21, 47, 14, 676933, tzinfo=utc)
    company_pcoptionslist_20.user = auth_user_5
    company_pcoptionslist_20.save()

    company_pcoptionslist_21 = PcOptionsList()
    company_pcoptionslist_21.pc = company_companypc_43
    company_pcoptionslist_21.option = company_pcoptions_2
    company_pcoptionslist_21.body = u'ST/320/SATA'
    company_pcoptionslist_21.date = datetime.datetime(2012, 8, 9, 12, 24, 42, 440980, tzinfo=utc)
    company_pcoptionslist_21.user = auth_user_8
    company_pcoptionslist_21.save()

    company_pcoptionslist_22 = PcOptionsList()
    company_pcoptionslist_22.pc = company_companypc_48
    company_pcoptionslist_22.option = company_pcoptions_2
    company_pcoptionslist_22.body = u'ST/160/'
    company_pcoptionslist_22.date = datetime.datetime(2012, 8, 9, 12, 34, 29, 523538, tzinfo=utc)
    company_pcoptionslist_22.user = auth_user_8
    company_pcoptionslist_22.save()

    company_pcoptionslist_23 = PcOptionsList()
    company_pcoptionslist_23.pc = company_companypc_43
    company_pcoptionslist_23.option = company_pcoptions_3
    company_pcoptionslist_23.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_23.date = datetime.datetime(2012, 8, 9, 12, 25, 40, 951426, tzinfo=utc)
    company_pcoptionslist_23.user = auth_user_8
    company_pcoptionslist_23.save()

    company_pcoptionslist_24 = PcOptionsList()
    company_pcoptionslist_24.pc = company_companypc_1
    company_pcoptionslist_24.option = company_pcoptions_3
    company_pcoptionslist_24.body = u'1024*2/DDR2/PC5300'
    company_pcoptionslist_24.date = datetime.datetime(2012, 8, 1, 6, 1, 8, 978000, tzinfo=utc)
    company_pcoptionslist_24.user = auth_user_5
    company_pcoptionslist_24.save()

    company_pcoptionslist_25 = PcOptionsList()
    company_pcoptionslist_25.pc = company_companypc_2
    company_pcoptionslist_25.option = company_pcoptions_3
    company_pcoptionslist_25.body = u'1024/DDR2/PC6400'
    company_pcoptionslist_25.date = datetime.datetime(2012, 8, 1, 6, 17, 49, 121000, tzinfo=utc)
    company_pcoptionslist_25.user = auth_user_5
    company_pcoptionslist_25.save()

    company_pcoptionslist_26 = PcOptionsList()
    company_pcoptionslist_26.pc = company_companypc_3
    company_pcoptionslist_26.option = company_pcoptions_3
    company_pcoptionslist_26.body = u'DDR2/2048/PC5300'
    company_pcoptionslist_26.date = datetime.datetime(2012, 8, 3, 10, 25, 35, 662289, tzinfo=utc)
    company_pcoptionslist_26.user = auth_user_8
    company_pcoptionslist_26.save()

    company_pcoptionslist_27 = PcOptionsList()
    company_pcoptionslist_27.pc = company_companypc_38
    company_pcoptionslist_27.option = company_pcoptions_3
    company_pcoptionslist_27.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_27.date = datetime.datetime(2012, 8, 9, 10, 57, 36, 72653, tzinfo=utc)
    company_pcoptionslist_27.user = auth_user_8
    company_pcoptionslist_27.save()

    company_pcoptionslist_28 = PcOptionsList()
    company_pcoptionslist_28.pc = company_companypc_39
    company_pcoptionslist_28.option = company_pcoptions_3
    company_pcoptionslist_28.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_28.date = datetime.datetime(2012, 8, 9, 11, 8, 37, 678893, tzinfo=utc)
    company_pcoptionslist_28.user = auth_user_8
    company_pcoptionslist_28.save()

    company_pcoptionslist_29 = PcOptionsList()
    company_pcoptionslist_29.pc = company_companypc_41
    company_pcoptionslist_29.option = company_pcoptions_3
    company_pcoptionslist_29.body = u'2*1024/DDR2/PC2-6400'
    company_pcoptionslist_29.date = datetime.datetime(2012, 8, 9, 12, 9, 22, 436676, tzinfo=utc)
    company_pcoptionslist_29.user = auth_user_8
    company_pcoptionslist_29.save()

    company_pcoptionslist_30 = PcOptionsList()
    company_pcoptionslist_30.pc = company_companypc_42
    company_pcoptionslist_30.option = company_pcoptions_3
    company_pcoptionslist_30.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_30.date = datetime.datetime(2012, 8, 9, 12, 13, 33, 517819, tzinfo=utc)
    company_pcoptionslist_30.user = auth_user_8
    company_pcoptionslist_30.save()

    company_pcoptionslist_31 = PcOptionsList()
    company_pcoptionslist_31.pc = company_companypc_44
    company_pcoptionslist_31.option = company_pcoptions_3
    company_pcoptionslist_31.body = u'2048/DD3/PC3-10700'
    company_pcoptionslist_31.date = datetime.datetime(2012, 8, 9, 12, 27, 11, 678703, tzinfo=utc)
    company_pcoptionslist_31.user = auth_user_8
    company_pcoptionslist_31.save()

    company_pcoptionslist_32 = PcOptionsList()
    company_pcoptionslist_32.pc = company_companypc_45
    company_pcoptionslist_32.option = company_pcoptions_3
    company_pcoptionslist_32.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_32.date = datetime.datetime(2012, 8, 9, 12, 29, 8, 980285, tzinfo=utc)
    company_pcoptionslist_32.user = auth_user_8
    company_pcoptionslist_32.save()

    company_pcoptionslist_33 = PcOptionsList()
    company_pcoptionslist_33.pc = company_companypc_46
    company_pcoptionslist_33.option = company_pcoptions_3
    company_pcoptionslist_33.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_33.date = datetime.datetime(2012, 8, 9, 12, 30, 52, 336371, tzinfo=utc)
    company_pcoptionslist_33.user = auth_user_8
    company_pcoptionslist_33.save()

    company_pcoptionslist_34 = PcOptionsList()
    company_pcoptionslist_34.pc = company_companypc_47
    company_pcoptionslist_34.option = company_pcoptions_3
    company_pcoptionslist_34.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_34.date = datetime.datetime(2012, 8, 9, 12, 32, 26, 313827, tzinfo=utc)
    company_pcoptionslist_34.user = auth_user_8
    company_pcoptionslist_34.save()

    company_pcoptionslist_35 = PcOptionsList()
    company_pcoptionslist_35.pc = company_companypc_48
    company_pcoptionslist_35.option = company_pcoptions_3
    company_pcoptionslist_35.body = u'1024/DDR2/PC2-5300'
    company_pcoptionslist_35.date = datetime.datetime(2012, 8, 9, 12, 35, 2, 290869, tzinfo=utc)
    company_pcoptionslist_35.user = auth_user_8
    company_pcoptionslist_35.save()

    company_pcoptionslist_36 = PcOptionsList()
    company_pcoptionslist_36.pc = company_companypc_49
    company_pcoptionslist_36.option = company_pcoptions_3
    company_pcoptionslist_36.body = u'1024/DDR2/PC2-6400'
    company_pcoptionslist_36.date = datetime.datetime(2012, 8, 9, 12, 37, 9, 841171, tzinfo=utc)
    company_pcoptionslist_36.user = auth_user_8
    company_pcoptionslist_36.save()

    company_pcoptionslist_37 = PcOptionsList()
    company_pcoptionslist_37.pc = company_companypc_50
    company_pcoptionslist_37.option = company_pcoptions_3
    company_pcoptionslist_37.body = u'2*512/DDR/PC3200'
    company_pcoptionslist_37.date = datetime.datetime(2012, 8, 9, 12, 39, 24, 531655, tzinfo=utc)
    company_pcoptionslist_37.user = auth_user_8
    company_pcoptionslist_37.save()

    company_pcoptionslist_38 = PcOptionsList()
    company_pcoptionslist_38.pc = company_companypc_51
    company_pcoptionslist_38.option = company_pcoptions_3
    company_pcoptionslist_38.body = u'2*512/DDR/PC3200'
    company_pcoptionslist_38.date = datetime.datetime(2012, 8, 9, 12, 43, 35, 970612, tzinfo=utc)
    company_pcoptionslist_38.user = auth_user_8
    company_pcoptionslist_38.save()

    company_pcoptionslist_39 = PcOptionsList()
    company_pcoptionslist_39.pc = company_companypc_52
    company_pcoptionslist_39.option = company_pcoptions_3
    company_pcoptionslist_39.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_39.date = datetime.datetime(2012, 8, 9, 12, 45, 23, 331154, tzinfo=utc)
    company_pcoptionslist_39.user = auth_user_8
    company_pcoptionslist_39.save()

    company_pcoptionslist_40 = PcOptionsList()
    company_pcoptionslist_40.pc = company_companypc_40
    company_pcoptionslist_40.option = company_pcoptions_3
    company_pcoptionslist_40.body = u'2048/DDR3/PC3-10700'
    company_pcoptionslist_40.date = datetime.datetime(2012, 8, 9, 13, 2, 46, 293702, tzinfo=utc)
    company_pcoptionslist_40.user = auth_user_8
    company_pcoptionslist_40.save()

    company_pcoptionslist_41 = PcOptionsList()
    company_pcoptionslist_41.pc = company_companypc_53
    company_pcoptionslist_41.option = company_pcoptions_3
    company_pcoptionslist_41.body = u'16 Mb'
    company_pcoptionslist_41.date = datetime.datetime(2012, 8, 9, 21, 46, 41, 50548, tzinfo=utc)
    company_pcoptionslist_41.user = auth_user_5
    company_pcoptionslist_41.save()

    company_pcoptionslist_42 = PcOptionsList()
    company_pcoptionslist_42.pc = company_companypc_16
    company_pcoptionslist_42.option = company_pcoptions_3
    company_pcoptionslist_42.body = u'2*1024/DDR3/PC3-10700'
    company_pcoptionslist_42.date = datetime.datetime(2012, 8, 10, 11, 13, 57, 557628, tzinfo=utc)
    company_pcoptionslist_42.user = auth_user_8
    company_pcoptionslist_42.save()

    company_pcoptionslist_43 = PcOptionsList()
    company_pcoptionslist_43.pc = company_companypc_35
    company_pcoptionslist_43.option = company_pcoptions_3
    company_pcoptionslist_43.body = u'2*512/DDR2/PC2-5300'
    company_pcoptionslist_43.date = datetime.datetime(2012, 8, 10, 11, 25, 41, 819577, tzinfo=utc)
    company_pcoptionslist_43.user = auth_user_8
    company_pcoptionslist_43.save()

    company_pcoptionslist_44 = PcOptionsList()
    company_pcoptionslist_44.pc = company_companypc_49
    company_pcoptionslist_44.option = company_pcoptions_4
    company_pcoptionslist_44.body = u'ICeleron/2.2/775'
    company_pcoptionslist_44.date = datetime.datetime(2012, 8, 9, 12, 37, 44, 439979, tzinfo=utc)
    company_pcoptionslist_44.user = auth_user_8
    company_pcoptionslist_44.save()

    company_pcoptionslist_45 = PcOptionsList()
    company_pcoptionslist_45.pc = company_companypc_41
    company_pcoptionslist_45.option = company_pcoptions_4
    company_pcoptionslist_45.body = u'IC2D/1.86/775'
    company_pcoptionslist_45.date = datetime.datetime(2012, 8, 9, 12, 10, 10, 355306, tzinfo=utc)
    company_pcoptionslist_45.user = auth_user_8
    company_pcoptionslist_45.save()

    company_pcoptionslist_46 = PcOptionsList()
    company_pcoptionslist_46.pc = company_companypc_3
    company_pcoptionslist_46.option = company_pcoptions_4
    company_pcoptionslist_46.body = u'IP4D/3.4/775'
    company_pcoptionslist_46.date = datetime.datetime(2012, 8, 3, 10, 26, 1, 931143, tzinfo=utc)
    company_pcoptionslist_46.user = auth_user_8
    company_pcoptionslist_46.save()

    company_pcoptionslist_47 = PcOptionsList()
    company_pcoptionslist_47.pc = company_companypc_50
    company_pcoptionslist_47.option = company_pcoptions_4
    company_pcoptionslist_47.body = u'ICeleron/2.4/478 mPGA'
    company_pcoptionslist_47.date = datetime.datetime(2012, 8, 9, 12, 40, 30, 2491, tzinfo=utc)
    company_pcoptionslist_47.user = auth_user_8
    company_pcoptionslist_47.save()

    company_pcoptionslist_48 = PcOptionsList()
    company_pcoptionslist_48.pc = company_companypc_39
    company_pcoptionslist_48.option = company_pcoptions_4
    company_pcoptionslist_48.body = u'IPDC/3.00/775'
    company_pcoptionslist_48.date = datetime.datetime(2012, 8, 9, 11, 9, 4, 463633, tzinfo=utc)
    company_pcoptionslist_48.user = auth_user_8
    company_pcoptionslist_48.save()

    company_pcoptionslist_49 = PcOptionsList()
    company_pcoptionslist_49.pc = company_companypc_2
    company_pcoptionslist_49.option = company_pcoptions_4
    company_pcoptionslist_49.body = u'IC2D/2.63/775'
    company_pcoptionslist_49.date = datetime.datetime(2012, 8, 1, 6, 16, 49, 225000, tzinfo=utc)
    company_pcoptionslist_49.user = auth_user_5
    company_pcoptionslist_49.save()

    company_pcoptionslist_50 = PcOptionsList()
    company_pcoptionslist_50.pc = company_companypc_51
    company_pcoptionslist_50.option = company_pcoptions_4
    company_pcoptionslist_50.body = u'ICeleron/2.4/478'
    company_pcoptionslist_50.date = datetime.datetime(2012, 8, 9, 12, 44, 23, 686267, tzinfo=utc)
    company_pcoptionslist_50.user = auth_user_8
    company_pcoptionslist_50.save()

    company_pcoptionslist_51 = PcOptionsList()
    company_pcoptionslist_51.pc = company_companypc_38
    company_pcoptionslist_51.option = company_pcoptions_4
    company_pcoptionslist_51.body = u'IPDC/3.00/775'
    company_pcoptionslist_51.date = datetime.datetime(2012, 8, 9, 10, 58, 59, 140961, tzinfo=utc)
    company_pcoptionslist_51.user = auth_user_8
    company_pcoptionslist_51.save()

    company_pcoptionslist_52 = PcOptionsList()
    company_pcoptionslist_52.pc = company_companypc_35
    company_pcoptionslist_52.option = company_pcoptions_4
    company_pcoptionslist_52.body = u'ICeleron/2.93/775'
    company_pcoptionslist_52.date = datetime.datetime(2012, 8, 10, 11, 26, 16, 240692, tzinfo=utc)
    company_pcoptionslist_52.user = auth_user_8
    company_pcoptionslist_52.save()

    company_pcoptionslist_53 = PcOptionsList()
    company_pcoptionslist_53.pc = company_companypc_52
    company_pcoptionslist_53.option = company_pcoptions_4
    company_pcoptionslist_53.body = u'IPG620/2.6/1155'
    company_pcoptionslist_53.date = datetime.datetime(2012, 8, 9, 12, 46, 34, 848510, tzinfo=utc)
    company_pcoptionslist_53.user = auth_user_8
    company_pcoptionslist_53.save()

    company_pcoptionslist_54 = PcOptionsList()
    company_pcoptionslist_54.pc = company_companypc_45
    company_pcoptionslist_54.option = company_pcoptions_4
    company_pcoptionslist_54.body = u'IPDC/3.00/775'
    company_pcoptionslist_54.date = datetime.datetime(2012, 8, 9, 12, 29, 34, 351248, tzinfo=utc)
    company_pcoptionslist_54.user = auth_user_8
    company_pcoptionslist_54.save()

    company_pcoptionslist_55 = PcOptionsList()
    company_pcoptionslist_55.pc = company_companypc_16
    company_pcoptionslist_55.option = company_pcoptions_4
    company_pcoptionslist_55.body = u'IPDC/3.00/775'
    company_pcoptionslist_55.date = datetime.datetime(2012, 8, 10, 11, 14, 27, 460956, tzinfo=utc)
    company_pcoptionslist_55.user = auth_user_8
    company_pcoptionslist_55.save()

    company_pcoptionslist_56 = PcOptionsList()
    company_pcoptionslist_56.pc = company_companypc_46
    company_pcoptionslist_56.option = company_pcoptions_4
    company_pcoptionslist_56.body = u'IPDC/3.00/775'
    company_pcoptionslist_56.date = datetime.datetime(2012, 8, 9, 12, 31, 15, 940988, tzinfo=utc)
    company_pcoptionslist_56.user = auth_user_8
    company_pcoptionslist_56.save()

    company_pcoptionslist_57 = PcOptionsList()
    company_pcoptionslist_57.pc = company_companypc_44
    company_pcoptionslist_57.option = company_pcoptions_4
    company_pcoptionslist_57.body = u'IPDC/3.00/775'
    company_pcoptionslist_57.date = datetime.datetime(2012, 8, 9, 12, 27, 46, 52334, tzinfo=utc)
    company_pcoptionslist_57.user = auth_user_8
    company_pcoptionslist_57.save()

    company_pcoptionslist_58 = PcOptionsList()
    company_pcoptionslist_58.pc = company_companypc_40
    company_pcoptionslist_58.option = company_pcoptions_4
    company_pcoptionslist_58.body = u'IPDC/3.00/775'
    company_pcoptionslist_58.date = datetime.datetime(2012, 8, 9, 13, 3, 16, 908529, tzinfo=utc)
    company_pcoptionslist_58.user = auth_user_8
    company_pcoptionslist_58.save()

    company_pcoptionslist_59 = PcOptionsList()
    company_pcoptionslist_59.pc = company_companypc_47
    company_pcoptionslist_59.option = company_pcoptions_4
    company_pcoptionslist_59.body = u'IPDC/3.00/775'
    company_pcoptionslist_59.date = datetime.datetime(2012, 8, 9, 12, 32, 56, 333374, tzinfo=utc)
    company_pcoptionslist_59.user = auth_user_8
    company_pcoptionslist_59.save()

    company_pcoptionslist_60 = PcOptionsList()
    company_pcoptionslist_60.pc = company_companypc_43
    company_pcoptionslist_60.option = company_pcoptions_4
    company_pcoptionslist_60.body = u'IPDC/3.00/775'
    company_pcoptionslist_60.date = datetime.datetime(2012, 8, 9, 12, 26, 11, 20243, tzinfo=utc)
    company_pcoptionslist_60.user = auth_user_8
    company_pcoptionslist_60.save()

    company_pcoptionslist_61 = PcOptionsList()
    company_pcoptionslist_61.pc = company_companypc_53
    company_pcoptionslist_61.option = company_pcoptions_4
    company_pcoptionslist_61.body = u'i486'
    company_pcoptionslist_61.date = datetime.datetime(2012, 8, 9, 21, 46, 22, 102106, tzinfo=utc)
    company_pcoptionslist_61.user = auth_user_5
    company_pcoptionslist_61.save()

    company_pcoptionslist_62 = PcOptionsList()
    company_pcoptionslist_62.pc = company_companypc_48
    company_pcoptionslist_62.option = company_pcoptions_4
    company_pcoptionslist_62.body = u'IP4/3.00/775'
    company_pcoptionslist_62.date = datetime.datetime(2012, 8, 9, 12, 35, 27, 995927, tzinfo=utc)
    company_pcoptionslist_62.user = auth_user_8
    company_pcoptionslist_62.save()

    company_pcoptionslist_63 = PcOptionsList()
    company_pcoptionslist_63.pc = company_companypc_42
    company_pcoptionslist_63.option = company_pcoptions_4
    company_pcoptionslist_63.body = u'IPDC/3.00/775'
    company_pcoptionslist_63.date = datetime.datetime(2012, 8, 9, 12, 14, 6, 252701, tzinfo=utc)
    company_pcoptionslist_63.user = auth_user_8
    company_pcoptionslist_63.save()

    company_pcoptionslist_64 = PcOptionsList()
    company_pcoptionslist_64.pc = company_companypc_1
    company_pcoptionslist_64.option = company_pcoptions_4
    company_pcoptionslist_64.body = u'IP4/2,4/775'
    company_pcoptionslist_64.date = datetime.datetime(2012, 8, 1, 5, 58, 56, 284000, tzinfo=utc)
    company_pcoptionslist_64.user = auth_user_5
    company_pcoptionslist_64.save()

    from company.models import PcOptionListHistory

    company_pcoptionlisthistory_1 = PcOptionListHistory()
    company_pcoptionlisthistory_1.pc = company_companypc_35
    company_pcoptionlisthistory_1.option = company_pcoptions_4
    company_pcoptionlisthistory_1.body = u'ICeleron/2.93/775'
    company_pcoptionlisthistory_1.date = datetime.datetime(2012, 8, 10, 11, 26, 16, 325075, tzinfo=utc)
    company_pcoptionlisthistory_1.user = auth_user_8
    company_pcoptionlisthistory_1.save()

    company_pcoptionlisthistory_2 = PcOptionListHistory()
    company_pcoptionlisthistory_2.pc = company_companypc_35
    company_pcoptionlisthistory_2.option = company_pcoptions_3
    company_pcoptionlisthistory_2.body = u'2*512/DDR2/PC2-5300'
    company_pcoptionlisthistory_2.date = datetime.datetime(2012, 8, 10, 11, 25, 41, 898428, tzinfo=utc)
    company_pcoptionlisthistory_2.user = auth_user_8
    company_pcoptionlisthistory_2.save()

    company_pcoptionlisthistory_3 = PcOptionListHistory()
    company_pcoptionlisthistory_3.pc = company_companypc_35
    company_pcoptionlisthistory_3.option = company_pcoptions_2
    company_pcoptionlisthistory_3.body = u'ST/80/'
    company_pcoptionlisthistory_3.date = datetime.datetime(2012, 8, 10, 11, 24, 43, 760896, tzinfo=utc)
    company_pcoptionlisthistory_3.user = auth_user_8
    company_pcoptionlisthistory_3.save()

    company_pcoptionlisthistory_4 = PcOptionListHistory()
    company_pcoptionlisthistory_4.pc = company_companypc_16
    company_pcoptionlisthistory_4.option = company_pcoptions_4
    company_pcoptionlisthistory_4.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_4.date = datetime.datetime(2012, 8, 10, 11, 14, 27, 574701, tzinfo=utc)
    company_pcoptionlisthistory_4.user = auth_user_8
    company_pcoptionlisthistory_4.save()

    company_pcoptionlisthistory_5 = PcOptionListHistory()
    company_pcoptionlisthistory_5.pc = company_companypc_16
    company_pcoptionlisthistory_5.option = company_pcoptions_3
    company_pcoptionlisthistory_5.body = u'2*1024/DDR3/PC3-10700'
    company_pcoptionlisthistory_5.date = datetime.datetime(2012, 8, 10, 11, 13, 57, 653446, tzinfo=utc)
    company_pcoptionlisthistory_5.user = auth_user_8
    company_pcoptionlisthistory_5.save()

    company_pcoptionlisthistory_6 = PcOptionListHistory()
    company_pcoptionlisthistory_6.pc = company_companypc_16
    company_pcoptionlisthistory_6.option = company_pcoptions_2
    company_pcoptionlisthistory_6.body = u'ST/240/SATA'
    company_pcoptionlisthistory_6.date = datetime.datetime(2012, 8, 10, 11, 13, 15, 278215, tzinfo=utc)
    company_pcoptionlisthistory_6.user = auth_user_8
    company_pcoptionlisthistory_6.save()

    company_pcoptionlisthistory_7 = PcOptionListHistory()
    company_pcoptionlisthistory_7.pc = company_companypc_53
    company_pcoptionlisthistory_7.option = company_pcoptions_2
    company_pcoptionlisthistory_7.body = u'40 Gb'
    company_pcoptionlisthistory_7.date = datetime.datetime(2012, 8, 9, 21, 47, 14, 651696, tzinfo=utc)
    company_pcoptionlisthistory_7.user = auth_user_5
    company_pcoptionlisthistory_7.save()

    company_pcoptionlisthistory_8 = PcOptionListHistory()
    company_pcoptionlisthistory_8.pc = company_companypc_53
    company_pcoptionlisthistory_8.option = company_pcoptions_2
    company_pcoptionlisthistory_8.body = u'40 Mb'
    company_pcoptionlisthistory_8.date = datetime.datetime(2012, 8, 9, 21, 46, 55, 487378, tzinfo=utc)
    company_pcoptionlisthistory_8.user = auth_user_5
    company_pcoptionlisthistory_8.save()

    company_pcoptionlisthistory_9 = PcOptionListHistory()
    company_pcoptionlisthistory_9.pc = company_companypc_53
    company_pcoptionlisthistory_9.option = company_pcoptions_3
    company_pcoptionlisthistory_9.body = u'16 Mb'
    company_pcoptionlisthistory_9.date = datetime.datetime(2012, 8, 9, 21, 46, 41, 61206, tzinfo=utc)
    company_pcoptionlisthistory_9.user = auth_user_5
    company_pcoptionlisthistory_9.save()

    company_pcoptionlisthistory_10 = PcOptionListHistory()
    company_pcoptionlisthistory_10.pc = company_companypc_53
    company_pcoptionlisthistory_10.option = company_pcoptions_4
    company_pcoptionlisthistory_10.body = u'i486'
    company_pcoptionlisthistory_10.date = datetime.datetime(2012, 8, 9, 21, 46, 22, 129687, tzinfo=utc)
    company_pcoptionlisthistory_10.user = auth_user_5
    company_pcoptionlisthistory_10.save()

    company_pcoptionlisthistory_11 = PcOptionListHistory()
    company_pcoptionlisthistory_11.pc = company_companypc_40
    company_pcoptionlisthistory_11.option = company_pcoptions_4
    company_pcoptionlisthistory_11.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_11.date = datetime.datetime(2012, 8, 9, 13, 3, 16, 926743, tzinfo=utc)
    company_pcoptionlisthistory_11.user = auth_user_8
    company_pcoptionlisthistory_11.save()

    company_pcoptionlisthistory_12 = PcOptionListHistory()
    company_pcoptionlisthistory_12.pc = company_companypc_40
    company_pcoptionlisthistory_12.option = company_pcoptions_3
    company_pcoptionlisthistory_12.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_12.date = datetime.datetime(2012, 8, 9, 13, 2, 46, 310679, tzinfo=utc)
    company_pcoptionlisthistory_12.user = auth_user_8
    company_pcoptionlisthistory_12.save()

    company_pcoptionlisthistory_13 = PcOptionListHistory()
    company_pcoptionlisthistory_13.pc = company_companypc_52
    company_pcoptionlisthistory_13.option = company_pcoptions_4
    company_pcoptionlisthistory_13.body = u'IPG620/2.6/1155'
    company_pcoptionlisthistory_13.date = datetime.datetime(2012, 8, 9, 12, 46, 34, 918270, tzinfo=utc)
    company_pcoptionlisthistory_13.user = auth_user_8
    company_pcoptionlisthistory_13.save()

    company_pcoptionlisthistory_14 = PcOptionListHistory()
    company_pcoptionlisthistory_14.pc = company_companypc_52
    company_pcoptionlisthistory_14.option = company_pcoptions_3
    company_pcoptionlisthistory_14.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_14.date = datetime.datetime(2012, 8, 9, 12, 45, 23, 434614, tzinfo=utc)
    company_pcoptionlisthistory_14.user = auth_user_8
    company_pcoptionlisthistory_14.save()

    company_pcoptionlisthistory_15 = PcOptionListHistory()
    company_pcoptionlisthistory_15.pc = company_companypc_52
    company_pcoptionlisthistory_15.option = company_pcoptions_2
    company_pcoptionlisthistory_15.body = u'ST/500/SATA'
    company_pcoptionlisthistory_15.date = datetime.datetime(2012, 8, 9, 12, 45, 0, 925062, tzinfo=utc)
    company_pcoptionlisthistory_15.user = auth_user_8
    company_pcoptionlisthistory_15.save()

    company_pcoptionlisthistory_16 = PcOptionListHistory()
    company_pcoptionlisthistory_16.pc = company_companypc_51
    company_pcoptionlisthistory_16.option = company_pcoptions_4
    company_pcoptionlisthistory_16.body = u'ICeleron/2.4/478'
    company_pcoptionlisthistory_16.date = datetime.datetime(2012, 8, 9, 12, 44, 23, 765930, tzinfo=utc)
    company_pcoptionlisthistory_16.user = auth_user_8
    company_pcoptionlisthistory_16.save()

    company_pcoptionlisthistory_17 = PcOptionListHistory()
    company_pcoptionlisthistory_17.pc = company_companypc_51
    company_pcoptionlisthistory_17.option = company_pcoptions_3
    company_pcoptionlisthistory_17.body = u'2*512/DDR/PC3200'
    company_pcoptionlisthistory_17.date = datetime.datetime(2012, 8, 9, 12, 43, 36, 38560, tzinfo=utc)
    company_pcoptionlisthistory_17.user = auth_user_8
    company_pcoptionlisthistory_17.save()

    company_pcoptionlisthistory_18 = PcOptionListHistory()
    company_pcoptionlisthistory_18.pc = company_companypc_51
    company_pcoptionlisthistory_18.option = company_pcoptions_2
    company_pcoptionlisthistory_18.body = u'WD/40/'
    company_pcoptionlisthistory_18.date = datetime.datetime(2012, 8, 9, 12, 43, 0, 790801, tzinfo=utc)
    company_pcoptionlisthistory_18.user = auth_user_8
    company_pcoptionlisthistory_18.save()

    company_pcoptionlisthistory_19 = PcOptionListHistory()
    company_pcoptionlisthistory_19.pc = company_companypc_50
    company_pcoptionlisthistory_19.option = company_pcoptions_4
    company_pcoptionlisthistory_19.body = u'ICeleron/2.4/478 mPGA'
    company_pcoptionlisthistory_19.date = datetime.datetime(2012, 8, 9, 12, 40, 30, 55389, tzinfo=utc)
    company_pcoptionlisthistory_19.user = auth_user_8
    company_pcoptionlisthistory_19.save()

    company_pcoptionlisthistory_20 = PcOptionListHistory()
    company_pcoptionlisthistory_20.pc = company_companypc_50
    company_pcoptionlisthistory_20.option = company_pcoptions_3
    company_pcoptionlisthistory_20.body = u'2*512/DDR/PC3200'
    company_pcoptionlisthistory_20.date = datetime.datetime(2012, 8, 9, 12, 39, 24, 620794, tzinfo=utc)
    company_pcoptionlisthistory_20.user = auth_user_8
    company_pcoptionlisthistory_20.save()

    company_pcoptionlisthistory_21 = PcOptionListHistory()
    company_pcoptionlisthistory_21.pc = company_companypc_50
    company_pcoptionlisthistory_21.option = company_pcoptions_2
    company_pcoptionlisthistory_21.body = u'WD/40/'
    company_pcoptionlisthistory_21.date = datetime.datetime(2012, 8, 9, 12, 38, 35, 62038, tzinfo=utc)
    company_pcoptionlisthistory_21.user = auth_user_8
    company_pcoptionlisthistory_21.save()

    company_pcoptionlisthistory_22 = PcOptionListHistory()
    company_pcoptionlisthistory_22.pc = company_companypc_49
    company_pcoptionlisthistory_22.option = company_pcoptions_4
    company_pcoptionlisthistory_22.body = u'ICeleron/2.2/775'
    company_pcoptionlisthistory_22.date = datetime.datetime(2012, 8, 9, 12, 37, 44, 559863, tzinfo=utc)
    company_pcoptionlisthistory_22.user = auth_user_8
    company_pcoptionlisthistory_22.save()

    company_pcoptionlisthistory_23 = PcOptionListHistory()
    company_pcoptionlisthistory_23.pc = company_companypc_49
    company_pcoptionlisthistory_23.option = company_pcoptions_3
    company_pcoptionlisthistory_23.body = u'1024/DDR2/PC2-6400'
    company_pcoptionlisthistory_23.date = datetime.datetime(2012, 8, 9, 12, 37, 9, 868032, tzinfo=utc)
    company_pcoptionlisthistory_23.user = auth_user_8
    company_pcoptionlisthistory_23.save()

    company_pcoptionlisthistory_24 = PcOptionListHistory()
    company_pcoptionlisthistory_24.pc = company_companypc_49
    company_pcoptionlisthistory_24.option = company_pcoptions_2
    company_pcoptionlisthistory_24.body = u'ST/80/'
    company_pcoptionlisthistory_24.date = datetime.datetime(2012, 8, 9, 12, 36, 6, 793019, tzinfo=utc)
    company_pcoptionlisthistory_24.user = auth_user_8
    company_pcoptionlisthistory_24.save()

    company_pcoptionlisthistory_25 = PcOptionListHistory()
    company_pcoptionlisthistory_25.pc = company_companypc_48
    company_pcoptionlisthistory_25.option = company_pcoptions_4
    company_pcoptionlisthistory_25.body = u'IP4/3.00/775'
    company_pcoptionlisthistory_25.date = datetime.datetime(2012, 8, 9, 12, 35, 28, 84462, tzinfo=utc)
    company_pcoptionlisthistory_25.user = auth_user_8
    company_pcoptionlisthistory_25.save()

    company_pcoptionlisthistory_26 = PcOptionListHistory()
    company_pcoptionlisthistory_26.pc = company_companypc_48
    company_pcoptionlisthistory_26.option = company_pcoptions_3
    company_pcoptionlisthistory_26.body = u'1024/DDR2/PC2-5300'
    company_pcoptionlisthistory_26.date = datetime.datetime(2012, 8, 9, 12, 35, 2, 333715, tzinfo=utc)
    company_pcoptionlisthistory_26.user = auth_user_8
    company_pcoptionlisthistory_26.save()

    company_pcoptionlisthistory_27 = PcOptionListHistory()
    company_pcoptionlisthistory_27.pc = company_companypc_48
    company_pcoptionlisthistory_27.option = company_pcoptions_2
    company_pcoptionlisthistory_27.body = u'ST/160/'
    company_pcoptionlisthistory_27.date = datetime.datetime(2012, 8, 9, 12, 34, 29, 687589, tzinfo=utc)
    company_pcoptionlisthistory_27.user = auth_user_8
    company_pcoptionlisthistory_27.save()

    company_pcoptionlisthistory_28 = PcOptionListHistory()
    company_pcoptionlisthistory_28.pc = company_companypc_47
    company_pcoptionlisthistory_28.option = company_pcoptions_4
    company_pcoptionlisthistory_28.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_28.date = datetime.datetime(2012, 8, 9, 12, 32, 56, 433684, tzinfo=utc)
    company_pcoptionlisthistory_28.user = auth_user_8
    company_pcoptionlisthistory_28.save()

    company_pcoptionlisthistory_29 = PcOptionListHistory()
    company_pcoptionlisthistory_29.pc = company_companypc_47
    company_pcoptionlisthistory_29.option = company_pcoptions_3
    company_pcoptionlisthistory_29.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_29.date = datetime.datetime(2012, 8, 9, 12, 32, 26, 391544, tzinfo=utc)
    company_pcoptionlisthistory_29.user = auth_user_8
    company_pcoptionlisthistory_29.save()

    company_pcoptionlisthistory_30 = PcOptionListHistory()
    company_pcoptionlisthistory_30.pc = company_companypc_47
    company_pcoptionlisthistory_30.option = company_pcoptions_2
    company_pcoptionlisthistory_30.body = u'ST/500/SATA'
    company_pcoptionlisthistory_30.date = datetime.datetime(2012, 8, 9, 12, 31, 55, 799791, tzinfo=utc)
    company_pcoptionlisthistory_30.user = auth_user_8
    company_pcoptionlisthistory_30.save()

    company_pcoptionlisthistory_31 = PcOptionListHistory()
    company_pcoptionlisthistory_31.pc = company_companypc_46
    company_pcoptionlisthistory_31.option = company_pcoptions_4
    company_pcoptionlisthistory_31.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_31.date = datetime.datetime(2012, 8, 9, 12, 31, 16, 29758, tzinfo=utc)
    company_pcoptionlisthistory_31.user = auth_user_8
    company_pcoptionlisthistory_31.save()

    company_pcoptionlisthistory_32 = PcOptionListHistory()
    company_pcoptionlisthistory_32.pc = company_companypc_46
    company_pcoptionlisthistory_32.option = company_pcoptions_3
    company_pcoptionlisthistory_32.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_32.date = datetime.datetime(2012, 8, 9, 12, 30, 52, 433926, tzinfo=utc)
    company_pcoptionlisthistory_32.user = auth_user_8
    company_pcoptionlisthistory_32.save()

    company_pcoptionlisthistory_33 = PcOptionListHistory()
    company_pcoptionlisthistory_33.pc = company_companypc_46
    company_pcoptionlisthistory_33.option = company_pcoptions_2
    company_pcoptionlisthistory_33.body = u'ST/500/SATA'
    company_pcoptionlisthistory_33.date = datetime.datetime(2012, 8, 9, 12, 30, 24, 186307, tzinfo=utc)
    company_pcoptionlisthistory_33.user = auth_user_8
    company_pcoptionlisthistory_33.save()

    company_pcoptionlisthistory_34 = PcOptionListHistory()
    company_pcoptionlisthistory_34.pc = company_companypc_45
    company_pcoptionlisthistory_34.option = company_pcoptions_4
    company_pcoptionlisthistory_34.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_34.date = datetime.datetime(2012, 8, 9, 12, 29, 34, 502586, tzinfo=utc)
    company_pcoptionlisthistory_34.user = auth_user_8
    company_pcoptionlisthistory_34.save()

    company_pcoptionlisthistory_35 = PcOptionListHistory()
    company_pcoptionlisthistory_35.pc = company_companypc_45
    company_pcoptionlisthistory_35.option = company_pcoptions_3
    company_pcoptionlisthistory_35.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_35.date = datetime.datetime(2012, 8, 9, 12, 29, 9, 31687, tzinfo=utc)
    company_pcoptionlisthistory_35.user = auth_user_8
    company_pcoptionlisthistory_35.save()

    company_pcoptionlisthistory_36 = PcOptionListHistory()
    company_pcoptionlisthistory_36.pc = company_companypc_45
    company_pcoptionlisthistory_36.option = company_pcoptions_2
    company_pcoptionlisthistory_36.body = u'ST/500/SATA'
    company_pcoptionlisthistory_36.date = datetime.datetime(2012, 8, 9, 12, 28, 37, 416832, tzinfo=utc)
    company_pcoptionlisthistory_36.user = auth_user_8
    company_pcoptionlisthistory_36.save()

    company_pcoptionlisthistory_37 = PcOptionListHistory()
    company_pcoptionlisthistory_37.pc = company_companypc_44
    company_pcoptionlisthistory_37.option = company_pcoptions_4
    company_pcoptionlisthistory_37.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_37.date = datetime.datetime(2012, 8, 9, 12, 27, 46, 106996, tzinfo=utc)
    company_pcoptionlisthistory_37.user = auth_user_8
    company_pcoptionlisthistory_37.save()

    company_pcoptionlisthistory_38 = PcOptionListHistory()
    company_pcoptionlisthistory_38.pc = company_companypc_44
    company_pcoptionlisthistory_38.option = company_pcoptions_3
    company_pcoptionlisthistory_38.body = u'2048/DD3/PC3-10700'
    company_pcoptionlisthistory_38.date = datetime.datetime(2012, 8, 9, 12, 27, 11, 775713, tzinfo=utc)
    company_pcoptionlisthistory_38.user = auth_user_8
    company_pcoptionlisthistory_38.save()

    company_pcoptionlisthistory_39 = PcOptionListHistory()
    company_pcoptionlisthistory_39.pc = company_companypc_44
    company_pcoptionlisthistory_39.option = company_pcoptions_2
    company_pcoptionlisthistory_39.body = u'ST/320/SATA'
    company_pcoptionlisthistory_39.date = datetime.datetime(2012, 8, 9, 12, 26, 53, 511530, tzinfo=utc)
    company_pcoptionlisthistory_39.user = auth_user_8
    company_pcoptionlisthistory_39.save()

    company_pcoptionlisthistory_40 = PcOptionListHistory()
    company_pcoptionlisthistory_40.pc = company_companypc_43
    company_pcoptionlisthistory_40.option = company_pcoptions_4
    company_pcoptionlisthistory_40.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_40.date = datetime.datetime(2012, 8, 9, 12, 26, 11, 110236, tzinfo=utc)
    company_pcoptionlisthistory_40.user = auth_user_8
    company_pcoptionlisthistory_40.save()

    company_pcoptionlisthistory_41 = PcOptionListHistory()
    company_pcoptionlisthistory_41.pc = company_companypc_43
    company_pcoptionlisthistory_41.option = company_pcoptions_3
    company_pcoptionlisthistory_41.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_41.date = datetime.datetime(2012, 8, 9, 12, 25, 41, 150841, tzinfo=utc)
    company_pcoptionlisthistory_41.user = auth_user_8
    company_pcoptionlisthistory_41.save()

    company_pcoptionlisthistory_42 = PcOptionListHistory()
    company_pcoptionlisthistory_42.pc = company_companypc_43
    company_pcoptionlisthistory_42.option = company_pcoptions_2
    company_pcoptionlisthistory_42.body = u'ST/320/SATA'
    company_pcoptionlisthistory_42.date = datetime.datetime(2012, 8, 9, 12, 24, 42, 586325, tzinfo=utc)
    company_pcoptionlisthistory_42.user = auth_user_8
    company_pcoptionlisthistory_42.save()

    company_pcoptionlisthistory_43 = PcOptionListHistory()
    company_pcoptionlisthistory_43.pc = company_companypc_42
    company_pcoptionlisthistory_43.option = company_pcoptions_4
    company_pcoptionlisthistory_43.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_43.date = datetime.datetime(2012, 8, 9, 12, 14, 6, 364602, tzinfo=utc)
    company_pcoptionlisthistory_43.user = auth_user_8
    company_pcoptionlisthistory_43.save()

    company_pcoptionlisthistory_44 = PcOptionListHistory()
    company_pcoptionlisthistory_44.pc = company_companypc_42
    company_pcoptionlisthistory_44.option = company_pcoptions_3
    company_pcoptionlisthistory_44.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_44.date = datetime.datetime(2012, 8, 9, 12, 13, 33, 569429, tzinfo=utc)
    company_pcoptionlisthistory_44.user = auth_user_8
    company_pcoptionlisthistory_44.save()

    company_pcoptionlisthistory_45 = PcOptionListHistory()
    company_pcoptionlisthistory_45.pc = company_companypc_42
    company_pcoptionlisthistory_45.option = company_pcoptions_2
    company_pcoptionlisthistory_45.body = u'ST/320/SATA'
    company_pcoptionlisthistory_45.date = datetime.datetime(2012, 8, 9, 12, 11, 59, 17865, tzinfo=utc)
    company_pcoptionlisthistory_45.user = auth_user_8
    company_pcoptionlisthistory_45.save()

    company_pcoptionlisthistory_46 = PcOptionListHistory()
    company_pcoptionlisthistory_46.pc = company_companypc_41
    company_pcoptionlisthistory_46.option = company_pcoptions_4
    company_pcoptionlisthistory_46.body = u'IC2D/1.86/775'
    company_pcoptionlisthistory_46.date = datetime.datetime(2012, 8, 9, 12, 10, 10, 420626, tzinfo=utc)
    company_pcoptionlisthistory_46.user = auth_user_8
    company_pcoptionlisthistory_46.save()

    company_pcoptionlisthistory_47 = PcOptionListHistory()
    company_pcoptionlisthistory_47.pc = company_companypc_41
    company_pcoptionlisthistory_47.option = company_pcoptions_3
    company_pcoptionlisthistory_47.body = u'2*1024/DDR2/PC2-6400'
    company_pcoptionlisthistory_47.date = datetime.datetime(2012, 8, 9, 12, 9, 22, 587864, tzinfo=utc)
    company_pcoptionlisthistory_47.user = auth_user_8
    company_pcoptionlisthistory_47.save()

    company_pcoptionlisthistory_48 = PcOptionListHistory()
    company_pcoptionlisthistory_48.pc = company_companypc_41
    company_pcoptionlisthistory_48.option = company_pcoptions_2
    company_pcoptionlisthistory_48.body = u'ST/160/'
    company_pcoptionlisthistory_48.date = datetime.datetime(2012, 8, 9, 12, 8, 32, 236837, tzinfo=utc)
    company_pcoptionlisthistory_48.user = auth_user_8
    company_pcoptionlisthistory_48.save()

    company_pcoptionlisthistory_49 = PcOptionListHistory()
    company_pcoptionlisthistory_49.pc = company_companypc_40
    company_pcoptionlisthistory_49.option = company_pcoptions_2
    company_pcoptionlisthistory_49.body = u'ST/320/SATA'
    company_pcoptionlisthistory_49.date = datetime.datetime(2012, 8, 9, 11, 10, 29, 621926, tzinfo=utc)
    company_pcoptionlisthistory_49.user = auth_user_8
    company_pcoptionlisthistory_49.save()

    company_pcoptionlisthistory_50 = PcOptionListHistory()
    company_pcoptionlisthistory_50.pc = company_companypc_39
    company_pcoptionlisthistory_50.option = company_pcoptions_4
    company_pcoptionlisthistory_50.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_50.date = datetime.datetime(2012, 8, 9, 11, 9, 4, 567944, tzinfo=utc)
    company_pcoptionlisthistory_50.user = auth_user_8
    company_pcoptionlisthistory_50.save()

    company_pcoptionlisthistory_51 = PcOptionListHistory()
    company_pcoptionlisthistory_51.pc = company_companypc_39
    company_pcoptionlisthistory_51.option = company_pcoptions_3
    company_pcoptionlisthistory_51.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_51.date = datetime.datetime(2012, 8, 9, 11, 8, 37, 733349, tzinfo=utc)
    company_pcoptionlisthistory_51.user = auth_user_8
    company_pcoptionlisthistory_51.save()

    company_pcoptionlisthistory_52 = PcOptionListHistory()
    company_pcoptionlisthistory_52.pc = company_companypc_39
    company_pcoptionlisthistory_52.option = company_pcoptions_2
    company_pcoptionlisthistory_52.body = u'ST/320/SATA'
    company_pcoptionlisthistory_52.date = datetime.datetime(2012, 8, 9, 11, 7, 51, 442598, tzinfo=utc)
    company_pcoptionlisthistory_52.user = auth_user_8
    company_pcoptionlisthistory_52.save()

    company_pcoptionlisthistory_53 = PcOptionListHistory()
    company_pcoptionlisthistory_53.pc = company_companypc_38
    company_pcoptionlisthistory_53.option = company_pcoptions_4
    company_pcoptionlisthistory_53.body = u'IPDC/3.00/775'
    company_pcoptionlisthistory_53.date = datetime.datetime(2012, 8, 9, 10, 58, 59, 188303, tzinfo=utc)
    company_pcoptionlisthistory_53.user = auth_user_8
    company_pcoptionlisthistory_53.save()

    company_pcoptionlisthistory_54 = PcOptionListHistory()
    company_pcoptionlisthistory_54.pc = company_companypc_38
    company_pcoptionlisthistory_54.option = company_pcoptions_3
    company_pcoptionlisthistory_54.body = u'2048/DDR3/PC3-10700'
    company_pcoptionlisthistory_54.date = datetime.datetime(2012, 8, 9, 10, 57, 36, 91106, tzinfo=utc)
    company_pcoptionlisthistory_54.user = auth_user_8
    company_pcoptionlisthistory_54.save()

    company_pcoptionlisthistory_55 = PcOptionListHistory()
    company_pcoptionlisthistory_55.pc = company_companypc_38
    company_pcoptionlisthistory_55.option = company_pcoptions_2
    company_pcoptionlisthistory_55.body = u'ST/320/SATA'
    company_pcoptionlisthistory_55.date = datetime.datetime(2012, 8, 9, 10, 55, 47, 949741, tzinfo=utc)
    company_pcoptionlisthistory_55.user = auth_user_8
    company_pcoptionlisthistory_55.save()

    company_pcoptionlisthistory_56 = PcOptionListHistory()
    company_pcoptionlisthistory_56.pc = company_companypc_3
    company_pcoptionlisthistory_56.option = company_pcoptions_1
    company_pcoptionlisthistory_56.body = u'ST/80/SATA'
    company_pcoptionlisthistory_56.date = datetime.datetime(2012, 8, 3, 10, 29, 51, 642783, tzinfo=utc)
    company_pcoptionlisthistory_56.user = auth_user_8
    company_pcoptionlisthistory_56.save()

    company_pcoptionlisthistory_57 = PcOptionListHistory()
    company_pcoptionlisthistory_57.pc = company_companypc_3
    company_pcoptionlisthistory_57.option = company_pcoptions_1
    company_pcoptionlisthistory_57.body = u'ST/80/SATA'
    company_pcoptionlisthistory_57.date = datetime.datetime(2012, 8, 3, 10, 27, 21, 840899, tzinfo=utc)
    company_pcoptionlisthistory_57.user = auth_user_8
    company_pcoptionlisthistory_57.save()

    company_pcoptionlisthistory_58 = PcOptionListHistory()
    company_pcoptionlisthistory_58.pc = company_companypc_3
    company_pcoptionlisthistory_58.option = company_pcoptions_2
    company_pcoptionlisthistory_58.body = u'ST/200/SATA'
    company_pcoptionlisthistory_58.date = datetime.datetime(2012, 8, 3, 10, 27, 10, 530922, tzinfo=utc)
    company_pcoptionlisthistory_58.user = auth_user_8
    company_pcoptionlisthistory_58.save()

    company_pcoptionlisthistory_59 = PcOptionListHistory()
    company_pcoptionlisthistory_59.pc = company_companypc_3
    company_pcoptionlisthistory_59.option = company_pcoptions_4
    company_pcoptionlisthistory_59.body = u'IP4D/3.4/775'
    company_pcoptionlisthistory_59.date = datetime.datetime(2012, 8, 3, 10, 26, 1, 954009, tzinfo=utc)
    company_pcoptionlisthistory_59.user = auth_user_8
    company_pcoptionlisthistory_59.save()

    company_pcoptionlisthistory_60 = PcOptionListHistory()
    company_pcoptionlisthistory_60.pc = company_companypc_3
    company_pcoptionlisthistory_60.option = company_pcoptions_3
    company_pcoptionlisthistory_60.body = u'DDR2/2048/PC5300'
    company_pcoptionlisthistory_60.date = datetime.datetime(2012, 8, 3, 10, 25, 35, 781283, tzinfo=utc)
    company_pcoptionlisthistory_60.user = auth_user_8
    company_pcoptionlisthistory_60.save()

    company_pcoptionlisthistory_61 = PcOptionListHistory()
    company_pcoptionlisthistory_61.pc = company_companypc_3
    company_pcoptionlisthistory_61.option = company_pcoptions_1
    company_pcoptionlisthistory_61.body = u'ST/200/SATA'
    company_pcoptionlisthistory_61.date = datetime.datetime(2012, 8, 3, 10, 24, 17, 384522, tzinfo=utc)
    company_pcoptionlisthistory_61.user = auth_user_8
    company_pcoptionlisthistory_61.save()

    company_pcoptionlisthistory_62 = PcOptionListHistory()
    company_pcoptionlisthistory_62.pc = company_companypc_2
    company_pcoptionlisthistory_62.option = company_pcoptions_3
    company_pcoptionlisthistory_62.body = u'1024/DDR2/PC6400'
    company_pcoptionlisthistory_62.date = datetime.datetime(2012, 8, 1, 6, 17, 49, 170000, tzinfo=utc)
    company_pcoptionlisthistory_62.user = auth_user_5
    company_pcoptionlisthistory_62.save()

    company_pcoptionlisthistory_63 = PcOptionListHistory()
    company_pcoptionlisthistory_63.pc = company_companypc_2
    company_pcoptionlisthistory_63.option = company_pcoptions_1
    company_pcoptionlisthistory_63.body = u'ST/250Gb/SATA'
    company_pcoptionlisthistory_63.date = datetime.datetime(2012, 8, 1, 6, 17, 14, 270000, tzinfo=utc)
    company_pcoptionlisthistory_63.user = auth_user_5
    company_pcoptionlisthistory_63.save()

    company_pcoptionlisthistory_64 = PcOptionListHistory()
    company_pcoptionlisthistory_64.pc = company_companypc_2
    company_pcoptionlisthistory_64.option = company_pcoptions_4
    company_pcoptionlisthistory_64.body = u'IC2D/2.63/775'
    company_pcoptionlisthistory_64.date = datetime.datetime(2012, 8, 1, 6, 16, 49, 267000, tzinfo=utc)
    company_pcoptionlisthistory_64.user = auth_user_5
    company_pcoptionlisthistory_64.save()

    company_pcoptionlisthistory_65 = PcOptionListHistory()
    company_pcoptionlisthistory_65.pc = company_companypc_1
    company_pcoptionlisthistory_65.option = company_pcoptions_3
    company_pcoptionlisthistory_65.body = u'1024*2/DDR2/PC5300'
    company_pcoptionlisthistory_65.date = datetime.datetime(2012, 8, 1, 6, 1, 8, 948000, tzinfo=utc)
    company_pcoptionlisthistory_65.user = auth_user_5
    company_pcoptionlisthistory_65.save()

    company_pcoptionlisthistory_66 = PcOptionListHistory()
    company_pcoptionlisthistory_66.pc = company_companypc_1
    company_pcoptionlisthistory_66.option = company_pcoptions_3
    company_pcoptionlisthistory_66.body = u'1024*2/DDR2/PC5300'
    company_pcoptionlisthistory_66.date = datetime.datetime(2012, 8, 1, 6, 0, 39, 309000, tzinfo=utc)
    company_pcoptionlisthistory_66.user = auth_user_5
    company_pcoptionlisthistory_66.save()

    company_pcoptionlisthistory_67 = PcOptionListHistory()
    company_pcoptionlisthistory_67.pc = company_companypc_1
    company_pcoptionlisthistory_67.option = company_pcoptions_1
    company_pcoptionlisthistory_67.body = u'WD/320Gb/SATA'
    company_pcoptionlisthistory_67.date = datetime.datetime(2012, 8, 1, 5, 59, 39, 933000, tzinfo=utc)
    company_pcoptionlisthistory_67.user = auth_user_5
    company_pcoptionlisthistory_67.save()

    company_pcoptionlisthistory_68 = PcOptionListHistory()
    company_pcoptionlisthistory_68.pc = company_companypc_1
    company_pcoptionlisthistory_68.option = company_pcoptions_4
    company_pcoptionlisthistory_68.body = u'IP4/2,4/775'
    company_pcoptionlisthistory_68.date = datetime.datetime(2012, 8, 1, 5, 58, 56, 378000, tzinfo=utc)
    company_pcoptionlisthistory_68.user = auth_user_5
    company_pcoptionlisthistory_68.save()

    from ques.models import Questions

    ques_questions_1 = Questions()
    ques_questions_1.user_from = auth_user_7
    ques_questions_1.pc_from = None
    ques_questions_1.worker_from = u''
    ques_questions_1.user_to = auth_user_5
    ques_questions_1.date = datetime.datetime(2012, 8, 7, 16, 58, 40, 75331, tzinfo=utc)
    ques_questions_1.body = u'1C\r\nJaber\r\nMail\r\nProxy\r\nBackUp\r\n\u041a\u043e\u043c\u043f. \u043a\u043b\u0430\u0441\u0441'
    ques_questions_1.user_check = False
    ques_questions_1.user_check_date = None
    ques_questions_1.slug = u'al0012'
    ques_questions_1.answers = 6
    ques_questions_1.save()

    ques_questions_2 = Questions()
    ques_questions_2.user_from = auth_user_6
    ques_questions_2.pc_from = None
    ques_questions_2.worker_from = u''
    ques_questions_2.user_to = auth_user_7
    ques_questions_2.date = datetime.datetime(2012, 8, 4, 8, 36, 32, 356187, tzinfo=utc)
    ques_questions_2.body = u'test2'
    ques_questions_2.user_check = True
    ques_questions_2.user_check_date = datetime.datetime(2012, 8, 4, 8, 39, 0, 284163, tzinfo=utc)
    ques_questions_2.slug = u'fr0011'
    ques_questions_2.answers = 0
    ques_questions_2.save()

    ques_questions_3 = Questions()
    ques_questions_3.user_from = auth_user_6
    ques_questions_3.pc_from = None
    ques_questions_3.worker_from = u''
    ques_questions_3.user_to = auth_user_7
    ques_questions_3.date = datetime.datetime(2012, 8, 4, 7, 10, 41, 544567, tzinfo=utc)
    ques_questions_3.body = u'test'
    ques_questions_3.user_check = True
    ques_questions_3.user_check_date = datetime.datetime(2012, 8, 4, 8, 38, 54, 132536, tzinfo=utc)
    ques_questions_3.slug = u'fr0010'
    ques_questions_3.answers = 0
    ques_questions_3.save()

    ques_questions_4 = Questions()
    ques_questions_4.user_from = auth_user_7
    ques_questions_4.pc_from = None
    ques_questions_4.worker_from = u''
    ques_questions_4.user_to = auth_user_5
    ques_questions_4.date = datetime.datetime(2012, 8, 4, 7, 3, 22, 877622, tzinfo=utc)
    ques_questions_4.body = u'\u041b\u0435\u0448, \u0432\u0438\u0434\u0435\u043b \u0432\u043e\u043f\u0440\u043e\u0441 \u043f\u0440\u043e \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0438\u0439 \u0447\u0430\u0442. \r\n\u0423\u0436\u0435 \u0440\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u044b\u0432\u0430\u043b \u0442\u0430\u043a\u0443\u044e \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u044c \u0443 \u0441\u0435\u0431\u044f \u0432 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u043d\u0430 \u0431\u0430\u0437\u0435 e-jabber (\u0447\u0442\u043e-\u0442\u043e \u0432\u0440\u043e\u0434\u0435 \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0439 iqc). \r\n\u0415\u0441\u0442\u044c \u0435\u0449\u0435 \u0432\u0430\u0440\u0438\u0430\u043d\u0442 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0447\u0430\u0442 \u0432 \u0445\u0435\u043b\u043f\u0434\u0435\u0441\u043a\u0435. \u041d\u0443\u0436\u043d\u043e \u0443\u0442\u043e\u0447\u043d\u0438\u0442\u044c \u0447\u0442\u043e \u0438\u043c\u0435\u043d\u043d\u043e \u043e\u043d\u0438 \u0445\u043e\u0442\u044f\u0442.'
    ques_questions_4.user_check = False
    ques_questions_4.user_check_date = None
    ques_questions_4.slug = u'al0009'
    ques_questions_4.answers = 3
    ques_questions_4.save()

    ques_questions_5 = Questions()
    ques_questions_5.user_from = auth_user_1
    ques_questions_5.pc_from = company_companypc_15
    ques_questions_5.worker_from = u'\u041c\u0438\u0445\u0430\u0438\u043b'
    ques_questions_5.user_to = auth_user_5
    ques_questions_5.date = datetime.datetime(2012, 8, 3, 11, 32, 12, 88161, tzinfo=utc)
    ques_questions_5.body = u'\u041f\u0440\u043e\u0448\u0443 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u043f\u0440\u0438\u043e\u0431\u0440\u0435\u0442\u0435\u043d\u0438\u044f Windows Server \u0434\u043b\u044f 1\u0421 \u043d\u0430 30 \u043f\u043e\u043b\u044c\u0437\u043e\u0432\u0430\u0442\u0435\u043b\u0435\u0439'
    ques_questions_5.user_check = False
    ques_questions_5.user_check_date = None
    ques_questions_5.slug = u'ge0008'
    ques_questions_5.answers = 1
    ques_questions_5.save()

    ques_questions_6 = Questions()
    ques_questions_6.user_from = auth_user_1
    ques_questions_6.pc_from = company_companypc_15
    ques_questions_6.worker_from = u'\u041c\u0438\u0445\u0430\u0438\u043b'
    ques_questions_6.user_to = auth_user_5
    ques_questions_6.date = datetime.datetime(2012, 8, 3, 11, 29, 22, 450048, tzinfo=utc)
    ques_questions_6.body = u'\u043f\u0440\u043e\u0448\u0443 \u0440\u0430\u0441\u0441\u043c\u043e\u0442\u0440\u0435\u0442\u044c \u0432\u0430\u0440\u0438\u0430\u043d\u0442\u044b \u0432\u043d\u0443\u0442\u0440\u0435\u043d\u043d\u0435\u0433\u043e \u0447\u0430\u0442\u0430'
    ques_questions_6.user_check = False
    ques_questions_6.user_check_date = None
    ques_questions_6.slug = u'ge0007'
    ques_questions_6.answers = 1
    ques_questions_6.save()

    ques_questions_7 = Questions()
    ques_questions_7.user_from = auth_user_8
    ques_questions_7.pc_from = None
    ques_questions_7.worker_from = u''
    ques_questions_7.user_to = auth_user_7
    ques_questions_7.date = datetime.datetime(2012, 8, 3, 10, 44, 3, 391543, tzinfo=utc)
    ques_questions_7.body = u'\u0414\u043b\u044f "ge".\r\n\r\n\u041f\u0440\u043e\u0448\u0443 \u0443\u0434\u0430\u043b\u0438\u0442\u044c \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u0433\u0440\u0443\u043f\u043f\u044b: \u041e\u0441\u043d\u043e\u0432\u043d\u043e\u0439, \u0413\u0440\u0443\u043f\u043f\u0430 \u043c\u0435\u043d\u0435\u0434\u0436\u0435\u0440\u043e\u0432, \u0420\u0443\u043a\u043e\u0432\u043e\u0434\u0441\u0442\u0432\u043e.\r\n\u0420\u0435\u0430\u043b\u0438\u0437\u043e\u0432\u0430\u0442\u044c \u0441\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0443 \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u0432 \u0432\u044b\u043f\u0430\u0434\u0430\u044e\u0449\u0435\u043c \u0441\u043f\u0438\u0441\u043a\u0435 \u043f\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0443. \r\n\r\n\u0421\u043f\u0430\u0441\u0438\u0431\u043e.'
    ques_questions_7.user_check = False
    ques_questions_7.user_check_date = None
    ques_questions_7.slug = u'gr0006'
    ques_questions_7.answers = 1
    ques_questions_7.save()

    ques_questions_8 = Questions()
    ques_questions_8.user_from = auth_user_1
    ques_questions_8.pc_from = company_companypc_1
    ques_questions_8.worker_from = u'\u0428\u0435\u043b\u0430\u0433\u0438\u043d \u0421\u0435\u0440\u0433\u0435\u0439'
    ques_questions_8.user_to = auth_user_5
    ques_questions_8.date = datetime.datetime(2012, 8, 1, 6, 4, 34, 356000, tzinfo=utc)
    ques_questions_8.body = u'\u0414\u043e\u0431\u0440\u044b\u0439 \u0434\u0435\u043d\u044c, \u0436\u0434\u0435\u043c \u0432\u0430\u0448\u0438\u0445 \u0441\u043f\u0435\u0446\u0438\u0430\u043b\u0438\u0441\u0442\u043e\u0432 \u0434\u043b\u044f \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u0435\u043d\u0438\u044f \u043d\u0430\u0448\u0435\u0439 \u0441\u0435\u0442\u0435\u0432\u043e\u0439 \u0442\u043e\u043f\u043e\u043b\u043e\u0433\u0438\u0438.\r\n'
    ques_questions_8.user_check = True
    ques_questions_8.user_check_date = datetime.datetime(2012, 8, 1, 6, 24, 19, 404000, tzinfo=utc)
    ques_questions_8.slug = u'ge0004'
    ques_questions_8.answers = 1
    ques_questions_8.save()

    from ques.models import Chat

    ques_chat_1 = Chat()
    ques_chat_1.question = ques_questions_8
    ques_chat_1.admin_name = auth_user_5
    ques_chat_1.date = datetime.datetime(2012, 8, 1, 6, 13, 40, 423000, tzinfo=utc)
    ques_chat_1.body = u'2 \u0430\u0432\u0433\u0443\u0441\u0442\u0430 \u043a \u0412\u0430\u043c \u043f\u0440\u0438\u0435\u0434\u0435\u0442 \u041c\u0438\u0445\u0430\u0438\u043b \u0432 \u0440\u0430\u0439\u043e\u043d\u0435 17 \u0447\u0430\u0441\u043e\u0432. \u041d\u0430\u0447\u043d\u0435\u0442 \u0441\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0442\u044c \u043f\u0435\u0440\u0432\u044b\u0439 \u044d\u0442\u0430\u043f \u0442\u043e\u043f\u043e\u043b\u043e\u0433\u0438\u0438 \u0441\u0435\u0442\u0438. \u042d\u0442\u043e \u0434\u043e\u043b\u0436\u043d\u043e \u0437\u0430\u043d\u044f\u0442\u044c  20-30 \u043c\u0438\u043d\u0443\u0442.'
    ques_chat_1.save()

    ques_chat_2 = Chat()
    ques_chat_2.question = ques_questions_7
    ques_chat_2.admin_name = auth_user_7
    ques_chat_2.date = datetime.datetime(2012, 8, 4, 7, 0, 7, 940251, tzinfo=utc)
    ques_chat_2.body = u'\u041f\u0440\u0438 \u0434\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0438 \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0430 \u0432 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044e, \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u043f\u0440\u0435\u0434\u043e\u0441\u0442\u0430\u0432\u043b\u044f\u0435\u0442\u0441\u044f \u043e\u0431\u0449\u0438\u0439 \u0434\u043b\u044f \u0432\u0441\u0435\u0445 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0439. \u041f\u043e\u0434\u0443\u043c\u0430\u044e \u043d\u0430\u0434 \u0442\u0435\u043c, \u0447\u0442\u043e\u0431\u044b \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0441\u0432\u043e\u0439 \u0441\u043f\u0438\u0441\u043e\u043a \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u0434\u043b\u044f \u043a\u0430\u0436\u0434\u043e\u0439 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438. \r\n\u0421\u043e\u0440\u0442\u0438\u0440\u043e\u0432\u043a\u0443 \u043e\u0442\u0434\u0435\u043b\u043e\u0432 \u043f\u043e \u0430\u043b\u0444\u0430\u0432\u0438\u0442\u0443 \u0440\u0435\u0430\u043b\u0438\u0437\u0443\u044e.'
    ques_chat_2.save()

    ques_chat_3 = Chat()
    ques_chat_3.question = ques_questions_6
    ques_chat_3.admin_name = None
    ques_chat_3.date = datetime.datetime(2012, 8, 6, 5, 14, 48, 553138, tzinfo=utc)
    ques_chat_3.body = u'\u041f\u043e\u043a\u0430 \u0432 \u043a\u0430\u0447\u0435\u0441\u0442\u0432\u0435 \u0441\u043b\u0443\u0436\u0431\u044b \u043e\u0431\u043c\u0435\u043d\u0430 \u0431\u044b\u0441\u0442\u0440\u044b\u043c\u0438 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u044f\u043c\u0438 \u0440\u0435\u043a\u043e\u043c\u0435\u043d\u0434\u0443\u0435\u043c \u043f\u0440\u0438\u043c\u0435\u043d\u044f\u0442\u044c Skype. \u0423\u043d\u0438\u0432\u0435\u0440\u0441\u0430\u043b\u044c\u043d\u044b\u0439 \u0438\u043d\u0442\u0435\u0440\u0444\u0435\u0439\u0441 \u043d\u0435 \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u043f\u0440\u0438\u0432\u044b\u043a\u0430\u043d\u0438\u044f \u0438 \u043e\u0431\u0443\u0447\u0435\u043d\u0438\u044f, \u043d\u043e \u0442\u0440\u0435\u0431\u0443\u0435\u0442 \u043d\u0430\u043b\u0438\u0447\u0438\u044f \u0438\u043d\u0442\u0435\u0440\u043d\u0435\u0442\u0430.'
    ques_chat_3.save()

    ques_chat_4 = Chat()
    ques_chat_4.question = ques_questions_5
    ques_chat_4.admin_name = None
    ques_chat_4.date = datetime.datetime(2012, 8, 6, 5, 15, 48, 127972, tzinfo=utc)
    ques_chat_4.body = u'\u0417\u0430\u044f\u0432\u043a\u0430 \u043e\u0442\u043f\u0440\u0430\u0432\u043b\u0435\u043d\u0430 \u0432\u0435\u043d\u0434\u043e\u0440\u0443 Microsoft.'
    ques_chat_4.save()

    ques_chat_5 = Chat()
    ques_chat_5.question = ques_questions_4
    ques_chat_5.admin_name = auth_user_5
    ques_chat_5.date = datetime.datetime(2012, 8, 6, 6, 40, 55, 488018, tzinfo=utc)
    ques_chat_5.body = u'\u0421\u043b\u0443\u0436\u0431\u0430 \u043c\u0433\u043d\u043e\u0432\u0435\u043d\u043d\u044b\u0445 \u0441\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0439 \u0432\u043d\u0443\u0442\u0440\u0438 \u043e\u0440\u0433\u0430\u043d\u0438\u0437\u0430\u0446\u0438\u0438. \u0411\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e. \u0423 \u0442\u0435\u0431\u044f \u0436\u0430\u0431\u0435\u0440- \u043a\u043b\u0438\u0435\u043d\u0442\u0430 \u043d\u0430\u0434\u043e \u043f\u043e\u043a\u0443\u043f\u0430\u0442\u044c?'
    ques_chat_5.save()

    ques_chat_6 = Chat()
    ques_chat_6.question = ques_questions_4
    ques_chat_6.admin_name = None
    ques_chat_6.date = datetime.datetime(2012, 8, 6, 7, 23, 4, 855838, tzinfo=utc)
    ques_chat_6.body = u'\u0412\u0441\u0435 \u0431\u0435\u0441\u043f\u043b\u0430\u0442\u043d\u043e(\u043e\u043f\u0435\u043d\u0441\u043e\u0443\u0440\u0441). E-jabber \u0441\u0435\u0440\u0432\u0435\u0440 \u043d\u0430 unix, \u043a\u043b\u0438\u0435\u043d\u0442 \u043d\u0430\u043f\u0440\u0438\u043c\u0435\u0440 PSI. \u0423 \u043c\u0435\u043d\u044f \u0432 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0438 \u0432\u0441\u0435 \u0440\u0430\u0431\u043e\u0442\u0430\u0435\u0442 \u043d\u043e\u0440\u043c\u0430\u043b\u044c\u043d\u043e \u0432\u0441\u0435 \u0434\u043e\u0432\u043e\u043b\u044c\u043d\u044b, \u043d\u0430\u0441\u0442\u0440\u0430\u0438\u0432\u0430\u043b \u0441\u0430\u043c'
    ques_chat_6.save()

    ques_chat_7 = Chat()
    ques_chat_7.question = ques_questions_1
    ques_chat_7.admin_name = auth_user_5
    ques_chat_7.date = datetime.datetime(2012, 8, 9, 21, 21, 14, 478856, tzinfo=utc)
    ques_chat_7.body = u'\u0430 \u0441\u0435\u0440\u0432\u0435\u0440?'
    ques_chat_7.save()

    ques_chat_8 = Chat()
    ques_chat_8.question = ques_questions_1
    ques_chat_8.admin_name = auth_user_5
    ques_chat_8.date = datetime.datetime(2012, 8, 9, 22, 12, 42, 167839, tzinfo=utc)
    ques_chat_8.body = u'\u0423\u0431\u0438\u0440\u0430\u0435\u043c \u0438\u0437 \u0441\u043f\u0438\u0441\u043a\u0430 \u043a\u043e\u043c\u043f\u0430\u043d\u0438\u0439: \u0442\u0435\u0441\u0442-\u043a\u043e\u043c\u043f\u0430\u043d\u0438\u044e \u0438 \u0430\u043f\u0435\u043b\u044c\u0441\u0438\u043d \u0441\u043e \u0432\u0441\u0435\u043c\u0438 \u0438\u0445 \u0445\u0432\u043e\u0441\u0442\u0430\u043c\u0438 \u0435\u0441\u043b\u0438 \u0435\u0441\u0442\u044c.'
    ques_chat_8.save()

    ques_chat_9 = Chat()
    ques_chat_9.question = ques_questions_1
    ques_chat_9.admin_name = auth_user_5
    ques_chat_9.date = datetime.datetime(2012, 8, 9, 22, 16, 25, 140506, tzinfo=utc)
    ques_chat_9.body = u'\u0413\u0438\u043f\u0435\u0440\u0441\u0441\u044b\u043b\u043a\u0443 \u043f\u0440\u0438\u043a\u0440\u0435\u043f\u043b\u0435\u043d\u043d\u043e\u0433\u043e \u0444\u0430\u0439\u043b\u0430 \u043e\u0441\u0442\u0430\u0432\u044c \u0442\u043e\u043b\u044c\u043a\u043e \u043d\u0430 \u0438\u043c\u0435\u043d\u0438 \u0444\u0430\u0439\u043b\u0430, \u0432\u0441\u044e \u0441\u043b\u0443\u0436\u0435\u0431\u043d\u0443\u044e \u0438\u043d\u0444\u0443 (\u0440\u0430\u0437\u043c\u0435\u0440 \u0438 \u0442.\u0434.) \u043b\u0443\u0447\u0448\u0435 \u0441\u0434\u0435\u043b\u0430\u0442\u044c \u0442\u0435\u043a\u0441\u0442\u043e\u043c. \u0421\u043a\u043e\u043b\u044c\u043a\u043e \u0444\u0430\u0439\u043b\u043e\u0432 \u043a \u043a\u043e\u043c\u043f\u0443 \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u0438\u043a\u0440\u0443\u0442\u0438\u0442\u044c, \u0438 \u0447\u0442\u043e \u0431\u0443\u0434\u0435\u0442, \u0435\u0441\u043b\u0438 \u0438\u043c\u0435\u043d\u0430 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u0435?'
    ques_chat_9.save()

    ques_chat_10 = Chat()
    ques_chat_10.question = ques_questions_1
    ques_chat_10.admin_name = auth_user_5
    ques_chat_10.date = datetime.datetime(2012, 8, 9, 22, 19, 4, 652962, tzinfo=utc)
    ques_chat_10.body = u'\u041d\u043e\u0432\u044b\u0435 \u043e\u0442\u0432\u0435\u0442\u044b \u0441\u0432\u0435\u0440\u0445\u0443 \u043b\u0443\u0447\u0448\u0435 \u0434\u043e\u0431\u0430\u0432\u043b\u044f\u0442\u044c \u0432 \u043f\u0435\u0440\u0435\u043f\u0438\u0441\u043a\u0435, \u0447\u0442\u043e\u0431\u044b \u043d\u0435 \u043c\u043e\u0442\u0430\u0442\u044c \u0441\u0442\u0440\u0430\u043d\u0438\u0446\u0443 \u0432\u043d\u0438\u0437. :)'
    ques_chat_10.save()

    ques_chat_11 = Chat()
    ques_chat_11.question = ques_questions_4
    ques_chat_11.admin_name = auth_user_5
    ques_chat_11.date = datetime.datetime(2012, 8, 9, 22, 20, 40, 438333, tzinfo=utc)
    ques_chat_11.body = u'\u043f\u0440\u0438\u0433\u043e\u0442\u043e\u0432\u044c \u0441\u043a\u0440\u0438\u043d-\u0448\u043e\u0442\u0438\u043a\u0438 \u0440\u0430\u0431\u043e\u0442\u044b \u0447\u0430\u0442\u0430 \u0438 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b \u0441\u0435\u0440\u0432\u0435\u0440\u0430, \u0447\u0442\u043e\u0431\u044b \u0438\u0445 \u043f\u043e\u043a\u0430\u0437\u0430\u0442\u044c \u0413\u041f.'
    ques_chat_11.save()

    ques_chat_12 = Chat()
    ques_chat_12.question = ques_questions_1
    ques_chat_12.admin_name = None
    ques_chat_12.date = datetime.datetime(2012, 8, 10, 4, 28, 23, 300096, tzinfo=utc)
    ques_chat_12.body = u'\u041a \u043a\u043e\u043c\u043f\u044c\u044e\u0442\u0435\u0440\u0443 \u043c\u043e\u0436\u043d\u043e \u043f\u0440\u0438\u043a\u0440\u0443\u0447\u0438\u0432\u0430\u0442\u044c \u0441\u043a\u043e\u043b\u044c\u043a\u043e \u0443\u0433\u043e\u0434\u043d\u043e \u0444\u0430\u0439\u043b\u043e\u0432. \u0415\u0441\u043b\u0438 \u0438\u043c\u0435\u043d\u0430 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u0435 \u0442\u043e \u043d\u0438\u0447\u0435\u0433\u043e \u0441\u0442\u0440\u0430\u0448\u043d\u043e\u0433\u043e \u043d\u0435 \u0441\u043b\u0443\u0447\u0438\u0442\u044c\u0441\u044f, \u043f\u0440\u043e\u0441\u0442\u043e \u0431\u0443\u0434\u0435\u0442 \u0434\u0432\u0435 \u043e\u0434\u0438\u043d\u0430\u043a\u043e\u0432\u044b\u0435 \u0441\u0442\u0440\u043e\u043a\u0438 \u0432 \u0441\u043f\u0438\u0441\u043a\u0435.'
    ques_chat_12.save()

    ques_chat_13 = Chat()
    ques_chat_13.question = ques_questions_1
    ques_chat_13.admin_name = None
    ques_chat_13.date = datetime.datetime(2012, 8, 10, 4, 31, 25, 117981, tzinfo=utc)
    ques_chat_13.body = u'\u041a\u043e\u043c\u043f\u0430\u043d\u0438\u044f "\u0412\u0435\u043a\u0442\u043e\u0440-\u041b" - \u0436\u0438\u0432\u0430\u044f ?'
    ques_chat_13.save()

