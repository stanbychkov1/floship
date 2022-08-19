import os

import requests
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.reverse import reverse

import warehouses
from floship import settings
from . import models, serializers


def define_host(data):
    if settings.HOSTNAME != settings.STORE_HOSTNAME:
        return settings.STORE_HOST
    return warehouses.WAREHOUSES_HOSTS[data.get('warehouse')]


@receiver(post_save, sender=models.Order)
def order_save_sync(created, instance, **kwargs):
    data = serializers.OrderSerializer(instance).data
    host = define_host(data)
    if created:
        url = reverse('orders:order-list')
        url = host + url
        requests.post(url, data=data)
    else:
        url = reverse('orders:order-detail',
                      kwargs={'order_number': data.pop('order_number')})
        url = host + url
        requests.patch(url, data=data)


@receiver(post_delete, sender=models.Order)
def order_post_delete(instance, **kwargs):
    data = serializers.OrderSerializer(instance).data
    host = define_host(data)
    url = reverse("orders:order-detail",
                  kwargs={'order_number': data.pop('order_number')})
    url = host + url
    requests.delete(url)
