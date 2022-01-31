from .base import BaseView
from ..models.dictionary import Word


class IndexDictionaryView(BaseView):
    template_name = 'kulupulang/dictionary/index.jinja'

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            'words': Word.objects.filter(passed=True).order_by('headword'),
        }
