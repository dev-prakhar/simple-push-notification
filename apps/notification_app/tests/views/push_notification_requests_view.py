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

        with self.assertNumQueries(4):
            # 1. SELECT (1) AS "a" FROM "notification_app_notification" WHERE "notification_app_notification"."id" = 1 LIMIT 1
            # 2. Create SAVEPOINT
            # 3. Insert push notification request data into DB
            # 4. Release SAVEPOINT
            response = self.client.post(url, push_notification_request_data, format='json')
        # Only ID is present in response
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(PushNotificationRequest.objects.filter(id=response.data).exists())

    def test_insert_request_with_status_in_input(self):
        url = reverse('push-notification-requests')
        notification_data = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'status': 'xyz',
            'notification_id': 1
        }
        with self.assertNumQueries(4):
            # 1. SELECT (1) AS "a" FROM "notification_app_notification" WHERE "notification_app_notification"."id" = 1 LIMIT 1
            # 2. Create SAVEPOINT
            # 3. Insert push notification request data into DB
            # 4. Release SAVEPOINT
            response = self.client.post(url, push_notification_request_data, format='json')

        # Status field is ignored
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_insert_request_with_invalid_notification_id(self):
        url = reverse('push-notification-requests')
        notification_data = Notification.objects.create(title="test title", options={})
        push_notification_request_data = {
            'notification_id': 200
        }
        with self.assertNumQueries(1):
            # 1. SELECT (1) AS "a" FROM "notification_app_notification" WHERE "notification_app_notification"."id" = 200 LIMIT 1
            response = self.client.post(url, push_notification_request_data, format='json')
        response = self.client.post(url, push_notification_request_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
