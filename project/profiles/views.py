from models import Profile
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import Http404
from company.Forms import CreateUserForm


class CreateUserView(FormView):
    """
    Представление для создания пользователя и профайла
    """

    form_class = CreateUserForm
    success_url = None
    template_name = ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        self.user_profile = Profile.objects.get(user=self.user)
        if self.user_profile.is_super_user:
            return super(CreateUser, self).dispatch(request, *args, **kwargs)
        else:
            raise Http404

    def form_valid(self, form):
        first_name      = form.cleaned_data['first_name']
        last_name       = form.cleaned_data['last_name']
        is_super_user   = form.cleaned_data['is_super_user']
        is_report       = form.cleaned_data['is_report']
        telefon         = form.cleaned_data['telefon']

