"""
Constants used in this app
"""

# Third Party
from bravado.exception import HTTPBadGateway, HTTPGatewayTimeout, HTTPServiceUnavailable

# Django
from django.utils.text import slugify

# AA Fleet Finder
from fleetfinder import __verbose_name__, __version__

verbose_name_slugified: str = slugify(__verbose_name__, allow_unicode=True)
github_url: str = "https://github.com/ppfeufer/aa-fleetfinder"

USER_AGENT = f"{verbose_name_slugified} v{__version__} {github_url}"

ESI_ERROR_LIMIT = 50
ESI_TIMEOUT_ONCE_ERROR_LIMIT_REACHED = 60
ESI_MAX_RETRIES = 3

CACHE_KEY_NOT_IN_FLEET_ERROR = (
    "fleetfinder_task_check_fleet_adverts_error_counter_not_in_fleet_"
)
CACHE_KEY_NO_FLEET_ERROR = (
    "fleetfinder_task_check_fleet_adverts_error_counter_no_fleet_"
)
CACHE_KEY_FLEET_CHANGED_ERROR = (
    "fleetfinder_task_check_fleet_adverts_error_counter_fleet_changed_"
)
CACHE_KEY_NO_FLEETBOSS_ERROR = (
    "fleetfinder_task_check_fleet_adverts_error_counter_no_fleetboss_"
)
CACHE_MAX_ERROR_COUNT = 3

# Params for all tasks
TASK_DEFAULT_KWARGS = {
    "time_limit": 120,  # stop after 2 minutes
}

# Params for tasks that make ESI calls
TASK_ESI_KWARGS = {
    **TASK_DEFAULT_KWARGS,
    **{
        "autoretry_for": (
            OSError,
            HTTPBadGateway,
            HTTPGatewayTimeout,
            HTTPServiceUnavailable,
        ),
        "retry_kwargs": {"max_retries": ESI_MAX_RETRIES},
        "retry_backoff": True,
    },
}