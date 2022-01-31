from django.shortcuts import get_object_or_404, redirect

from .base import BaseFormView, BaseView
from ..forms.dictionary import BatchForm
from ..models.dictionary import Batch


class NewBatchView(BaseFormView):
    template_name = 'kulupulang/batch/form.jinja'
    form_class = BatchForm
    verb = 'new batch'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()
        return redirect(form.instance.get_absolute_url())


class ShowBatchView(BaseView):
    template_name = 'kulupulang/batch/show.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': get_object_or_404(Batch, pk=kwargs.get('batch'))
        }
