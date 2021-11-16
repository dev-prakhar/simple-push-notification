from django.contrib import admin
from .models import PushSubscription, Notification, PushNotificationRequest


class PushSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'endpoint', 'status')


class NotificationAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'options')


class PushNotificationRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'notification_id', 'status')


admin.site.register(PushSubscription, PushSubscriptionAdmin)
admin.site.register(Notification, NotificationAdmin)
admin.site.register(PushNotificationRequest, PushNotificationRequestAdmin)
