from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'main.settings')
app = Celery("main1")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

app.conf.update(result_expires=3600,
                enable_utc=True,
                timezone='Europe/Moscow', )

app.conf.beat_schedule = {
    "every minute": {
        "task": "email_sender",
        'schedule': crontab(minute=0, hour=18),
    }
}

app.autodiscover_tasks()