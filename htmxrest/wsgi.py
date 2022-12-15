"""
WSGI config for htmxrest project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import sys, os, logging

sys.path.append(os.path.join(sys.path[0], 'env', 'lib', 'python3.10', 'site-packages'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'htmxrest.settings')

application = get_wsgi_application()
