from django.urls import path
from .views import views

urlpatterns = [
    path('push-subscriptions', views.PushSubscriptionList.as_view(), name="push-subscriptions")
]



