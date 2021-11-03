from django.urls import path
from .views import push_subscriptions_view, requests_view, request_view

urlpatterns = [
    path('push-subscriptions', push_subscriptions_view.PushSubscriptionsView.as_view(), name="push-subscriptions"),
    path('push-notification-requests', requests_view.PushNotificationRequestsView.as_view(), name="push-notification-requests"),
    path('push-notification-requests/<int:request_id>', request_view.PushNotificationRequestView.as_view(), name="push-notification-request")
]
