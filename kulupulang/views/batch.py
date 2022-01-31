from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property

from .base import BaseFormView, BaseView
from ..forms.dictionary import BatchForm
from ..models.dictionary import Batch, Root, Word


class BatchMixin:
    @cached_property
    def batch(self):
        return get_object_or_404(Batch, pk=self.kwargs.get('batch'))


class NewBatchView(BaseFormView):
    template_name = 'kulupulang/batch/form.jinja'
    form_class = BatchForm
    verb = 'new batch'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()
        return redirect(form.instance.get_absolute_url())


class ShowBatchView(BatchMixin, BaseView):
    template_name = 'kulupulang/batch/show.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
            'roots': Root.objects.filter(batch=self.batch),
            'words': Word.objects.filter(batch=self.batch),
        }
