# Generated by Django 4.2.16 on 2024-11-14 12:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0002_alter_client_phone_alter_client_phone_extension"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Directions",
            new_name="Direction",
        ),
    ]