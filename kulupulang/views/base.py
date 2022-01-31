from django.views.generic import TemplateView
from django.views.generic.edit import FormView


class BaseView(TemplateView):
    pass


class BaseFormView(BaseView, FormView):
    verb = 'Submit form'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'verb': self.verb,
        }
