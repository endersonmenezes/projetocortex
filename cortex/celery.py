#  Copyright (c) 2020. Enderson Menezes Cândido [www.endersonmenezes.com.br]

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cortex.settings')

app = Celery('cortex')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
