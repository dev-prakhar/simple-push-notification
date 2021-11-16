from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Notification, PushNotificationRequest


class PushNotificationRequestView(APITestCase):
    def test_get_status_of_valid_push_notification_request_id(self):
        notification_object = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'notification_id': 1
        }
        push_notification_request_object = PushNotificationRequest.objects.create(**push_notification_request_data)
        url = reverse('push-notification-request', kwargs={'request_id': 1})
        with self.assertNumQueries(1):
            # 1. Select all notification instances from Notiifcation model
            response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 3)
        self.assertTrue('id' in response.json())
        self.assertTrue('notification_id' in response.json())
        self.assertTrue('status' in response.json())

    def test_get_status_of_invalid_push_notification_request_id(self):
        url = reverse('push-notification-request', kwargs={'request_id': 1})
        with self.assertNumQueries(1):
            # 1. Select all notification instances from Notification model
            response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
