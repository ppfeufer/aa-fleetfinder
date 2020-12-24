"""
models
"""

from datetime import datetime

from django.db import models

from allianceauth.groupmanagement.models import AuthGroup


class General(models.Model):
    """
    General module permissions
    """

    class Meta:
        """
        meta
        """

        default_permissions = ()
        permissions = (
            ("access_fleetfinder", "Can access the Fleet Finder app"),
            ("manage_fleets", "Can manage fleets"),
        )


class Fleet(models.Model):
    """
    Fleet
    """

    fleet_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, default="")
    fleet_commander_id = models.BigIntegerField()
    created_at = models.DateTimeField()
    motd = models.CharField(max_length=4000)
    is_free_move = models.BooleanField()

    groups = models.ManyToManyField(
        AuthGroup,
        related_name="restricted_groups",
        help_text="Group listed here will be able to join the fleet",
    )

    class Meta:
        """
        meta
        """

        default_permissions = ()


class FleetInformation(models.Model):
    """
    Fleet Information
    """

    fleet = models.ForeignKey(Fleet, on_delete=models.CASCADE)
    ship_type_name = models.CharField(max_length=100)
    count = models.IntegerField()
    date = models.DateTimeField(default=datetime.now)

    class Meta:
        """
        meta
        """

        default_permissions = ()
