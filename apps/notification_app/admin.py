from django.contrib import admin
from .models import PushSubscription, Notification, PushNotificationRequest

@admin.register(PushSubscription)
class PushSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'endpoint', 'status')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'options')

@admin.register(PushNotificationRequest)
class PushNotificationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'notification_id', 'status')

