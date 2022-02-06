from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property

from .base import BaseFormView, BaseView
from .batch import BatchMixin
from ..forms.dictionary import RootForm
from ..models.dictionary import Root


class RootMixin:
    @cached_property
    def root(self):
        return get_object_or_404(Root, batch=self.batch, pk=self.kwargs.get('root'))


class DeleteRootView(BatchMixin, RootMixin, UserPassesTestMixin, BaseView):
    template_name = 'kulupulang/root/delete.jinja'

    def post(self, request, **kwargs):
        self.root.delete()
        return redirect(self.batch.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
            'root': self.root,
        }

    def test_func(self):
        return self.has_edit_permission and self.root.editable


class EditRootView(BatchMixin, RootMixin, UserPassesTestMixin, BaseFormView):
    template_name = 'kulupulang/root/form.jinja'
    form_class = RootForm

    def form_valid(self, form):
        form.instance.save()
        return redirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
        }

    def get_form(self):
        return RootForm(instance=self.root, **self.get_form_kwargs())

    def test_func(self):
        return self.has_edit_permission and self.root.editable

    @property
    def verb(self):
        return 'edit root: %s' % self.root.root


class NewRootView(BatchMixin, UserPassesTestMixin, BaseFormView):
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

    def test_func(self):
        return self.has_edit_permission and self.batch.editable


class ShowRootView(BatchMixin, RootMixin, BaseView):
    template_name = 'kulupulang/root/show.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'root': self.root,
            'batch': self.batch,
            'has_edit_permission': self.has_edit_permission,
        }
