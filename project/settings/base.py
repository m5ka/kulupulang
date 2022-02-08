"""
These are the base settings for kulupulang - they should not be used directly.
To set up your project settings, you should copy local.example.py to local.py and edit those values.
"""
import os


# Base directory
# This points to the project root (i.e the folder containing conlangdev/ and project/)
# In any derived files (e.g local.py) you can use this as follows:
# os.path.join(BASE_DIR, 'conlangdev', 'example')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# Application definition

WSGI_APPLICATION = 'project.wsgi.application'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_jinja',
    'django_crontab',
    'kulupulang',
]


# Middleware

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# URLs

ROOT_URLCONF = 'project.urls'


# Authentication
# https://docs.djangoproject.com/en/3.2/topics/auth/customizing/#auth-custom-user

AUTH_USER_MODEL = 'kulupulang.User'
LOGIN_URL = 'login'


# Templates

TEMPLATES = [
    {
        'BACKEND': 'django_jinja.backend.Jinja2',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'filters': {
                'naturaltime': 'django.contrib.humanize.templatetags.humanize.naturaltime',
            },
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'policies': {
                'ext.i18n.trimmed': True,
            },
        },
    },
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# Cron jobs
# https://pypi.org/project/django-crontab/#description

CRONJOBS = [
    ('*/15 * * * *', 'kulupulang.cron.promote_oven_to_dictionary_task'),
]


# User themes
# Make sure one of them is default!
KULUPULANG_USER_THEMES = (
    ('default', 'minimal theme (default)'),
    ('digital', 'digital theme'),
    ('mint', 'mint theme'),
)
