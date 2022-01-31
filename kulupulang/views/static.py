from .base import BaseView
from ..models.dictionary import Batch


class DashboardView(BaseView):
    template_name = 'kulupulang/static/dashboard.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'unsubmitted_batches': Batch.objects.filter(created_by=self.request.user, submitted=False)
        }
