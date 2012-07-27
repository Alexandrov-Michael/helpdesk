# -*- coding:utf-8 -*-
__author__ = 'michael'


from django.http import HttpResponsePermanentRedirect
from proj import settings




class SecureRequiredMiddleware(object):
    """
    Мидлваре для перенаправления на https
    """
    def __init__(self):
        self.enabled = getattr(settings, 'HTTPS_SUPPORT')

    def process_request(self, request):
        if self.enabled and not request.is_secure():
            request_url = request.build_absolute_uri(request.get_full_path())
            secure_url = request_url.replace('http://', 'https://')
            return HttpResponsePermanentRedirect(secure_url)
        return None