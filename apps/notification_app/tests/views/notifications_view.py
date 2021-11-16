from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Notification


class NotificationsView(APITestCase):
    def test_get_all_notifications(self):
        url = reverse('notification-contents')
        notification_object = Notification.objects.create(title="test title", options={})
        with self.assertNumQueries(1):
            # 1. Select all notification instances from Notiification model
            response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()[0]), 2)
        self.assertTrue('id' in response.json()[0])
        self.assertTrue('title' in response.json()[0])

    def test_get_notifications_when_zero_notifications_present(self):
        url = reverse('notification-contents')
        with self.assertNumQueries(1):
            # 1. Select all notification instances from Notiification model
            response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 0)
