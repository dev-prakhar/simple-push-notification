from apps.notification_app.models import PushNotificationRequest, Notification, PushSubscription


class PushNotificationService:
    def send_notification(self, request_id):
        print('reached final service file = ', request_id)
        """
        # Retrieve the specific request object
        request_object = PushNotificationRequest.objects.get(id=request_id)

        # Retrieve the notification content requested in the request_object
        notification_object = Notification.objects.get(id=request_object.notification_id)

        # Retrieve the push subscriptionof only one subscriber
        push_subscription_object = PushSubscription.objects.get(id=1)

        # Send the notification
"""