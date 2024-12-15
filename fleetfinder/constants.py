"""
Constants used in this app
"""

# Alliance Auth
from esi import __version__ as esi_version

# AA Fleet Finder
from fleetfinder import __version__

APP_NAME = "aa-fleetfinder"
GITHUB_URL = f"https://github.com/ppfeufer/{APP_NAME}"
USER_AGENT = f"{APP_NAME}/{__version__} ({GITHUB_URL}) via django-esi/{esi_version}"
