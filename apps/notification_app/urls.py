from django.urls import path

from apps.notification_app import views

urlpatterns = [
    path('push-subscriptions', views.PushSubscriptionsView.as_view(), name="push-subscriptions"),
    path('push-notification-requests', views.PushNotificationRequestsView.as_view(),
         name="push-notification-requests"),
    path('push-notification-requests/<int:request_id>',
         views.PushNotificationRequestView.as_view(), name="push-notification-request"),
    path('notification-contents', views.NotificationsView.as_view(), name="notification-contents")
]
