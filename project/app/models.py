from django.db import models

class Mailing(models.Model):
    start = models.DateTimeField()
    text = models.TextField()
    client_property = models.JSONField()
    end = models.DateTimeField()
    current_status = models.CharField(max_length=50)


class Client(models.Model):
    phone_number = models.CharField(max_length=50)
    operator_code = models.CharField(max_length=50)
    tag = models.CharField(max_length=50)
    timezone = models.CharField(max_length=50)


class Message(models.Model):
    sent = models.DateTimeField()
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)

    def __str__(self):
        return self.status
