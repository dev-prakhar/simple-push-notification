from django.urls import path
from .views import push_subscriptions_view

urlpatterns = [
    path('push-subscriptions', push_subscriptions_view.PushSubscriptionsView.as_view(), name="push-subscriptions")
]
