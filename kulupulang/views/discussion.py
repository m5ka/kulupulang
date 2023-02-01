from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.functional import cached_property

from .base import BaseView
from .batch import BatchMixin
from ..models.dictionary import Batch, Discussion


class IndexDiscussionView(BaseView):
    template_name = "kulupulang/discussion/index.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batches": Batch.objects.flagged(),
        }


class NewDiscussionView(BatchMixin, LoginRequiredMixin, BaseView):
    template_name = "kulupulang/discussion/new.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.batch,
        }

    def post(self, request, **kwargs):
        self.batch.raise_discussion(self.request.user)
        return redirect(reverse("discussion.index"))


class ResolveDiscussionView(UserPassesTestMixin, BaseView):
    template_name = "kulupulang/discussion/resolve.jinja"

    @cached_property
    def discussion(self):
        return get_object_or_404(Discussion, pk=self.kwargs.get("discussion"))

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.discussion.batch,
        }

    def post(self, request, **kwargs):
        self.discussion.resolve()
        return redirect(reverse("discussion.index"))

    def test_func(self):
        return self.discussion.opened_by == self.request.user
