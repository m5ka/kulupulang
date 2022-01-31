from .base import BaseModelForm
from ..models.dictionary import Batch


class BatchForm(BaseModelForm):
    class Meta:
        model = Batch
        fields = ('name', 'description', 'voting_hours',)
