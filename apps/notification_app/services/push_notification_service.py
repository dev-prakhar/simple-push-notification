import json

from django.conf import settings
from pywebpush import WebPushException, webpush

from ..constants import PushNotificationRequestStatus
from ..models import PushNotificationRequest, PushSubscription


class PushNotificationService:
    def send_notification(self, push_notification_request_id):
        notification_dict = self.__get_notification_content(push_notification_request_id)

        for subscription in PushSubscription.objects.all():
            push_subscription_dict = self.__get_push_subscription(subscription)
            self.__send_notification_with_webpush(push_notification_request_id, push_subscription_dict,
                                                  notification_dict)

    def __get_push_subscription(self, push_subscription_object):
        push_subscription_dict = {
            "endpoint": push_subscription_object.endpoint,
            "keys": {
                "p256dh": push_subscription_object.key,
                "auth": push_subscription_object.auth
            }
        }
        return push_subscription_dict

    def __get_notification_content(self, push_notification_request_id):
        notification_content = PushNotificationRequest.objects.select_related('notification').get(
            id=push_notification_request_id).notification
        notification_dict = {
            "title": notification_content.title,
            "options": notification_content.options
        }
        return notification_dict

    def __send_notification_with_webpush(self, push_notification_request_id, push_subscription, notification_content):
        push_notification_request_object = PushNotificationRequest.objects.get(id=push_notification_request_id)
        try:
            webpush(
                push_subscription,
                json.dumps(notification_content),
                vapid_private_key=settings.VAPID_PRIVATE_KEY,
                vapid_claims={"sub": "mailto: x@gmail.com"}
            )
        except WebPushException as ex:
            print("error = ", ex)
            push_notification_request_object.status = PushNotificationRequestStatus.FAILED
            push_notification_request_object.save()
        else:
            push_notification_request_object.status = PushNotificationRequestStatus.SUCCESSFUL
            push_notification_request_object.save()
