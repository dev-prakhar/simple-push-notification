from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.notification_app.views import views


urlpatterns = [
    path('push-subscriptions/', views.PushSubscriptionList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)