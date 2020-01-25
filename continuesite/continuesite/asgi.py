"""
ASGI config for continuesite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

"""
    TODO: Update default settings module
    @author: aayush
    @date: 25/01/20
    @time: 5:11 PM
"""
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'continuesite.settings')

application = get_asgi_application()
