"""
Django settings for CRM project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-c@z-3r0u+!sgxpyxhbh1hn$#96n33ojqmswo^&5)zis(+x!44j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'base',
    'accounts',
    'leads',
    'pagesallocation',
    'clearcache',
    'multi_company',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'CRM.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates'
        ],
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

WSGI_APPLICATION = 'CRM.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'plome',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        'PORT': '5432'
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Europe/Paris'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

if DEBUG :
    STATICFILES_DIRS = [ 'static/' ]
else:
    STATIC_ROOT = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


AUTH_USER_MODEL = 'accounts.CustomUserTypes'


MAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'kant.jatin55@gmail.com'
EMAIL_HOST_PASSWORD = 'blmcqarkyklglcwr' #past the key or password app here
EMAIL_PORT = 587
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'default from email'




# # settings.py
# from kombu import Queue 
# from datetime import datetime, timedelta

# # CELERY_BROKER_URL = 'redis://localhost:6379/5'
# # CELERY_RESULT_BACKEND = 'redis://localhost:6379/5'
# # CELERY_ACCEPT_CONTENT = ['json']
# # CELERY_TASK_SERIALIZER = 'json'
# # CELERY_RESULT_SERIALIZER = 'json'
# # CELERY_TIMEZONE = 'Europe/Paris'

# BROKER_URL = "redis://localhost:6379/0" 
# CELERY_RESULT_BACKEND = "redis://localhost:6379/0"
# CELERY_TASK_SERIALIZER = "json"
# CELERY_RESULT_SERIALIZER = "json"
# CELERY_DEFAULT_QUEUE = "CRM"
# CELERY_ACCEPT_CONTENT = ["json"]  # Add this line
# CELERY_TRACK_STARTED = True
# CELERY_QUEUES = (Queue("CRM", routing_key="task.#"),)
# CELERY_TIMEZONE = 'Europe/Paris'

# CELERY_BEAT_SCHEDULE = {
#     "send_appointment_reminder": {
#         "task": "send_appointment_reminder",
#         "schedule": timedelta(seconds=10),
#     },
# }

# LOGGING = {
#     "version": 1,
#     "disable_existing_loggers": False,
#     "formatters": {
#         "verbose": {
#             "format": "%(levelname)s %(asctime)s %(module)s %(lineno)d %(funcName)s %(message)s"
#         }
#     },
#     "filters": {
#         "require_debug_false": {"()": "django.utils.log.RequireDebugFalse"}
#     },
#     "handlers": {
#         "error_handler": {
#             "level": "DEBUG",
#             "class": "logging.FileHandler",
#             "filename": BASE_DIR / "logs/error.log",
#             "formatter": "verbose",
#         },
#         "base_handler": {
#             "level": "DEBUG",
#             "class": "logging.handlers.RotatingFileHandler",
#             "filename": BASE_DIR / "logs/request.log",
#             "maxBytes": 1024 * 1024 * 16,
#             "backupCount": 100,
#             "formatter": "verbose",
#         },
        
#     },
#     "loggers": {
#         "error_logger": {
#             "handlers": ["error_handler"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#         "request_logger": {
#             "handlers": ["base_handler"],
#             "level": "DEBUG",
#             "propagate": False,
#         },
#     },
# }