# from .tasks import report_generator_function
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from .serializers import *
from .models import *
from django.db.models import Count, OuterRef

# Create your views here.

class MailingAPIView(APIView):

    def get(self, request):
        queryset = Mailing.objects.all()
        serializer = MailingSerializer(queryset, many=True)
        print(serializer.data)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):
        serializer = MailingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The new Mailing instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        id = request.data['id']

        instance = get_object_or_404(Mailing.objects.all(), pk=id)
        serializer = MailingSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The Mailing instance has been updated"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Mailing.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response({"message": f"The Mailing instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Mailing instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

class GeneralStatAPIView(APIView):
    def get(self, request):
        queryset = Mailing.objects.all().annotate(messages_sent=Count(Message.objects.filter(mailing_id=OuterRef("pk"), status='Sent').values('status')))\
                                        .annotate(messages_not_sent=Count(Message.objects.filter(mailing_id=OuterRef("pk"), status='Not sent').values('status')))\
                                        .order_by('-messages_sent')

        serializer = GeneralStatSerializer(queryset, many=True)
        print(serializer.data)
        return Response(serializer.data, status=200)

class DetailStatAPIView(APIView):
    def get(self, request):
        mailing_instance = None
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            print(request.query_params['id'])
            mailing_instance = Mailing.objects.get(pk=request.query_params['id'])
        except:
            return Response({'error': 'Mailing instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)

        messages_queryset = Message.objects.filter(mailing=mailing_instance)

        response_data = {
            'mailing': DetailStatSerializer(mailing_instance).data,
            'messages': MessageSerializer(messages_queryset, many=True).data
        }

        return Response(response_data, status=200)

class ClientAPIView(APIView):
    def get(self, request):
        queryset = Client.objects.all()
        serializer = ClientSerializer(queryset, many=True)

        return Response(
            serializer.data,
            status=200,
        )

    def post(self, request):
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The new Client instance has been created"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def put(self, request):
        id = request.data['id']

        instance = get_object_or_404(Client.objects.all(), pk=id)
        serializer = ClientSerializer(instance, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response({"message": "The Client instance has been updated"}, status=status.HTTP_200_OK)
        else:
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request):
        if 'id' not in request.query_params:
            return Response({'error': '<id> url parameter is required'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            instance = Client.objects.get(pk=request.query_params['id'])
            instance.delete()
            return Response({"message": f"The Client instance with id {request.query_params['id']} has been deleted"},
                            status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response({'error': 'Client instance with that id does not exist'},
                            status=status.HTTP_400_BAD_REQUEST)