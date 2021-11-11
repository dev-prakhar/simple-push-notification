from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notification_app.models import PushNotificationRequest
from apps.notification_app.serializers import PushNotificationRequestSerializer


class PushNotificationRequestView(APIView):
    def get(self, request, request_id, **kwargs):
        request_object = PushNotificationRequest.objects.filter(id=request_id).first()
        if request_object:
            serializer = PushNotificationRequestSerializer(request_object)
            return Response(serializer.data)
        else:
            return Response("Invalid ID")
