# -*- coding:utf-8 -*-
from django.core.urlresolvers import reverse
from models import SimpleWiki
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from proj.utils.mixin import LoginRequiredMixin
from forms import AddWikiPageForm


class IndexWikiView(LoginRequiredMixin, ListView):
    """
    Представление для списка статей
    """
    model = SimpleWiki
    template_name = 'wiki_index.html'
    context_object_name = 'articals'

    def do_before_handler(self):
        self.skip_only_user()


class AddArticleView(LoginRequiredMixin, CreateView):
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



class ReadArcticleView(LoginRequiredMixin, DetailView):
    """
    Представление для просмотра статьи
    """
    model = SimpleWiki
    template_name = 'read_article.html'
    context_object_name = 'article'

    def do_before_handler(self):
        self.skip_only_user()
