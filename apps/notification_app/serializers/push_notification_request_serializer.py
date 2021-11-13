from rest_framework import serializers

from apps.notification_app.models import PushNotificationRequest, Notification


class PushNotificationRequestSerializer(serializers.ModelSerializer):
    notification_id = serializers.IntegerField(required=True)

    class Meta:
        model = PushNotificationRequest
        fields = ['id', 'notification_id']

    def validate_notification_id(self, value):
        if not Notification.objects.filter(id=value).first():
            raise serializers.ValidationError("invalid notification ID")
        return value
