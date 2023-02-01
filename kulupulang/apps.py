from django.apps import AppConfig


class KulupulangConfig(AppConfig):
    name = "kulupulang"
    verbose_name = "kulupu lang"

    def ready(self):
        from . import signals
