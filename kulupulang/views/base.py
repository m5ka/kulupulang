from random import choice

from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'greeting': choice([
                'hello',
                'howdy',
                'greetings',
                'jubilations',
                '\'sup',
                'how\'s it hangin\'',
                'henlo',
                'uwu',
                'merriment',
                'charmed i\'m sure',
                'salutations',
            ])
        }


class BaseFormView(BaseView, FormView):
    verb = 'Submit form'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'verb': self.verb,
        }
