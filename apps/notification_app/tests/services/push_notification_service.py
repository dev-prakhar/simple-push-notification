import json
from unittest.mock import patch

from django.conf import settings
from pywebpush import WebPushException
from rest_framework import status
from rest_framework.test import APITestCase

from ...models import Notification, PushSubscription, PushNotificationRequest
from ...services import PushNotificationService


class PushNotificationServiceTest(APITestCase):
    @patch('apps.notification_app.services.push_notification_service.webpush')
    def test_if_webpush_is_being_called(self, mock_check_webpush):
        notification_data = Notification.objects.create(title="test title", options={})
        notification_data_to_be_inserted_into_model = {
            'notification_id': notification_data.id
        }
        notification_dict_passed_into_webpush = {
            'title': notification_data.title,
            'options': notification_data.options
        }
        push_subscription_data_to_be_inserted_into_model = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        push_subscription_dict_passed_into_webpush = {
            'endpoint': 'https://something.com',
            'keys': {
                'p256dh': 'any_string_value',
                'auth': 'another_string_value'
            }
        }
        mock_vapid_claims = {'sub': 'mailto: x@gmail.com'}
        push_subscription_object = PushSubscription.objects.create(**push_subscription_data_to_be_inserted_into_model)
        push_notification_request_object = PushNotificationRequest.objects.create(
            **notification_data_to_be_inserted_into_model)
        PushNotificationService().send_notification(push_notification_request_object.id)
        mock_check_webpush.assert_called()
        mock_check_webpush.assert_called_once()
        mock_check_webpush.assert_called_with(push_subscription_dict_passed_into_webpush,
                                              json.dumps(notification_dict_passed_into_webpush),
                                              vapid_private_key=settings.VAPID_PRIVATE_KEY,
                                              vapid_claims=mock_vapid_claims)
        updated_push_notification_request_object = PushNotificationRequest.objects.get(id=push_subscription_object.id)
        self.assertEqual(updated_push_notification_request_object.status, 'successful')

    @patch('apps.notification_app.services.push_notification_service.webpush')
    def test_webpush_failed(self, mock_web_push):
        notification_data = Notification.objects.create(title="test title", options={})
        notification_data_to_be_inserted_into_model = {
            'notification_id': notification_data.id
        }
        push_subscription_data_to_be_inserted_into_model = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        push_subscription_object = PushSubscription.objects.create(**push_subscription_data_to_be_inserted_into_model)
        push_notification_request_object = PushNotificationRequest.objects.create(
            **notification_data_to_be_inserted_into_model)

        PushNotificationService().send_notification(push_notification_request_object.id)

        mock_web_push.side_effect = WebPushException('Test')
        self.assertRaises(WebPushException, mock_web_push)

        mock_web_push.response.status_code = status.HTTP_400_BAD_REQUEST
        self.assertEqual(mock_web_push.response.status_code, status.HTTP_400_BAD_REQUEST)
