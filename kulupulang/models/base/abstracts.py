from django.apps import apps
from django.db import models
from django.utils.translation import gettext_lazy as _


class UpdatableModel(models.Model):
    updated_at = models.DateTimeField(
        auto_now=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        db_index=True
    )

    class Meta:
        abstract = True
