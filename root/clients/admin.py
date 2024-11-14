from django.contrib.admin import ModelAdmin, register

from clients.models import Client, Directions


@register(Client)
class ClientAdmin(ModelAdmin):
    pass


@register(Directions)
class DirectionAdmin(ModelAdmin):
    pass
