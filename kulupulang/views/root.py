from django.shortcuts import redirect

from .base import BaseFormView
from .batch import BatchMixin
from ..forms.dictionary import RootForm


class NewRootView(BatchMixin, BaseFormView):
    template_name = 'kulupulang/root/form.jinja'
    form_class = RootForm
    verb = 'new root'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
        }

    def form_valid(self, form):
        form.instance.batch = self.batch
        form.instance.created_by = self.request.user
        form.instance.save()
        return redirect(self.batch.get_absolute_url())
