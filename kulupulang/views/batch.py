from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, reverse
from django.utils.functional import cached_property

from .base import BaseFormView, BaseView
from ..forms.dictionary import BatchForm
from ..forms.user import UserSelectForm
from ..models.dictionary import Batch, Discussion, Word
from ..models.user import User


class BatchMixin:
    @cached_property
    def batch(self):
        return get_object_or_404(Batch, pk=self.kwargs.get("batch"))

    @cached_property
    def has_edit_permission(self):
        if not self.request.user.is_authenticated:
            return False
        return self.batch.is_editable_by(self.request.user)


class AddContributorBatchView(BatchMixin, UserPassesTestMixin, BaseFormView):
    template_name = "kulupulang/batch/add_contributor.jinja"
    form_class = UserSelectForm
    verb = "add contributor"

    def form_valid(self, form):
        if (
            not form.cleaned_data["user"] == self.request.user
            and form.cleaned_data["user"] not in self.batch.contributors.all()
        ):
            self.batch.contributors.add(form.cleaned_data["user"])
        return redirect(self.batch.get_absolute_url())

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.batch,
        }

    def get_form(self):
        return UserSelectForm(
            excludes=[self.request.user, *self.batch.contributors.all()],
            **self.get_form_kwargs(),
        )

    def test_func(self):
        return self.has_edit_permission and self.batch.editable


class EditBatchView(BatchMixin, UserPassesTestMixin, BaseFormView):
    template_name = "kulupulang/batch/form.jinja"
    form_class = BatchForm

    def form_valid(self, form):
        form.instance.save()
        return redirect(form.instance.get_absolute_url())

    def get_form(self):
        return BatchForm(instance=self.batch, **self.get_form_kwargs())

    def test_func(self):
        return self.has_edit_permission and self.batch.editable

    @property
    def verb(self):
        return "edit batch: %s" % self.batch


class IndexBatchView(BaseView):
    template_name = "kulupulang/batch/index.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batches": Batch.objects.passed(),
        }


class NewBatchView(LoginRequiredMixin, BaseFormView):
    template_name = "kulupulang/batch/form.jinja"
    form_class = BatchForm
    verb = "new batch"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.save()
        return redirect(form.instance.get_absolute_url())


class OvenBatchView(BaseView):
    template_name = "kulupulang/batch/oven.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batches": Batch.objects.in_oven(),
        }


class PromoteBatchView(BatchMixin, UserPassesTestMixin, BaseView):
    template_name = "kulupulang/batch/promote.jinja"

    def post(self, request, **kwargs):
        with transaction.atomic():
            if not self.batch.submitted:
                self.batch.submit()
            self.batch.pass_batch()
        return redirect(reverse("dictionary.index"))

    def test_func(self):
        return self.request.user.is_superuser


class ShowBatchView(BatchMixin, BaseView):
    template_name = "kulupulang/batch/show.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.batch,
            "words": Word.objects.filter(batch=self.batch).order_by("headword"),
            "has_edit_permission": self.has_edit_permission,
            "user_discussion": self.get_user_discussion(),
        }

    def get_user_discussion(self):
        if not self.request.user.is_authenticated:
            return None
        return Discussion.objects.filter(
            batch=self.batch, resolved=False, opened_by=self.request.user
        ).first()


class SubmitBatchView(BatchMixin, UserPassesTestMixin, BaseView):
    template_name = "kulupulang/batch/submit.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.batch,
        }

    def post(self, request, **kwargs):
        self.batch.submit()
        return redirect(reverse("batch.oven"))

    def test_func(self):
        return self.has_edit_permission and self.batch.editable


class UnsubmitBatchView(BatchMixin, UserPassesTestMixin, BaseView):
    template_name = "kulupulang/batch/unsubmit.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "batch": self.batch,
        }

    def post(self, request, **kwargs):
        self.batch.unsubmit()
        return redirect(self.batch.get_absolute_url())

    def test_func(self):
        return (
            self.has_edit_permission and self.batch.submitted and not self.batch.passed
        )
