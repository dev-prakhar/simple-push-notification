from django.db import models


class PushSubscription(models.Model):
    endpoint = models.URLField(max_length=200)
    key = models.CharField(max_length=100)
    auth = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
