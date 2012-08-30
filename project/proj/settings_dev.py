# -*- coding:utf-8 -*-
from settings import HOST_NAME
from settings import INSTALLED_APPS, MIDDLEWARE_CLASSES

__author__ = 'michael'


HOSTER = False
HOME = False

HOME_HOST_NAME = 'ubuntu'

if HOST_NAME == HOME_HOST_NAME:
    HOME = True

if HOME:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
            'NAME': 'helpdesk_dev2',                      # Or path to database file if using sqlite3.
            'USER': 'postgres',                      # Not used with sqlite3.
            'PASSWORD': '0',                  # Not used with sqlite3.
            'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
            'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        }
    }
else:
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


INSTALLED_APPS += ('debug_toolbar',)
MIDDLEWARE_CLASSES += ('debug_toolbar.middleware.DebugToolbarMiddleware',)
INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS' : False,
    }