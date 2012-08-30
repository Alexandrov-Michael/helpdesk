# -*- coding:utf-8 -*-
__author__ = 'michael'
import os


HOSTER = True


PROJECT_PATH = os.path.dirname(__file__)
BETA_PATH = '/home/f/fregatscom/helpBeta/project/proj/'

if PROJECT_PATH == BETA_PATH:
    BETA = True
else:
    BETA = False


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