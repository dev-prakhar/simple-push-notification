from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import PushNotificationRequestSerializer
from ..services.push_notification_request_service import PushNotificationRequestService


class PushNotificationRequestsView(APIView):
    def post(self, request, format=None):
        serializer = PushNotificationRequestSerializer(data=request.data)
        if serializer.is_valid():
            request_id = PushNotificationRequestService().request_to_send_notification(serializer.data)
            return Response(request_id, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
