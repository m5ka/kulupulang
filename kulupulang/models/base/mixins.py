from django.db import models
from slugify import slugify


class AutoSlugMixin:
    auto_slug_field = 'slug'
    auto_slug_populate_from = 'name'

    def hydrate_slug(self):
        existing = getattr(self, self.auto_slug_field)
        if existing:
            return

        source = getattr(self, self.auto_slug_populate_from)
        if source:
            setattr(self, self.auto_slug_field, slugify(source))
