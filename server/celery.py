from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'server.settings')

app = Celery('server', broker='redis://redis:6379/0',
             backend='redis://redis:6379/0',
             include=['image_processing.tasks'])
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()
