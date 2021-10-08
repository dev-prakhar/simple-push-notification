from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=100)
    options = models.JSONField()
