#!/work/sites/helpdesk/env/bin/python2
# -*- coding:utf-8 -*-
activate_this = '/work/sites/helpdesk/env/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

import os
import sys

sys.path.insert( 0, '/work/sites/helpdesk/env/lib/site-packages/django')
sys.path.insert( 0, '/work/sites/helpdesk/project')

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

# This application object is used by any WSGI server configured to use this
# file. This includes Django's development server, if the WSGI_APPLICATION
# setting points here.
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Apply WSGI middleware here.
# from helloworld.wsgi import HelloWorldApplication
# application = HelloWorldApplication(application)
