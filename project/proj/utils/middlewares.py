# -*- coding:utf-8 -*-
__author__ = 'michael'


from django.http import HttpResponsePermanentRedirect, get_host
from django.conf import settings







class SSLRedirect(object):
    """
    Мидл варе для перенаправления на https
    """
    SSL = 'SSL'

    def is_secure(self, request):
        if 'HTTP_X_FORWARDED_SSL' in request.META:
            return request.META['HTTP_X_FORWARDED_SSL'] == 'on'
        return False

    def process_view(self, request, view_func, view_args, view_kwargs):
        if self.SSL in view_kwargs:
            secure = view_kwargs[self.SSL]
            del view_kwargs[self.SSL]
        else:
            secure = False
        if not secure == self.is_secure(request):
            return self._redirect(request, secure)

    def _redirect(self, request, secure):
        protocol = secure and "https" or "http"
        newurl = "%s://%s%s" % (protocol,get_host(request),request.get_full_path())
        if settings.DEBUG and request.method == 'POST':
            raise RuntimeError,\
            """Django can't perform a SSL redirect while maintaining POST data.
  Please structure your views so that redirects only occur during GETs."""
        return HttpResponsePermanentRedirect(newurl) #I have not had time to test this, but it appears to work better.
