"""
Models
"""

# Django
from django.db import models
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth.eveonline.models import EveCharacter
from allianceauth.groupmanagement.models import AuthGroup


class General(models.Model):
    """
    General module permissions
    """

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta Definitions
        """

        verbose_name = "Fleet Finder"
        managed = False
        default_permissions = ()
        permissions = (
            ("access_fleetfinder", "Can access the Fleet Finder app"),
            ("manage_fleets", "Can manage fleets"),
        )


class Fleet(models.Model):
    """
    Fleet Model
    """

    fleet_id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, default="", verbose_name=_("Fleet Name"))
    fleet_commander = models.ForeignKey(
        EveCharacter,
        on_delete=models.SET_NULL,
        related_name="fleetfinder_fleet_commander",
        default=None,
        null=True,
        blank=True,
        verbose_name=_("Fleet Commander"),
    )
    created_at = models.DateTimeField(verbose_name=_("Creation date and time"))
    motd = models.TextField(blank=True, default="", verbose_name=_("Fleet MOTD"))
    is_free_move = models.BooleanField(verbose_name=_("Free move"))

    groups = models.ManyToManyField(
        AuthGroup,
        related_name="fleetfinder_restricted_groups",
        help_text="Groups listed here will be able to join the fleet",
        verbose_name=_("Group restrictions"),
    )

    class Meta:  # pylint: disable=too-few-public-methods
        """
        Meta Definitions
        """

        default_permissions = ()
