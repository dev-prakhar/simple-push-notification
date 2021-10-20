from django.db import models
from apps.notification_app.constants import PushSubscriptionStatus


class PushSubscription(models.Model):
    endpoint = models.URLField(max_length=256)
    key = models.CharField(max_length=128)
    auth = models.CharField(max_length=128)
    status = models.CharField(max_length=32, choices=PushSubscriptionStatus.choices, default=PushSubscriptionStatus.ACTIVE)
