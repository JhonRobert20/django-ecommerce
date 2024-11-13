import uuid

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    phone_extension = models.CharField(max_length=5, blank=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Directions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    direction = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    is_principal = models.BooleanField(default=False)

    def __str__(self):
        return f"Direction for {self.client.user.first_name} {self.client.user.last_name}"

    def clean(self):
        if (
            self.is_principal
            and Directions.objects.filter(client=self.client, is_principal=True)
            .exclude(id=self.id)
            .exists()
        ):
            raise ValidationError("A client can only have one principal address.")


def save(self, *args, **kwargs):
    self.clean()
    super().save(*args, **kwargs)
