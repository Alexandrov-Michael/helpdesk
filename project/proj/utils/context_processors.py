# -*- coding:utf-8 -*-
__author__ = 'michael'

def username(request):
    """
    Контестный процессор для личного кабинет вычисляет имя пользователя или компании
    """
    try:
        user = request.user.first_name
    except AttributeError:
        user = u'Пользователь'

    return {
        u'USER_LOGON' : user,
    }