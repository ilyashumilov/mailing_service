import os
from datetime import datetime
from django.db.models import Count
from .models import *
import requests

KEY = os.getenv('KEY',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDAwMzUyNzEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImlseWFzaHVtaWxvdiJ9.n3iOSk33Ma017oW73A81MXrNALKKZoyCFXUOFmNfEUU')

def message_sender(mailing):
    target_audience = None
    if 'phone_number' in mailing.client_property:
        target_audience = Client.objects.filter(phone_number=mailing.client_property['phone_number'])
    if 'operator_code' in mailing.client_property:
        target_audience = Client.objects.filter(operator_code=mailing.client_property['operator_code'])
    if 'tag' in mailing.client_property:
        target_audience = Client.objects.filter(tag=mailing.client_property['tag'])
    if 'code' in mailing.client_property:
        target_audience = Client.objects.filter(tag=mailing.client_property['code'])

    for target_client in target_audience:
        new_message = Message(datetime.now(), mailing, target_client, 'Not sent')
        new_message.save()

        endpoint = "https://probe.fbrq.cloud/v1/send/%s" % str(new_message.id)
        data = {
            "id": 0,
            "phone": target_client.phone_number,
            "text": mailing.text
        }
        headers = {"Authorization": "Bearer %s" % KEY}
        response = requests.post(endpoint, data=data, headers=headers)

        if response.status_code == 200:
            new_message.status = 'Sent'
            new_message.save()

        if mailing.end >= datetime.now():
            break
