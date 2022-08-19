from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from orders import models, serializers


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    lookup_field = 'order_number'
