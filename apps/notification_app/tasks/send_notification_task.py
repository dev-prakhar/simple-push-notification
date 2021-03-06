from ..services.push_notification_service import PushNotificationService
from simple_push_notification.task_names import SEND_NOTIFICATIONS
from simple_push_notification.celery import app as celery_app


@celery_app.task(name=SEND_NOTIFICATIONS)
def send_notification_task(request_id):
    PushNotificationService().send_notification(request_id)
