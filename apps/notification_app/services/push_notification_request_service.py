from django.db import transaction

from simple_push_notification.celery import app as celery_app
from simple_push_notification.task_names import SEND_NOTIFICATIONS

from ..models import PushNotificationRequest


class PushNotificationRequestService:
    @transaction.atomic
    def request_to_send_notification(self, push_notification_request_data):
        push_notification_request_object = PushNotificationRequest.objects.create(**push_notification_request_data)
        # Send ID of the new request to the celery task
        push_notification_request_id = push_notification_request_object.id
        transaction.on_commit(lambda: celery_app.send_task(name=SEND_NOTIFICATIONS, args=(push_notification_request_id,)))
        return push_notification_request_id
