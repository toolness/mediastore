"""
Django settings for mediastore project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
import dj_database_url

from .settings_utils import set_default_env, set_default_db, \
                            parse_secure_proxy_ssl_header

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
path = lambda *parts: os.path.join(BASE_DIR, *parts)

if os.path.basename(sys.argv[0]) == 'manage.py' or 'DEBUG' in os.environ:
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/
    set_default_env(
        SECRET_KEY='development mode',
        DEBUG='indeed',
        # TODO: Support any alternative port passed-in from the command-line.
        PORT='8000',
    )

if 'SECURE_PROXY_SSL_HEADER' in os.environ:
    SECURE_PROXY_SSL_HEADER = parse_secure_proxy_ssl_header(
        os.environ['SECURE_PROXY_SSL_HEADER']
    )

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = TEMPLATE_DEBUG = 'DEBUG' in os.environ
PORT = int(os.environ['PORT'])

set_default_db('sqlite:///%s' % path('db.sqlite3'))

if 'ALLOWED_HOSTS' in os.environ:
    ALLOWED_HOSTS = [os.environ['ALLOWED_HOSTS'].split(',')]

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'mediastore.urls'

WSGI_APPLICATION = 'mediastore.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config()
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = path('staticfiles')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'stream': sys.stdout
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR'
        }
    }
}
