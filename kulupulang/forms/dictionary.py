from .base import BaseModelForm
from ..models.dictionary import Batch, Word


class BatchForm(BaseModelForm):
    class Meta:
        model = Batch
        fields = (
            "name",
            "description",
            "voting_hours",
        )


class WordForm(BaseModelForm):
    class Meta:
        model = Word
        fields = (
            "headword",
            "pos",
            "cls",
            "definition",
            "etymology",
            "notes",
        )
