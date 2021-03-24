from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.signing import BadSignature
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from django.views.generic.base import TemplateView
from django.views.generic.edit import UpdateView, CreateView
from .utilities import signer
from .models import AdvUser
from .forms import ChangeUserinfoForm, RegisterUserForm


@login_required
def profile(request) :
    return render(request, 'accounts/profile.html')

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView) :
    model = AdvUser
    template_name = 'accounts/change_user_info.html'
    form_class = ChangeUserinfoForm
    success_url = reverse_lazy('accounts:profile')
    success_message = 'Данные пользователя изменены'

    def setup(self, request, *args, **kwargs) :
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class AccountsPasswordChangeView(PasswordChangeView):
    success_url = reverse_lazy('accounts:profile')
    template_name = 'accounts/password_change.html'


class RegisterUserView(CreateView):
    model = AdvUser
    template_name = 'accounts/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('accounts:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'accounts/register_done.html'


def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'accounts/bad_signature.html')
    user = get_object_or_404(AdvUser, username=username)
    if user.is_activated:
        template = 'accounts/user_is_activated.html'
    else:
        template = 'accounts/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)
