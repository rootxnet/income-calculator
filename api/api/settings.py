"""
Django settings for api project.

Generated by 'django-admin startproject' using Django 3.1.4.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
from environ import environ

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
env = environ.Env(
    ALLOWED_HOSTS=(list, []),
    DEBUG=(bool, False),
    SENTRY_DSN=(str, None),
    SENTRY_PII=(bool, False),
    ELASTIC_APM=(bool, False),
    DEBUG_TOOLBAR_ENABLED=(bool, False),
    CORS_ALLOW_ALL_ORIGINS=(bool, False),
    CORS_ALLOWED_ORIGINS=(list, []),
    EMAIL_USE_SSL=(bool, False),
    EMAIL_USE_TLS=(bool, False),
    USE_X_FORWARDED_HOST=(bool, False),
)

# SECURITY WARNING: don't run with debug turned on in production!
ALLOWED_HOSTS = env('ALLOWED_HOSTS')
DEBUG = env('DEBUG')

CORS_ALLOW_ALL_ORIGINS = env("CORS_ALLOW_ALL_ORIGINS")
CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS")

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'admins',
    'api_keys'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 10
}

ROOT_URLCONF = 'api.urls'

TEMPLATES = [
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

WSGI_APPLICATION = 'api.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': env.db(),
}

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'admins.AdminUser'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
PROJECT_ROOT = os.path.join(os.path.abspath(__file__))
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Add configuration for static files storage using whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

EMAIL_HOST = env('EMAIL_SERVER')
EMAIL_HOST_USER = env('EMAIL_USERNAME')
EMAIL_HOST_PASSWORD = env('EMAIL_PASSWORD')
EMAIL_PORT = env('EMAIL_PORT')
EMAIL_USE_SSL = env('EMAIL_USE_SSL')
EMAIL_USE_TLS = env('EMAIL_USE_TLS')
EMAIL_SENDER = env('EMAIL_SENDER')
EMAIL_SENDER_NAME = env('EMAIL_SENDER_NAME')

FRONTEND_URL = env('FRONTEND_URL')
BASE_URL = env('BASE_URL')

USE_X_FORWARDED_HOST = env("USE_X_FORWARDED_HOST")
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

if env('SENTRY_DSN'):
    import sentry_sdk
    from sentry_sdk.integrations.django import DjangoIntegration

    sentry_sdk.init(
        dsn=env('SENTRY_DSN'),
        integrations=[DjangoIntegration()],
        # If you wish to associate users to errors (assuming you are using
        # django.contrib.auth) you may enable sending PII data
        send_default_pii=env('SENTRY_PII'),
    )

DEBUG_TOOLBAR_ENABLED = env("DEBUG_TOOLBAR_ENABLED")
if DEBUG_TOOLBAR_ENABLED:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = [
        '127.0.0.1',
    ]
