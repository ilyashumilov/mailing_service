from celery import shared_task
from django.utils.html import strip_tags
from django.template import loader
from django.core.mail import send_mail
import requests

@shared_task(bind=True,
             name='email_sender',
             max_retries=3,
             soft_time_limit=20)
def email_sender():
    data = requests.get('http://localhost:8000/api/v1/general_stat').text
    print(data)
    try:
        send_mail(
        'Test',
        data,
        'noreply@example.com',
        ['shumilov00001@gmail.com'],
        fail_silently=False
    )
    except:
        pass

