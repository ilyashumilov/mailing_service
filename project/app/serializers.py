from rest_framework import serializers
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .models import *
import pytz

class MailingSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    text = serializers.CharField()
    client_property = serializers.JSONField()
    end = serializers.DateTimeField()
    current_status = serializers.CharField()

    def create(self, data):
      return Mailing.objects.create(**data)

    def update(self, instance, validated_data):
        instance.start = validated_data["start"]
        instance.text = validated_data["text"]
        instance.client_property = validated_data["client_property"]
        instance.end = validated_data["end"]

        instance.current_status = validated_data["current_status"]
        instance.save()
        return instance


class ClientSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    phone_number = serializers.CharField(max_length=50)
    operator_code = serializers.CharField(max_length=50)
    tag = serializers.CharField(max_length=50)
    timezone = serializers.CharField(max_length=50)

    def create(self, data):
        return Client.objects.create(**data)

    def update(self, instance, validated_data):
        instance.phone_number = validated_data["phone_number"]
        instance.operator_code = validated_data["operator_code"]
        instance.tag = validated_data["tag"]
        instance.timezone = validated_data["timezone"]
        instance.save()
        return instance

class ClientSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    phone_number = serializers.CharField(max_length=50)
    operator_code = serializers.CharField(max_length=50)
    tag = serializers.CharField(max_length=50)
    timezone = serializers.CharField(max_length=50)

    def create(self, data):
        return Client.objects.create(**data)

    def update(self, instance, validated_data):
        instance.phone_number = validated_data["phone_number"]
        instance.operator_code = validated_data["operator_code"]
        instance.tag = validated_data["tag"]
        instance.timezone = validated_data["timezone"]
        instance.save()
        return instance

class GeneralStatSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    text = serializers.CharField()
    client_property = serializers.JSONField()
    end = serializers.DateTimeField()
    messages_sent = serializers.CharField()
    messages_not_sent = serializers.CharField()

class DetailStatSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    start = serializers.DateTimeField()
    text = serializers.CharField()
    client_property = serializers.JSONField()
    end = serializers.DateTimeField()

class MessageSerializer(serializers.Serializer):
    sent = serializers.DateTimeField()
    status = serializers.CharField(max_length=50)

