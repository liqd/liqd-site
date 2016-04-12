"""
Django settings for liquidsite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
import os
from os.path import abspath, dirname, join
from django.utils.translation import ugettext_lazy as _

# Absolute filesystem path to the Django project directory:
BASE_DIR = os.path.dirname(dirname(dirname(abspath(__file__))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '49q9cm=n7lbzn7$rr(oekk=s7ymk49t+40-791ywdaxb8u#dzj'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://example.com'


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'wagtail.contrib.settings',
    'django_bleach',

    'compressor',
    'taggit',
    'modelcluster',
    'djangobower',

    'wagtail.wagtailcore',
    'wagtail.wagtailadmin',
    'wagtail.wagtaildocs',
    'wagtail.wagtailsnippets',
    'wagtail.wagtailusers',
    'wagtail.wagtailsites',
    'wagtail.wagtailimages',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsearch',
    'wagtail.wagtailredirects',
    'wagtail.wagtailforms',
    'wagtail.contrib.wagtailstyleguide',

    'core',
    'blog',
    'persons',
    'projects',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'django.middleware.locale.LocaleMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware',
)

ROOT_URLCONF = 'liquidsite.urls'
WSGI_APPLICATION = 'liquidsite.wsgi.application'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'locale')
]

LANGUAGE_CODE = 'en'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LANGUAGES = (
    ('de', _('German')),
    ('en', _('English')),
)
# MODELTRANSLATION_LANGUAGES = ('de', 'en')

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_ROOT = join(BASE_DIR, 'static')
STATIC_URL = '/static/'

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

MEDIA_ROOT = join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

COMPRESS_PRECOMPILERS = (
    # ('text/x-scss', 'contrib.sass.sass.SassMapFilter'),
    ('text/x-scss', 'django_libsass.SassCompiler'),
)
LIBSASS_SOURCEMAPS = True

# Template configuration

from django.conf import global_settings

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    'django.core.context_processors.request',
    'wagtail.contrib.settings.context_processors.settings',
)

BOWER_COMPONENTS_ROOT = os.path.join(BASE_DIR, 'core', 'static', 'third-party')
BOWER_INSTALLED_APPS = (
    'jquery',
    'fontawesome',
    'slick-carousel',
    'jquery-smartresize',
    'bootstrap-sass',
)
BOWER_PATH = os.path.join(BASE_DIR, 'node_modules', '.bin', 'bower')

BLEACH_ALLOWED_TAGS = []
BLEACH_ALLOWED_ATTRIBUTES = []
BLEACH_STRIP_TAGS = True


# Wagtail settings

LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

WAGTAIL_SITE_NAME = "liquidsite"

# Use Elasticsearch as the search backend for extra performance and better search results:
# http://wagtail.readthedocs.org/en/latest/howto/performance.html#search
# http://wagtail.readthedocs.org/en/latest/core_components/search/backends.html#elasticsearch-backend
#
# WAGTAILSEARCH_BACKENDS = {
#     'default': {
#         'BACKEND': 'wagtail.wagtailsearch.backends.elasticsearch.ElasticSearch',
#         'INDEX': 'liquidsite',
#     },
# }


# Whether to use face/feature detection to improve image cropping -
# requires OpenCV
WAGTAILIMAGES_FEATURE_DETECTION_ENABLED = False
