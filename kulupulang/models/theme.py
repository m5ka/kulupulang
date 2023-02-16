from os import path

from django.conf import settings
from django.db import models


class Theme(models.Model):
    name = models.CharField(
        max_length=255,
        unique=True,
    )
    description = models.TextField(
        blank=True,
        null=True,
    )
    css = models.CharField(
        max_length=255,
    )
    external_css = models.TextField(
        blank=True,
        null=True,
    )
    external_js = models.TextField(
        blank=True,
        null=True,
    )

    @property
    def css_path(self):
        return path.join(settings.STATIC_URL, "css", self.css)

    def get_external_css(self):
        if not self.external_css:
            return []
        return self.external_css.split("|")

    def get_external_js(self):
        if not self.external_js:
            return []
        return self.external_js.split("|")

    def __str__(self):
        return self.name
