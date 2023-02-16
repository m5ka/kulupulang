from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ReadOnlyModelViewSet

from kulupulang.models.dictionary import Batch, Word
from kulupulang.serializers.dictionary import BatchSerializer, WordSerializer


class BatchViewSet(ReadOnlyModelViewSet):
    queryset = Batch.objects.prefetch_related("word_set")
    serializer_class = BatchSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["name", "passed"]
    search_fields = ["name"]


class WordViewSet(ReadOnlyModelViewSet):
    queryset = Word.objects.filter(passed=True)
    serializer_class = WordSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["headword", "pos", "cls", "definition"]
    search_fields = ["definition"]
