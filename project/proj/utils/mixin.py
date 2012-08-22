# -*- coding:utf-8 -*-
__author__ = 'michael'
from django.utils import simplejson
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from profiles.models import Profile



class JSONResponseMixin(object):
    """
    Микшин для ответа JSON
    context = {item: value}
    """
    def render_to_response(self, context, **response_kwargs):
        json = simplejson.dumps(context)
        return HttpResponse(json, mimetype='application/json', **response_kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)




class JSONQuerySetValuesResponseMixin(object):
    """
    Микшин для ответа JSON, context = queryset.values()
    """
    def render_to_response(self, context, **response_kwargs):
        data = {}
        i = 0
        if context:
            for item in context:
                data[i] = item
                i += 1
        json = simplejson.dumps(data)
        return HttpResponse(json, mimetype='application/json', **response_kwargs)

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)



class LoginRequiredMixin(object):
    """
    Микшин для проверки логина пользователя
    """

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # Try to dispatch to the right method; if a method doesn't exist,
        # defer to the error handler. Also defer to the error handler if the
        # request method isn't on the approved list.
        if request.method.lower() in self.http_method_names:
            handler = getattr(self, request.method.lower(), self.http_method_not_allowed)
        else:
            handler = self.http_method_not_allowed
        self.request = request
        self.args = args
        self.kwargs = kwargs
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        self.do_before_handler()
        return handler(request, *args, **kwargs)

    def do_before_handler(self):
        pass

    def skip_only_super_user(self):
        if not self.user_profile.is_super_user:
            raise Http404

    def skip_only_user(self):
        if self.user_profile.is_company:
            raise Http404

    def skip_only_report(self):
        if not self.user_profile.is_report:
            raise Http404

    def skip_only_buh(self):
        if not self.user_profile.is_buh:
            raise Http404


class UpdateContextDataMixin(object):
    """
    Микшин для апдейта контекст дата
    """

    def update_context(self, context):
        context['user_is_company']  = self.user_profile.is_company
        context['user_is_report']   = self.user_profile.is_report
        context['user_is_super']    = self.user_profile.is_super_user
        context['success_message']  = self.request.session.pop('message', '')
        context['is_error_message'] = self.request.session.pop('is_error_message', False)
        context['user_is_buh']      = self.user_profile.is_buh
        return context

    def set_message(self, text, is_error_message = False):
        """
        устанавливает сообщение для вывода
        """
        self.request.session['message'] = text
        if is_error_message:
            self.request.session['is_error_message'] = True


class GetOdjectMixin(object):
    """
    Микшин для определения pk
    """
    pk_url_kwarg  = 'pk'

    def get_pk(self):
        pk = self.kwargs.get(self.pk_url_kwarg, None)
        if pk is not None:
            return pk
        else:
            raise Http404



class SummMixen(LoginRequiredMixin, UpdateContextDataMixin, GetOdjectMixin):
    """
    Общий микшин
    """
    pass