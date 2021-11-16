from django.utils.translation import gettext_lazy as _
from django.db import models


class PushSubscriptionStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    EXPIRED = 'expired', _('Expired')
    UNSUBSCRIBED = 'unsubscribed', _('Unsubscribed')


class PushNotificationRequestStatus(models.TextChoices):
    IN_PROGRESS = 'in_progress', _('In Progress')
    SUCCESSFUL = 'successful', _('Successful')
    FAILED = 'failed', _('Failed')
