# Generated by Django 4.2.16 on 2024-11-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clients", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="client",
            name="phone",
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name="client",
            name="phone_extension",
            field=models.IntegerField(blank=True, help_text="Exclude +", null=True),
        ),
    ]