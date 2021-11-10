from rest_framework import serializers

from apps.notification_app.models import PushNotificationRequest, Notification


class PushNotificationRequestSerializer(serializers.ModelSerializer):
    notification_id = serializers.IntegerField(required=True)

    class Meta:
        model = PushNotificationRequest
        fields = ['id', 'status', 'notification_id']

    def validate_status(self, value):
        if value != "":
            raise serializers.ValidationError("status should not be given as input")
        return value

    def validate_notification_id(self, value):
        if value not in Notification.objects.all().values_list('pk', flat=True):
            raise serializers.ValidationError("invalid notification ID")
        return value
