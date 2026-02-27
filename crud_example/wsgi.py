"""
WSGI config for crud_example project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_example.settings')
# Run migrations automatically (dangerous on each start!)
call_command('migrate', interactive=False)

application = get_wsgi_application()
