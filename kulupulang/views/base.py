from os import path
from random import choice

from django.conf import settings
from django.views.generic import TemplateView
from django.views.generic.edit import FormView

from kulupulang.models.theme import Theme


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "theme": self.get_user_theme(),
            "greeting": choice(
                [
                    "hello",
                    "howdy",
                    "greetings",
                    "jubilations",
                    "'sup",
                    "how's it hangin'",
                    "henlo",
                    "uwu",
                    "merriment",
                    "charmed i'm sure",
                    "salutations",
                ]
            ),
        }

    def get_user_theme(self):
        if not self.request.user.is_authenticated:
            try:
                return Theme.objects.get(name="default")
            except Theme.DoesNotExist:
                return None
        return self.request.user.theme


class BaseFormView(BaseView, FormView):
    verb = "Submit form"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "verb": self.verb,
        }
