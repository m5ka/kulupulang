from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_slug, MinLengthValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    username = models.CharField(
        help_text=_('This is the unique identifier you will to log in. It may only contain letters and numbers.'),
        max_length=32,
        unique=True,
        db_index=True,
        validators=[validate_slug, MinLengthValidator(3)],
    )
    email = models.EmailField(
        verbose_name=_('Email address'),
        help_text=_(
            'This should be your email address. '
            'Make sure it\'s a valid email address and that you have access to it.'
        ),
        max_length=128,
        blank=True,
    )
    preferred_name = models.CharField(
        verbose_name=_('Display name'),
        help_text=_('This name will appear instead of your username on the site.'),
        max_length=64,
        blank=True,
    )

    @property
    def display_name(self):
        return self.preferred_name or self.username

    def get_absolute_url(self):
        return reverse('profile.show', kwargs={'profile': self.username})

    def __str__(self):
        return self.display_name
