from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.utils.functional import cached_property

from .base import BaseFormView, BaseView
from .batch import BatchMixin
from ..forms.dictionary import WordForm
from ..models.dictionary import Word


class WordMixin:
    @cached_property
    def word(self):
        return get_object_or_404(Word, batch=self.batch, pk=self.kwargs.get('word'))


class DeleteWordView(BatchMixin, WordMixin, UserPassesTestMixin, BaseView):
    template_name = 'kulupulang/word/delete.jinja'
    form_class = WordForm

    def post(self, request, **kwargs):
        self.word.delete()
        return redirect(self.batch.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
            'word': self.word,
        }

    def test_func(self):
        return self.has_edit_permission and self.word.editable


class EditWordView(BatchMixin, WordMixin, UserPassesTestMixin, BaseFormView):
    template_name = 'kulupulang/word/form.jinja'
    form_class = WordForm

    def form_valid(self, form):
        form.instance.save()
        return redirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
        }

    def get_form(self):
        return WordForm(instance=self.word, **self.get_form_kwargs())

    def test_func(self):
        return self.has_edit_permission and self.word.editable

    @property
    def verb(self):
        return 'edit word: %s' % self.word.headword


class NewWordView(BatchMixin, UserPassesTestMixin, BaseFormView):
    template_name = 'kulupulang/word/form.jinja'
    form_class = WordForm
    verb = 'new word'

    def form_valid(self, form):
        form.instance.batch = self.batch
        form.instance.created_by = self.request.user
        form.instance.save()
        return redirect(form.instance.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
        }

    def test_func(self):
        return self.has_edit_permission and self.batch.editable


class ShowWordView(BatchMixin, WordMixin, BaseView):
    template_name = 'kulupulang/word/show.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'batch': self.batch,
            'word': self.word,
            'has_edit_permission': self.has_edit_permission,
        }
