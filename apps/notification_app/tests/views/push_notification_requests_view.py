from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from apps.notification_app.models import Notification


class PushNotificationRequestsView(APITestCase):
    def test_insert_request_with_valid_data(self):
        url = reverse('push-notification-requests')
        # Push Notification Request Model
        data = {
            'status': 'in_progress',
            'notification': '1'
        }

        with self.assertNumQueries(1):
            # 1. Insert push notification request data into DB
            response = self.client.post(url, data, format='json')
        print('response.data = ', response.data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(len(response.data), 3)
        self.assertTrue('id' in response.data)
        self.assertEqual(response.data['status'], data['status'])
        self.assertEqual(response.data['notification'], data['notification'])

    def test_insert_request_with_invalid_status(self):
        url = reverse('push-notification-requests')
        notification_data = Notification.objects.create(title="test title", options={})
        # push_notification_request_data = PushNotificationRequest.objects.create(status="random_status", notification=notification_data)
        data = {
            'status': 'random_status',
            'notification': notification_data.id
        }
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
