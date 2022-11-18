from app.models import Mailing, Message, Client
from django.utils import timezone
import threading
import requests
import os
import pytz

from django.core.management import BaseCommand
import time

KEY = os.getenv('KEY',
                'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MDAwMzUyNzEsImlzcyI6ImZhYnJpcXVlIiwibmFtZSI6ImlseWFzaHVtaWxvdiJ9.n3iOSk33Ma017oW73A81MXrNALKKZoyCFXUOFmNfEUU')

def message_sender(mailing):
    target_audience = None
    print(mailing.client_property)
    if 'phone_number' in mailing.client_property:
        target_audience = Client.objects.filter(phone_number=mailing.client_property['phone_number'])
    if 'operator_code' in mailing.client_property:
        target_audience = Client.objects.filter(operator_code=mailing.client_property['operator_code'])
    if 'tag' in mailing.client_property:
        target_audience = Client.objects.filter(tag=mailing.client_property['tag'])
    if not target_audience:
        return

    print(target_audience)
    if target_audience.count() == 0:
        return

    for target_client in target_audience:
        new_message = Message(sent=timezone.now(), mailing=mailing, client=target_client, status='Not sent')
        new_message.save()

        endpoint = "https://probe.fbrq.cloud/v1/send/1"#%s" % str(new_message.id)
        print(endpoint)
        data = {
            "id": 0,
            "phone": target_client.phone_number,
            "text": mailing.text
        }

        headers = {'Authorization': 'Bearer %s' % KEY}
        print(headers)
        import json
        print(data)
        print(json.dumps(data))
        try:
            response = requests.post(endpoint, json=json.dumps(data), headers=headers)
            print(response)
        except:
            print('eroor')
            pass

        if response.status_code == 200:
            new_message.status = 'Sent'
            new_message.save()

        if mailing.end >= timezone.now():
            print(mailing.id, 'stoppped')
            break
class Command(BaseCommand):
    def handle(self, *args, **options):
        while True:
            mailings = Mailing.objects.all()
            for mailing in mailings:
                now = timezone.now()

                if (now >= mailing.start) and (now <= mailing.end) \
                        and mailing.current_status == 'Pending':
                    sender_thread = threading.Thread(target=message_sender, args=(mailing,))
                    sender_thread.start()
                    mailing.current_status = 'Processed'
                    mailing.save()
                else:
                    print('nothing')
            time.sleep(5)