from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from apps.notification_app.serializers.push_subscription_serializer import PushSubscriptionSerializer


@csrf_exempt
@api_view(['POST'])
def persist_subscriber_data(request):
    serializer = PushSubscriptionSerializer(data=request.data)
    print('function entered')
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

