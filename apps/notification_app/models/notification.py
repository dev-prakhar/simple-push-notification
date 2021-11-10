from django.db import models


class Notification(models.Model):
    title = models.CharField(max_length=128)
    options = models.JSONField(default=dict)

    def __str__(self):
        return str(self.id)
