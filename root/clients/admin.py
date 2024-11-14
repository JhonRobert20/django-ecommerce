from django.contrib.admin import ModelAdmin, register

from clients.models import Client, Direction


@register(Client)
class ClientAdmin(ModelAdmin):
    pass


@register(Direction)
class DirectionAdmin(ModelAdmin):
    pass
