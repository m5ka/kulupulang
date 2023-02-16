from rest_framework import serializers

from kulupulang.models.dictionary import Batch, Word


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ["headword", "pos", "cls", "definition", "etymology", "notes"]


class BatchSerializer(serializers.ModelSerializer):
    word_set = WordSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Batch
        fields = [
            "name",
            "description",
            "submitted",
            "submitted_at",
            "discussion_count",
            "passed",
            "passed_at",
            "voting_from",
            "voting_hours",
            "word_set",
        ]
