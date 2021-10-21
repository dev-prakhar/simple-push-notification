from django.utils.translation import gettext_lazy as _
from django.db import models


class PushSubscriptionStatus(models.TextChoices):
    ACTIVE = 'active', _('Active')
    EXPIRED = 'expired', _('Expired')
    UNSUBSCRIBED = 'unsubscribed', _('Unsubscribed')
