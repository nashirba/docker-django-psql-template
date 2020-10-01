'''
Base settings.py, import it to create new settings
'''

import environ
import structlog

from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent.parent

# ENV init
# -----------------------------------------------------------------------------
env = environ.Env()
env.read_env(str(BASE_DIR / '.env'))


# GENERAL
# -----------------------------------------------------------------------------
SECRET_KEY = env.str('DJANGO_SECRET_KEY')
DEBUG = env.bool('DJANGO_DEBUG', False)
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
LOCALE_PATHS = [str(BASE_DIR / 'locale')]

# INTERNATIONALIZATION
# -----------------------------------------------------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Almaty'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# HOSTS
# -----------------------------------------------------------------------------
ALLOWED_HOSTS = []


# APPLICATIONS
# -----------------------------------------------------------------------------
DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = []

LOCAL_APPS = []

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# MIDDLEWARE
# -----------------------------------------------------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# TEMPLATES
# -----------------------------------------------------------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [str(BASE_DIR / 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    }
]

# STATIC
# ------------------------------------------------------------------------------
STATIC_ROOT = str(BASE_DIR / 'staticfiles')
STATIC_URL = '/static/'
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
]

# MEDIA
# -----------------------------------------------------------------------------
MEDIA_ROOT = str(BASE_DIR / 'media')
MEDIA_URL = '/media/'


# Database
# -----------------------------------------------------------------------------
DATABASES = {
    'default': env.db('DATABASE_URL')
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # NOQA
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', # NOQA
    },
]


# LOGGING
# -----------------------------------------------------------------------------
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'json_formatter': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.JSONRenderer(),
        },
        'plain_console': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.dev.ConsoleRenderer(),
        },
        'key_value': {
            '()': structlog.stdlib.ProcessorFormatter,
            'processor': structlog.processors.KeyValueRenderer(
                key_order=['timestamp', 'level', 'event', 'logger']
            ),
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'plain_console',
        },
        'json_stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'json_formatter',
        },
        'flat_line_stream': {
            'class': 'logging.StreamHandler',
            'formatter': 'key_value',
        },
    },
    'loggers': {
        'django_structlog': {
            'handlers': ['json_stream'],
            'level': 'INFO',
        },
        'debugger': {
            'handlers': ['flat_line_stream'],
            'level': 'DEBUG',
        },
        'gunicorn.error': {
            'level': 'INFO',
            'handlers': ['json_stream'],
            'propagate': True,
        },
        'gunicorn.access': {
            'level': 'INFO',
            'handlers': ['json_stream'],
            'propagate': False,
        },
    },
}
