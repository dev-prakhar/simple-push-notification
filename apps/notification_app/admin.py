from django.contrib import admin
from .models import PushSubscription
from .models import Notification

# Register your models here.
admin.site.register(PushSubscription)
admin.site.register(Notification)
