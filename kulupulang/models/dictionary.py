from datetime import timedelta

from django.db import models, transaction
from django.utils import timezone
from django.urls import reverse

from .base.abstracts import UpdatableModel
from .base.choices import PartOfSpeech, WordClass
from .base.mixins import AutoSlugMixin
from .user import User


class Batch(UpdatableModel):
    name = models.CharField(
        db_index=True,
        max_length=255,
        help_text='a nice little name for this batch you\'re cooking up. any name will do.',
    )
    description = models.TextField(
        blank=True,
        help_text='this is optional, but if you feel like giving a little description then hey that\'s totally cool',
    )
    submitted = models.BooleanField(
        default=False,
    )
    submitted_at = models.DateTimeField(
        null=True,
    )
    flagged = models.BooleanField(
        default=False,
    )
    passed = models.BooleanField(
        default=False,
    )
    passed_at = models.DateTimeField(
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )
    voting_from = models.DateTimeField(
        default=timezone.now,
    )
    voting_hours = models.IntegerField(
        default=48,
        help_text='how many hours should this stay in the oven before it\'s cooked and in the dictionary?',
    )

    def check_passed(self):
        voting_end = self.voting_from + timedelta(hours=self.voting_hours)
        return not (self.flagged or timezone.now() < voting_end)

    def get_absolute_url(self):
        return reverse('batch.show', kwargs={'batch': self.pk})

    @transaction.atomic
    def pass_batch(self):
        self.passed = True
        self.passed_at = timezone.now()
        self.save()

        Root.objects.filter(batch=self).update(passed=True, passed_at=timezone.now)
        Word.objects.filter(batch=self).update(passed=True, passed_at=timezone.now)

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
        self.resolved = True
        self.save()

        if not Discussion.objects.filter(batch=self.batch, resolved=False).exists():
            self.batch.flagged = False
            self.batch.voting_from = timezone.now()
            self.batch.save()


class Root(UpdatableModel, AutoSlugMixin):
    root = models.CharField(
        db_index=True,
        max_length=255,
        blank=False,
        help_text='this is the root itself. make sure it\'s valid as a root!',
    )
    slug = models.CharField(
        max_length=255,
        blank=True,
        null=False,
    )
    gloss = models.TextField(
        blank=False,
        help_text='what\'s the general meaning of this root?',
    )
    notes = models.TextField(
        blank=True,
        help_text='this is for any optional notes you may want to make about this root.',
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
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    auto_slug_populate_from = 'root'

    def __str__(self):
        return self.root


class Word(UpdatableModel, AutoSlugMixin):
    headword = models.CharField(
        db_index=True,
        max_length=255,
        blank=False,
        help_text='this is the word itself.',
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
    gloss = models.TextField(
        blank=False,
        help_text='what does this word mean?',
    )
    etymology = models.TextField(
        blank=True,
        help_text='optionally, where does this word come from?',
    )
    notes = models.TextField(
        blank=True,
        help_text='any other optional notes about this word',
    )
    roots = models.ManyToManyField(
        Root,
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
        null=True,
    )
    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
    )

    auto_slug_populate_from = 'headword'

    def __str__(self):
        return self.headword
