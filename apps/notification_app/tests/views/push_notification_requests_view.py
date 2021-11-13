from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Notification, PushNotificationRequest


class PushNotificationRequestsView(APITestCase):
    def test_insert_request_with_valid_data(self):
        url = reverse('push-notification-requests')
        notification_object = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'notification_id': 1
        }

        with self.assertNumQueries(2):
            # 1. Select first notification from the list of notification objects filtered with id=notfication_id as a
            # serializer check during PushNotificationRequest object creation
            # 2. Insert push notification request data into DB
            response = self.client.post(url, push_notification_request_data, format='json')

        # Only ID is present in response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(PushNotificationRequest.objects.filter(id=response.data).first)

    def test_insert_request_with_status_in_input(self):
        url = reverse('push-notification-requests')
        notification_data = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'status': 'xyz',
            'notification_id': 1
        }

        response = self.client.post(url, push_notification_request_data, format='json')
        # Status field is ignored
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_insert_request_with_invalid_notification_id(self):
        url = reverse('push-notification-requests')
        notification_data = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'notification_id': 200
        }
        response = self.client.post(url, push_notification_request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
