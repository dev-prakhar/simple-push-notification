from simple_push_notification.celery import app as celery_app

from ..models import PushNotificationRequest
from ..task_names import SEND_NOTIFICATIONS
from ..tasks import send_notification_task


class PushNotificationRequestService:
    def request_to_send_notification(self, serializer_data):

        # Insert request data into model
        PushNotificationRequest.objects.create(**serializer_data)

        # Send ID of the new request to the celery task
        request_id = serializer_data.get('id')
        print('req = ', serializer_data)
        # celery_app.send_task(name=SEND_NOTIFICATIONS, args=request_id)
