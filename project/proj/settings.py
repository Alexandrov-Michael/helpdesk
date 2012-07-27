# -*- coding:utf-8 -*-
from proj.utils import utils
# Django settings for proj project.

HOSTER = False
BETA = False

if HOSTER:
    DEBUG = False
else:
    DEBUG = True

#DEBUG = True
TEMPLATE_DEBUG = DEBUG




ADMINS = (
     ('Alexandrov Michael', 'mikle_a@list.ru'),
)

MANAGERS = ADMINS

if not HOSTER:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'helpdesk_dev2',                      # Or path to database file if using sqlite3.
            'USER': 'postgres',                      # Not used with sqlite3.
            'PASSWORD': '0',                  # Not used with sqlite3.
            'HOST': '192.168.1.6',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
    if BETA:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'fregatscom_beta',                      # Or path to database file if using sqlite3.
                'USER': 'fregatscom_beta',                      # Not used with sqlite3.
                'PASSWORD': 'h5ret34op',                  # Not used with sqlite3.
                'HOST': 'pg.sweb.ru',                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
            }
        }
    else:
        DATABASES = {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
                'NAME': 'fregatscom_help',                      # Or path to database file if using sqlite3.
                'USER': 'fregatscom_help',                      # Not used with sqlite3.
                'PASSWORD': 'h5ret34op',                  # Not used with sqlite3.
                'HOST': 'pg.sweb.ru',                      # Set to empty string for localhost. Not used with sqlite3.
                'PORT': '5432',                      # Set to empty string for default. Not used with sqlite3.
            }
        }

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'Europe/Moscow'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'ru-RU'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = utils.site_path( u'public_html/media/', True )
#MEDIA_ROOT = '../../public_html/media/'



# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = utils.site_path( u'dj_static/', True )

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

fistStaticDir = utils.site_path( u'public_html/static/', True )
# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    fistStaticDir,
    )

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'a_*jq_rt=e-fo7^uaj-v7(nr7whknsn($lqpnv8xqk!6getc94'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'proj.utils.middlewares.HttpsRedirect',

    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'proj.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'proj.wsgi.application'

fistTemplateDir = utils.site_path( u'project/proj/templates' )
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    fistTemplateDir,
    )

INSTALLED_APPS = (
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
     'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
     'django.contrib.admindocs',

    #utils

    'django_extensions',

    #myapp

    'ques',
    'company',
    'profiles',
    'files',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

### My settings ###

TEMPLATE_CONTEXT_PROCESSORS = utils.TEMPLATE_CONTEXT_PROCESSORS


ANONYMOUS_USER_ID = -1


LOGIN_REDIRECT_URL = u'/'

ADMIN_MEDIA_PREFIX = '/static/admin/'

#значение которое прибавляется к стандартнму id для идентификатора вопроса
PLUS_SLUG_FIELD = 0


if not HOSTER:
    INSTALLED_APPS += ('debug_toolbar',)
    MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
    INTERNAL_IPS = ('127.0.0.1',)
    DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS' : False,
        }



EMAIL_HOST = 'smtp.spaceweb.ru'
EMAIL_PORT = 2525
EMAIL_HOST_USER = 'fregatsoft.com+help'
EMAIL_HOST_PASSWORD = 'ngt543edcvf'
EMAIL_USE_TLS = True

