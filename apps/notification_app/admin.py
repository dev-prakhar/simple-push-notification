from django.contrib import admin
from .models import PushSubscription
from .models import Notification


admin.site.register(PushSubscription)
admin.site.register(Notification)
