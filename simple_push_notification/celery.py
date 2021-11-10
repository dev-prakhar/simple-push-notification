import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'simple_push_notification.settings')

# Creating the app instance here
app = Celery('simple_push_notification')

# Celery configures itself from Django settings module
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()