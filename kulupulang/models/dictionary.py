from datetime import timedelta
from math import ceil

from django.db import models, transaction
from django.utils import timezone
from django.urls import reverse

from .base.abstracts import UpdatableModel
from .base.choices import PartOfSpeech, WordClass
from .base.mixins import AutoSlugMixin
from .user import User


class BatchManager(models.Manager):
    def in_oven(self):
        return self.filter(submitted=True, discussion_count=0, passed=False)

    def passed(self):
        return self.filter(passed=True)

    def flagged(self):
        return self.filter(submitted=True, discussion_count__gt=0)


class Batch(UpdatableModel):
    name = models.CharField(
        db_index=True,
        max_length=255,
        help_text="a nice little name for this batch you're cooking up. any name will do.",
    )
    description = models.TextField(
        blank=True,
        help_text="this is optional, but if you feel like giving a little description then hey that's totally cool",
    )
    submitted = models.BooleanField(
        default=False,
    )
    submitted_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    discussion_count = models.IntegerField(
        default=0,
    )
    hours_left_before_discussion = models.IntegerField(
        default=0,
    )
    passed = models.BooleanField(
        default=False,
    )
    passed_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name="batch_set",
    )
    contributors = models.ManyToManyField(
        User,
        blank=True,
        related_name="batch_contribution_set",
    )
    voting_from = models.DateTimeField(
        default=timezone.now,
    )
    voting_hours = models.IntegerField(
        default=48,
        help_text="how many hours should this stay in the oven before it's cooked and in the dictionary?",
    )

    objects = BatchManager()

    def check_passed(self):
        voting_end = self.voting_from + timedelta(hours=self.voting_hours)
        return not (self.discussion_count > 0 or timezone.now() < voting_end)

    def decrement_discussion_count(self):
        if self.discussion_count > 0:
            self.discussion_count -= 1
            if self.discussion_count == 0:
                hours = (
                    self.hours_left_before_discussion
                    if self.hours_left_before_discussion >= 1
                    else 1
                )
                self.submitted_at = timezone.now() - timedelta(
                    hours=self.voting_hours - hours
                )
                self.hours_left_before_discussion = 0
            self.save()

    @property
    def editable(self):
        return not self.submitted and not self.passed

    def get_absolute_url(self):
        return reverse("batch.show", kwargs={"batch": self.pk})

    def is_editable_by(self, user):
        return self.created_by == user or user in self.contributors.all()

    @transaction.atomic
    def pass_batch(self):
        self.passed = True
        self.passed_at = timezone.now()
        self.save()

        Word.objects.filter(batch=self).update(passed=True, passed_at=timezone.now())

    def raise_discussion(self, user):
        if Discussion.objects.filter(
            batch=self, resolved=False, opened_by=user
        ).exists():
            return
        with transaction.atomic():
            Discussion.objects.create(
                batch=self,
                opened_by=user,
            )
            if self.hours_left_before_discussion == 0:
                time_elapsed = timezone.now() - self.submitted_at
                self.hours_left_before_discussion = ceil(
                    time_elapsed.total_seconds() / 60 / 60
                )
            self.discussion_count += 1
            self.save()

    def submit(self):
        self.submitted = True
        self.submitted_at = timezone.now()
        self.save()

    @transaction.atomic
    def unsubmit(self):
        Discussion.objects.filter(batch=self).delete()
        self.discussion_count = 0
        self.submitted = False
        self.save()

    def __str__(self):
        return self.name


class Discussion(UpdatableModel):
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
    )
    resolved = models.BooleanField(
        default=False,
    )
    opened_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )

    @transaction.atomic
    def resolve(self):
        if self.resolved:
            return
        self.resolved = True
        self.save()
        self.batch.decrement_discussion_count()


class Word(UpdatableModel, AutoSlugMixin):
    headword = models.CharField(
        db_index=True,
        max_length=255,
        blank=False,
        help_text="this is the word itself.",
    )
    slug = models.CharField(
        max_length=255,
        blank=True,
        null=False,
    )
    pos = models.CharField(
        max_length=128,
        blank=False,
        choices=PartOfSpeech.CHOICES,
    )
    cls = models.CharField(
        max_length=128,
        blank=True,
        choices=WordClass.CHOICES,
    )
    definition = models.TextField(
        blank=False,
        help_text="what does this word mean? this will appear in the overall dictionary page with the part of speech.",
    )
    etymology = models.TextField(
        blank=True,
        help_text="optionally, where does this word come from? this will only appear on the word's page.",
    )
    notes = models.TextField(
        blank=True,
        help_text="any other optional notes about this word. this will only appear on the word's page.",
    )
    batch = models.ForeignKey(
        Batch,
        on_delete=models.CASCADE,
        null=True,
    )
    passed = models.BooleanField(
        default=False,
    )
    passed_at = models.DateTimeField(
        blank=True,
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    auto_slug_populate_from = "headword"

    @property
    def editable(self):
        return not self.passed and self.batch.editable

    def get_absolute_url(self):
        if self.passed:
            return reverse("dictionary.show", kwargs={"slug": self.slug})
        return reverse("word.show", kwargs={"batch": self.batch.pk, "word": self.pk})

    def __str__(self):
        return self.headword
