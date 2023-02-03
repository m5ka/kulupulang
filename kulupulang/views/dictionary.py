from django.core.paginator import Paginator

from .base import BaseView
from ..models.dictionary import Word


class IndexDictionaryView(BaseView):
    template_name = "kulupulang/dictionary/index.jinja"
    words_per_page = 100

    def get_words(self, search=None, by=None):
        words = Word.objects.filter(passed=True).order_by("headword")
        if search:
            if by == "definition":
                return words.filter(definition__icontains=search)
            return words.filter(headword__istartswith=search)
        return words

    def get_context_data(self, **kwargs):
        search = self.request.GET.get("search", None)
        by = self.request.GET.get("by", None)
        words = self.get_words(search=search, by=by)
        paginator = Paginator(words, self.words_per_page)
        page_num = int(self.request.GET.get("page", 1))
        return {
            **super().get_context_data(**kwargs),
            "page": paginator.get_page(page_num),
            "search": search if search else "",
            "by": by if by else "headword",
        }


class ShowDictionaryView(BaseView):
    template_name = "kulupulang/dictionary/show.jinja"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "words": Word.objects.filter(
                slug=self.kwargs.get("slug"), passed=True
            ).order_by("headword"),
        }
