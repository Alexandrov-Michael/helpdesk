# -*- coding:utf-8 -*-
__author__ = 'michael'


from proj import settings
from django.http import HttpResponsePermanentRedirect, get_host
import re


class HttpsRedirect(object):

    def process_request(self, request):
        system_secure = request.session.get('SYSTEM_S', False)
        path = request.get_full_path()
        path_first = path.split('/')[1]
        reg = re.compile('media')
        media = reg.search(path_first)
        static = None
        ajax = None
        if not media:
            reg = re.compile('static')
            static =reg.search(path_first)
            if not static:
                reg = re.compile('ajax')
                ajax = reg.search(path_first)
        if not system_secure and not request.method == 'POST' and not ajax and not media and not static:
            if settings.HOSTER:
                newurl = u'https://%s%s' % (get_host(request),request.get_full_path())
            else:
                newurl = u'http://%s%s' % (get_host(request),request.get_full_path())
            request.session['SYSTEM_S'] = True
            return HttpResponsePermanentRedirect(newurl)
        else:
            request.session['SYSTEM_S'] = False
