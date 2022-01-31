from django.db.models.signals import pre_save

from .models.base.mixins import AutoSlugMixin
from .utils import base_receiver


@base_receiver(pre_save, sender=AutoSlugMixin)
def add_auto_slug(sender, instance, **kwargs):
    instance.hydrate_slug()
