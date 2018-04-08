"""
WSGI config for locallibrary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sys
from django.core.wsgi import get_wsgi_application

sys.path.append('/Users/floshin33/DjangoProject/locallibrary')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "locallibrary.settings")

application = get_wsgi_application()
