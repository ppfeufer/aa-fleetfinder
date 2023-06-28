# Generated by Django 4.0.10 on 2023-06-28 12:38

# Django
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("fleetfinder", "0002_model_verbose_names"),
    ]

    operations = [
        migrations.AddField(
            model_name="fleet",
            name="esi_error_count",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="fleet",
            name="last_esi_error",
            field=models.CharField(
                blank=True,
                choices=[
                    (
                        "NOT_IN_FLEET",
                        "FC is not in the registered fleet anymore or fleet is no longer available.",
                    ),
                    ("NO_FLEET", "Registered fleet seems to be no longer available."),
                    ("NOT_FLEETBOSS", "FC is no longer the fleet boss."),
                    ("FC_CHANGED_FLEET", "FC switched to another fleet."),
                ],
                default="",
                max_length=16,
            ),
        ),
        migrations.AddField(
            model_name="fleet",
            name="last_esi_error_time",
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]
