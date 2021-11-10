import factory

from ...models import PushNotificationRequest


class PushSubscriptionRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = PushNotificationRequest
        