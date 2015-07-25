"""Production settings and globals."""

from __future__ import absolute_import

from os import environ

from .base import *


########## HOST CONFIGURATION
# See: https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['.gogamereview.com']
########## END HOST CONFIGURATION

# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-use-tls
EMAIL_USE_TLS = True

# ########## DATABASE CONFIGURATION
# DATABASES = {}
# ########## END DATABASE CONFIGURATION


# ########## CACHE CONFIGURATION
# # See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
# CACHES = {}
# ########## END CACHE CONFIGURATION


########## SECRET CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
SECRET_KEY = get_env_variable('SECRET_KEY')
########## END SECRET CONFIGURATION

INSTALLED_APPS += ('storages',)

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_QUERYSTRING_AUTH = False  # For now lets not do this
AWS_ACCESS_KEY_ID = get_env_variable('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = get_env_variable('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = 'go-game-review'
AWS_PRELOAD_METADATA = True  # necessary to fix manage.py collectstatic command to only upload changed files instead of all files
STATIC_URL = ('https://s3.amazonaws.com/%s/' % AWS_STORAGE_BUCKET_NAME) # TODO: annoyingly collectstatic fails on EU buckets, only US standard works. Solution?!
ADMIN_MEDIA_PREFIX = ('https://s3.amazonaws.com/%s/admin' % AWS_STORAGE_BUCKET_NAME)

MIDDLEWARE_CLASSES += ('project.middleware.PrependWWW', )