import os
from django.contrib import admin

from floship import settings
from . import models


class OrderAdmin(admin.ModelAdmin):
    if settings.HOSTNAME != settings.STORE_HOSTNAME:
        exclude = ('order_number', 'warehouse',)
        readonly_fields = ('order_number', 'warehouse')

    def has_add_permission(self, request):
        if settings.HOSTNAME != settings.STORE_HOSTNAME:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        if settings.HOSTNAME != settings.STORE_HOSTNAME:
            return False
        return super().has_delete_permission(request, obj=None)

    def has_change_permission(self, request, obj=None):
        if settings.HOSTNAME == settings.STORE_HOSTNAME:
            return False
        return super().has_change_permission(request, obj=None)


admin.site.register(models.Order, OrderAdmin)
