#################
# BASE SETTINGS #
#################

import os

import dj_database_url

######################
# PATH CONFIGURATION #
######################

# Absolute filesystem path to the Django project directory
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Absolute filesystem path to the top-level project folder
SITE_DIR = os.path.dirname(BASE_DIR)


#######################
# DEBUG CONFIGURATION #
#######################

# https://docs.djangoproject.com/en/1.6/ref/settings/#debug
DEBUG = False

# https://docs.djangoproject.com/en/1.6/ref/settings/#template-debug
TEMPLATE_DEBUG = DEBUG


############################
# SECRET KEY CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.6/ref/settings/#secret-key
# This key should only be used for development and testing!
SECRET_KEY = 'this_is_my_development_key'


#####################
# APP CONFIGURATION #
#####################

# https://docs.djangoproject.com/en/1.6/ref/settings/#installed-apps
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # helper apps
    'south',

    # installed apps
    'boundaries',
    'debt_context',
)


############################
# MIDDLEWARE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.6/ref/settings/#middleware-classes
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)


##########################
# DATABASE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
DATABASES = {
    'default': dj_database_url.config(default='postgis://localhost/local_debt')
}


#####################
# URL CONFIGURATION #
#####################

ROOT_URLCONF = 'local_debt.urls'


######################
# WSGI CONFIGURATION #
######################

WSGI_APPLICATION = 'local_debt.wsgi.application'


#########################
# GENERAL CONFIGURATION #
#########################

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#language-code
LANGUAGE_CODE = 'en-us'

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#time-zone
TIME_ZONE = 'America/Chicago'

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#site-id
SITE_ID = 1

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#use-i18n
USE_I18N = True

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#use-l10n
USE_L10N = True

# See: https://docs.djangoproject.com/en/1.6/ref/settings/#use-tz
USE_TZ = True


##########################
# TEMPLATE CONFIGURATION #
##########################

# https://docs.djangoproject.com/en/1.6/ref/settings/#template-dirs
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
)

#############################
# STATIC FILE CONFIGURATION #
#############################

# https://docs.djangoproject.com/en/1.6/ref/settings/#static-root
STATIC_ROOT = os.path.join(BASE_DIR, 'assets')

# https://docs.djangoproject.com/en/1.6/ref/settings/#static-url
STATIC_URL = '/static/'

# https://docs.djangoproject.com/en/1.6/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


############################
# MEDIA FILE CONFIGURATION #
############################

# https://docs.djangoproject.com/en/1.6/ref/settings/#media-root
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# https://docs.djangoproject.com/en/1.6/ref/settings/#media-url
MEDIA_URL = '/media/'


############################
# WHITENOISE CONFIGURATION #
############################

# http://whitenoise.evans.io/en/latest/django.html#add-gzip-and-caching-support
# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
