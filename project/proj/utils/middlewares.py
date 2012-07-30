# -*- coding:utf-8 -*-
__author__ = 'michael'


from proj import settings
from django.http import HttpResponsePermanentRedirect, get_host
import re


class HttpsRedirect(object):
    """
    Мидлваре для перенаправления на ssl,
    потому что у хостера стоит связка nginx и apache,
    и нет возможности настроить nginx
    """

    def process_request(self, request):
        if settings.HOSTER:
            system_secure = request.session.get('SYSTEM_S', False)
            path = request.get_full_path()
            path_first = path.split('/')[1]
            reg = re.compile(ur'(media)|(static)|(ajax)')
            search = reg.search(path_first)
            if not system_secure and not request.method == 'POST' and not search:
                newurl = u'https://%s%s' % (get_host(request),request.get_full_path())
                request.session['SYSTEM_S'] = True
                return HttpResponsePermanentRedirect(newurl)
            else:
                request.session['SYSTEM_S'] = False
