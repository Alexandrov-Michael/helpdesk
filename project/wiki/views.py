# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from models import SimpleWiki
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.detail import DetailView
from proj.utils.mixin import LoginRequiredMixin, UpdateContextDataMixin
from forms import AddWikiPageForm
from conformity.models import Conform
from proj import settings
from django.contrib.auth.models import User


class IndexWikiView(LoginRequiredMixin, UpdateContextDataMixin, ListView):
    """
    Представление для списка статей
    """
    model = SimpleWiki
    template_name = 'wiki_index.html'
    context_object_name = 'articals'

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        context = super(IndexWikiView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def get_queryset(self):
        queryset = super(IndexWikiView, self).get_queryset()
        return queryset.order_by('-date')


class AddArticleView(LoginRequiredMixin, UpdateContextDataMixin, CreateView):
    """
    Представление для создания вики страницы
    """
    model = SimpleWiki
    form_class = AddWikiPageForm
    success_url = None
    template_name = 'add_wiki_page.html'

    def do_before_handler(self):
        self.skip_only_user()

    def get_success_url(self):
        url = reverse('wiki')
        return url

    def get_context_data(self, **kwargs):
        context = super(AddArticleView, self).get_context_data(**kwargs)
        context['is_system_programmer'] = self.is_system_programmer()
        return self.update_context(context)

    def form_valid(self, form):
        self.set_message(u'Страница успешно добавлена.')
        return super(AddArticleView, self).form_valid(form)

    def is_system_programmer(self):
        """
        определяет системный програмист ли этот юзер
        """
        result = False
        try:
            conform = Conform.objects.get(perem = settings.SYSTEM_PROGRAMMER)
            sys_user = User.objects.get(id = conform.object_id)
        except Conform.DoesNotExist:
            self.set_message(u'Глобавльная переменная соответствия %s не определена' % (settings.SYSTEM_PROGRAMMER), True)
            return result
        except User.DoesNotExist:
            self.set_message(u'Пользователь для системных изменений по глобальной переменной не существует', True)
            return result
        if self.user == sys_user:
            result = True
        return result




class ReadArcticleView(LoginRequiredMixin, UpdateContextDataMixin, DetailView):
    """
    Представление для просмотра статьи
    """
    model = SimpleWiki
    template_name = 'read_article.html'
    context_object_name = 'article'

    def do_before_handler(self):
        self.skip_only_user()

    def get_context_data(self, **kwargs):
        context = super(ReadArcticleView, self).get_context_data(**kwargs)
        return self.update_context(context)


class EditArticleView(LoginRequiredMixin, UpdateContextDataMixin, UpdateView):
    """
    Представление для изменения статьи в вики
    """
    model = SimpleWiki
    template_name = 'edit_article.html'
    form_class = AddWikiPageForm
    success_url = None

    def do_before_handler(self):
        self.skip_only_user()


    def get_success_url(self):
        url = reverse('wiki')
        return url

    def get_context_data(self, **kwargs):
        context = super(EditArticleView, self).get_context_data(**kwargs)
        return self.update_context(context)

    def form_valid(self, form):
        self.set_message(u'Страница успешно изменена.')
        return super(EditArticleView, self).form_valid(form)
