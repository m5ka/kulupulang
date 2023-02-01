"""
These are your local (default) settings.
Generate this file by copying it from local.example.py to local.py, then configure as you need.
If you want different settings for e.g testing, copy to another location and you can append
any management commands with e.g --settings=project.settings.test
You can use the base directory (the one containing the project/ and kulupulang/ directories) like so:
os.path.join(BASE_DIR, 'kulupulang', 'example')
"""
import os

from .base import *


# Environment
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-DEBUG

DEBUG = True


# Secret Key
# https://docs.djangoproject.com/en/3.2/ref/settings/#secret-key

SECRET_KEY = "insecure-little-cat-hTYWR0eTIzZzttIHlqY2I0IDQ1dA=="


# Allowed hosts
# https://docs.djangoproject.com/en/3.2/ref/settings/#allowed-hosts

ALLOWED_HOSTS = ["localhost"]


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "name",
        "USER": "user",
        "PASSWORD": "password",
        "HOST": "localhost",
        "PORT": "3306",
    }
}


# Cache
# https://docs.djangoproject.com/en/3.2/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
        "LOCATION": "127.0.0.1:11211",
    }
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "kulupulang", "static")


# Media root for uploaded files
# https://docs.djangoproject.com/en/3.2/ref/settings/#std:setting-MEDIA_ROOT

MEDIA_URL = "/media/"
MEDIA_ROOT = "/opt/kulupulang/media"


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-gb"
TIME_ZONE = "UTC"
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Public site URL

PUBLIC_URL = "http://localhost:8000/"

# Discord webhook

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/abc/xyz"
DISCORD_WEBHOOK_COLOR = "A0FB79"
