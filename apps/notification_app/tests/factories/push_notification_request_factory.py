import factory

from .notification_factory import NotificationFactory
from ...models import PushNotificationRequest


class PushSubscriptionRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PushNotificationRequest

    notification_id = factory.SubFactory(NotificationFactory)

        