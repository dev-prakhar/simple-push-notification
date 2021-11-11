import json
from unittest.mock import patch

from django.conf import settings
from rest_framework.test import APITestCase

from ...models import Notification, PushSubscription, PushNotificationRequest
from ...services import PushNotificationService


@patch('apps.notification_app.services.push_notification_service.webpush')
class PushNotificationServiceTest(APITestCase):
    def test_if_webpush_is_being_called(self, mock_check_webpush):
        notification_object = Notification.objects.create(title="test title", options={})
        notification_data = {
            'notification_id': notification_object.id
        }
        push_subscription_data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        push_subscription_object = PushSubscription.objects.create(**push_subscription_data)
        push_notification_request_object = PushNotificationRequest.objects.create(**notification_data)
        PushNotificationService().send_notification(push_notification_request_object.id)
        mock_check_webpush.assert_called()

    def test_arguments_used_in_webpush(self, mock_check_webpush):
        # In __send_notification_with_webpush , we have created dicts of push subscription and notification which are
        # passed in webpush()
        notification_data = Notification.objects.create(title='test title', options={})
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
        push_notification_request_object = PushNotificationRequest.objects.create(**notification_data_to_be_inserted_into_model)
        PushNotificationService().send_notification(push_notification_request_object.id)
        mock_check_webpush.assert_called_with(push_subscription_dict_passed_into_webpush, json.dumps(notification_dict_passed_into_webpush), vapid_private_key=settings.VAPID_PRIVATE_KEY, vapid_claims=mock_vapid_claims)

    def test_if_webpush_is_being_called_only_once(self, mock_check_webpush):
        notification_object = Notification.objects.create(title="test title", options={})
        notification_data = {
            'notification_id': notification_object.id
        }
        push_subscription_data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        push_subscription_object = PushSubscription.objects.create(**push_subscription_data)
        push_notification_request_object = PushNotificationRequest.objects.create(**notification_data)
        PushNotificationService().send_notification(push_notification_request_object.id)
        mock_check_webpush.assert_called_once()

    def test_request_status_updated_when_notification_send_successful(self, mock_web_push):
        notification_object = Notification.objects.create(title="test title", options={})
        notification_data = {
            'notification_id': notification_object.id
        }
        push_subscription_data = {
            'endpoint': 'https://something.com',
            'key': 'any_string_value',
            'auth': 'another_string_value'
        }
        push_subscription_object = PushSubscription.objects.create(**push_subscription_data)
        push_notification_request_object = PushNotificationRequest.objects.create(**notification_data)
        PushNotificationService().send_notification(push_notification_request_object.id)
        updated_push_notification_request_object = PushNotificationRequest.objects.get(id=push_subscription_object.id)
        self.assertEqual(updated_push_notification_request_object.status, 'successful')
