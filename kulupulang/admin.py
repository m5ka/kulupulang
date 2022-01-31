from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import models


for model in [getattr(models, m) for m in models.__all__]:
    if model.__name__ != 'User':
        admin.site.register(model)

admin.site.register(models.User, UserAdmin)
