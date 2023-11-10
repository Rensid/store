from typing import Any, Dict

from django import http
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from common.views import TitleMixin
from products.models import Basket
from users.forms import UserLoginForm, UserProfileForm, UserRegistrationForm
from users.models import EmailVerification, User


class LoginUserView(LoginView):
    authentication_form = UserLoginForm
    template_name = 'users/login.html'


class UserRegistrationView(SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы'


class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    title = 'Store - Профиль'

    def get_success_url(self) -> str:
        return reverse_lazy('users:profile', args=(self.object.id,))

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context


class EmailVerificationView(TitleMixin, TemplateView):
    title = 'Store - подтверждение электронной почты'
    template_name = 'users/email_verification.html'

    def get(self, request, *args: Any, **kwargs: Any):
        code = kwargs.get('code')
        user = User.objects.get(email=kwargs.get('email'))
        email_verifications = EmailVerification.objects.filter(
            user=user, code=code)
        if email_verifications.exists and not email_verifications.first().is_expired():
            user.is_verified_email = True
            user.save()
            return super().get(request, *args, **kwargs)
        else:
            return HttpResponseRedirect(reverse('index'))
