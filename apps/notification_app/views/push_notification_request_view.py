from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notification_app.models import PushNotificationRequest
from apps.notification_app.serializers import PushNotificationRequestSerializer


class PushNotificationRequestView(APIView):
    def get(self, request, request_id, **kwargs):
        request_object = get_object_or_404(PushNotificationRequest, id=request_id)
        return Response(PushNotificationRequestSerializer(request_object).data)
