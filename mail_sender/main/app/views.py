from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# Webhook for receiving mail status change
class MailStatusAPIView(APIView):
    def post(self, request):
        # process status
        return Response(
            status=200,
        )