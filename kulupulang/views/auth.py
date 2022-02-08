from django.contrib import messages
from django.contrib.auth import views
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy

from .base import BaseFormView, BaseView
from ..forms.user import UserSettingsForm


class LoginView(BaseView, views.LoginView):
    template_name = 'kulupulang/auth/login.jinja'
    success_url = reverse_lazy('dashboard')

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'next': self.request.GET.get('next', self.success_url)
        }

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect(self.success_url)
        return super().get(request, *args, **kwargs)


class LogoutView(views.LogoutView):
    next_page = 'login'


class SettingsView(LoginRequiredMixin, BaseFormView):
    template_name = 'kulupulang/auth/settings.jinja'
    form_class = UserSettingsForm

    def form_valid(self, form):
        form.instance.save()
        messages.success(self.request, 'your settings were saved successfully')
        return redirect(reverse('settings'))

    def get_form(self):
        return UserSettingsForm(instance=self.request.user,  **self.get_form_kwargs())
