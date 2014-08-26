#######################
# PRODUCTION SETTINGS #
#######################

from os import environ

from django.core.exceptions import ImproperlyConfigured

from .base import *


def get_env_setting(setting):
    """ Get the environment setting or return exception """
    try:
        return environ[setting]
    except KeyError:
        error_msg = "Set the %s env variable" % setting
        raise ImproperlyConfigured(error_msg)


######################
# HOST CONFIGURATION #
######################

# https://docs.djangoproject.com/en/1.6/ref/settings/#allowed-hosts
# https://docs.djangoproject.com/en/1.5/releases/1.5/#allowed-hosts-required-in-production
ALLOWED_HOSTS = ['*']


##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
# DATABASES = {}


#######################
# CACHE CONFIGURATION #
#######################

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'local_debt_cache',
    }
}


############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.6/ref/settings/#secret-key
SECRET_KEY = get_env_setting('SECRET_KEY')


################################
# DJANGO STORAGE CONFIGURATION #
################################

# http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
