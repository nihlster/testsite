"""
WSGI config for testsite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os, sys

from django.core.wsgi import get_wsgi_application

sys.path.append('/home/alexhag87/testsite')
os.environ['DJANGO_SETTINGS_MODULE'] = 'testsite.settings'

application = get_wsgi_application()

activator = '/home/alexhag87/.virtualenvs/testsite/bin/activate_this.py'
with open(activator) as f:
    exec(f.read(), {'__file__': activator})
