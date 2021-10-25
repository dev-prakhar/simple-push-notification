from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class PushSubscriptionsViewTestCase(APITestCase):
    def test_insert_valid_data_with_default_status(self):
        url = reverse('push-subscriptions')
        data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertNumQueries(5)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(True, 'id' in response.data)
        self.assertEqual(response.data['endpoint'], data['endpoint'])
        self.assertEqual(response.data['key'], data['key'])
        self.assertEqual(response.data['auth'], data['auth'])
        self.assertEqual(response.data['status'], 'active')

    def test_insert_valid_data_with_status_expired(self):
        url = reverse('push-subscriptions')
        data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value',
            'status': 'expired'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(len(response.data), 5)
        self.assertEqual(True, 'id' in response.data)
        self.assertEqual(response.data['endpoint'], data['endpoint'])
        self.assertEqual(response.data['key'], data['key'])
        self.assertEqual(response.data['auth'], data['auth'])
        self.assertEqual(response.data['status'], 'expired')


    def test_insert_valid_data_with_status_unsubscribed(self):
        url = reverse('push-subscriptions')
        data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value',
            'status': 'unsubscribed'
        }
        response = self.client.post(url, data, format='json')

        self.assertEqual(len(response.data), 5)
        self.assertEqual(True, 'id' in response.data)
        self.assertEqual(response.data['endpoint'], data['endpoint'])
        self.assertEqual(response.data['key'], data['key'])
        self.assertEqual(response.data['auth'], data['auth'])
        self.assertEqual(response.data['status'], 'unsubscribed')

    def test_insert_invalid_data(self):
        url = reverse('push-subscriptions')
        data = {
            'endpoint': 'some_string_not_url',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
