from django.db import models

from . import Notification
from ..constants import PushNotificationRequestStatus


class PushNotificationRequest(models.Model):
    status = models.CharField(max_length=32, choices=PushNotificationRequestStatus.choices,
                              default=PushNotificationRequestStatus.IN_PROGRESS)
    notification = models.ForeignKey(Notification, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f'{str(self.id)} {self.status} {self.notification}'
