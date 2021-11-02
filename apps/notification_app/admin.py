from django.contrib import admin
from .models import PushSubscription, Notification, PushNotificationRequest


admin.site.register(PushSubscription)
admin.site.register(Notification)
admin.site.register(PushNotificationRequest)
