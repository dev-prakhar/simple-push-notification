from rest_framework import serializers

from apps.notification_app.models import PushNotificationRequest, Notification


class PushNotificationRequestSerializer(serializers.ModelSerializer):
    notification_id = serializers.IntegerField(required=True)

    class Meta:
        model = PushNotificationRequest
        fields = ['id', 'notification_id', 'status']
        read_only_fields = ['status']

    def validate_notification_id(self, value):
        if not Notification.objects.filter(id=value).exists():
            raise serializers.ValidationError("invalid notification ID")
        return value
