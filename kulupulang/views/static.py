from django.db.models import Q

from .base import BaseView
from ..models.dictionary import Batch


class DashboardView(BaseView):
    template_name = "kulupulang/static/dashboard.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "unsubmitted_batches": self.get_unsubmitted_batches(),
        }

    def get_unsubmitted_batches(self):
        return Batch.objects.filter(
            Q(contributors=self.request.user) | Q(created_by=self.request.user),
            submitted=False,
        )
