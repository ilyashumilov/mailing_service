from django.core.management import BaseCommand
from app.tasks import email_sender

class Command(BaseCommand):
    def handle(self, *args, **options):
        # email_sender.s().apply_async(countdown=row['delay'])
        email_sender()
