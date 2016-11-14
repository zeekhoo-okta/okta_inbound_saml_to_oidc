"""
WSGI config for okta_inbound_saml_to_oidc project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "okta_inbound_saml_to_oidc.settings")

application = get_wsgi_application()
