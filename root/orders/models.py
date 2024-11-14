from uuid import uuid4

from clients.models import Client
from django.db.models import (
    CASCADE,
    SET_NULL,
    CharField,
    DateTimeField,
    FloatField,
    ForeignKey,
    IntegerField,
    Model,
    OneToOneField,
    UUIDField,
)
from products.models import Product


class OrderState(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    name = CharField(max_length=255)


class Order(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    client = ForeignKey(Client, on_delete=SET_NULL)
    total = FloatField(null=False, blank=False)
    date = DateTimeField()
    order_state = ForeignKey(OrderState, on_delete=SET_NULL)


class OrderDetail(Model):
    order = OneToOneField(Order, on_delete=CASCADE)
    product = ForeignKey(Product, on_delete=SET_NULL, blank=False)
    unit_price = FloatField(null=False)
    amount = IntegerField(null=False)


class Payment(Model):
    id = UUIDField(primary_key=True, default=uuid4, editable=False)
    client = ForeignKey(Client, on_delete=SET_NULL)
    order = ForeignKey(Order, on_delete=SET_NULL)
    payment_method = CharField(help_text="WIP")
    date = DateTimeField()
