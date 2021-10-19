from django.db import models


status_choices = (
    ("1", "Active"),
    ("2", "Expired"),
    ("3", "Unsubscribed"),
)


class PushSubscription(models.Model):
    endpoint = models.URLField(max_length=200)
    key = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=status_choices)
