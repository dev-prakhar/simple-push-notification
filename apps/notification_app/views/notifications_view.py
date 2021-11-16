from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.notification_app.models import Notification
from apps.notification_app.serializers import NotificationSerializer


class NotificationsView(APIView):
    def get(self, request):
        notification_objects = Notification.objects.all()
        serializer = NotificationSerializer(notification_objects, many=True)
        return Response(serializer.data)
