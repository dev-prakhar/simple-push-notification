from rest_framework import serializers

from ..models.push_notification_request import PushNotificationRequest


class PushNotificationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushNotificationRequest
        fields = ['id', 'status', 'notification_id']
        