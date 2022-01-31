from .base import BaseModelForm
from ..models.dictionary import Batch, Root, Word


class BatchForm(BaseModelForm):
    class Meta:
        model = Batch
        fields = ('name', 'description', 'voting_hours',)


class RootForm(BaseModelForm):
    class Meta:
        model = Root
        fields = ('root', 'gloss', 'notes',)


class WordForm(BaseModelForm):
    class Meta:
        model = Word
        fields = ('headword', 'pos', 'cls', 'gloss', 'etymology', 'notes',)
