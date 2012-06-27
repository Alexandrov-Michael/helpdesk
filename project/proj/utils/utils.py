# -*- coding:utf-8 -*-
from os.path import join, dirname, abspath, pardir
from django.http import HttpResponse

def site_path( path = False, parent = False ):
    thisDir   = abspath( join(dirname(abspath(__file__)), pardir))
    parent = abspath( join   ( thisDir , pardir ) )
    parentDir = abspath( join   ( parent , pardir ) )
    if not path:
        return thisDir
    if parent:
        return join( parentDir, path )
    else:
        return join( thisDir  , path )
        
        
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'django.core.context_processors.request',
    'proj.utils.context_processors.username',
    )
