from apps.notification_app.models.push_subscription import PushSubscription
from rest_framework import serializers


class PushSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PushSubscription
        fields = ['endpoint', 'key', 'auth', 'status']
