import uuid

from django.core.exceptions import ValidationError
from django.db import models


class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.IntegerField(max_length=20)
    phone_extension = models.IntegerField(
        max_length=5, blank=True, null=True, help_text="Exclude +"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Directions(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    direction = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    is_principal = models.BooleanField(default=False)

    def __str__(self):
        return (
            f"Direction for {self.client.first_name} {self.client.last_name} "
            f"with name {self.name}: {self.direction}"
        )

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
