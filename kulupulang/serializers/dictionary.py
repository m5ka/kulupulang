from rest_framework import serializers

from kulupulang.models.dictionary import Batch, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = [
            "id",
            "headword",
            "slug",
            "pos",
            "cls",
            "definition",
            "etymology",
            "notes",
            "url",
        ]


class BatchSerializer(serializers.ModelSerializer):
    word_set = WordSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Batch
        fields = [
            "id",
            "name",
            "description",
            "submitted",
            "submitted_at",
            "discussion_count",
            "passed",
            "passed_at",
            "voting_from",
            "voting_hours",
            "url",
            "word_set",
        ]
