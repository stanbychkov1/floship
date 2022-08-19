from django.db import models

import warehouses
from . import statuses


class Order(models.Model):
    order_number = models.CharField(max_length=25,
                                    blank=False,
                                    unique=True)
    status = models.CharField(max_length=25,
                              choices=statuses.ORDERS_STATUS,
                              default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    warehouse = models.CharField(max_length=25,
                                 choices=warehouses.WAREHOUSES,
                                 blank=False)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'Заказ {self.order_number} со статусом {self.status} ' \
               f'на складе {self.warehouse}'
