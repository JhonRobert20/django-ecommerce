from django.contrib.admin import ModelAdmin, register

from orders.models import Order, OrderDetail, OrderState, Payment


@register(OrderState)
class OrderStateAdmin(ModelAdmin):
    pass


@register(Order)
class OrderAdmin(ModelAdmin):
    pass


@register(OrderDetail)
class OrderDetailAdmin(ModelAdmin):
    pass


@register(Payment)
class PaymentAdmin(ModelAdmin):
    pass
