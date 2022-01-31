from django.contrib.auth import views
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy


class LoginView(views.LoginView):
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
