from rest_framework import serializers

from apps.notification_app.models import PushNotificationRequest


class PushNotificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotificationRequest
        fields = ['id', 'status', 'notification_id']
        